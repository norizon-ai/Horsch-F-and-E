"""
Confluence MCP Tools

Tools for searching Confluence via the mcp-atlassian MCP server.
Uses the MCP SDK with SSE transport to call MCP tools remotely.
"""

import json
from typing import Any, Dict, List, Optional

from mcp import ClientSession
from mcp.client.sse import sse_client
from mcp.types import CallToolResult, TextContent

from deepsearch.models import SearchResult, ToolResult
from deepsearch.observability import get_logger, TracingContext, SpanKind
from deepsearch.tools import BaseTool
from deepsearch.tools.base import ToolParameter

logger = get_logger(__name__)


async def _call_mcp_tool(
    mcp_server_url: str,
    tool_name: str,
    arguments: Dict[str, Any],
) -> CallToolResult:
    """
    Call an MCP tool on the mcp-atlassian server via SSE transport.

    Establishes an SSE session, initializes the MCP client, calls the tool,
    and returns the result.

    Args:
        mcp_server_url: Base URL of the MCP server (e.g. http://localhost:8005)
        tool_name: Name of the MCP tool to call
        arguments: Tool arguments

    Returns:
        CallToolResult from the MCP server

    Raises:
        Exception: If the MCP call fails
    """
    sse_url = f"{mcp_server_url.rstrip('/')}/sse"

    async with sse_client(sse_url) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            result = await session.call_tool(tool_name, arguments)
            return result


class ConfluenceSearchTool(BaseTool):
    """
    Search Confluence pages via CQL using the MCP server.

    Calls the mcp-atlassian confluence_search tool to perform
    live searches against Confluence Cloud.
    """

    def __init__(self, mcp_server_url: str, source_type: str = "confluence"):
        self._mcp_server_url = mcp_server_url
        self._source_type = source_type

    @property
    def name(self) -> str:
        return "confluence_search"

    @property
    def description(self) -> str:
        return (
            "Search Confluence pages using CQL (Confluence Query Language). "
            "Examples: text ~ \"keyword\", title ~ \"topic\", "
            "type=page AND space=\"KB\"."
        )

    @property
    def parameters(self) -> List[ToolParameter]:
        return [
            ToolParameter(
                name="query",
                type="string",
                description=(
                    "CQL search expression. Use text ~ \"keyword\" for full-text, "
                    "title ~ \"topic\" for title search, or combine with AND/OR."
                ),
                required=True,
            ),
            ToolParameter(
                name="limit",
                type="integer",
                description="Maximum number of results to return (default: 10)",
                required=False,
                default=10,
            ),
        ]

    async def execute(
        self,
        query: str,
        limit: int = 10,
        **kwargs,
    ) -> ToolResult:
        """
        Search Confluence via MCP.

        Args:
            query: CQL search expression
            limit: Max results
            **kwargs: Additional parameters (ignored)

        Returns:
            ToolResult with search results
        """
        async with TracingContext(
            "confluence.mcp.search",
            span_kind=SpanKind.CLIENT,
            attributes={
                "mcp.server_url": self._mcp_server_url,
                "mcp.tool": "confluence_search",
                "search.query": query,
                "search.limit": limit,
            },
        ) as span:
            try:
                # If query doesn't look like CQL, wrap it as a text search
                if not any(op in query for op in ["~", "=", " AND ", " OR "]):
                    cql_query = f'text ~ "{query}"'
                else:
                    cql_query = query

                result = await _call_mcp_tool(
                    self._mcp_server_url,
                    "confluence_search",
                    {"query": cql_query, "limit": limit},
                )

                if result.isError:
                    error_text = _extract_text(result)
                    return ToolResult.fail(f"Confluence search error: {error_text}")

                # Parse MCP response into SearchResult objects
                pages = self._parse_search_response(result)

                results_data = [
                    {
                        "id": p.id,
                        "title": p.title,
                        "content": p.content[:2000] if p.content else "",
                        "score": p.score,
                        "url": p.url,
                        "highlight": p.highlight,
                    }
                    for p in pages
                ]

                span.set_attribute("output.total_found", len(pages))
                span.set_attribute("output.results_count", len(results_data))

                logger.info(
                    "confluence_search_complete",
                    query=cql_query,
                    results_count=len(pages),
                )

                return ToolResult.ok(
                    data={
                        "results": results_data,
                        "total_found": len(pages),
                        "query": cql_query,
                        "sources": pages,
                    },
                )

            except Exception as e:
                span.set_attribute("error", True)
                span.set_attribute("error.type", type(e).__name__)
                span.set_attribute("error.message", str(e))
                logger.error(
                    "confluence_search_error",
                    query=query,
                    error=str(e),
                )
                return ToolResult.fail(f"Confluence search failed: {e}")

    def _parse_search_response(self, result: CallToolResult) -> List[SearchResult]:
        """Parse MCP CallToolResult into SearchResult objects."""
        results = []

        for item in result.content:
            if not isinstance(item, TextContent):
                continue
            text = item.text
            try:
                parsed = json.loads(text)
                if isinstance(parsed, list):
                    for page in parsed:
                        results.append(self._page_to_search_result(page))
                elif isinstance(parsed, dict):
                    pages = parsed.get("results", parsed.get("pages", [parsed]))
                    if isinstance(pages, list):
                        for page in pages:
                            results.append(self._page_to_search_result(page))
                    else:
                        results.append(self._page_to_search_result(parsed))
            except json.JSONDecodeError:
                # Plain text response
                if text.strip():
                    results.append(
                        SearchResult(
                            id="mcp-text",
                            title="Confluence Search Result",
                            content=text,
                            score=1.0,
                            source_type=self._source_type,
                        )
                    )

        return results

    def _page_to_search_result(self, page: Dict[str, Any]) -> SearchResult:
        """Convert a page dict from MCP to a SearchResult."""
        # Handle various field names from mcp-atlassian
        page_id = str(
            page.get("id", page.get("pageId", page.get("content_id", "")))
        )
        title = page.get("title", page.get("name", "Untitled"))
        content = page.get("content", page.get("body", page.get("excerpt", "")))
        # mcp-atlassian may return content as {'value': '...', 'format': 'view'}
        if isinstance(content, dict):
            content = content.get("value", content.get("text", str(content)))
        url = page.get("url", page.get("_links", {}).get("webui", ""))
        score = float(page.get("score", page.get("relevance", 1.0)))

        return SearchResult(
            id=page_id,
            title=title,
            content=content,
            score=score,
            source_type=self._source_type,
            url=url,
            highlight=page.get("excerpt", page.get("highlight", None)),
            metadata={
                "space_key": page.get("space", {}).get("key", page.get("spaceKey", "")),
                "labels": page.get("labels", []),
            },
        )


class ConfluenceGetPageTool(BaseTool):
    """
    Get full content of a Confluence page by ID.

    Calls the mcp-atlassian confluence_get_page tool to retrieve
    the complete page content.
    """

    def __init__(self, mcp_server_url: str, source_type: str = "confluence"):
        self._mcp_server_url = mcp_server_url
        self._source_type = source_type

    @property
    def name(self) -> str:
        return "confluence_get_page"

    @property
    def description(self) -> str:
        return (
            "Get the full content of a Confluence page by its ID. "
            "Use this after searching to get complete page text."
        )

    @property
    def parameters(self) -> List[ToolParameter]:
        return [
            ToolParameter(
                name="page_id",
                type="string",
                description="The Confluence page ID to retrieve",
                required=True,
            ),
        ]

    async def execute(
        self,
        page_id: str = "",
        query: str = "",
        **kwargs,
    ) -> ToolResult:
        """
        Get full Confluence page content.

        Args:
            page_id: The page ID to fetch
            query: Unused, accepted for interface compatibility
            **kwargs: Additional parameters

        Returns:
            ToolResult with page content
        """
        # Handle case where page_id comes via kwargs or query
        actual_page_id = page_id or kwargs.get("page_id", "") or query
        if not actual_page_id:
            return ToolResult.fail("page_id is required")

        async with TracingContext(
            "confluence.mcp.get_page",
            span_kind=SpanKind.CLIENT,
            attributes={
                "mcp.server_url": self._mcp_server_url,
                "mcp.tool": "confluence_get_page",
                "confluence.page_id": actual_page_id,
            },
        ) as span:
            try:
                result = await _call_mcp_tool(
                    self._mcp_server_url,
                    "confluence_get_page",
                    {"page_id": actual_page_id},
                )

                if result.isError:
                    error_text = _extract_text(result)
                    return ToolResult.fail(f"Get page error: {error_text}")

                # Parse MCP response
                page_data = self._parse_page_response(result, actual_page_id)

                span.set_attribute("output.title", page_data.get("title", ""))
                span.set_attribute(
                    "output.content_length", len(page_data.get("content", ""))
                )

                logger.info(
                    "confluence_get_page_complete",
                    page_id=actual_page_id,
                    title=page_data.get("title", ""),
                )

                return ToolResult.ok(
                    data={
                        "results": [page_data],
                        "content": page_data.get("content", ""),
                        "title": page_data.get("title", ""),
                        "url": page_data.get("url", ""),
                        "sources": [
                            SearchResult(
                                id=actual_page_id,
                                title=page_data.get("title", "Untitled"),
                                content=page_data.get("content", ""),
                                score=1.0,
                                source_type=self._source_type,
                                url=page_data.get("url"),
                                metadata=page_data.get("metadata", {}),
                            )
                        ],
                    },
                )

            except Exception as e:
                span.set_attribute("error", True)
                span.set_attribute("error.type", type(e).__name__)
                span.set_attribute("error.message", str(e))
                logger.error(
                    "confluence_get_page_error",
                    page_id=actual_page_id,
                    error=str(e),
                )
                return ToolResult.fail(f"Failed to get Confluence page: {e}")

    def _parse_page_response(
        self, result: CallToolResult, page_id: str
    ) -> Dict[str, Any]:
        """Parse MCP CallToolResult into a page dict."""
        title = "Untitled"
        content = ""
        url = ""
        labels = []

        for item in result.content:
            if not isinstance(item, TextContent):
                continue
            text = item.text
            try:
                parsed = json.loads(text)
                if isinstance(parsed, dict):
                    title = parsed.get("title", title)
                    content = parsed.get(
                        "content",
                        parsed.get("body", parsed.get("markdown", text)),
                    )
                    # mcp-atlassian may return content as {'value': '...', 'format': 'view'}
                    if isinstance(content, dict):
                        content = content.get("value", content.get("text", str(content)))
                    url = parsed.get(
                        "url", parsed.get("_links", {}).get("webui", "")
                    )
                    labels = parsed.get("labels", [])
            except json.JSONDecodeError:
                content = text

        return {
            "id": page_id,
            "title": title,
            "content": content,
            "url": url,
            "score": 1.0,
            "metadata": {
                "labels": labels,
                "page_id": page_id,
            },
        }


def _extract_text(result: CallToolResult) -> str:
    """Extract text from a CallToolResult for error messages."""
    parts = []
    for item in result.content:
        if isinstance(item, TextContent):
            parts.append(item.text)
    return " ".join(parts) if parts else "Unknown error"
