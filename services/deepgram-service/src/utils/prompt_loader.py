import logging
from pathlib import Path
from string import Template
from src.config import settings
import yaml

logger = logging.getLogger(__name__)

def load_prompt(name: str, **variables) -> dict[str, str]:
    """Load a YAML prompt template and substitute variables."""

    path = Path(settings.prompts_dir) / f"{name}.yaml"
    with open(path) as f:
        raw = yaml.safe_load(f)

    result = {}
    for key in ("system", "user"):
        if key in raw:
            result[key] = Template(str(raw[key])).safe_substitute(**variables)
    return result


def load_patterns(name: str = "patterns") -> dict[str, list[str]]:
    """Load pattern templates from prompts/{name}.yaml. File is read on every call — edits take effect immediately."""

    path = Path(settings.prompts_dir) / f"{name}.yaml"
    with open(path) as f:
        return yaml.safe_load(f)