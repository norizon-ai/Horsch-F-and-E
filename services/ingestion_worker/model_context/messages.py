"""Code copied from the intranet connector. This is the message sent through the message queue."""
from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class CrawledContentMessage(BaseModel):
    """
    Represents the message sent to the message queue after a page has been crawled.
    """
    source_type: str
    source_uri: str
    content: str
    metadata: Dict[str, Any]
    permissions: List[str]
