import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

from .config import ScraperConfig
from .api_client import ConfluenceAPIClient
from .extractors import (
    SpaceExtractor, PageExtractor, BlogPostExtractor,
    CommentExtractor, AttachmentExtractor, LabelExtractor,
    UserExtractor
)
from .checkpoint import CheckpointManager, ProgressTracker


class ConfluenceScraper:
    def __init__(self, config: ScraperConfig):
        self.config = config
        self.api_client = ConfluenceAPIClient(config)
        self.checkpoint_manager = CheckpointManager(config.checkpoint_file, config.output_dir)
        
        self._setup_logging()
        self._initialize_extractors()
        
        self.logger.info(f"Initialized Confluence Scraper")
        self.logger.info(f"Base URL: {config.base_url}")
        self.logger.info(f"Output directory: {config.output_dir}")
    
    def _setup_logging(self):
        log_file = Path(self.config.output_dir) / "logs" / f"scraper_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler(sys.stdout)
            ]
        )
        
        self.logger = logging.getLogger(__name__)
    
    def _initialize_extractors(self):
        self.space_extractor = SpaceExtractor(self.api_client, self.config.output_dir)
        self.page_extractor = PageExtractor(self.api_client, self.config.output_dir)
        self.blog_extractor = BlogPostExtractor(self.api_client, self.config.output_dir)
        self.comment_extractor = CommentExtractor(self.api_client, self.config.output_dir)
        self.attachment_extractor = AttachmentExtractor(self.api_client, self.config.output_dir)
        self.label_extractor = LabelExtractor(self.api_client, self.config.output_dir)
        self.user_extractor = UserExtractor(self.api_client, self.config.output_dir)
    
    def test_connection(self) -> bool:
        self.logger.info("Testing connection to Confluence API...")
        return self.api_client.test_connection()
    
    def scrape_all(self, resume: bool = True):
        if not self.test_connection():
            self.logger.error("Failed to connect to Confluence API. Please check your credentials.")
            return False
        
        if not resume:
            self.checkpoint_manager.reset()
            self.logger.info("Starting fresh scrape (checkpoint reset)")
        else:
            resume_point = self.checkpoint_manager.get_resume_point()
            if resume_point:
                self.logger.info(f"Resuming from space: {resume_point}")
        
        try:
            self._save_metadata()
            
            spaces = self.space_extractor.extract_all_spaces()
            self.checkpoint_manager.update_statistics("total_spaces", len(spaces))
            
            space_progress = ProgressTracker(len(spaces), "Processing spaces")
            
            for space in spaces:
                space_key = space.get("key", "unknown")
                
                if self.checkpoint_manager.is_space_completed(space_key):
                    self.logger.info(f"Skipping already completed space: {space_key}")
                    space_progress.update(1, f"Skipped {space_key}")
                    continue
                
                self.logger.info(f"Processing space: {space_key} - {space.get('name', 'Unknown')}")
                self.checkpoint_manager.mark_space_in_progress(space_key)
                
                try:
                    self._process_space(space)
                    self.checkpoint_manager.mark_space_completed(space_key)
                    space_progress.update(1, f"Completed {space_key}")
                except Exception as e:
                    self.logger.error(f"Failed to process space {space_key}: {e}")
                    self.checkpoint_manager.add_failed_item("space", space_key, str(e))
            
            space_progress.complete()
            self._generate_report()
            
            self.logger.info("Scraping completed successfully!")
            return True
            
        except Exception as e:
            self.logger.error(f"Fatal error during scraping: {e}")
            return False
    
    def _process_space(self, space: Dict):
        space_key = space.get("key")
        
        try:
            self.user_extractor.extract_space_permissions(space_key)
        except Exception as e:
            self.logger.warning(f"Failed to extract permissions for space {space_key}: {e}")
        
        pages = self.page_extractor.extract_pages_from_space(space_key)
        
        page_progress = ProgressTracker(len(pages), f"Processing pages in {space_key}")
        
        with ThreadPoolExecutor(max_workers=self.config.max_workers) as executor:
            futures = []
            
            for page in pages:
                page_id = page.get("id")
                
                if self.checkpoint_manager.is_page_completed(space_key, page_id):
                    page_progress.update(1, f"Skipped page {page_id}")
                    continue
                
                future = executor.submit(self._process_content_item, 
                                       page, "page", space_key)
                futures.append((future, page_id))
            
            for future, page_id in futures:
                try:
                    future.result()
                    self.checkpoint_manager.mark_page_completed(space_key, page_id)
                    page_progress.update(1, f"Completed page {page_id}")
                except Exception as e:
                    self.logger.error(f"Failed to process page {page_id}: {e}")
                    self.checkpoint_manager.add_failed_item("page", page_id, str(e))
        
        page_progress.complete()
        
        blogs = self.blog_extractor.extract_blogposts_from_space(space_key)
        
        if blogs:
            blog_progress = ProgressTracker(len(blogs), f"Processing blogs in {space_key}")
            
            for blog in blogs:
                blog_id = blog.get("id")
                try:
                    self._process_content_item(blog, "blogpost", space_key)
                    self.checkpoint_manager.mark_blog_completed(space_key, blog_id)
                    blog_progress.update(1, f"Completed blog {blog_id}")
                except Exception as e:
                    self.logger.error(f"Failed to process blog {blog_id}: {e}")
                    self.checkpoint_manager.add_failed_item("blog", blog_id, str(e))
            
            blog_progress.complete()
    
    def _process_content_item(self, content: Dict, content_type: str, space_key: str):
        content_id = content.get("id")
        
        try:
            comments = self.comment_extractor.extract_comments_for_content(
                content_id, content_type, space_key
            )
            if comments:
                self.checkpoint_manager.update_statistics("total_comments", len(comments))
        except Exception as e:
            self.logger.warning(f"Failed to extract comments for {content_type} {content_id}: {e}")
        
        try:
            attachments = self.attachment_extractor.extract_attachments_for_content(
                content_id, content_type, space_key
            )
            if attachments:
                self.checkpoint_manager.update_statistics("total_attachments", len(attachments))
        except Exception as e:
            self.logger.warning(f"Failed to extract attachments for {content_type} {content_id}: {e}")
        
        try:
            labels = self.label_extractor.extract_labels_for_content(
                content_id, content_type, space_key
            )
            
            if labels:
                labels_dir = Path(self.config.output_dir) / "spaces" / space_key / "labels"
                labels_dir.mkdir(parents=True, exist_ok=True)
                
                labels_file = labels_dir / f"{content_type}_{content_id}_labels.json"
                with open(labels_file, 'w') as f:
                    json.dump(labels, f, indent=2)
        except Exception as e:
            self.logger.warning(f"Failed to extract labels for {content_type} {content_id}: {e}")
    
    def _save_metadata(self):
        metadata = {
            "export_date": datetime.now().isoformat(),
            "confluence_url": self.config.base_url,
            "export_config": {
                "page_size": self.config.page_size,
                "max_workers": self.config.max_workers,
                "download_attachments": self.config.download_attachments,
                "export_format": self.config.export_format
            }
        }
        
        metadata_file = Path(self.config.output_dir) / "metadata.json"
        with open(metadata_file, 'w') as f:
            json.dump(metadata, f, indent=2)
    
    def _generate_report(self):
        stats = self.checkpoint_manager.get_statistics()
        failed_items = self.checkpoint_manager.checkpoint_data.get("failed_items", [])
        
        report = {
            "export_summary": {
                "start_time": self.checkpoint_manager.checkpoint_data.get("start_time"),
                "end_time": datetime.now().isoformat(),
                "confluence_url": self.config.base_url,
                "output_directory": self.config.output_dir
            },
            "statistics": stats,
            "failed_items": failed_items,
            "api_requests": {
                "total_requests": self.api_client.request_count
            }
        }
        
        report_file = Path(self.config.output_dir) / "export_report.json"
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        self.logger.info("\n" + "="*50)
        self.logger.info("EXPORT SUMMARY")
        self.logger.info("="*50)
        self.logger.info(f"Total Spaces: {stats.get('total_spaces', 0)}")
        self.logger.info(f"Processed Spaces: {stats.get('processed_spaces', 0)}")
        self.logger.info(f"Total Pages: {stats.get('total_pages', 0)}")
        self.logger.info(f"Total Blog Posts: {stats.get('total_blogs', 0)}")
        self.logger.info(f"Total Attachments: {stats.get('total_attachments', 0)}")
        self.logger.info(f"Total Comments: {stats.get('total_comments', 0)}")
        self.logger.info(f"Errors: {stats.get('errors', 0)}")
        self.logger.info(f"Total API Requests: {self.api_client.request_count}")
        self.logger.info("="*50)
        
        if failed_items:
            self.logger.warning(f"\nFailed items saved to: {report_file}")
            self.logger.warning(f"Total failed items: {len(failed_items)}")