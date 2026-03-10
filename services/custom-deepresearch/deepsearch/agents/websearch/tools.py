"""
WebSearch Agent Tools

Tools available to the WebSearch agent for searching and fetching web content.
Uses SearXNG as the search backend.
"""

from typing import Any, Dict, List, Optional

from deepsearch.tools import BaseTool, ToolParameter
from deepsearch.models import ToolResult, SearchResult
from deepsearch.observability import get_logger

logger = get_logger(__name__)


class SearXNGSearchTool(BaseTool):
    """
    Tool for performing web searches using SearXNG.

    SearXNG is a privacy-respecting metasearch engine that aggregates
    results from multiple search engines.
    """

    def __init__(
        self,
        searxng_url: str,
        timeout: float = 30.0,
        default_engines: Optional[List[str]] = None,
    ):
        """
        Initialize the SearXNG search tool.

        Args:
            searxng_url: Base URL of the SearXNG instance.
            timeout: Request timeout in seconds.
            default_engines: Default search engines to use.
        """
        self.searxng_url = searxng_url.rstrip("/")
        self.timeout = timeout
        self.default_engines = default_engines or ["google", "bing", "duckduckgo"]

    @property
    def name(self) -> str:
        return "web_search"

    @property
    def description(self) -> str:
        return (
            "Search the web for information using SearXNG metasearch. "
            "Returns relevant web pages with titles, URLs, and content snippets. "
            "Use short, focused search queries for best results."
        )

    @property
    def parameters(self) -> List[ToolParameter]:
        return [
            ToolParameter(
                name="query",
                type="string",
                description="Search query - keep it short and focused",
                required=True,
            ),
            ToolParameter(
                name="max_results",
                type="integer",
                description="Maximum number of results (default: 10)",
                required=False,
                default=10,
            ),
            ToolParameter(
                name="categories",
                type="string",
                description="Search categories (default: 'general'). Options: general, images, news, science",
                required=False,
                default="general",
            ),
        ]

    async def execute(
        self,
        query: str,
        max_results: int = 10,
        categories: str = "general",
        **kwargs,
    ) -> ToolResult:
        """Execute a SearXNG search."""
        import httpx

        try:
            logger.info(
                "searxng_search_execute",
                query=query[:100],
                max_results=max_results,
                categories=categories,
            )

            search_url = f"{self.searxng_url}/search"

            params = {
                "q": query,
                "format": "json",
                "categories": categories,
                "engines": ",".join(self.default_engines),
            }

            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(search_url, params=params)
                response.raise_for_status()
                data = response.json()

            # Parse results
            results = []
            for item in data.get("results", [])[:max_results]:
                result = SearchResult(
                    id=item.get("url", ""),
                    title=item.get("title", ""),
                    content=item.get("content", ""),
                    score=item.get("score", 0.0),
                    source_type="web",
                    url=item.get("url", ""),
                    metadata={
                        "engine": item.get("engine", ""),
                        "category": item.get("category", ""),
                        "parsed_url": item.get("parsed_url", []),
                    },
                )
                results.append(result)

            logger.info(
                "searxng_search_complete",
                query=query[:100],
                results_count=len(results),
            )

            return ToolResult.ok(
                data={
                    "results": results,
                    "query": query,
                    "total_found": len(results),
                    "engines_used": self.default_engines,
                },
                tool_name=self.name,
            )

        except httpx.HTTPStatusError as e:
            logger.error(
                "searxng_http_error",
                status=e.response.status_code,
                query=query[:100],
            )
            return ToolResult.fail(
                error=f"SearXNG HTTP error: {e.response.status_code}",
                tool_name=self.name,
            )
        except Exception as e:
            logger.error(
                "searxng_search_error",
                error=str(e),
                query=query[:100],
            )
            return ToolResult.fail(error=str(e), tool_name=self.name)


class FetchUrlTool(BaseTool):
    """
    Tool for fetching content from a specific URL.

    Use this to get detailed content from a promising search result.
    """

    def __init__(
        self,
        timeout: float = 30.0,
        max_content_length: int = 50000,
    ):
        """
        Initialize the URL fetch tool.

        Args:
            timeout: Request timeout in seconds.
            max_content_length: Maximum content length to return.
        """
        self.timeout = timeout
        self.max_content_length = max_content_length

    @property
    def name(self) -> str:
        return "fetch_url"

    @property
    def description(self) -> str:
        return (
            "Fetch content from a specific URL. Use this to get detailed "
            "content from a promising search result. Returns the page "
            "content and status."
        )

    @property
    def parameters(self) -> List[ToolParameter]:
        return [
            ToolParameter(
                name="url",
                type="string",
                description="The URL to fetch",
                required=True,
            ),
        ]

    async def execute(
        self,
        url: str = None,
        query: str = None,
        **kwargs,
    ) -> ToolResult:
        """Fetch content from a URL."""
        import httpx

        target_url = url or query
        if not target_url:
            return ToolResult.fail(
                error="No URL provided", tool_name=self.name
            )

        try:
            logger.info("fetch_url_execute", url=target_url)

            async with httpx.AsyncClient(
                timeout=self.timeout, follow_redirects=True
            ) as client:
                response = await client.get(target_url)
                response.raise_for_status()

                content = response.text[: self.max_content_length]
                content_type = response.headers.get("content-type", "")

                return ToolResult.ok(
                    data={
                        "url": str(response.url),
                        "content": content,
                        "status_code": response.status_code,
                        "content_type": content_type,
                        "content_length": len(response.text),
                    },
                    tool_name=self.name,
                )

        except httpx.HTTPStatusError as e:
            logger.warning(
                "fetch_url_http_error",
                url=target_url,
                status=e.response.status_code,
            )
            return ToolResult.fail(
                error=f"HTTP {e.response.status_code}: {e.response.reason_phrase}",
                tool_name=self.name,
            )
        except httpx.TimeoutException:
            logger.warning("fetch_url_timeout", url=target_url)
            return ToolResult.fail(
                error="Request timed out", tool_name=self.name
            )
        except Exception as e:
            logger.error(
                "fetch_url_error",
                url=target_url,
                error=str(e),
            )
            return ToolResult.fail(error=str(e), tool_name=self.name)


class ExtractContentTool(BaseTool):
    """
    Tool for extracting main content from HTML.

    Removes navigation, ads, and boilerplate to get the main text content.
    """

    @property
    def name(self) -> str:
        return "extract_content"

    @property
    def description(self) -> str:
        return (
            "Extract main text content from HTML, removing navigation, "
            "ads, and scripts. Use this after fetching a URL to get "
            "clean, readable text."
        )

    @property
    def parameters(self) -> List[ToolParameter]:
        return [
            ToolParameter(
                name="html",
                type="string",
                description="HTML content to extract text from",
                required=True,
            ),
            ToolParameter(
                name="max_length",
                type="integer",
                description="Maximum length of extracted text (default: 10000)",
                required=False,
                default=10000,
            ),
        ]

    async def execute(
        self,
        html: str = None,
        query: str = None,
        max_length: int = 10000,
        **kwargs,
    ) -> ToolResult:
        """Extract text content from HTML."""
        content = html or query
        if not content:
            return ToolResult.fail(
                error="No HTML content provided", tool_name=self.name
            )

        try:
            extracted = self._extract_text(content, max_length)

            return ToolResult.ok(
                data={
                    "content": extracted,
                    "original_length": len(content),
                    "extracted_length": len(extracted),
                },
                tool_name=self.name,
            )

        except Exception as e:
            logger.error("extract_content_error", error=str(e))
            return ToolResult.fail(error=str(e), tool_name=self.name)

    def _extract_text(self, html: str, max_length: int) -> str:
        """Extract text from HTML using HTMLParser."""
        from html.parser import HTMLParser

        class TextExtractor(HTMLParser):
            def __init__(self):
                super().__init__()
                self.text_parts = []
                self.skip_tags = {"script", "style", "nav", "header", "footer", "aside"}
                self.current_skip = set()

            def handle_starttag(self, tag, attrs):
                if tag in self.skip_tags:
                    self.current_skip.add(tag)

            def handle_endtag(self, tag):
                self.current_skip.discard(tag)

            def handle_data(self, data):
                if not self.current_skip:
                    text = data.strip()
                    if text and len(text) > 1:
                        self.text_parts.append(text)

        try:
            extractor = TextExtractor()
            extractor.feed(html)
            extracted = " ".join(extractor.text_parts)

            # Clean up whitespace
            import re

            extracted = re.sub(r"\s+", " ", extracted).strip()

            return extracted[:max_length]

        except Exception:
            # Fallback: regex-based HTML stripping
            import re

            text = re.sub(
                r"<(script|style)[^>]*>.*?</\1>",
                "",
                html,
                flags=re.DOTALL | re.IGNORECASE,
            )
            text = re.sub(r"<[^>]+>", " ", text)
            text = re.sub(r"\s+", " ", text).strip()
            text = re.sub(r"&\w+;", " ", text)
            return text[:max_length]
