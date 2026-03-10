#!/usr/bin/env python3
"""
Batch processor for crawled data stored on disk.

This processor reads crawled data from disk storage and performs
chunking, embedding, and other processing operations that would
normally be done by the ingestion worker.
"""

import json
import os
from pathlib import Path
from typing import List, Dict, Any, Optional, Generator
from datetime import datetime
import hashlib


class BatchProcessor:
    """
    Processes crawled data stored on disk.
    
    Features:
    - Read JSON/Parquet files from storage
    - Chunk large documents
    - Generate embeddings (placeholder for now)
    - Export to various formats
    - Progress tracking and resume capability
    """
    
    def __init__(self, storage_path: str = "./crawled_data"):
        """
        Initialize the batch processor.
        
        Args:
            storage_path: Path to crawled data storage
        """
        self.storage_path = Path(storage_path)
        self.processed_files = set()
        self.stats = {
            "files_processed": 0,
            "chunks_created": 0,
            "errors": 0
        }
    
    def process_session(self, session_id: Optional[str] = None, 
                       chunk_size: int = 1000,
                       chunk_overlap: int = 200) -> Generator[Dict[str, Any], None, None]:
        """
        Process all files from a specific session or the latest session.
        
        Args:
            session_id: Session ID to process (latest if None)
            chunk_size: Maximum size of each chunk
            chunk_overlap: Overlap between chunks
            
        Yields:
            Processed chunks with metadata
        """
        # Find session directory
        if session_id:
            session_dir = self.storage_path / session_id
        else:
            # Get latest session
            sessions = [d for d in self.storage_path.iterdir() if d.is_dir()]
            if not sessions:
                raise ValueError(f"No sessions found in {self.storage_path}")
            session_dir = max(sessions, key=lambda d: d.stat().st_mtime)
        
        print(f"Processing session: {session_dir.name}")
        
        # Process all JSON files in session
        for json_file in session_dir.rglob("*.json"):
            # Skip index and statistics files
            if json_file.name in ["index.jsonl", "statistics.json"]:
                continue
            
            try:
                # Read article data
                with open(json_file, "r", encoding="utf-8") as f:
                    article_data = json.load(f)
                
                # Process the article
                chunks = self._chunk_content(
                    article_data["content"],
                    chunk_size,
                    chunk_overlap
                )
                
                # Generate processed chunks
                for i, chunk_text in enumerate(chunks):
                    chunk_data = {
                        "chunk_id": f"{article_data['source_document_id']}_{i}",
                        "source_document_id": article_data["source_document_id"],
                        "chunk_index": i,
                        "content": chunk_text,
                        "url": article_data["source"]["uri"],
                        "metadata": article_data.get("metadata", {}),
                        "permissions": article_data.get("permissions", []),
                        "processed_at": datetime.utcnow().isoformat()
                    }
                    
                    # Add embedding placeholder
                    chunk_data["embedding"] = self._generate_embedding(chunk_text)
                    
                    self.stats["chunks_created"] += 1
                    yield chunk_data
                
                self.stats["files_processed"] += 1
                self.processed_files.add(str(json_file))
                
                if self.stats["files_processed"] % 10 == 0:
                    print(f"Processed {self.stats['files_processed']} files, "
                          f"created {self.stats['chunks_created']} chunks")
                
            except Exception as e:
                print(f"Error processing {json_file}: {e}")
                self.stats["errors"] += 1
    
    def _chunk_content(self, text: str, chunk_size: int, overlap: int) -> List[str]:
        """
        Split text into chunks with overlap.
        
        Args:
            text: Text to chunk
            chunk_size: Maximum size of each chunk
            overlap: Overlap between chunks
            
        Returns:
            List of text chunks
        """
        if not text:
            return []
        
        chunks = []
        start = 0
        text_len = len(text)
        
        while start < text_len:
            # Find end of chunk
            end = start + chunk_size
            
            # Try to break at sentence boundary
            if end < text_len:
                # Look for sentence end markers
                for marker in ['. ', '.\n', '! ', '? ', '\n\n']:
                    marker_pos = text.rfind(marker, start + overlap, end)
                    if marker_pos != -1:
                        end = marker_pos + len(marker)
                        break
            
            # Extract chunk
            chunk = text[start:end].strip()
            if chunk:
                chunks.append(chunk)
            
            # Move to next chunk with overlap
            start = end - overlap if end < text_len else text_len
        
        return chunks
    
    def _generate_embedding(self, text: str) -> List[float]:
        """
        Generate embedding for text chunk.
        
        This is a placeholder that returns a simple hash-based vector.
        In production, replace with actual embedding model.
        
        Args:
            text: Text to embed
            
        Returns:
            Embedding vector (placeholder)
        """
        # Placeholder: Generate deterministic pseudo-embedding from text hash
        text_hash = hashlib.md5(text.encode()).hexdigest()
        # Convert to list of 384 floats (typical embedding size)
        embedding = []
        for i in range(0, len(text_hash), 2):
            value = int(text_hash[i:i+2], 16) / 255.0
            embedding.append(value)
        
        # Pad to standard size (384 dimensions)
        while len(embedding) < 384:
            embedding.append(0.0)
        
        return embedding[:384]
    
    def export_to_jsonl(self, output_file: str, session_id: Optional[str] = None,
                       chunk_size: int = 1000, chunk_overlap: int = 200):
        """
        Export processed data to JSONL format.
        
        Args:
            output_file: Path to output JSONL file
            session_id: Session to process
            chunk_size: Chunk size for text splitting
            chunk_overlap: Overlap between chunks
        """
        print(f"Exporting to {output_file}...")
        
        with open(output_file, "w", encoding="utf-8") as f:
            for chunk in self.process_session(session_id, chunk_size, chunk_overlap):
                # Remove embedding for JSONL export (too large)
                chunk_export = {k: v for k, v in chunk.items() if k != "embedding"}
                f.write(json.dumps(chunk_export) + "\n")
        
        print(f"Export complete!")
        print(f"Files processed: {self.stats['files_processed']}")
        print(f"Chunks created: {self.stats['chunks_created']}")
        print(f"Errors: {self.stats['errors']}")
    
    def export_to_csv(self, output_file: str, session_id: Optional[str] = None):
        """
        Export processed data to CSV format.
        
        Args:
            output_file: Path to output CSV file
            session_id: Session to process
        """
        try:
            import pandas as pd
        except ImportError:
            raise ImportError("CSV export requires pandas. Install with: pip install pandas")
        
        print(f"Exporting to {output_file}...")
        
        chunks = []
        for chunk in self.process_session(session_id):
            # Flatten for CSV
            flat_chunk = {
                "chunk_id": chunk["chunk_id"],
                "url": chunk["url"],
                "chunk_index": chunk["chunk_index"],
                "content": chunk["content"],
                "title": chunk["metadata"].get("title", ""),
                "processed_at": chunk["processed_at"]
            }
            chunks.append(flat_chunk)
        
        df = pd.DataFrame(chunks)
        df.to_csv(output_file, index=False)
        
        print(f"Exported {len(chunks)} chunks to {output_file}")
    
    def get_session_info(self, session_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Get information about a session.
        
        Args:
            session_id: Session to analyze (latest if None)
            
        Returns:
            Session information
        """
        if session_id:
            session_dir = self.storage_path / session_id
        else:
            sessions = [d for d in self.storage_path.iterdir() if d.is_dir()]
            if not sessions:
                return {"error": "No sessions found"}
            session_dir = max(sessions, key=lambda d: d.stat().st_mtime)
        
        # Read statistics if available
        stats_file = session_dir / "statistics.json"
        if stats_file.exists():
            with open(stats_file, "r") as f:
                stats = json.load(f)
        else:
            stats = {}
        
        # Count files
        json_files = list(session_dir.rglob("*.json"))
        json_files = [f for f in json_files if f.name not in ["index.jsonl", "statistics.json"]]
        
        # Calculate total size
        total_size = sum(f.stat().st_size for f in json_files)
        
        return {
            "session_id": session_dir.name,
            "path": str(session_dir),
            "file_count": len(json_files),
            "total_size_mb": total_size / (1024 * 1024),
            "statistics": stats
        }


def main():
    """
    CLI interface for the batch processor.
    """
    import argparse
    
    parser = argparse.ArgumentParser(description="Process crawled data from disk storage")
    parser.add_argument("--storage", default="./crawled_data", help="Path to storage directory")
    parser.add_argument("--session", help="Session ID to process (latest if not specified)")
    parser.add_argument("--export", choices=["jsonl", "csv"], help="Export format")
    parser.add_argument("--output", help="Output file path")
    parser.add_argument("--chunk-size", type=int, default=1000, help="Chunk size")
    parser.add_argument("--chunk-overlap", type=int, default=200, help="Chunk overlap")
    parser.add_argument("--info", action="store_true", help="Show session information")
    
    args = parser.parse_args()
    
    processor = BatchProcessor(args.storage)
    
    if args.info:
        # Show session information
        info = processor.get_session_info(args.session)
        print("\nSession Information:")
        print("=" * 50)
        for key, value in info.items():
            if key != "statistics":
                print(f"{key}: {value}")
        if "statistics" in info and info["statistics"]:
            print("\nStatistics:")
            for key, value in info["statistics"].items():
                if not isinstance(value, (list, dict)):
                    print(f"  {key}: {value}")
    
    elif args.export and args.output:
        # Export data
        if args.export == "jsonl":
            processor.export_to_jsonl(args.output, args.session, 
                                    args.chunk_size, args.chunk_overlap)
        elif args.export == "csv":
            processor.export_to_csv(args.output, args.session)
    
    else:
        # Process and print chunks
        print("Processing chunks...")
        chunk_count = 0
        for chunk in processor.process_session(args.session, args.chunk_size, args.chunk_overlap):
            chunk_count += 1
            if chunk_count <= 3:  # Show first 3 chunks as examples
                print(f"\nChunk {chunk_count}:")
                print(f"  ID: {chunk['chunk_id']}")
                print(f"  URL: {chunk['url']}")
                print(f"  Content preview: {chunk['content'][:100]}...")
        
        print(f"\nTotal chunks processed: {chunk_count}")
        print(f"Files processed: {processor.stats['files_processed']}")
        print(f"Errors: {processor.stats['errors']}")


if __name__ == "__main__":
    main()