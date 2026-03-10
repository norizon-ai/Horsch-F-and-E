"""
File-based storage publisher for crawled data.

This publisher saves crawled data directly to disk in JSON format,
allowing for immediate data collection without requiring the ingestion
worker to be complete.
"""

import json
import os
from pathlib import Path
from datetime import datetime, timezone
from typing import Optional, List, Dict, Any
import hashlib
from urllib.parse import urlparse

from publishing.publisher_base import PublisherBase
from models.articles import RawArticle
from core.error_tracker import ErrorTracker


class FileStoragePublisher(PublisherBase):
    """
    Publisher that saves crawled data to disk in JSON format.
    
    Features:
    - Organized directory structure by date and domain
    - JSON storage for easy processing
    - Metadata index for tracking all saved files
    - Batch writing for efficiency
    - Resume capability with deduplication
    """
    
    def __init__(self, storage_path: str = "./crawled_data", batch_size: int = 10):
        """
        Initialize the file storage publisher.
        
        Args:
            storage_path: Base directory for storing crawled data
            batch_size: Number of articles to batch before writing to disk
        """
        self.storage_path = Path(storage_path)
        self.batch_size = batch_size
        self.current_batch: List[RawArticle] = []
        self.is_connected = False
        self.stats = {
            "total_saved": 0,
            "total_size_bytes": 0,
            "domains": set(),
            "session_start": None,
            "session_id": None
        }
        self.index_file = None
        self.processed_urls = set()
        self.error_tracker = None
        self.subdomain_state = {
            "base_domain": "",
            "discovered_subdomains": set(),
            "crawled_subdomains": set(),
            "pending_subdomains": set(),
            "failed_subdomains": set(),
            "subdomain_urls": {}
        }
        self.subdomain_file = None
        
    async def connect(self) -> None:
        """
        Initialize storage directory and index file.
        """
        # Create storage directory structure
        self.storage_path.mkdir(parents=True, exist_ok=True)
        
        # Generate session ID
        self.stats["session_start"] = datetime.now(timezone.utc)
        self.stats["session_id"] = self.stats["session_start"].strftime("%Y%m%d_%H%M%S")
        
        # Create session directory
        session_dir = self.storage_path / self.stats["session_id"]
        session_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize index file
        index_path = session_dir / "index.jsonl"
        self.index_file = open(index_path, "a", encoding="utf-8")
        
        # Load existing URLs to avoid duplicates
        self._load_processed_urls()
        
        # Load subdomain state from previous sessions
        self._load_subdomain_state()
        
        # Initialize error tracker
        self.error_tracker = ErrorTracker(str(self.storage_path), self.stats["session_id"])
        self.error_tracker.initialize()
        
        print(f"FileStoragePublisher: Connected to storage at {self.storage_path}")
        print(f"Session ID: {self.stats['session_id']}")
        self.is_connected = True
    
    def _load_processed_urls(self) -> None:
        """
        Load URLs that have already been processed to avoid duplicates.
        """
        # Check all session directories for existing data
        if self.storage_path.exists():
            for session_dir in self.storage_path.iterdir():
                if session_dir.is_dir():
                    index_file = session_dir / "index.jsonl"
                    if index_file.exists():
                        with open(index_file, "r", encoding="utf-8") as f:
                            for line in f:
                                try:
                                    entry = json.loads(line)
                                    self.processed_urls.add(entry.get("url", ""))
                                except json.JSONDecodeError:
                                    continue
        
        if self.processed_urls:
            print(f"Loaded {len(self.processed_urls)} previously processed URLs")
    
    def _load_subdomain_state(self) -> None:
        """
        Load subdomain state from previous sessions.
        """
        # Look for most recent subdomain state file
        subdomain_files = []
        if self.storage_path.exists():
            for session_dir in self.storage_path.iterdir():
                if session_dir.is_dir():
                    subdomain_file = session_dir / "subdomains.json"
                    if subdomain_file.exists():
                        subdomain_files.append(subdomain_file)
        
        if subdomain_files:
            # Load the most recent subdomain state
            latest_file = max(subdomain_files, key=lambda f: f.stat().st_mtime)
            with open(latest_file, "r", encoding="utf-8") as f:
                state = json.load(f)
                
                # Convert lists back to sets
                self.subdomain_state["base_domain"] = state.get("base_domain", "")
                self.subdomain_state["discovered_subdomains"] = set(state.get("discovered_subdomains", []))
                self.subdomain_state["crawled_subdomains"] = set(state.get("crawled_subdomains", []))
                self.subdomain_state["pending_subdomains"] = set(state.get("pending_subdomains", []))
                self.subdomain_state["failed_subdomains"] = set(state.get("failed_subdomains", []))
                self.subdomain_state["subdomain_urls"] = state.get("subdomain_urls", {})
                
                print(f"Loaded subdomain state from {latest_file}")
                print(f"  Discovered: {len(self.subdomain_state['discovered_subdomains'])} subdomains")
                print(f"  Crawled: {len(self.subdomain_state['crawled_subdomains'])} subdomains")
                print(f"  Pending: {len(self.subdomain_state['pending_subdomains'])} subdomains")
    
    async def save_subdomain_state(self, base_domain: str = None, 
                                  discovered: set = None,
                                  crawled: set = None,
                                  pending: set = None,
                                  failed: set = None,
                                  subdomain_urls: dict = None) -> None:
        """
        Save subdomain state to disk.
        
        Args:
            base_domain: Base domain being crawled
            discovered: Set of discovered subdomains
            crawled: Set of crawled subdomains
            pending: Set of pending subdomains
            failed: Set of failed subdomains
            subdomain_urls: Mapping of subdomains to example URLs
        """
        if not self.is_connected:
            return
            
        # Update internal state
        if base_domain:
            self.subdomain_state["base_domain"] = base_domain
        if discovered is not None:
            self.subdomain_state["discovered_subdomains"] = discovered
        if crawled is not None:
            self.subdomain_state["crawled_subdomains"] = crawled
        if pending is not None:
            self.subdomain_state["pending_subdomains"] = pending
        if failed is not None:
            self.subdomain_state["failed_subdomains"] = failed
        if subdomain_urls is not None:
            self.subdomain_state["subdomain_urls"] = subdomain_urls
        
        # Save to file
        session_dir = self.storage_path / self.stats["session_id"]
        subdomain_file = session_dir / "subdomains.json"
        
        # Convert sets to lists for JSON serialization
        state_to_save = {
            "base_domain": self.subdomain_state["base_domain"],
            "discovered_subdomains": list(self.subdomain_state["discovered_subdomains"]),
            "crawled_subdomains": list(self.subdomain_state["crawled_subdomains"]),
            "pending_subdomains": list(self.subdomain_state["pending_subdomains"]),
            "failed_subdomains": list(self.subdomain_state["failed_subdomains"]),
            "subdomain_urls": self.subdomain_state["subdomain_urls"],
            "last_updated": datetime.now(timezone.utc).isoformat()
        }
        
        with open(subdomain_file, "w", encoding="utf-8") as f:
            json.dump(state_to_save, f, ensure_ascii=False, indent=2)
    
    def get_subdomain_state(self) -> Dict[str, Any]:
        """
        Get current subdomain state.
        
        Returns:
            Dictionary with subdomain state
        """
        return {
            "base_domain": self.subdomain_state["base_domain"],
            "discovered_subdomains": self.subdomain_state["discovered_subdomains"],
            "crawled_subdomains": self.subdomain_state["crawled_subdomains"],
            "pending_subdomains": self.subdomain_state["pending_subdomains"],
            "failed_subdomains": self.subdomain_state["failed_subdomains"],
            "subdomain_urls": self.subdomain_state["subdomain_urls"]
        }
    
    async def publish_message(self, message: RawArticle) -> None:
        """
        Add message to batch and save when batch is full.
        
        Args:
            message: RawArticle to save
        """
        if not self.is_connected:
            raise ConnectionError("Publisher is not connected. Call connect() first.")
        
        # Skip if URL already processed
        url = message.source.uri
        if url in self.processed_urls:
            # Silently skip duplicates - they're already counted at the crawler level
            return
        
        # Add to batch
        self.current_batch.append(message)
        self.processed_urls.add(url)
        
        # Save batch if full
        if len(self.current_batch) >= self.batch_size:
            await self._save_batch()
    
    async def report_error(self, url: str, error: str) -> None:
        """
        Report a crawl error for tracking.
        
        Args:
            url: The URL that failed
            error: Error message
        """
        if self.error_tracker:
            self.error_tracker.add_error(url, error)
    
    async def _save_batch(self) -> None:
        """
        Save current batch to disk.
        """
        if not self.current_batch:
            return
        
        session_dir = self.storage_path / self.stats["session_id"]
        
        for article in self.current_batch:
            # Generate filename based on URL hash
            url_hash = hashlib.md5(article.source.uri.encode()).hexdigest()[:8]
            domain = urlparse(article.source.uri).netloc.replace(".", "_")
            
            # Create domain subdirectory
            domain_dir = session_dir / domain
            domain_dir.mkdir(parents=True, exist_ok=True)
            
            # Save article data
            filename = f"{url_hash}_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.json"
            file_path = domain_dir / filename
            
            # Convert to dictionary for JSON serialization
            article_dict = article.model_dump()
            
            # Convert datetime objects to ISO format strings
            if "source" in article_dict and "retrieved_at" in article_dict["source"]:
                article_dict["source"]["retrieved_at"] = article_dict["source"]["retrieved_at"].isoformat()
            
            # Write article to file
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(article_dict, f, ensure_ascii=False, indent=2)
            
            # Update index
            index_entry = {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "file_path": str(file_path.relative_to(self.storage_path)),
                "url": article.source.uri,
                "title": article.metadata.get("title", ""),
                "content_size": len(article.content),
                "domain": domain
            }
            self.index_file.write(json.dumps(index_entry) + "\n")
            self.index_file.flush()
            
            # Update statistics
            self.stats["total_saved"] += 1
            self.stats["total_size_bytes"] += len(article.content)
            self.stats["domains"].add(domain)
            
            print(f"Saved: {article.source.uri[:80]}... ({len(article.content)} chars)")
        
        print(f"Batch saved: {len(self.current_batch)} articles")
        self.current_batch.clear()
    
    async def close(self) -> None:
        """
        Save remaining batch and close index file.
        """
        if not self.is_connected:
            return
        
        # Save any remaining articles
        if self.current_batch:
            await self._save_batch()
        
        # Close index file
        if self.index_file:
            self.index_file.close()
        
        # Save session statistics
        await self._save_statistics()
        
        # Save final subdomain state
        await self.save_subdomain_state()
        
        # Close error tracker and generate report
        if self.error_tracker:
            error_stats = self.error_tracker.get_statistics()
            if error_stats['total_errors'] > 0:
                print(f"\nError Summary:")
                print(f"  Failed URLs: {error_stats['unique_failed_urls']}")
                print(f"  Retryable: {error_stats['retryable_urls']}")
                print(f"  Permanent failures: {error_stats['permanent_failures']}")
                print(f"\n  Error report saved to: {self.storage_path}/{self.stats['session_id']}/error_report.txt")
            self.error_tracker.close()
        
        print(f"\nFileStoragePublisher: Closed")
        print(f"Total articles saved: {self.stats['total_saved']}")
        print(f"Total size: {self.stats['total_size_bytes'] / (1024*1024):.2f} MB")
        print(f"Unique domains: {len(self.stats['domains'])}")
        
        self.is_connected = False
    
    async def _save_statistics(self) -> None:
        """
        Save session statistics to a summary file.
        """
        session_dir = self.storage_path / self.stats["session_id"]
        stats_file = session_dir / "statistics.json"
        
        stats_data = {
            "session_id": self.stats["session_id"],
            "session_start": self.stats["session_start"].isoformat(),
            "session_end": datetime.now(timezone.utc).isoformat(),
            "total_articles": self.stats["total_saved"],
            "total_size_bytes": self.stats["total_size_bytes"],
            "total_size_mb": self.stats["total_size_bytes"] / (1024*1024),
            "unique_domains": list(self.stats["domains"]),
            "domain_count": len(self.stats["domains"]),
            "subdomain_info": {
                "base_domain": self.subdomain_state["base_domain"],
                "discovered_count": len(self.subdomain_state["discovered_subdomains"]),
                "crawled_count": len(self.subdomain_state["crawled_subdomains"]),
                "pending_count": len(self.subdomain_state["pending_subdomains"]),
                "failed_count": len(self.subdomain_state["failed_subdomains"]),
                "discovered_subdomains": list(self.subdomain_state["discovered_subdomains"])[:20]  # Top 20 for summary
            }
        }
        
        with open(stats_file, "w", encoding="utf-8") as f:
            json.dump(stats_data, f, ensure_ascii=False, indent=2)
    
    def get_storage_info(self) -> Dict[str, Any]:
        """
        Get information about current storage session.
        
        Returns:
            Dictionary with storage statistics and paths
        """
        session_dir = self.storage_path / self.stats["session_id"] if self.stats["session_id"] else None
        
        return {
            "storage_path": str(self.storage_path),
            "session_id": self.stats["session_id"],
            "session_directory": str(session_dir) if session_dir else None,
            "articles_saved": self.stats["total_saved"],
            "total_size_mb": self.stats["total_size_bytes"] / (1024*1024),
            "unique_domains": len(self.stats["domains"]),
            "is_connected": self.is_connected
        }


class ParquetStoragePublisher(PublisherBase):
    """
    Alternative publisher that saves data in Parquet format for better compression
    and faster batch processing with tools like Pandas or DuckDB.
    """
    
    def __init__(self, storage_path: str = "./crawled_data_parquet", batch_size: int = 100):
        """
        Initialize the Parquet storage publisher.
        
        Args:
            storage_path: Base directory for storing crawled data
            batch_size: Number of articles to batch before writing to disk
        """
        self.storage_path = Path(storage_path)
        self.batch_size = batch_size
        self.current_batch: List[Dict[str, Any]] = []
        self.is_connected = False
        self.file_counter = 0
        
    async def connect(self) -> None:
        """
        Initialize storage directory.
        """
        import warnings
        warnings.filterwarnings("ignore", category=FutureWarning)
        
        try:
            import pandas as pd
            import pyarrow.parquet as pq
        except ImportError:
            raise ImportError(
                "Parquet storage requires pandas and pyarrow. "
                "Install with: pip install pandas pyarrow"
            )
        
        self.storage_path.mkdir(parents=True, exist_ok=True)
        
        # Create session directory
        session_id = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        self.session_dir = self.storage_path / session_id
        self.session_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"ParquetStoragePublisher: Connected to storage at {self.storage_path}")
        print(f"Session directory: {self.session_dir}")
        self.is_connected = True
    
    async def publish_message(self, message: RawArticle) -> None:
        """
        Add message to batch and save when batch is full.
        
        Args:
            message: RawArticle to save
        """
        if not self.is_connected:
            raise ConnectionError("Publisher is not connected. Call connect() first.")
        
        # Convert to flat dictionary for DataFrame
        flat_dict = {
            "url": message.source.uri,
            "source_document_id": message.source_document_id,
            "content": message.content,
            "module": message.source.module,
            "retrieved_at": message.source.retrieved_at,
            "author": message.author.name if message.author else None,
            "tags": json.dumps(message.tags),
            "permissions": json.dumps(message.permissions),
            "metadata": json.dumps(message.metadata)
        }
        
        self.current_batch.append(flat_dict)
        
        # Save batch if full
        if len(self.current_batch) >= self.batch_size:
            await self._save_batch()
    
    async def _save_batch(self) -> None:
        """
        Save current batch to Parquet file.
        """
        if not self.current_batch:
            return
        
        import pandas as pd
        
        # Create DataFrame from batch
        df = pd.DataFrame(self.current_batch)
        
        # Save to Parquet
        self.file_counter += 1
        filename = f"batch_{self.file_counter:04d}.parquet"
        file_path = self.session_dir / filename
        
        df.to_parquet(file_path, compression="snappy", index=False)
        
        print(f"Saved batch {self.file_counter}: {len(self.current_batch)} articles to {filename}")
        self.current_batch.clear()
    
    async def close(self) -> None:
        """
        Save remaining batch and close.
        """
        if not self.is_connected:
            return
        
        # Save any remaining articles
        if self.current_batch:
            await self._save_batch()
        
        print(f"ParquetStoragePublisher: Closed")
        print(f"Total batches saved: {self.file_counter}")
        print(f"Data location: {self.session_dir}")
        
        self.is_connected = False