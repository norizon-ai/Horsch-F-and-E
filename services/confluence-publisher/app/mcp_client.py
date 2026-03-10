"""
Confluence Publisher - MCP Client.

Thin client that calls the mcp-atlassian server to create/update pages.
Uses the MCP SDK with SSE transport.
"""

import json
import logging
import os
import base64
import urllib.request
from typing import Any, Dict, List, Optional

from mcp import ClientSession
from mcp.client.sse import sse_client
from mcp.types import TextContent

logger = logging.getLogger(__name__)


class ConfluenceMCPPublisher:
    """Client for publishing pages to Confluence via the MCP server."""

    def __init__(self, mcp_server_url: str):
        self.mcp_server_url = mcp_server_url.rstrip("/")

    async def create_page(
        self,
        space_key: str,
        title: str,
        content_markdown: str,
        parent_page_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Create a Confluence page via the MCP server.

        Args:
            space_key: Confluence space key (e.g. "DOCS")
            title: Page title
            content_markdown: Page content as markdown
            parent_page_id: Optional parent page ID for nesting

        Returns:
            Dict with page_id and url of the created page
        """
        arguments: Dict[str, Any] = {
            "space_key": space_key,
            "title": title,
            "content": content_markdown,
        }
        if parent_page_id:
            arguments["parent_id"] = parent_page_id

        result = await self._call_mcp_tool(
            "confluence_create_page", arguments
        )

        return self._parse_create_response(result)

    async def update_page(
        self,
        page_id: str,
        title: str,
        content_markdown: str,
    ) -> Dict[str, Any]:
        """
        Update an existing Confluence page via the MCP server.

        Args:
            page_id: ID of the page to update
            title: Updated page title
            content_markdown: Updated content as markdown

        Returns:
            Dict with page_id and url of the updated page
        """
        result = await self._call_mcp_tool(
            "confluence_update_page",
            {
                "page_id": page_id,
                "title": title,
                "content": content_markdown,
            },
        )

        return self._parse_create_response(result)

    async def get_spaces(self) -> List[Dict[str, Any]]:
        """
        Get list of Confluence spaces via the MCP server or REST API fallback.
        """
        try:
            result = await self._call_mcp_tool("confluence_get_spaces", {})
            return self._parse_list_response(result)
        except Exception as e:
            logger.warning(f"MCP confluence_get_spaces failed or missing ({e}), falling back to direct REST API")
            return self._get_spaces_rest()

    async def get_pages(
        self, space_key: str, parent_id: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Get pages in a Confluence space via the MCP server or REST API fallback.
        """
        arguments = {"space_key": space_key}
        if parent_id:
            arguments["parent_id"] = parent_id

        try:
            result = await self._call_mcp_tool("confluence_get_pages", arguments)
            return self._parse_list_response(result)
        except Exception as e:
            logger.warning(f"MCP confluence_get_pages failed or missing ({e}), falling back to direct REST API")
            return self._get_pages_rest(space_key, parent_id)

    def _get_auth_headers(self) -> Dict[str, str]:
        """Get authentication headers for direct REST API calls."""
        # The variables should be passed to the container
        url = os.environ.get("CONFLUENCE_URL", "")
        username = os.environ.get("CONFLUENCE_USERNAME", "")
        token = os.environ.get("CONFLUENCE_API_TOKEN", "")
        
        if not url or not username or not token:
            logger.warning("Confluence credentials not found in environment for REST fallback")
            return {}
            
        auth_string = f"{username}:{token}"
        encoded_auth = base64.b64encode(auth_string.encode("utf-8")).decode("utf-8")
        return {
            "Authorization": f"Basic {encoded_auth}",
            "Accept": "application/json"
        }
        
    def _get_api_base_url(self) -> str:
        url = os.environ.get("CONFLUENCE_URL", "").rstrip("/")
        if url.endswith("/wiki"):
            return url
        # Just in case it's only the domain
        return url + "/wiki" if not url.endswith("/") else url + "wiki"

    def _get_spaces_rest(self) -> List[Dict[str, Any]]:
        """Direct REST API call to get spaces."""
        headers = self._get_auth_headers()
        if not headers:
            return []
            
        base_url = self._get_api_base_url()
        url = f"{base_url}/rest/api/space?limit=50"
        
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())
                
                spaces = []
                for s in data.get("results", []):
                    spaces.append({
                        "id": str(s.get("id", "")),
                        "key": s.get("key", ""),
                        "name": s.get("name", ""),
                        "icon": "folder",
                        "type": s.get("type", "global")
                    })
                return spaces
        except Exception as e:
            logger.error(f"Confluence REST api/space failed: {e}")
            return []

    def _get_pages_rest(self, space_key: str, parent_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """Direct REST API call to get pages for a space."""
        headers = self._get_auth_headers()
        if not headers:
            return []
            
        base_url = self._get_api_base_url()
        url = f"{base_url}/rest/api/content?spaceKey={space_key}&type=page&limit=50&expand=children.page"
        
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())
                
                pages = []
                for p in data.get("results", []):
                    # Filter by parent_id if provided
                    if parent_id:
                        # This is a simplification; Atlassian REST API requires specific queries for children
                        # But we'll leave it simple here, since the frontend only asks for top-level pages typically
                        pass
                        
                    pages.append({
                        "id": str(p.get("id", "")),
                        "title": p.get("title", ""),
                        "parentId": None, # Complex to get from this endpoint directly
                        "hasChildren": len(p.get("children", {}).get("page", {}).get("results", [])) > 0
                    })
                return pages
        except Exception as e:
            logger.error(f"Confluence REST api/content failed: {e}")
            return []

    async def _call_mcp_tool(
        self, tool_name: str, arguments: Dict[str, Any]
    ):
        """Call an MCP tool via SSE transport."""
        sse_url = f"{self.mcp_server_url}/sse"

        async with sse_client(sse_url) as (read_stream, write_stream):
            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()
                return await session.call_tool(tool_name, arguments)

    def _parse_create_response(self, result) -> Dict[str, Any]:
        """Parse MCP CallToolResult to extract page_id and url."""
        if result.isError:
            parts = []
            for item in result.content:
                if isinstance(item, TextContent):
                    parts.append(item.text)
            raise ValueError(f"MCP error: {' '.join(parts)}")

        for item in result.content:
            if not isinstance(item, TextContent):
                continue

            try:
                parsed = json.loads(item.text)
            except json.JSONDecodeError:
                continue

            if not isinstance(parsed, dict):
                continue

            # mcp-atlassian nests page data under "page" key
            page_data = parsed.get("page", parsed)

            page_id = str(
                page_data.get("id", page_data.get("pageId", ""))
            )
            url = page_data.get(
                "url",
                page_data.get("_links", {}).get("webui", ""),
            )
            return {"page_id": page_id, "url": url}

        raise ValueError(
            "Could not parse page creation response"
        )

    def _parse_list_response(self, result) -> List[Dict[str, Any]]:
        """Parse MCP CallToolResult to extract list data."""
        if result.isError:
            parts = []
            for item in result.content:
                if isinstance(item, TextContent):
                    parts.append(item.text)
            raise ValueError(f"MCP error: {' '.join(parts)}")

        for item in result.content:
            if not isinstance(item, TextContent):
                continue

            try:
                parsed = json.loads(item.text)
            except json.JSONDecodeError:
                continue

            # If it's a list, return it directly
            if isinstance(parsed, list):
                return parsed

            # If it's a dict with a list under a key, return the list
            if isinstance(parsed, dict):
                for key in ["spaces", "pages", "results", "data"]:
                    if key in parsed and isinstance(parsed[key], list):
                        return parsed[key]

        # Return empty list if nothing found
        return []
