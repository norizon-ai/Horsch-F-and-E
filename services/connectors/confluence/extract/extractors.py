import json
import os
import logging
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime
from .api_client import ConfluenceAPIClient
from .api_version_adapter import APIVersionAdapter


class BaseExtractor:
    def __init__(self, api_client: ConfluenceAPIClient, output_dir: str):
        self.api_client = api_client
        self.output_dir = output_dir
        self.logger = logging.getLogger(self.__class__.__name__)
        self.adapter = APIVersionAdapter(api_client)
    
    def save_json(self, data: Dict, file_path: str):
        Path(os.path.dirname(file_path)).mkdir(parents=True, exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def save_html(self, content: str, file_path: str):
        Path(os.path.dirname(file_path)).mkdir(parents=True, exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)


class SpaceExtractor(BaseExtractor):
    def extract_all_spaces(self) -> List[Dict]:
        self.logger.info("Extracting all spaces...")
        
        spaces = self.api_client.get_paginated(
            self.adapter.get_spaces_endpoint(),
            expand=self.adapter.get_expand_fields("space")
        )
        
        self.logger.info(f"Found {len(spaces)} spaces")
        
        normalized_spaces = []
        for space in spaces:
            normalized = self.adapter.adapt_space_data(space)
            self._save_space_data(normalized)
            normalized_spaces.append(normalized)
        
        return normalized_spaces
    
    def _save_space_data(self, space: Dict):
        space_key = space.get("key", "unknown")
        space_dir = os.path.join(self.output_dir, "spaces", space_key)
        
        self.save_json(space, os.path.join(space_dir, "space_info.json"))
        
        self.logger.debug(f"Saved space data for {space_key}")


class PageExtractor(BaseExtractor):
    def extract_pages_from_space(self, space_key: str) -> List[Dict]:
        self.logger.info(f"Extracting pages from space: {space_key}")
        
        pages = []
        
        # Use adapter for correct endpoint and expand fields
        endpoint = self.adapter.get_pages_endpoint(space_key)
        expand_fields = self.adapter.get_expand_fields("page")
        
        page_results = self.api_client.get_paginated(
            endpoint,
            expand=expand_fields
        )
        
        for page in page_results:
            self._save_page_data(page, space_key)
            pages.append(page)
        
        self.logger.info(f"Extracted {len(pages)} pages from space {space_key}")
        return pages
    
    def _save_page_data(self, page: Dict, space_key: str):
        page_id = page.get("id", "unknown")
        page_dir = os.path.join(self.output_dir, "spaces", space_key, "pages")
        
        self.save_json(page, os.path.join(page_dir, f"{page_id}.json"))
        
        if "body" in page and "storage" in page["body"]:
            html_content = page["body"]["storage"].get("value", "")
            if html_content:
                self.save_html(html_content, os.path.join(page_dir, f"{page_id}.html"))
        
        self.logger.debug(f"Saved page {page_id} in space {space_key}")


class BlogPostExtractor(BaseExtractor):
    def extract_blogposts_from_space(self, space_key: str) -> List[Dict]:
        self.logger.info(f"Extracting blog posts from space: {space_key}")
        
        blogposts = []
        
        # Use adapter for correct endpoint and expand fields
        endpoint = self.adapter.get_blogposts_endpoint(space_key)
        expand_fields = self.adapter.get_expand_fields("blogpost")
        
        blog_results = self.api_client.get_paginated(
            endpoint,
            expand=expand_fields
        )
        
        for blog in blog_results:
            self._save_blogpost_data(blog, space_key)
            blogposts.append(blog)
        
        self.logger.info(f"Extracted {len(blogposts)} blog posts from space {space_key}")
        return blogposts
    
    def _save_blogpost_data(self, blog: Dict, space_key: str):
        blog_id = blog.get("id", "unknown")
        blog_dir = os.path.join(self.output_dir, "spaces", space_key, "blogs")
        
        self.save_json(blog, os.path.join(blog_dir, f"{blog_id}.json"))
        
        if "body" in blog and "storage" in blog["body"]:
            html_content = blog["body"]["storage"].get("value", "")
            if html_content:
                self.save_html(html_content, os.path.join(blog_dir, f"{blog_id}.html"))
        
        self.logger.debug(f"Saved blog post {blog_id} in space {space_key}")


class CommentExtractor(BaseExtractor):
    def extract_comments_for_content(self, content_id: str, content_type: str, 
                                    space_key: str) -> List[Dict]:
        self.logger.debug(f"Extracting comments for {content_type} {content_id}")
        
        comments = self.api_client.get_paginated(
            f"/api/v2/{content_type}s/{content_id}/footer-comments",
            expand=["body.storage", "version", "history"]
        )
        
        if comments:
            self._save_comments_data(comments, content_id, content_type, space_key)
        
        return comments
    
    def _save_comments_data(self, comments: List[Dict], content_id: str, 
                           content_type: str, space_key: str):
        comments_dir = os.path.join(self.output_dir, "spaces", space_key, 
                                   "comments", content_type)
        comments_file = os.path.join(comments_dir, f"{content_id}_comments.json")
        
        self.save_json(comments, comments_file)
        self.logger.debug(f"Saved {len(comments)} comments for {content_type} {content_id}")


class AttachmentExtractor(BaseExtractor):
    def extract_attachments_for_content(self, content_id: str, content_type: str, 
                                       space_key: str) -> List[Dict]:
        self.logger.debug(f"Extracting attachments for {content_type} {content_id}")
        
        attachments = self.api_client.get_paginated(
            f"/api/v2/{content_type}s/{content_id}/attachments",
            expand=["version", "metadata"]
        )
        
        if attachments:
            self._process_attachments(attachments, content_id, content_type, space_key)
        
        return attachments
    
    def _process_attachments(self, attachments: List[Dict], content_id: str, 
                           content_type: str, space_key: str):
        attachments_dir = os.path.join(self.output_dir, "spaces", space_key, 
                                      "attachments", content_type, content_id)
        Path(attachments_dir).mkdir(parents=True, exist_ok=True)
        
        metadata = []
        
        for attachment in attachments:
            att_id = attachment.get("id")
            filename = attachment.get("title", f"attachment_{att_id}")
            download_link = attachment.get("downloadLink")
            
            if download_link and self.api_client.config.download_attachments:
                file_path = os.path.join(attachments_dir, filename)
                
                if self.api_client.download_file(download_link, file_path):
                    self.logger.debug(f"Downloaded attachment: {filename}")
                    attachment["local_path"] = file_path
            
            metadata.append({
                "id": att_id,
                "title": filename,
                "mediaType": attachment.get("mediaType"),
                "fileSize": attachment.get("fileSize"),
                "version": attachment.get("version"),
                "downloadLink": download_link
            })
        
        if metadata:
            metadata_file = os.path.join(attachments_dir, "metadata.json")
            self.save_json(metadata, metadata_file)


class LabelExtractor(BaseExtractor):
    def extract_labels_for_content(self, content_id: str, content_type: str, 
                                  space_key: str) -> List[Dict]:
        self.logger.debug(f"Extracting labels for {content_type} {content_id}")
        
        labels = self.api_client.get_paginated(
            f"/api/v2/{content_type}s/{content_id}/labels"
        )
        
        return labels if labels else []


class UserExtractor(BaseExtractor):
    def extract_space_permissions(self, space_key: str) -> Dict:
        self.logger.debug(f"Extracting permissions for space {space_key}")
        
        permissions = self.api_client.get(
            f"/api/v2/spaces/{space_key}/permissions"
        )
        
        if permissions:
            perm_file = os.path.join(self.output_dir, "spaces", space_key, "permissions.json")
            self.save_json(permissions, perm_file)
        
        return permissions if permissions else {}