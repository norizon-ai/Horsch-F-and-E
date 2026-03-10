import os
from dataclasses import dataclass
from typing import Optional
import json
from pathlib import Path


@dataclass
class ScraperConfig:
    base_url: str
    bearer_token: str
    output_dir: str = "confluence_export"
    max_workers: int = 5
    page_size: int = 50
    retry_max_attempts: int = 3
    retry_wait_exponential_multiplier: int = 2
    retry_wait_exponential_max: int = 60
    request_timeout: int = 30
    download_attachments: bool = True
    export_format: list = None
    checkpoint_file: str = "checkpoint.json"
    
    def __post_init__(self):
        if self.export_format is None:
            self.export_format = ["json", "html"]
        
        self.base_url = self.base_url.rstrip("/")
        
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)
        Path(f"{self.output_dir}/logs").mkdir(parents=True, exist_ok=True)
    
    @classmethod
    def from_file(cls, config_file: str) -> "ScraperConfig":
        with open(config_file, "r") as f:
            config_data = json.load(f)
        return cls(**config_data)
    
    def save_to_file(self, config_file: str):
        config_data = {
            "base_url": self.base_url,
            "bearer_token": self.bearer_token,
            "output_dir": self.output_dir,
            "max_workers": self.max_workers,
            "page_size": self.page_size,
            "retry_max_attempts": self.retry_max_attempts,
            "retry_wait_exponential_multiplier": self.retry_wait_exponential_multiplier,
            "retry_wait_exponential_max": self.retry_wait_exponential_max,
            "request_timeout": self.request_timeout,
            "download_attachments": self.download_attachments,
            "export_format": self.export_format,
            "checkpoint_file": self.checkpoint_file
        }
        with open(config_file, "w") as f:
            json.dump(config_data, f, indent=2)