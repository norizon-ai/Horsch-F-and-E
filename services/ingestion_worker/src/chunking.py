"""
Smart chunking module for processing different content types.
Handles HTML to Markdown conversion and intelligent text splitting.
"""
import re
from typing import List, Dict, Any, Tuple
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter


class SmartChunker:
    """
    Handles intelligent content chunking based on content type and structure.
    """
    
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        
        # Initialize text splitters
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )
        
        # Markdown header splitter for structured documents
        self.markdown_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=[
                ("#", "Header 1"),
                ("##", "Header 2"),
                ("###", "Header 3"),
                ("####", "Header 4"),
            ]
        )
    
    def detect_content_type(self, content: str, source_uri: str = "") -> str:
        """
        Detect the content type based on content and URI.
        """
        # Check if content contains HTML tags
        if re.search(r'<[^>]+>', content):
            return "html"
        
        # Check file extension in URI
        if source_uri.endswith(('.md', '.markdown')):
            return "markdown"
        elif source_uri.endswith(('.html', '.htm')):
            return "html"
        elif source_uri.endswith(('.pdf', '.doc', '.docx')):
            return "document"
        
        # Default to plain text
        return "text"
    
    def html_to_markdown(self, html_content: str) -> str:
        """
        Convert HTML content to clean Markdown.
        """
        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        
        # Convert to markdown
        markdown_content = md(str(soup), heading_style="ATX")
        
        # Clean up excessive whitespace
        markdown_content = re.sub(r'\n\s*\n\s*\n', '\n\n', markdown_content)
        markdown_content = markdown_content.strip()
        
        return markdown_content
    
    def extract_metadata_from_html(self, html_content: str) -> Dict[str, Any]:
        """
        Extract metadata from HTML content (title, headings, etc.).
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        metadata = {}
        
        # Extract title
        title_tag = soup.find('title')
        if title_tag:
            metadata['title'] = title_tag.get_text().strip()
        
        # Extract meta tags
        meta_tags = soup.find_all('meta')
        for meta in meta_tags:
            if meta.get('name') == 'description':
                metadata['description'] = meta.get('content', '').strip()
            elif meta.get('name') == 'keywords':
                metadata['keywords'] = meta.get('content', '').strip()
            elif meta.get('name') == 'author':
                metadata['author'] = meta.get('content', '').strip()
        
        # Extract headings structure
        headings = []
        for i in range(1, 7):
            for heading in soup.find_all(f'h{i}'):
                headings.append({
                    'level': i,
                    'text': heading.get_text().strip()
                })
        
        if headings:
            metadata['headings'] = headings
        
        return metadata
    
    def chunk_by_headers(self, markdown_content: str) -> List[Dict[str, Any]]:
        """
        Chunk markdown content by headers, preserving structure.
        """
        try:
            # Split by headers first
            header_splits = self.markdown_splitter.split_text(markdown_content)
            
            chunks = []
            for split in header_splits:
                # Get the content and metadata
                content = split.page_content
                metadata = split.metadata
                
                # If the chunk is still too large, split it further
                if len(content) > self.chunk_size:
                    sub_chunks = self.text_splitter.split_text(content)
                    for i, sub_chunk in enumerate(sub_chunks):
                        chunk_metadata = metadata.copy()
                        chunk_metadata['sub_chunk'] = i + 1
                        chunks.append({
                            'content': sub_chunk,
                            'metadata': chunk_metadata
                        })
                else:
                    chunks.append({
                        'content': content,
                        'metadata': metadata
                    })
            
            return chunks
            
        except Exception as e:
            # Fallback to regular text splitting
            print(f"Header-based chunking failed: {e}. Falling back to text splitting.")
            text_chunks = self.text_splitter.split_text(markdown_content)
            return [{'content': chunk, 'metadata': {}} for chunk in text_chunks]
    
    def chunk_content(self, content: str, source_uri: str = "", 
                     existing_metadata: Dict[str, Any] = None) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
        """
        Main chunking method that handles different content types intelligently.
        
        Returns:
            Tuple of (chunks, enhanced_metadata)
        """
        if existing_metadata is None:
            existing_metadata = {}
        
        content_type = self.detect_content_type(content, source_uri)
        enhanced_metadata = existing_metadata.copy()
        enhanced_metadata['content_type'] = content_type
        
        processed_content = content
        
        # Process HTML content
        if content_type == "html":
            # Extract metadata from HTML
            html_metadata = self.extract_metadata_from_html(content)
            enhanced_metadata.update(html_metadata)
            
            # Convert to markdown
            processed_content = self.html_to_markdown(content)
            enhanced_metadata['original_format'] = 'html'
            enhanced_metadata['converted_to'] = 'markdown'
        
        # Chunk the content
        if content_type in ["html", "markdown"] and len(processed_content) > self.chunk_size:
            # Use header-based chunking for structured content
            chunks = self.chunk_by_headers(processed_content)
        else:
            # Use regular text splitting
            text_chunks = self.text_splitter.split_text(processed_content)
            chunks = [{'content': chunk, 'metadata': {}} for chunk in text_chunks]
        
        # Add common metadata to all chunks
        for i, chunk in enumerate(chunks):
            chunk['metadata'].update({
                'source_uri': source_uri,
                'chunk_index': i,
                'total_chunks': len(chunks),
                'chunk_size': len(chunk['content']),
                'content_type': content_type
            })
        
        return chunks, enhanced_metadata


def create_chunker(chunk_size: int = 1000, chunk_overlap: int = 200) -> SmartChunker:
    """
    Factory function to create a SmartChunker instance.
    """
    return SmartChunker(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
