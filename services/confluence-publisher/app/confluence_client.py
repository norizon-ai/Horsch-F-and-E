"""Confluence API Client for publishing pages."""

import logging
from typing import Dict, Any, Optional, List
from atlassian import Confluence
from .config import settings

logger = logging.getLogger(__name__)


class ConfluenceClient:
    """Client for interacting with Confluence API."""

    def __init__(self):
        """Initialize Confluence client with credentials from settings."""
        if not settings.confluence_url or not settings.confluence_email or not settings.confluence_api_token:
            raise ValueError(
                "Missing Confluence credentials. Set CONFLUENCE_URL, CONFLUENCE_EMAIL, and CONFLUENCE_API_TOKEN"
            )

        self.confluence = Confluence(
            url=settings.confluence_url,
            username=settings.confluence_email,
            password=settings.confluence_api_token,
            cloud=True,  # Set to False for Server/Data Center
        )
        logger.info(f"Initialized Confluence client for {settings.confluence_url}")

    def test_connection(self) -> bool:
        """Test if the Confluence connection is working."""
        try:
            # Try to get server info to verify authentication
            # This works for both Cloud and Server/Data Center
            spaces = self.confluence.get_all_spaces(limit=1)
            logger.info(f"Successfully connected to Confluence")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to Confluence: {e}")
            return False

    def list_spaces(self) -> List[Dict[str, Any]]:
        """List all available Confluence spaces."""
        try:
            spaces = self.confluence.get_all_spaces(start=0, limit=100)
            return [
                {
                    "key": space["key"],
                    "name": space["name"],
                    "type": space.get("type", "global"),
                }
                for space in spaces.get("results", [])
            ]
        except Exception as e:
            logger.error(f"Failed to list spaces: {e}")
            return []

    def get_space(self, space_key: str) -> Optional[Dict[str, Any]]:
        """Get information about a specific space."""
        try:
            return self.confluence.get_space(space_key)
        except Exception as e:
            logger.error(f"Failed to get space {space_key}: {e}")
            return None

    def protocol_to_confluence_storage(self, protocol: Dict[str, Any]) -> str:
        """
        Convert protocol JSON to Confluence storage format (HTML-like).

        Confluence Cloud uses the storage format for page content:
        https://confluence.atlassian.com/doc/confluence-storage-format-790796544.html
        """
        title = protocol.get("title", "Meeting Protocol")
        date = protocol.get("date", "")
        attendees = protocol.get("attendees", [])
        executive_summary = protocol.get("executiveSummary", "")
        action_items = protocol.get("actionItems", [])
        decisions = protocol.get("decisions", [])
        next_steps = protocol.get("nextSteps", [])

        # Build Confluence storage format HTML
        content = []

        # Meeting Info Panel
        content.append('<ac:structured-macro ac:name="info">')
        content.append('<ac:rich-text-body>')
        content.append(f'<p><strong>Date:</strong> {date}</p>')
        if attendees:
            content.append(f'<p><strong>Attendees:</strong> {", ".join(attendees)}</p>')
        content.append('</ac:rich-text-body>')
        content.append('</ac:structured-macro>')

        # Executive Summary
        if executive_summary:
            content.append('<h2>Executive Summary</h2>')
            content.append(f'<p>{executive_summary}</p>')

        # Action Items
        if action_items:
            content.append('<h2>Action Items</h2>')
            content.append('<table>')
            content.append('<tbody>')
            content.append('<tr>')
            content.append('<th>Task</th>')
            content.append('<th>Assignee</th>')
            content.append('<th>Due Date</th>')
            content.append('</tr>')

            for item in action_items:
                if isinstance(item, dict):
                    task = item.get("text", "")
                    assignee = item.get("assignee", "")
                    due_date = item.get("dueDate", "")
                else:
                    task = str(item)
                    assignee = ""
                    due_date = ""

                content.append('<tr>')
                content.append(f'<td>{task}</td>')
                content.append(f'<td>{assignee}</td>')
                content.append(f'<td>{due_date}</td>')
                content.append('</tr>')

            content.append('</tbody>')
            content.append('</table>')

        # Decisions
        if decisions:
            content.append('<h2>Decisions</h2>')
            content.append('<ul>')
            for decision in decisions:
                content.append(f'<li>{decision}</li>')
            content.append('</ul>')

        # Next Steps
        if next_steps:
            content.append('<h2>Next Steps</h2>')
            content.append('<ol>')
            for step in next_steps:
                content.append(f'<li>{step}</li>')
            content.append('</ol>')

        return '\n'.join(content)

    def publish_page(
        self,
        protocol: Dict[str, Any],
        space_key: Optional[str] = None,
        parent_page_id: Optional[str] = None,
    ) -> Dict[str, str]:
        """
        Publish a protocol as a new Confluence page.

        Args:
            protocol: Protocol data dictionary
            space_key: Target space key (defaults to settings.confluence_space_key)
            parent_page_id: Optional parent page ID

        Returns:
            Dictionary with page_id and page_url
        """
        space_key = space_key or settings.confluence_space_key
        parent_page_id = parent_page_id or settings.confluence_parent_page_id

        if not space_key:
            raise ValueError("Space key is required. Set CONFLUENCE_SPACE_KEY or provide space_key parameter")

        # Get page title from protocol
        title = protocol.get("title", "Meeting Protocol")

        # Convert protocol to Confluence storage format
        content = self.protocol_to_confluence_storage(protocol)

        try:
            # Check if page with this title already exists in the space
            existing_page = self.confluence.get_page_by_title(
                space=space_key,
                title=title,
            )

            if existing_page:
                # Update existing page
                logger.info(f"Updating existing page: {title}")
                page_id = existing_page["id"]

                result = self.confluence.update_page(
                    page_id=page_id,
                    title=title,
                    body=content,
                )
            else:
                # Create new page
                logger.info(f"Creating new page: {title}")

                result = self.confluence.create_page(
                    space=space_key,
                    title=title,
                    body=content,
                    parent_id=parent_page_id,
                )

            page_id = result["id"]
            page_url = f"{settings.confluence_url}/wiki/spaces/{space_key}/pages/{page_id}"

            logger.info(f"Successfully published page: {page_url}")

            return {
                "page_id": page_id,
                "page_url": page_url,
            }

        except Exception as e:
            logger.error(f"Failed to publish page: {e}")
            raise


# Singleton instance
_client: Optional[ConfluenceClient] = None


def get_confluence_client() -> ConfluenceClient:
    """Get or create the Confluence client singleton."""
    global _client
    if _client is None:
        _client = ConfluenceClient()
    return _client
