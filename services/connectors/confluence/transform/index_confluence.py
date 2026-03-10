#!/usr/bin/env python3
"""
Confluence HTML indexer for DeepResearch Elasticsearch backend.
Parses Confluence HTML exports and indexes them with embeddings for hybrid search.
"""

import os
import hashlib
import re
import json
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
import datetime
import logging
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import html2text

from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
from tqdm import tqdm
from langchain_text_splitters import RecursiveCharacterTextSplitter

from dotenv import load_dotenv

load_dotenv()

# Configuration
ELASTIC_URL = os.getenv("ELASTIC_URL", "http://localhost:9200")
INDEX_NAME = os.getenv("ELASTIC_INDEX", "confluence_kb")
CONFLUENCE_DIR = os.getenv("CONFLUENCE_DIR", "/Users/lisaschmidt/Documents/GitHub/tier0-Horsch/confluence_export")
EMBED_MODEL = os.getenv("EMBED_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
ELASTIC_ALIAS = os.getenv("ELASTIC_ALIAS", f"{INDEX_NAME}_alias")
INDEX_STRATEGY = os.getenv("INDEX_STRATEGY", "RESET").upper()

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)


@dataclass
class ConfluencePage:
    """Represents a parsed Confluence page."""
    page_id: str
    space_key: str
    title: str
    content: str
    url: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class ConfluenceHTMLParser:
    """Parser for Confluence HTML exports."""
    
    def __init__(self):
        self.h2t = html2text.HTML2Text()
        self.h2t.ignore_links = False
        self.h2t.ignore_images = True
        self.h2t.body_width = 0  # No line wrapping
        
    def parse_html_file(self, file_path: Path) -> ConfluencePage:
        """Parse a single Confluence HTML file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                html_content = f.read()

            # Parse with BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')

            # Extract metadata from path
            parts = file_path.parts
            space_idx = parts.index('spaces') if 'spaces' in parts else -1
            space_key = parts[space_idx + 1] if space_idx != -1 and space_idx + 1 < len(parts) else 'UNKNOWN'
            page_id = file_path.stem

            # Extract title (try various methods)
            title = self._extract_title(soup, file_path)

            # Clean and convert content to markdown
            content = self._clean_content(soup)

            # Try to get proper Confluence URL from JSON metadata
            url = self._get_confluence_url(file_path, space_key, page_id)

            return ConfluencePage(
                page_id=page_id,
                space_key=space_key,
                title=title,
                content=content,
                url=url,
                metadata={
                    'file_path': str(file_path),
                    'space': space_key,
                }
            )
        except Exception as e:
            logger.error(f"Error parsing {file_path}: {e}")
            raise
    
    def _get_confluence_url(self, html_file_path: Path, space_key: str, page_id: str) -> str:
        """Extract proper Confluence URL from JSON metadata file."""
        # Look for corresponding JSON file
        json_file_path = html_file_path.with_suffix('.json')

        try:
            if json_file_path.exists():
                with open(json_file_path, 'r', encoding='utf-8') as f:
                    metadata = json.load(f)

                # Extract webui link from _links.webui
                webui_path = metadata.get('_links', {}).get('webui', '')

                if webui_path:
                    # Construct full Confluence URL
                    # Assuming Confluence base URL is https://confluence.horsch.com
                    confluence_base = os.getenv('CONFLUENCE_BASE_URL', 'https://confluence.horsch.com')

                    # webui_path starts with /, so just concatenate
                    full_url = f"{confluence_base}{webui_path}"
                    logger.debug(f"Extracted Confluence URL for page {page_id}: {full_url}")
                    return full_url
        except Exception as e:
            logger.warning(f"Could not extract Confluence URL from {json_file_path}: {e}")

        # Fallback to pseudo-URL
        fallback_url = f"confluence://{space_key}/pages/{page_id}"
        logger.debug(f"Using fallback URL for page {page_id}: {fallback_url}")
        return fallback_url

    def _extract_title(self, soup: BeautifulSoup, file_path: Path) -> str:
        """Extract page title from HTML."""
        # Try to find title in various places
        title_candidates = [
            soup.find('title'),
            soup.find('h1'),
            soup.find('meta', {'name': 'title'}),
            soup.find('meta', {'property': 'og:title'}),
        ]
        
        for candidate in title_candidates:
            if candidate:
                if hasattr(candidate, 'get'):
                    title = candidate.get('content', '')
                else:
                    title = candidate.get_text()
                if title:
                    return title.strip()
        
        # Fallback to filename
        return file_path.stem
    
    def _clean_content(self, soup: BeautifulSoup) -> str:
        """Clean and extract text content from HTML."""
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        
        # Remove Confluence-specific markup
        for elem in soup.find_all(['ac:structured-macro', 'ac:parameter', 'ac:rich-text-body']):
            elem.unwrap()
        
        # Convert to markdown
        html_str = str(soup)
        markdown_content = self.h2t.handle(html_str)
        
        # Clean up excessive whitespace
        markdown_content = re.sub(r'\n{3,}', '\n\n', markdown_content)
        markdown_content = re.sub(r' {2,}', ' ', markdown_content)
        
        return markdown_content.strip()


def es_client() -> Elasticsearch:
    """Create Elasticsearch client."""
    return Elasticsearch(
        ELASTIC_URL,
        verify_certs=False,
        request_timeout=120,
        max_retries=5,
        retry_on_timeout=True,
    )


def ensure_index(es: Elasticsearch, dims: int, index_name: str = INDEX_NAME):
    """Create index with proper mapping if it doesn't exist."""
    try:
        if es.indices.exists(index=index_name):
            return
    except Exception:
        # Index might not exist, continue to create it
        pass
    
    body = {
        "settings": {
            "number_of_shards": 2,
            "number_of_replicas": 0,
            "analysis": {
                "analyzer": {
                    "default": {
                        "type": "standard"
                    }
                }
            }
        },
        "mappings": {
            "_source": {
                "excludes": ["embedding"]  # Don't return embeddings in search results
            },
            "properties": {
                "content": {"type": "text", "analyzer": "standard"},
                "title": {"type": "text", "fields": {"keyword": {"type": "keyword"}}},
                "section": {"type": "text", "fields": {"keyword": {"type": "keyword"}}},
                "source": {"type": "keyword"},
                "space": {"type": "keyword"},
                "page_id": {"type": "keyword"},
                "url": {"type": "keyword"},
                "page": {"type": "integer"},
                "char_start": {"type": "integer"},
                "content_sha": {"type": "keyword"},
                "vector": {
                    "type": "dense_vector",
                    "dims": dims,
                    "index": True,
                    "similarity": "cosine",
                    "index_options": {
                        "type": "hnsw",
                        "m": 16,
                        "ef_construction": 100
                    }
                },
                "indexed_at": {"type": "date"}
            }
        }
    }
    
    es.indices.create(index=index_name, body=body)
    logger.info(f"Created index: {index_name}")


def prepare_index(es: Elasticsearch, dims: int) -> str:
    """Prepare index based on strategy."""
    if INDEX_STRATEGY == "RESET":
        logger.info(f"RESET strategy: deleting and recreating index '{INDEX_NAME}'")
        try:
            if es.indices.exists(index=INDEX_NAME):
                es.indices.delete(index=INDEX_NAME)
        except Exception as e:
            logger.warning(f"Could not check/delete existing index: {e}")
        ensure_index(es, dims, INDEX_NAME)
        return INDEX_NAME
    
    # Default: APPEND
    try:
        if not es.indices.exists(index=INDEX_NAME):
            ensure_index(es, dims, INDEX_NAME)
    except Exception:
        ensure_index(es, dims, INDEX_NAME)
    return INDEX_NAME


def load_confluence_pages(base_dir: str) -> List[ConfluencePage]:
    """Load all Confluence HTML pages from export directory."""
    parser = ConfluenceHTMLParser()
    pages = []
    base_path = Path(base_dir)
    
    # Find all HTML files in spaces directory
    html_files = list(base_path.glob("spaces/**/pages/*.html"))
    
    logger.info(f"Found {len(html_files)} HTML files to process")
    
    for html_file in tqdm(html_files, desc="Parsing Confluence pages"):
        try:
            page = parser.parse_html_file(html_file)
            pages.append(page)
        except Exception as e:
            logger.warning(f"Skipping {html_file}: {e}")
            continue
    
    return pages


def chunk_pages(pages: List[ConfluencePage]) -> List[Dict[str, Any]]:
    """Split pages into chunks for indexing."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        separators=["\n\n", "\n", " ", ""]
    )
    
    chunks = []
    
    for page in pages:
        # Create chunks from content
        page_chunks = splitter.split_text(page.content)
        
        for i, chunk_text in enumerate(page_chunks):
            chunk = {
                'content': chunk_text,
                'title': page.title,
                'source': page.url,
                'space': page.space_key,
                'page_id': page.page_id,
                'url': page.url,
                'page': i,  # Chunk number within page
                'section': f"{page.space_key}/{page.title}",
                'metadata': page.metadata
            }
            chunks.append(chunk)
    
    return chunks


def make_id(source: str, page: int, chunk_text: str) -> str:
    """Generate unique ID for a chunk."""
    base = f"{source}|{page}|{hashlib.md5(chunk_text.encode()).hexdigest()}"
    return hashlib.sha1(base.encode()).hexdigest()[:20]


def index_chunks(chunks: List[Dict[str, Any]], es: Elasticsearch, encoder: SentenceTransformer, index_name: str):
    """Index chunks into Elasticsearch."""
    logger.info(f"Indexing {len(chunks)} chunks into '{index_name}'...")
    
    batch_size = 100
    for i in tqdm(range(0, len(chunks), batch_size), desc="Indexing batches"):
        batch = chunks[i:i + batch_size]
        
        # Generate embeddings for batch
        texts = [chunk['content'] for chunk in batch]
        embeddings = encoder.encode(texts, normalize_embeddings=True, show_progress_bar=False)
        
        # Prepare bulk operations
        bulk_ops = []
        for chunk, embedding in zip(batch, embeddings):
            doc_id = make_id(chunk['source'], chunk['page'], chunk['content'])
            
            doc = {
                'content': chunk['content'],
                'title': chunk.get('title', ''),
                'source': chunk['source'],
                'space': chunk.get('space', ''),
                'page_id': chunk.get('page_id', ''),
                'url': chunk.get('url', ''),
                'page': chunk['page'],
                'section': chunk.get('section', ''),
                'char_start': 0,
                'content_sha': hashlib.sha1(chunk['content'].encode()).hexdigest(),
                'vector': embedding.tolist(),
                'indexed_at': datetime.datetime.utcnow().isoformat()
            }
            
            bulk_ops.extend([
                {"index": {"_index": index_name, "_id": doc_id}},
                doc
            ])
        
        # Bulk index
        if bulk_ops:
            es.bulk(body=bulk_ops)
    
    # Refresh index
    es.indices.refresh(index=index_name)
    logger.info(f"Indexing complete. Indexed {len(chunks)} chunks.")


def verify_index(es: Elasticsearch, index_name: str):
    """Verify index statistics."""
    stats = es.indices.stats(index=index_name)
    doc_count = stats['indices'][index_name]['primaries']['docs']['count']
    size = stats['indices'][index_name]['primaries']['store']['size_in_bytes']
    
    logger.info(f"Index '{index_name}' statistics:")
    logger.info(f"  - Documents: {doc_count:,}")
    logger.info(f"  - Size: {size / (1024**2):.2f} MB")
    
    # Test search
    test_query = "jira workflow"
    result = es.search(
        index=index_name,
        body={
            "size": 3,
            "query": {
                "match": {
                    "content": test_query
                }
            }
        }
    )
    
    logger.info(f"Test search for '{test_query}': {result['hits']['total']['value']} hits")


def main():
    """Main indexing pipeline."""
    logger.info("Starting Confluence indexing pipeline")
    
    # Initialize components
    encoder = SentenceTransformer(EMBED_MODEL)
    es = es_client()
    
    # Prepare index
    dims = encoder.get_sentence_embedding_dimension()
    index_name = prepare_index(es, dims)
    
    # Load and parse Confluence pages
    pages = load_confluence_pages(CONFLUENCE_DIR)
    logger.info(f"Loaded {len(pages)} Confluence pages")
    
    # Chunk pages
    chunks = chunk_pages(pages)
    logger.info(f"Created {len(chunks)} chunks from pages")
    
    # Index chunks
    index_chunks(chunks, es, encoder, index_name)
    
    # Verify
    verify_index(es, index_name)
    
    logger.info("Confluence indexing complete!")


if __name__ == "__main__":
    main()