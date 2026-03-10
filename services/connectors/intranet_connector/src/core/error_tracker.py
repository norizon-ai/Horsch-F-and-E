"""
Error tracking and management for web crawling.

This module provides comprehensive error tracking, categorization,
and recovery mechanisms for failed crawl attempts.
"""

import json
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any, Set
from enum import Enum
from collections import defaultdict
import re


class ErrorType(Enum):
    """Categories of crawl errors."""
    TIMEOUT = "timeout"
    NETWORK = "network"
    DNS = "dns"
    CONNECTION = "connection"
    HTTP_ERROR = "http_error"
    PARSING = "parsing"
    UNKNOWN = "unknown"


class CrawlError:
    """Represents a single crawl error."""
    
    def __init__(self, url: str, error_message: str, error_type: Optional[ErrorType] = None,
                 timestamp: Optional[datetime] = None, retry_count: int = 0,
                 status_code: Optional[int] = None):
        """
        Initialize a crawl error.
        
        Args:
            url: The URL that failed
            error_message: The error message
            error_type: Type of error (auto-detected if None)
            timestamp: When the error occurred
            retry_count: Number of retry attempts
            status_code: HTTP status code if applicable
        """
        self.url = url
        self.error_message = error_message
        self.error_type = error_type or self._detect_error_type(error_message)
        self.timestamp = timestamp or datetime.now(timezone.utc)
        self.retry_count = retry_count
        self.status_code = status_code
    
    def _detect_error_type(self, error_message: str) -> ErrorType:
        """
        Auto-detect error type from error message.
        
        Args:
            error_message: The error message to analyze
            
        Returns:
            Detected error type
        """
        error_lower = error_message.lower()
        
        if any(x in error_lower for x in ['timeout', 'timed out', 'time-out']):
            return ErrorType.TIMEOUT
        elif any(x in error_lower for x in ['dns', 'nxdomain', 'name resolution']):
            return ErrorType.DNS
        elif any(x in error_lower for x in ['connection', 'refused', 'reset']):
            return ErrorType.CONNECTION
        elif any(x in error_lower for x in ['network', 'net::', 'err_']):
            return ErrorType.NETWORK
        elif any(x in error_lower for x in ['404', '403', '500', '502', '503', 'status']):
            return ErrorType.HTTP_ERROR
        elif any(x in error_lower for x in ['parsing', 'parse', 'decode']):
            return ErrorType.PARSING
        else:
            return ErrorType.UNKNOWN
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            "url": self.url,
            "error_message": self.error_message,
            "error_type": self.error_type.value,
            "timestamp": self.timestamp.isoformat(),
            "retry_count": self.retry_count,
            "status_code": self.status_code
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CrawlError':
        """Create from dictionary."""
        return cls(
            url=data["url"],
            error_message=data["error_message"],
            error_type=ErrorType(data["error_type"]),
            timestamp=datetime.fromisoformat(data["timestamp"]),
            retry_count=data.get("retry_count", 0),
            status_code=data.get("status_code")
        )


class ErrorTracker:
    """
    Tracks and manages crawl errors.
    
    Features:
    - Error categorization and analysis
    - Persistent storage of failed URLs
    - Retry management
    - Error reporting and statistics
    """
    
    def __init__(self, storage_path: str = "./crawled_data", session_id: Optional[str] = None):
        """
        Initialize the error tracker.
        
        Args:
            storage_path: Base directory for error logs
            session_id: Session ID for this crawl
        """
        self.storage_path = Path(storage_path)
        self.session_id = session_id or datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        self.errors: List[CrawlError] = []
        self.error_file = None
        self.stats = defaultdict(int)
        
    def initialize(self) -> None:
        """Initialize error tracking files."""
        session_dir = self.storage_path / self.session_id
        session_dir.mkdir(parents=True, exist_ok=True)
        
        # Open error log file
        error_log_path = session_dir / "failed_urls.jsonl"
        self.error_file = open(error_log_path, "a", encoding="utf-8")
        
        # Load existing errors if any
        if error_log_path.exists() and error_log_path.stat().st_size > 0:
            self._load_existing_errors(error_log_path)
    
    def _load_existing_errors(self, error_log_path: Path) -> None:
        """Load existing errors from file."""
        with open(error_log_path, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    error_data = json.loads(line)
                    error = CrawlError.from_dict(error_data)
                    self.errors.append(error)
                    self.stats[error.error_type.value] += 1
                except (json.JSONDecodeError, KeyError):
                    continue
    
    def add_error(self, url: str, error_message: str, retry_count: int = 0) -> CrawlError:
        """
        Add a new error to tracking.
        
        Args:
            url: Failed URL
            error_message: Error message
            retry_count: Number of retries attempted
            
        Returns:
            The created CrawlError object
        """
        error = CrawlError(url, error_message, retry_count=retry_count)
        self.errors.append(error)
        self.stats[error.error_type.value] += 1
        
        # Write to file immediately
        if self.error_file:
            self.error_file.write(json.dumps(error.to_dict()) + "\n")
            self.error_file.flush()
        
        return error
    
    def get_retryable_urls(self, max_retries: int = 3) -> List[str]:
        """
        Get URLs that can be retried.
        
        Args:
            max_retries: Maximum retry attempts
            
        Returns:
            List of URLs eligible for retry
        """
        retryable_types = {ErrorType.TIMEOUT, ErrorType.NETWORK, ErrorType.CONNECTION}
        retryable = []
        
        for error in self.errors:
            if error.error_type in retryable_types and error.retry_count < max_retries:
                retryable.append(error.url)
        
        return list(set(retryable))  # Remove duplicates
    
    def get_permanent_failures(self, max_retries: int = 3) -> List[CrawlError]:
        """
        Get URLs that have permanently failed.
        
        Args:
            max_retries: Maximum retry attempts
            
        Returns:
            List of permanently failed errors
        """
        permanent = []
        for error in self.errors:
            if error.retry_count >= max_retries:
                permanent.append(error)
        
        return permanent
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Get error statistics.
        
        Returns:
            Dictionary with error statistics
        """
        total_errors = len(self.errors)
        unique_urls = len(set(e.url for e in self.errors))
        
        # Count by error type
        error_by_type = defaultdict(int)
        for error in self.errors:
            error_by_type[error.error_type.value] += 1
        
        # Find most common errors
        error_patterns = defaultdict(int)
        for error in self.errors:
            # Extract common error patterns
            if "timeout" in error.error_message.lower():
                error_patterns["Timeout errors"] += 1
            elif "404" in error.error_message:
                error_patterns["404 Not Found"] += 1
            elif "connection" in error.error_message.lower():
                error_patterns["Connection errors"] += 1
        
        return {
            "total_errors": total_errors,
            "unique_failed_urls": unique_urls,
            "errors_by_type": dict(error_by_type),
            "common_patterns": dict(error_patterns),
            "retryable_urls": len(self.get_retryable_urls()),
            "permanent_failures": len(self.get_permanent_failures())
        }
    
    def generate_report(self) -> str:
        """
        Generate a human-readable error report.
        
        Returns:
            Formatted error report
        """
        stats = self.get_statistics()
        
        report = []
        report.append("=" * 60)
        report.append("CRAWL ERROR REPORT")
        report.append("=" * 60)
        report.append(f"Session: {self.session_id}")
        report.append(f"Total errors: {stats['total_errors']}")
        report.append(f"Unique failed URLs: {stats['unique_failed_urls']}")
        report.append("")
        
        # Errors by type
        report.append("Errors by Type:")
        for error_type, count in stats['errors_by_type'].items():
            percentage = (count / stats['total_errors'] * 100) if stats['total_errors'] > 0 else 0
            report.append(f"  {error_type:15} {count:5} ({percentage:.1f}%)")
        
        report.append("")
        report.append(f"Retryable URLs: {stats['retryable_urls']}")
        report.append(f"Permanent failures: {stats['permanent_failures']}")
        
        # Sample of failed URLs
        report.append("")
        report.append("Sample Failed URLs:")
        for error in self.errors[:10]:  # Show first 10
            report.append(f"  {error.url}")
            report.append(f"    Error: {error.error_message[:80]}...")
            report.append(f"    Type: {error.error_type.value}, Retries: {error.retry_count}")
        
        # Recommendations
        report.append("")
        report.append("Recommendations:")
        
        timeout_errors = stats['errors_by_type'].get('timeout', 0)
        if timeout_errors > stats['total_errors'] * 0.3:
            report.append("  ⚠️ High timeout rate detected. Consider:")
            report.append("     - Increasing page_timeout setting")
            report.append("     - Checking network connectivity")
            report.append("     - Reducing crawl speed")
        
        network_errors = stats['errors_by_type'].get('network', 0)
        if network_errors > stats['total_errors'] * 0.2:
            report.append("  ⚠️ Network errors detected. Consider:")
            report.append("     - Checking internet connection")
            report.append("     - Verifying DNS settings")
            report.append("     - Using a different network")
        
        report.append("=" * 60)
        
        return "\n".join(report)
    
    def export_failed_urls(self, output_file: str, format: str = "txt") -> None:
        """
        Export failed URLs to a file.
        
        Args:
            output_file: Output file path
            format: Export format (txt, json, csv)
        """
        output_path = Path(output_file)
        
        if format == "txt":
            with open(output_path, "w", encoding="utf-8") as f:
                for error in self.errors:
                    f.write(f"{error.url}\n")
        
        elif format == "json":
            errors_data = [e.to_dict() for e in self.errors]
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(errors_data, f, indent=2)
        
        elif format == "csv":
            import csv
            with open(output_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["URL", "Error Type", "Error Message", "Retry Count", "Timestamp"])
                for error in self.errors:
                    writer.writerow([
                        error.url,
                        error.error_type.value,
                        error.error_message,
                        error.retry_count,
                        error.timestamp.isoformat()
                    ])
        
        print(f"Exported {len(self.errors)} failed URLs to {output_path}")
    
    def close(self) -> None:
        """Close error tracking files."""
        if self.error_file:
            # Write final statistics
            stats_file = self.storage_path / self.session_id / "error_statistics.json"
            with open(stats_file, "w", encoding="utf-8") as f:
                json.dump(self.get_statistics(), f, indent=2)
            
            self.error_file.close()
            
            # Generate and save report
            report_file = self.storage_path / self.session_id / "error_report.txt"
            with open(report_file, "w", encoding="utf-8") as f:
                f.write(self.generate_report())