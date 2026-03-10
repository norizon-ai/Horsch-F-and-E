from pydantic import BaseModel, Field, HttpUrl
from typing import Dict, List, Optional

class CrawlJob(BaseModel):
    """
    Represents a job request for the Intranet Connector to crawl a specific Intranet instance.
    """
    source_type: str = Field(..., description="The type of the source, e.g., 'INTRANET'.")
    base_url: HttpUrl = Field(..., description="The base URL of the Intranet instance to crawl.")
    auth_token: Optional[str] = Field(None, description="Authentication token for accessing the Intranet API.")
    start_urls: Optional[List[HttpUrl]] = Field(None, description="Specific URLs to start crawling from. If None, the connector will attempt to discover pages.")
    config: Dict = Field({}, description="Additional configuration specific to the Intranet instance.")
