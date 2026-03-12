"""
Jira MCP Tools

Tools for searching Jira via the mcp-atlassian MCP server.
Uses the MCP SDK with SSE transport to call MCP tools remotely.
"""

import json
from typing import Any, Dict, List

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

    Args:
        mcp_server_url: Base URL of the MCP server (e.g. http://localhost:8006)
        tool_name: Name of the MCP tool to call
        arguments: Tool arguments

    Returns:
        CallToolResult from the MCP server
    """
    sse_url = f"{mcp_server_url.rstrip('/')}/sse"

    async with sse_client(sse_url) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            result = await session.call_tool(tool_name, arguments)
            return result


class JiraSearchTool(BaseTool):
    """
    Search Jira issues via JQL using the MCP server.

    Calls the mcp-atlassian jira_search tool to perform
    live searches against Jira.
    """

    def __init__(self, mcp_server_url: str, source_type: str = "jira"):
        self._mcp_server_url = mcp_server_url
        self._source_type = source_type

    @property
    def name(self) -> str:
        return "jira_search"

    @property
    def description(self) -> str:
        return (
            "Search Jira issues using JQL (Jira Query Language). "
            "Examples: text ~ \"keyword\", project = \"FUE\", "
            "summary ~ \"topic\" AND status = \"Open\"."
        )

    @property
    def parameters(self) -> List[ToolParameter]:
        return [
            ToolParameter(
                name="query",
                type="string",
                description=(
                    "JQL search expression. Use text ~ \"keyword\" for full-text, "
                    "summary ~ \"topic\" for title search, or combine with AND/OR."
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
        Search Jira via MCP.

        Args:
            query: JQL search expression
            limit: Max results
            **kwargs: Additional parameters (ignored)

        Returns:
            ToolResult with search results
        """
        async with TracingContext(
            "jira.mcp.search",
            span_kind=SpanKind.CLIENT,
            attributes={
                "mcp.server_url": self._mcp_server_url,
                "mcp.tool": "jira_search",
                "search.query": query,
                "search.limit": limit,
            },
        ) as span:
            try:
                # If query doesn't look like JQL, wrap it as a text search
                if not any(op in query for op in ["~", "=", " AND ", " OR ", " IN "]):
                    jql_query = f'text ~ "{query}"'
                else:
                    jql_query = query

                result = await _call_mcp_tool(
                    self._mcp_server_url,
                    "jira_search",
                    {"query": jql_query, "limit": limit},
                )

                if result.isError:
                    error_text = _extract_text(result)
                    return ToolResult.fail(f"Jira search error: {error_text}")

                # Parse MCP response into SearchResult objects
                issues = self._parse_search_response(result)

                results_data = [
                    {
                        "id": issue.id,
                        "title": issue.title,
                        "content": issue.content[:2000] if issue.content else "",
                        "score": issue.score,
                        "url": issue.url,
                        "highlight": issue.highlight,
                    }
                    for issue in issues
                ]

                span.set_attribute("output.total_found", len(issues))
                span.set_attribute("output.results_count", len(results_data))

                logger.info(
                    "jira_search_complete",
                    query=jql_query,
                    results_count=len(issues),
                )

                return ToolResult.ok(
                    data={
                        "results": results_data,
                        "total_found": len(issues),
                        "query": jql_query,
                        "sources": issues,
                    },
                )

            except Exception as e:
                span.set_attribute("error", True)
                span.set_attribute("error.type", type(e).__name__)
                span.set_attribute("error.message", str(e))
                logger.error(
                    "jira_search_error",
                    query=query,
                    error=str(e),
                )
                return ToolResult.fail(f"Jira search failed: {e}")

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
                    for issue in parsed:
                        results.append(self._issue_to_search_result(issue))
                elif isinstance(parsed, dict):
                    issues = parsed.get("results", parsed.get("issues", [parsed]))
                    if isinstance(issues, list):
                        for issue in issues:
                            results.append(self._issue_to_search_result(issue))
                    else:
                        results.append(self._issue_to_search_result(parsed))
            except json.JSONDecodeError:
                # Plain text response
                if text.strip():
                    results.append(
                        SearchResult(
                            id="mcp-text",
                            title="Jira Search Result",
                            content=text,
                            score=1.0,
                            source_type=self._source_type,
                        )
                    )

        return results

    def _issue_to_search_result(self, issue: Dict[str, Any]) -> SearchResult:
        """Convert an issue dict from MCP to a SearchResult."""
        issue_key = str(
            issue.get("key", issue.get("id", issue.get("issue_key", "")))
        )
        summary = issue.get("summary", issue.get("title", issue.get("name", "Untitled")))

        # Description or comments as content
        description = issue.get("description", issue.get("body", issue.get("content", "")))
        if isinstance(description, dict):
            description = description.get("value", description.get("text", str(description)))

        url = issue.get("url", issue.get("self", ""))
        score = float(issue.get("score", issue.get("relevance", 1.0)))

        # Build metadata from issue fields
        fields = issue.get("fields", {})
        status = fields.get("status", issue.get("status", ""))
        if isinstance(status, dict):
            status = status.get("name", str(status))
        issue_type = fields.get("issuetype", issue.get("type", ""))
        if isinstance(issue_type, dict):
            issue_type = issue_type.get("name", str(issue_type))
        project = fields.get("project", issue.get("project", ""))
        if isinstance(project, dict):
            project = project.get("key", str(project))

        return SearchResult(
            id=issue_key,
            title=f"[{issue_key}] {summary}" if issue_key else summary,
            content=description,
            score=score,
            source_type=self._source_type,
            url=url,
            highlight=issue.get("excerpt", issue.get("highlight", None)),
            metadata={
                "issue_key": issue_key,
                "status": status,
                "issue_type": issue_type,
                "project": project,
                "labels": issue.get("labels", fields.get("labels", [])),
            },
        )


class JiraGetIssueTool(BaseTool):
    """
    Get full content of a Jira issue by key.

    Calls the mcp-atlassian jira_get_issue tool to retrieve
    the complete issue content including comments.
    """

    def __init__(self, mcp_server_url: str, source_type: str = "jira"):
        self._mcp_server_url = mcp_server_url
        self._source_type = source_type

    @property
    def name(self) -> str:
        return "jira_get_issue"

    @property
    def description(self) -> str:
        return (
            "Get the full content of a Jira issue by its key (e.g. FUE-123). "
            "Use this after searching to get complete issue details and comments."
        )

    @property
    def parameters(self) -> List[ToolParameter]:
        return [
            ToolParameter(
                name="issue_key",
                type="string",
                description="The Jira issue key to retrieve (e.g. FUE-123)",
                required=True,
            ),
        ]

    async def execute(
        self,
        issue_key: str = "",
        query: str = "",
        **kwargs,
    ) -> ToolResult:
        """
        Get full Jira issue content.

        Args:
            issue_key: The issue key to fetch (e.g. FUE-123)
            query: Unused, accepted for interface compatibility
            **kwargs: Additional parameters

        Returns:
            ToolResult with issue content
        """
        actual_key = issue_key or kwargs.get("issue_key", "") or query
        if not actual_key:
            return ToolResult.fail("issue_key is required")

        async with TracingContext(
            "jira.mcp.get_issue",
            span_kind=SpanKind.CLIENT,
            attributes={
                "mcp.server_url": self._mcp_server_url,
                "mcp.tool": "jira_get_issue",
                "jira.issue_key": actual_key,
            },
        ) as span:
            try:
                result = await _call_mcp_tool(
                    self._mcp_server_url,
                    "jira_get_issue",
                    {"issue_key": actual_key},
                )

                if result.isError:
                    error_text = _extract_text(result)
                    return ToolResult.fail(f"Get issue error: {error_text}")

                # Parse MCP response
                issue_data = self._parse_issue_response(result, actual_key)

                span.set_attribute("output.title", issue_data.get("title", ""))
                span.set_attribute(
                    "output.content_length", len(issue_data.get("content", ""))
                )

                logger.info(
                    "jira_get_issue_complete",
                    issue_key=actual_key,
                    title=issue_data.get("title", ""),
                )

                return ToolResult.ok(
                    data={
                        "results": [issue_data],
                        "content": issue_data.get("content", ""),
                        "title": issue_data.get("title", ""),
                        "url": issue_data.get("url", ""),
                        "sources": [
                            SearchResult(
                                id=actual_key,
                                title=issue_data.get("title", "Untitled"),
                                content=issue_data.get("content", ""),
                                score=1.0,
                                source_type=self._source_type,
                                url=issue_data.get("url"),
                                metadata=issue_data.get("metadata", {}),
                            )
                        ],
                    },
                )

            except Exception as e:
                span.set_attribute("error", True)
                span.set_attribute("error.type", type(e).__name__)
                span.set_attribute("error.message", str(e))
                logger.error(
                    "jira_get_issue_error",
                    issue_key=actual_key,
                    error=str(e),
                )
                return ToolResult.fail(f"Failed to get Jira issue: {e}")

    def _parse_issue_response(
        self, result: CallToolResult, issue_key: str
    ) -> Dict[str, Any]:
        """Parse MCP CallToolResult into an issue dict."""
        title = "Untitled"
        content = ""
        url = ""
        labels = []
        status = ""
        issue_type = ""

        for item in result.content:
            if not isinstance(item, TextContent):
                continue
            text = item.text
            try:
                parsed = json.loads(text)
                if isinstance(parsed, dict):
                    summary = parsed.get("summary", parsed.get("title", title))
                    key = parsed.get("key", issue_key)
                    title = f"[{key}] {summary}" if key else summary

                    description = parsed.get(
                        "description",
                        parsed.get("body", parsed.get("content", "")),
                    )
                    if isinstance(description, dict):
                        description = description.get("value", description.get("text", str(description)))

                    # Include comments in content
                    comments = parsed.get("comments", [])
                    comment_text = ""
                    if comments and isinstance(comments, list):
                        comment_parts = []
                        for c in comments:
                            author = c.get("author", {})
                            if isinstance(author, dict):
                                author = author.get("displayName", author.get("name", "Unknown"))
                            body = c.get("body", c.get("text", ""))
                            if isinstance(body, dict):
                                body = body.get("value", body.get("text", str(body)))
                            comment_parts.append(f"[Comment by {author}]: {body}")
                        comment_text = "\n\n".join(comment_parts)

                    content = description
                    if comment_text:
                        content = f"{description}\n\n--- Comments ---\n\n{comment_text}"

                    url = parsed.get("url", parsed.get("self", ""))
                    labels = parsed.get("labels", [])

                    fields = parsed.get("fields", {})
                    s = fields.get("status", parsed.get("status", ""))
                    status = s.get("name", str(s)) if isinstance(s, dict) else str(s)
                    t = fields.get("issuetype", parsed.get("type", ""))
                    issue_type = t.get("name", str(t)) if isinstance(t, dict) else str(t)
            except json.JSONDecodeError:
                content = text

        return {
            "id": issue_key,
            "title": title,
            "content": content,
            "url": url,
            "score": 1.0,
            "metadata": {
                "labels": labels,
                "issue_key": issue_key,
                "status": status,
                "issue_type": issue_type,
            },
        }


def _extract_text(result: CallToolResult) -> str:
    """Extract text from a CallToolResult for error messages."""
    parts = []
    for item in result.content:
        if isinstance(item, TextContent):
            parts.append(item.text)
    return " ".join(parts) if parts else "Unknown error"
