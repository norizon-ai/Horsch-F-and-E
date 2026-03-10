"""Configuration management for HPC CLI.

Supports:
- TOML config file (~/.config/hpc-cli/config.toml)
- Environment variables
- Keyring for secure credential storage
"""

import os
import toml
import keyring
from pathlib import Path
from typing import Optional, Dict, Any
from dataclasses import dataclass, field, asdict
from rich.table import Table
from rich.console import Console


@dataclass
class LLMConfig:
    """LLM configuration."""
    url: str = "http://lme49.cs.fau.de:30000/v1"
    model: str = "openai/gpt-oss-120b"
    temperature: float = 0.2
    max_tokens: int = 2000
    timeout: int = 30
    api_key: str = "dummy"


@dataclass
class ElasticsearchConfig:
    """Elasticsearch configuration."""
    url: str = "http://localhost:9200"
    docs_index: str = "docs"
    tickets_index: str = "tickets"
    timeout: int = 10


@dataclass
class DRConfig:
    """Deep Research configuration."""
    api_url: str = "http://localhost:8001"  # DR API endpoint
    max_iterations: int = 3
    confidence_threshold: float = 0.6
    quality_threshold: float = 0.7
    max_search_results: int = 10
    timeout: int = 180  # DR can take a while


@dataclass
class ClusterCockpitConfig:
    """ClusterCockpit monitoring configuration."""
    url: str = "https://monitoring.nhr.fau.de"
    clusters: list = field(default_factory=lambda: ["alex", "helma"])
    timeout: int = 30
    # JWT token stored in keyring, not in config file


@dataclass
class Config:
    """Main configuration container."""
    llm: LLMConfig = field(default_factory=LLMConfig)
    elasticsearch: ElasticsearchConfig = field(default_factory=ElasticsearchConfig)
    dr: DRConfig = field(default_factory=DRConfig)
    clustercockpit: ClusterCockpitConfig = field(default_factory=ClusterCockpitConfig)

    @classmethod
    def get_config_path(cls) -> Path:
        """Get config file path."""
        config_dir = Path.home() / ".config" / "hpc-cli"
        config_dir.mkdir(parents=True, exist_ok=True)
        return config_dir / "config.toml"

    @classmethod
    def load(cls) -> "Config":
        """Load configuration from file and environment variables."""
        config_path = cls.get_config_path()

        # Start with defaults
        config_dict: Dict[str, Any] = {
            "llm": {},
            "elasticsearch": {},
            "dr": {},
            "clustercockpit": {}
        }

        # Load from TOML file if it exists
        if config_path.exists():
            try:
                file_config = toml.load(config_path)
                # Merge with defaults
                for section in config_dict.keys():
                    if section in file_config:
                        config_dict[section].update(file_config[section])
            except Exception as e:
                print(f"Warning: Failed to load config from {config_path}: {e}")

        # Override with environment variables
        # LLM
        if os.getenv("LLM_BASE_URL"):
            config_dict["llm"]["url"] = os.getenv("LLM_BASE_URL")
        if os.getenv("LLM_MODEL"):
            config_dict["llm"]["model"] = os.getenv("LLM_MODEL")
        if os.getenv("LLM_API_KEY"):
            config_dict["llm"]["api_key"] = os.getenv("LLM_API_KEY")

        # Elasticsearch
        if os.getenv("ELASTIC_URL"):
            config_dict["elasticsearch"]["url"] = os.getenv("ELASTIC_URL")
        if os.getenv("DOCS_INDEX"):
            config_dict["elasticsearch"]["docs_index"] = os.getenv("DOCS_INDEX")
        if os.getenv("TICKETS_INDEX"):
            config_dict["elasticsearch"]["tickets_index"] = os.getenv("TICKETS_INDEX")

        # DR
        if os.getenv("DR_API_URL"):
            config_dict["dr"]["api_url"] = os.getenv("DR_API_URL")
        if os.getenv("MAX_ITERATIONS"):
            config_dict["dr"]["max_iterations"] = int(os.getenv("MAX_ITERATIONS"))
        if os.getenv("CONFIDENCE_THRESHOLD"):
            config_dict["dr"]["confidence_threshold"] = float(os.getenv("CONFIDENCE_THRESHOLD"))

        # ClusterCockpit
        if os.getenv("CLUSTERCOCKPIT_URL"):
            config_dict["clustercockpit"]["url"] = os.getenv("CLUSTERCOCKPIT_URL")

        # Create config objects
        return cls(
            llm=LLMConfig(**config_dict["llm"]),
            elasticsearch=ElasticsearchConfig(**config_dict["elasticsearch"]),
            dr=DRConfig(**config_dict["dr"]),
            clustercockpit=ClusterCockpitConfig(**config_dict["clustercockpit"])
        )

    def save(self) -> None:
        """Save configuration to file."""
        config_path = self.get_config_path()

        config_dict = {
            "llm": asdict(self.llm),
            "elasticsearch": asdict(self.elasticsearch),
            "dr": asdict(self.dr),
            "clustercockpit": asdict(self.clustercockpit)
        }

        # Don't save sensitive data to file (use keyring instead)
        if "api_key" in config_dict["llm"] and config_dict["llm"]["api_key"] != "dummy":
            # Store in keyring
            keyring.set_password("hpc-cli", "llm_api_key", config_dict["llm"]["api_key"])
            config_dict["llm"]["api_key"] = "***stored-in-keyring***"

        with open(config_path, "w") as f:
            toml.dump(config_dict, f)

    def set(self, key: str, value: str) -> None:
        """Set configuration value using dot notation.

        Examples:
            config.set("llm.url", "http://localhost:11434/v1")
            config.set("dr.max_iterations", "5")
        """
        parts = key.split(".")

        if len(parts) != 2:
            raise ValueError(f"Invalid config key: {key}. Use format: section.key")

        section, attr = parts

        if section == "llm":
            setattr(self.llm, attr, self._convert_value(attr, value))
        elif section == "elasticsearch":
            setattr(self.elasticsearch, attr, self._convert_value(attr, value))
        elif section == "dr":
            setattr(self.dr, attr, self._convert_value(attr, value))
        elif section == "clustercockpit":
            if attr == "jwt":
                # Store JWT in keyring
                keyring.set_password("hpc-cli", "clustercockpit_jwt", value)
                return
            setattr(self.clustercockpit, attr, self._convert_value(attr, value))
        else:
            raise ValueError(f"Unknown config section: {section}")

        # Save to file
        self.save()

    def get_clustercockpit_jwt(self) -> Optional[str]:
        """Get ClusterCockpit JWT from keyring."""
        try:
            return keyring.get_password("hpc-cli", "clustercockpit_jwt")
        except Exception:
            return None

    def _convert_value(self, attr: str, value: str) -> Any:
        """Convert string value to appropriate type."""
        # Try to convert to int
        try:
            return int(value)
        except ValueError:
            pass

        # Try to convert to float
        try:
            return float(value)
        except ValueError:
            pass

        # Try to convert to bool
        if value.lower() in ("true", "yes", "1"):
            return True
        if value.lower() in ("false", "no", "0"):
            return False

        # Return as string
        return value

    def to_rich_table(self) -> Table:
        """Create Rich table for display."""
        table = Table(title="HPC CLI Configuration", show_header=True, header_style="bold magenta")
        table.add_column("Section", style="cyan", no_wrap=True)
        table.add_column("Setting", style="green")
        table.add_column("Value", style="yellow")

        # LLM
        table.add_row("LLM", "URL", self.llm.url)
        table.add_row("", "Model", self.llm.model)
        table.add_row("", "Temperature", str(self.llm.temperature))
        table.add_row("", "Max Tokens", str(self.llm.max_tokens))

        # Elasticsearch
        table.add_row("Elasticsearch", "URL", self.elasticsearch.url)
        table.add_row("", "Docs Index", self.elasticsearch.docs_index)
        table.add_row("", "Tickets Index", self.elasticsearch.tickets_index)

        # DR
        table.add_row("Deep Research", "API URL", self.dr.api_url)
        table.add_row("", "Max Iterations", str(self.dr.max_iterations))
        table.add_row("", "Confidence Threshold", str(self.dr.confidence_threshold))
        table.add_row("", "Timeout", f"{self.dr.timeout}s")

        # ClusterCockpit
        table.add_row("ClusterCockpit", "URL", self.clustercockpit.url)
        table.add_row("", "Clusters", ", ".join(self.clustercockpit.clusters))

        jwt = self.get_clustercockpit_jwt()
        jwt_status = "[green]✓ Configured[/green]" if jwt else "[red]✗ Not set[/red]"
        table.add_row("", "JWT Token", jwt_status)

        # Config file location
        table.add_row("", "", "")
        table.add_row("System", "Config File", str(self.get_config_path()))

        return table


# Global config instance
_config: Optional[Config] = None


def get_config() -> Config:
    """Get global config instance (lazy load)."""
    global _config
    if _config is None:
        _config = Config.load()
    return _config


def reload_config() -> Config:
    """Reload configuration from file."""
    global _config
    _config = Config.load()
    return _config
