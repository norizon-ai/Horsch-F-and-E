import logging
from typing import Dict, List, Optional


class APIVersionAdapter:
    """Adapter to handle differences between Confluence API v1 and v2"""
    
    def __init__(self, api_client):
        self.api_client = api_client
        self.logger = logging.getLogger(__name__)
        self.api_version = self._detect_api_version()
    
    def _detect_api_version(self) -> str:
        """Detect which API version is available"""
        try:
            response = self.api_client.get("/api/v2/spaces?limit=1")
            if response:
                self.logger.info("Using Confluence API v2")
                return "v2"
        except:
            pass
        
        try:
            response = self.api_client.get("/rest/api/space?limit=1")
            if response:
                self.logger.info("Using Confluence API v1")
                return "v1"
        except:
            pass
        
        self.logger.warning("Could not detect API version, defaulting to v1")
        return "v1"
    
    def get_spaces_endpoint(self) -> str:
        return "/api/v2/spaces" if self.api_version == "v2" else "/rest/api/space"
    
    def get_pages_endpoint(self, space_key: str) -> str:
        if self.api_version == "v2":
            return f"/api/v2/spaces/{space_key}/pages"
        else:
            # v1 uses content endpoint with type filter
            return f"/rest/api/content?spaceKey={space_key}&type=page"
    
    def get_blogposts_endpoint(self, space_key: str) -> str:
        if self.api_version == "v2":
            return f"/api/v2/spaces/{space_key}/blogposts"
        else:
            # v1 uses content endpoint with type filter
            return f"/rest/api/content?spaceKey={space_key}&type=blogpost"
    
    def get_content_endpoint(self, content_id: str) -> str:
        if self.api_version == "v2":
            return f"/api/v2/pages/{content_id}"
        else:
            return f"/rest/api/content/{content_id}"
    
    def get_comments_endpoint(self, content_id: str, content_type: str) -> str:
        if self.api_version == "v2":
            return f"/api/v2/{content_type}s/{content_id}/footer-comments"
        else:
            return f"/rest/api/content/{content_id}/child/comment"
    
    def get_attachments_endpoint(self, content_id: str, content_type: str) -> str:
        if self.api_version == "v2":
            return f"/api/v2/{content_type}s/{content_id}/attachments"
        else:
            return f"/rest/api/content/{content_id}/child/attachment"
    
    def get_labels_endpoint(self, content_id: str, content_type: str) -> str:
        if self.api_version == "v2":
            return f"/api/v2/{content_type}s/{content_id}/labels"
        else:
            return f"/rest/api/content/{content_id}/label"
    
    def get_permissions_endpoint(self, space_key: str) -> str:
        if self.api_version == "v2":
            return f"/api/v2/spaces/{space_key}/permissions"
        else:
            return f"/rest/api/space/{space_key}/permission"
    
    def get_expand_fields(self, content_type: str) -> List[str]:
        """Get appropriate expand fields based on API version and content type"""
        if self.api_version == "v2":
            if content_type == "space":
                return ["permissions", "settings", "theme", "lookAndFeel"]
            elif content_type in ["page", "blogpost"]:
                return ["body.storage", "body.view", "version", "ancestors", 
                       "children", "history", "metadata.labels", "restrictions"]
            elif content_type == "comment":
                return ["body.storage", "version", "history"]
            else:
                return []
        else:  # v1
            if content_type == "space":
                # Minimal expand for v1 to avoid 500 errors
                return []
            elif content_type in ["page", "blogpost"]:
                # Start with minimal and gradually add more
                return ["body.storage", "version", "metadata.labels"]
            elif content_type == "comment":
                return ["body.storage", "version"]
            else:
                return []
    
    def adapt_space_data(self, space: Dict) -> Dict:
        """Normalize space data between API versions"""
        if self.api_version == "v1":
            # v1 might have different structure
            return {
                "key": space.get("key"),
                "name": space.get("name"),
                "id": space.get("id"),
                "type": space.get("type"),
                "_links": space.get("_links", {})
            }
        return space
    
    def adapt_content_data(self, content: Dict) -> Dict:
        """Normalize content data between API versions"""
        if self.api_version == "v1":
            # Adapt v1 response to be more like v2
            return {
                "id": content.get("id"),
                "title": content.get("title"),
                "type": content.get("type"),
                "body": content.get("body", {}),
                "version": content.get("version", {}),
                "space": content.get("space", {}),
                "_links": content.get("_links", {})
            }
        return content