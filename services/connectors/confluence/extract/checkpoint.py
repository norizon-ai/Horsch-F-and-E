import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Set
from pathlib import Path
import logging


class CheckpointManager:
    def __init__(self, checkpoint_file: str, output_dir: str):
        self.checkpoint_file = os.path.join(output_dir, checkpoint_file)
        self.output_dir = output_dir
        self.logger = logging.getLogger(__name__)
        self.checkpoint_data = self._load_checkpoint()
    
    def _load_checkpoint(self) -> Dict:
        if os.path.exists(self.checkpoint_file):
            try:
                with open(self.checkpoint_file, 'r') as f:
                    data = json.load(f)
                    self.logger.info(f"Loaded checkpoint from {self.checkpoint_file}")
                    return data
            except Exception as e:
                self.logger.error(f"Failed to load checkpoint: {e}")
        
        return {
            "start_time": datetime.now().isoformat(),
            "last_update": datetime.now().isoformat(),
            "completed_spaces": [],
            "in_progress_space": None,
            "completed_pages": {},
            "completed_blogs": {},
            "failed_items": [],
            "statistics": {
                "total_spaces": 0,
                "processed_spaces": 0,
                "total_pages": 0,
                "total_blogs": 0,
                "total_attachments": 0,
                "total_comments": 0,
                "errors": 0
            }
        }
    
    def save_checkpoint(self):
        self.checkpoint_data["last_update"] = datetime.now().isoformat()
        
        try:
            with open(self.checkpoint_file, 'w') as f:
                json.dump(self.checkpoint_data, f, indent=2)
            self.logger.debug("Checkpoint saved")
        except Exception as e:
            self.logger.error(f"Failed to save checkpoint: {e}")
    
    def mark_space_completed(self, space_key: str):
        if space_key not in self.checkpoint_data["completed_spaces"]:
            self.checkpoint_data["completed_spaces"].append(space_key)
            self.checkpoint_data["statistics"]["processed_spaces"] += 1
        
        if self.checkpoint_data["in_progress_space"] == space_key:
            self.checkpoint_data["in_progress_space"] = None
        
        self.save_checkpoint()
    
    def mark_space_in_progress(self, space_key: str):
        self.checkpoint_data["in_progress_space"] = space_key
        self.save_checkpoint()
    
    def is_space_completed(self, space_key: str) -> bool:
        return space_key in self.checkpoint_data["completed_spaces"]
    
    def mark_page_completed(self, space_key: str, page_id: str):
        if space_key not in self.checkpoint_data["completed_pages"]:
            self.checkpoint_data["completed_pages"][space_key] = []
        
        if page_id not in self.checkpoint_data["completed_pages"][space_key]:
            self.checkpoint_data["completed_pages"][space_key].append(page_id)
            self.checkpoint_data["statistics"]["total_pages"] += 1
        
        self.save_checkpoint()
    
    def is_page_completed(self, space_key: str, page_id: str) -> bool:
        return (space_key in self.checkpoint_data["completed_pages"] and 
                page_id in self.checkpoint_data["completed_pages"][space_key])
    
    def mark_blog_completed(self, space_key: str, blog_id: str):
        if space_key not in self.checkpoint_data["completed_blogs"]:
            self.checkpoint_data["completed_blogs"][space_key] = []
        
        if blog_id not in self.checkpoint_data["completed_blogs"][space_key]:
            self.checkpoint_data["completed_blogs"][space_key].append(blog_id)
            self.checkpoint_data["statistics"]["total_blogs"] += 1
        
        self.save_checkpoint()
    
    def add_failed_item(self, item_type: str, item_id: str, error: str):
        failed_item = {
            "type": item_type,
            "id": item_id,
            "error": str(error),
            "timestamp": datetime.now().isoformat()
        }
        self.checkpoint_data["failed_items"].append(failed_item)
        self.checkpoint_data["statistics"]["errors"] += 1
        self.save_checkpoint()
    
    def update_statistics(self, stat_name: str, value: int = 1):
        if stat_name in self.checkpoint_data["statistics"]:
            self.checkpoint_data["statistics"][stat_name] += value
        else:
            self.checkpoint_data["statistics"][stat_name] = value
        self.save_checkpoint()
    
    def get_resume_point(self) -> Optional[str]:
        return self.checkpoint_data.get("in_progress_space")
    
    def get_statistics(self) -> Dict:
        return self.checkpoint_data["statistics"]
    
    def reset(self):
        self.checkpoint_data = self._load_checkpoint()
        self.checkpoint_data["start_time"] = datetime.now().isoformat()
        self.checkpoint_data["completed_spaces"] = []
        self.checkpoint_data["in_progress_space"] = None
        self.checkpoint_data["completed_pages"] = {}
        self.checkpoint_data["completed_blogs"] = {}
        self.checkpoint_data["failed_items"] = []
        self.checkpoint_data["statistics"] = {
            "total_spaces": 0,
            "processed_spaces": 0,
            "total_pages": 0,
            "total_blogs": 0,
            "total_attachments": 0,
            "total_comments": 0,
            "errors": 0
        }
        self.save_checkpoint()


class ProgressTracker:
    def __init__(self, total_items: int = 0, description: str = "Processing"):
        self.total_items = total_items
        self.current_item = 0
        self.description = description
        self.start_time = datetime.now()
        self.logger = logging.getLogger(__name__)
    
    def update(self, increment: int = 1, message: str = None):
        self.current_item += increment
        
        if self.total_items > 0:
            progress = (self.current_item / self.total_items) * 100
            elapsed = (datetime.now() - self.start_time).total_seconds()
            
            if self.current_item > 0:
                eta_seconds = (elapsed / self.current_item) * (self.total_items - self.current_item)
                eta_str = self._format_time(eta_seconds)
            else:
                eta_str = "N/A"
            
            progress_msg = f"{self.description}: {self.current_item}/{self.total_items} ({progress:.1f}%) - ETA: {eta_str}"
            
            if message:
                progress_msg += f" - {message}"
            
            self.logger.info(progress_msg)
    
    def _format_time(self, seconds: float) -> str:
        if seconds < 60:
            return f"{int(seconds)}s"
        elif seconds < 3600:
            return f"{int(seconds / 60)}m {int(seconds % 60)}s"
        else:
            hours = int(seconds / 3600)
            minutes = int((seconds % 3600) / 60)
            return f"{hours}h {minutes}m"
    
    def complete(self):
        elapsed = (datetime.now() - self.start_time).total_seconds()
        self.logger.info(f"{self.description} completed in {self._format_time(elapsed)}")