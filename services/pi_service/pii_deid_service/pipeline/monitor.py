"""
PipelineMonitor for PII De-identification Service.

This module tracks execution progress and performance metrics.
"""

import time
import logging
from typing import Dict, Any, Optional, List
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

logger = logging.getLogger(__name__)


class ProcessingStatus(Enum):
    """Processing status enumeration."""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


@dataclass
class ProcessingMetrics:
    """Metrics for processing operations."""
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    total_items: int = 0
    processed_items: int = 0
    failed_items: int = 0
    entities_detected: int = 0
    processing_time: float = 0.0
    avg_time_per_item: float = 0.0
    
    def start(self):
        """Start timing."""
        self.start_time = datetime.now()
    
    def end(self):
        """End timing and calculate metrics."""
        self.end_time = datetime.now()
        if self.start_time:
            self.processing_time = (self.end_time - self.start_time).total_seconds()
            if self.processed_items > 0:
                self.avg_time_per_item = self.processing_time / self.processed_items
    
    def update_progress(self, items_processed: int = 1, entities_found: int = 0):
        """Update progress metrics."""
        self.processed_items += items_processed
        self.entities_detected += entities_found
    
    def mark_failed(self, count: int = 1):
        """Mark items as failed."""
        self.failed_items += count


class PipelineMonitor:
    """Monitors pipeline execution progress and performance."""
    
    def __init__(self, pipeline_name: str = "default"):
        """Initialize the monitor.
        
        Args:
            pipeline_name: Name of the pipeline being monitored
        """
        self.pipeline_name = pipeline_name
        self.status = ProcessingStatus.PENDING
        self.metrics = ProcessingMetrics()
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.start_time = None
        self.end_time = None
        
    def start_processing(self, total_items: int = 0):
        """Start processing monitoring.
        
        Args:
            total_items: Total number of items to process
        """
        self.status = ProcessingStatus.RUNNING
        self.start_time = datetime.now()
        self.metrics.total_items = total_items
        self.metrics.start()
        logger.info(f"Pipeline {self.pipeline_name} started processing {total_items} items")
    
    def update_progress(self, items_processed: int = 1, entities_found: int = 0):
        """Update processing progress.
        
        Args:
            items_processed: Number of items processed in this update
            entities_found: Number of entities found in this update
        """
        self.metrics.update_progress(items_processed, entities_found)
        
        # Log progress every 10% or every 100 items
        if (self.metrics.processed_items % 100 == 0 or 
            (self.metrics.total_items > 0 and 
             self.metrics.processed_items % max(1, self.metrics.total_items // 10) == 0)):
            
            progress_pct = (self.metrics.processed_items / self.metrics.total_items * 100) if self.metrics.total_items > 0 else 0
            logger.info(f"Pipeline {self.pipeline_name} progress: {self.metrics.processed_items}/{self.metrics.total_items} ({progress_pct:.1f}%)")
    
    def mark_failed(self, error_message: str, count: int = 1):
        """Mark items as failed.
        
        Args:
            error_message: Error message
            count: Number of items that failed
        """
        self.metrics.mark_failed(count)
        self.errors.append(f"{datetime.now()}: {error_message}")
        logger.error(f"Pipeline {self.pipeline_name} error: {error_message}")
    
    def add_warning(self, warning_message: str):
        """Add a warning message.
        
        Args:
            warning_message: Warning message
        """
        self.warnings.append(f"{datetime.now()}: {warning_message}")
        logger.warning(f"Pipeline {self.pipeline_name} warning: {warning_message}")
    
    def complete_processing(self):
        """Mark processing as completed."""
        self.status = ProcessingStatus.COMPLETED
        self.end_time = datetime.now()
        self.metrics.end()
        
        logger.info(f"Pipeline {self.pipeline_name} completed successfully")
        logger.info(f"Processing time: {self.metrics.processing_time:.2f}s")
        logger.info(f"Items processed: {self.metrics.processed_items}/{self.metrics.total_items}")
        logger.info(f"Entities detected: {self.metrics.entities_detected}")
        logger.info(f"Failed items: {self.metrics.failed_items}")
        if self.metrics.avg_time_per_item > 0:
            logger.info(f"Average time per item: {self.metrics.avg_time_per_item:.3f}s")
    
    def fail_processing(self, error_message: str):
        """Mark processing as failed.
        
        Args:
            error_message: Error message
        """
        self.status = ProcessingStatus.FAILED
        self.end_time = datetime.now()
        self.metrics.end()
        self.errors.append(f"{datetime.now()}: {error_message}")
        
        logger.error(f"Pipeline {self.pipeline_name} failed: {error_message}")
    
    def cancel_processing(self):
        """Cancel processing."""
        self.status = ProcessingStatus.CANCELLED
        self.end_time = datetime.now()
        self.metrics.end()
        
        logger.info(f"Pipeline {self.pipeline_name} cancelled")
    
    def get_summary(self) -> Dict[str, Any]:
        """Get processing summary.
        
        Returns:
            Dictionary with processing summary
        """
        return {
            "pipeline_name": self.pipeline_name,
            "status": self.status.value,
            "start_time": self.start_time.isoformat() if self.start_time else None,
            "end_time": self.end_time.isoformat() if self.end_time else None,
            "total_items": self.metrics.total_items,
            "processed_items": self.metrics.processed_items,
            "failed_items": self.metrics.failed_items,
            "entities_detected": self.metrics.entities_detected,
            "processing_time": self.metrics.processing_time,
            "avg_time_per_item": self.metrics.avg_time_per_item,
            "error_count": len(self.errors),
            "warning_count": len(self.warnings),
            "success_rate": (self.metrics.processed_items - self.metrics.failed_items) / max(1, self.metrics.processed_items) * 100
        }
    
    def log_summary(self):
        """Log processing summary."""
        summary = self.get_summary()
        logger.info("=== Pipeline Processing Summary ===")
        for key, value in summary.items():
            if isinstance(value, float):
                logger.info(f"{key}: {value:.2f}")
            else:
                logger.info(f"{key}: {value}")
        logger.info("===================================") 