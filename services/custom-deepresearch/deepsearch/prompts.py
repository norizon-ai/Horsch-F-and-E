"""
Prompts Module

Manages prompt templates for the deepsearch system.
"""

from pathlib import Path
from typing import Dict, Optional
import yaml


class PromptManager:
    """
    Manages prompt templates loaded from YAML files.
    """
    
    def __init__(self, prompts_dir: Path | str = None):
        """
        Initialize prompt manager.
        
        Args:
            prompts_dir: Directory containing prompt YAML files
        """
        self.prompts_dir = Path(prompts_dir) if prompts_dir else Path("/app/prompts")
        self._prompts: Dict[str, str] = {}
        self._load_prompts()
    
    def _load_prompts(self) -> None:
        """Load all prompt templates from directory."""
        if not self.prompts_dir.exists():
            return
        
        for prompt_file in self.prompts_dir.glob("*.yml"):
            try:
                with open(prompt_file, "r") as f:
                    data = yaml.safe_load(f)
                    if data and isinstance(data, dict):
                        # Support both direct string and nested structure
                        for key, value in data.items():
                            if isinstance(value, str):
                                self._prompts[key] = value
                            elif isinstance(value, dict) and "template" in value:
                                self._prompts[key] = value["template"]
            except Exception as e:
                print(f"Warning: Failed to load prompt file {prompt_file}: {e}")
    
    def get(self, name: str, default: Optional[str] = None) -> str:
        """
        Get a prompt template by name.
        
        Args:
            name: Prompt template name
            default: Default value if prompt not found
            
        Returns:
            Prompt template string
        """
        return self._prompts.get(name, default or "")
    
    def format(self, name: str, **kwargs) -> str:
        """
        Get and format a prompt template.
        
        Args:
            name: Prompt template name
            **kwargs: Variables to interpolate into template
            
        Returns:
            Formatted prompt string
        """
        template = self.get(name)
        try:
            return template.format(**kwargs)
        except KeyError as e:
            raise ValueError(f"Missing required variable {e} for prompt '{name}'")
    
    def has(self, name: str) -> bool:
        """Check if a prompt template exists."""
        return name in self._prompts
    
    def list_prompts(self) -> list[str]:
        """List all available prompt names."""
        return list(self._prompts.keys())


__all__ = ["PromptManager"]
