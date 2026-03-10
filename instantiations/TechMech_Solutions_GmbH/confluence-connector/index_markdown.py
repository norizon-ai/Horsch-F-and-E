#!/usr/bin/env python3
"""
Index markdown files with YAML frontmatter into Elasticsearch.
Enhanced version with German analyzers, text chunking, and metadata extraction.
Used for the TechMech Solutions demo confluence assistant.
"""

import os
import sys
import re
import json
import hashlib
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime, timezone
import yaml
from elasticsearch import Elasticsearch, helpers
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Space name mapping (code -> human-readable name)
SPACE_NAMES = {
    "ENG": "Engineering",
    "PRJ": "Projects",
    "CMP": "Company",
    "QM": "Quality Management",
    "SRV": "Service",
    "MTG": "Meetings",
    "IT": "IT",
    "HR": "Human Resources",
}

# Content type detection patterns
CONTENT_TYPE_PATTERNS = {
    "technical_spec": [
        r"technische?\s+spezifikation",
        r"technical\s+spec",
        r"datenblatt",
        r"^##\s*\d+\.\s*(technische|allgemeine)\s+daten",
    ],
    "troubleshooting": [
        r"fehler",
        r"problem",
        r"troubleshoot",
        r"bekannte\s+probleme",
        r"störung",
        r"diagnose",
    ],
    "procedure": [
        r"anleitung",
        r"checkliste",
        r"arbeitsanweisung",
        r"awa-\d+",
        r"verfahren",
        r"ablauf",
    ],
    "maintenance": [
        r"wartung",
        r"maintenance",
        r"inspektion",
        r"kalibrierung",
        r"schmierung",
    ],
    "meeting_notes": [
        r"meeting",
        r"protokoll",
        r"besprechung",
        r"notes\s*kw",
    ],
    "project": [
        r"prj-\d{4}-\d{3}",
        r"projekt",
        r"lastenheft",
        r"pflichtenheft",
    ],
    "quality": [
        r"8d-\d{4}-\d{3}",
        r"reklamation",
        r"kvp-\d{4}-\d{3}",
        r"audit",
        r"prüf",
    ],
    "hr": [
        r"urlaub",
        r"arbeitszeit",
        r"gehalt",
        r"bewerbung",
        r"onboarding",
    ],
}


class MarkdownIndexer:
    """Indexes markdown files with YAML frontmatter into Elasticsearch."""

    # Chunking configuration
    CHUNK_SIZE = 800
    CHUNK_OVERLAP = 80

    def __init__(
        self,
        es_url: str,
        index_name: str,
        embed_model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
    ):
        self.es = Elasticsearch([es_url])
        self.index_name = index_name
        self.embed_model = SentenceTransformer(embed_model_name)

        # Load mapping from JSON file
        mapping_path = Path(__file__).parent / "mapping.json"
        if mapping_path.exists():
            with open(mapping_path, "r", encoding="utf-8") as f:
                self.mapping = json.load(f)
        else:
            raise FileNotFoundError(f"Mapping file not found: {mapping_path}")

        print(f"Connected to Elasticsearch at {es_url}")
        print(f"Loaded embedding model: {embed_model_name}")

    def extract_headings(self, content: str) -> List[str]:
        """Extract all markdown headings from content."""
        pattern = r"^#{1,4}\s+(.+)$"
        headings = re.findall(pattern, content, re.MULTILINE)
        return headings

    def extract_product_codes(self, text: str) -> List[str]:
        """Extract TechMech product codes from text."""
        patterns = [
            r"\b(RC-\d{4})\b",  # Roboterzellen: RC-3000, RC-5000
            r"\b(RBS-\d{4})\b",  # Rollenbahnsysteme: RBS-2400
            r"\b(LTS-[A-Z]+)\b",  # Lineartransport: LTS-X
            r"\b(VS-Pro(?:\s+\d+\.?\d*)?)\b",  # Vision System: VS-Pro 3.0
            r"\b(DMS-\d{3})\b",  # Drehmomentsensoren: DMS-100, DMS-200
        ]
        codes = set()
        for pattern in patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            codes.update([m.upper() if isinstance(m, str) else m[0].upper() for m in matches])
        return list(codes)

    def extract_norm_references(self, text: str) -> List[str]:
        """Extract ISO/DIN/IEC norm references from text."""
        patterns = [
            r"\b(ISO\s*\d{4,5}(?:-\d+)?)\b",
            r"\b(DIN\s*(?:EN\s*)?\d{4,5}(?:-\d+)?)\b",
            r"\b(IEC\s*\d{4,5}(?:-\d+)?)\b",
            r"\b(EN\s*\d{4,5}(?:-\d+)?)\b",
        ]
        norms = set()
        for pattern in patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            norms.update([m.upper().replace("  ", " ") for m in matches])
        return list(norms)

    def detect_content_type(self, title: str, content: str) -> str:
        """Detect content type based on title and content patterns."""
        combined = f"{title}\n{content}".lower()
        for content_type, patterns in CONTENT_TYPE_PATTERNS.items():
            for pattern in patterns:
                if re.search(pattern, combined, re.IGNORECASE):
                    return content_type
        return "general"

    def build_hierarchy_path(self, space: str, parent: str, title: str) -> str:
        """Build a breadcrumb-style hierarchy path."""
        space_name = SPACE_NAMES.get(space, space)
        parts = [space_name]
        if parent and parent.lower() not in ["none", "home", ""]:
            parts.append(parent)
        parts.append(title)
        return " > ".join(parts)

    def generate_page_id(self, file_path: Path) -> str:
        """Generate a deterministic page ID from file path."""
        return hashlib.md5(str(file_path).encode()).hexdigest()[:12]

    def chunk_text(self, text: str) -> List[Tuple[str, int]]:
        """
        Split text into overlapping chunks.
        Returns list of (chunk_text, chunk_index) tuples.
        """
        if len(text) <= self.CHUNK_SIZE:
            return [(text, 0)]

        chunks = []
        start = 0
        chunk_index = 0

        while start < len(text):
            end = start + self.CHUNK_SIZE

            # Try to break at paragraph or sentence boundary
            if end < len(text):
                # Look for paragraph break
                para_break = text.rfind("\n\n", start, end)
                if para_break > start + self.CHUNK_SIZE // 2:
                    end = para_break + 2
                else:
                    # Look for sentence break
                    sentence_break = max(
                        text.rfind(". ", start, end),
                        text.rfind(".\n", start, end),
                    )
                    if sentence_break > start + self.CHUNK_SIZE // 2:
                        end = sentence_break + 2

            chunk = text[start:end].strip()
            if chunk:
                chunks.append((chunk, chunk_index))
                chunk_index += 1

            # Move start forward, accounting for overlap
            start = end - self.CHUNK_OVERLAP
            if start >= len(text) - self.CHUNK_OVERLAP:
                break

        return chunks

    def parse_markdown_file(self, file_path: Path) -> Optional[Dict]:
        """Parse a markdown file with YAML frontmatter."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Split frontmatter and content
            parts = content.split("---\n", 2)
            if len(parts) < 3:
                print(f"  Skipping {file_path}: No YAML frontmatter found")
                return None

            # Parse YAML frontmatter
            try:
                metadata = yaml.safe_load(parts[1])
            except yaml.YAMLError as e:
                print(f"  Error parsing YAML in {file_path}: {e}")
                return None

            # Get markdown content (after frontmatter)
            markdown_content = parts[2].strip()

            return {
                "title": metadata.get("title", ""),
                "space": metadata.get("space", ""),
                "parent": metadata.get("parent", ""),
                "level": metadata.get("level", 0),
                "content": markdown_content,
                "file_path": str(file_path),
            }

        except Exception as e:
            print(f"  Error reading {file_path}: {e}")
            return None

    def create_index(self):
        """Create the Elasticsearch index with German analyzers."""
        if self.es.indices.exists(index=self.index_name):
            print(f"Deleting existing index: {self.index_name}")
            self.es.indices.delete(index=self.index_name)

        print(f"Creating index: {self.index_name}")
        # ES 8.x client: pass settings and mappings as keyword arguments
        self.es.indices.create(
            index=self.index_name,
            settings=self.mapping.get("settings", {}),
            mappings=self.mapping.get("mappings", {}),
        )

    def test_german_analyzer(self):
        """Test that the German analyzer is working."""
        print("Testing German analyzer...")
        try:
            result = self.es.indices.analyze(
                index=self.index_name,
                analyzer="german_technical",
                text="Sicherheitssteuerung Wartungsanleitung technische Spezifikationen",
            )
            tokens = [t["token"] for t in result["tokens"]]
            print(f"  Analyzer tokens: {tokens}")
            return True
        except Exception as e:
            print(f"  Analyzer test failed: {e}")
            return False

    def index_documents(self, data_dir: Path):
        """Index all markdown files from the data directory with chunking."""
        markdown_files = list(data_dir.rglob("*.md"))

        if not markdown_files:
            print(f"No markdown files found in {data_dir}")
            return 0

        print(f"Found {len(markdown_files)} markdown files to index")
        print()

        # Test German analyzer
        if not self.test_german_analyzer():
            print("Warning: German analyzer test failed, continuing anyway...")
        print()

        documents = []
        total_chunks = 0
        indexed_at = datetime.now(timezone.utc).isoformat()

        for i, file_path in enumerate(markdown_files, 1):
            doc_data = self.parse_markdown_file(file_path)
            if not doc_data:
                continue

            # Extract metadata
            title = doc_data["title"]
            content = doc_data["content"]
            space = doc_data["space"]
            parent = doc_data["parent"]
            level = doc_data["level"]

            headings = self.extract_headings(content)
            product_codes = self.extract_product_codes(f"{title}\n{content}")
            norm_references = self.extract_norm_references(content)
            content_type = self.detect_content_type(title, content)
            hierarchy_path = self.build_hierarchy_path(space, parent, title)
            page_id = self.generate_page_id(file_path)

            # Chunk the content
            chunks = self.chunk_text(content)
            chunk_count = len(chunks)

            for chunk_text, chunk_index in chunks:
                # Generate embedding with title context
                embed_text = f"{title}\n\n{chunk_text}"
                embedding = self.embed_model.encode(embed_text).tolist()

                # Create document for bulk API
                doc = {
                    "_index": self.index_name,
                    "_id": f"{page_id}_{chunk_index}",
                    "_source": {
                        "title": title,
                        "content": chunk_text,
                        "headings": " ".join(headings),
                        "space": space,
                        "space_name": SPACE_NAMES.get(space, space),
                        "parent_page": parent if parent else None,
                        "hierarchy_path": hierarchy_path,
                        "level": level,
                        "content_type": content_type,
                        "product_codes": product_codes if product_codes else None,
                        "norm_references": norm_references if norm_references else None,
                        "page_id": page_id,
                        "chunk_index": chunk_index,
                        "chunk_count": chunk_count,
                        "url": f"/wiki/spaces/{space}/pages/{page_id}",
                        "source_file": str(
                            file_path.relative_to(data_dir.parent)
                            if file_path.is_relative_to(data_dir.parent)
                            else file_path.name
                        ),
                        "vector": embedding,
                        "indexed_at": indexed_at,
                    },
                }
                documents.append(doc)
                total_chunks += 1

            # Progress indicator
            print(
                f"[{i}/{len(markdown_files)}] {space}/{title[:40]}... ({chunk_count} chunks)"
            )

        # Bulk index
        print()
        print(f"Bulk indexing {total_chunks} chunks from {len(markdown_files)} pages...")

        success_count = 0
        errors = []

        for ok, response in helpers.streaming_bulk(
            self.es,
            documents,
            raise_on_error=False,
            raise_on_exception=False,
        ):
            if ok:
                success_count += 1
            else:
                errors.append(response)
                if len(errors) <= 3:
                    print(f"  Error: {response}")

        print(f"Successfully indexed: {success_count} chunks")
        if errors:
            print(f"Failed to index: {len(errors)}")

        # Refresh index
        self.es.indices.refresh(index=self.index_name)

        return success_count

    def verify_indexing(self):
        """Verify the indexing by showing stats."""
        count_result = self.es.count(index=self.index_name)
        total_docs = count_result["count"]

        # Get aggregations (ES 8.x: use keyword args instead of body)
        agg_result = self.es.search(
            index=self.index_name,
            size=0,
            aggs={
                "by_space": {"terms": {"field": "space", "size": 20}},
                "by_content_type": {"terms": {"field": "content_type", "size": 20}},
                "unique_pages": {"cardinality": {"field": "page_id"}},
                "products_mentioned": {"terms": {"field": "product_codes", "size": 20}},
            },
        )

        print()
        print("=" * 60)
        print("Indexing Summary")
        print("=" * 60)
        print(f"Total chunks indexed: {total_docs}")
        print(
            f"Unique pages: {agg_result['aggregations']['unique_pages']['value']}"
        )
        print()

        print("Chunks by space:")
        for bucket in agg_result["aggregations"]["by_space"]["buckets"]:
            space_name = SPACE_NAMES.get(bucket["key"], bucket["key"])
            print(f"  {bucket['key']} ({space_name}): {bucket['doc_count']}")
        print()

        print("Chunks by content type:")
        for bucket in agg_result["aggregations"]["by_content_type"]["buckets"]:
            print(f"  {bucket['key']}: {bucket['doc_count']}")
        print()

        print("Products mentioned:")
        for bucket in agg_result["aggregations"]["products_mentioned"]["buckets"]:
            print(f"  {bucket['key']}: {bucket['doc_count']} chunks")
        print("=" * 60)

    def test_search(self):
        """Run a sample search to verify everything works."""
        print()
        print("Testing search...")

        # Test BM25 search (ES 8.x: use keyword args instead of body)
        result = self.es.search(
            index=self.index_name,
            query={
                "multi_match": {
                    "query": "RC-3000 Wartung",
                    "fields": ["title^4", "headings^2", "content", "product_codes^3"],
                }
            },
            highlight={
                "fields": {"content": {"fragment_size": 150, "number_of_fragments": 2}}
            },
            size=3,
        )

        print(f"BM25 search for 'RC-3000 Wartung': {result['hits']['total']['value']} hits")
        for hit in result["hits"]["hits"][:3]:
            source = hit["_source"]
            print(f"  - {source['title']} (score: {hit['_score']:.2f})")
            if "highlight" in hit:
                print(f"    Highlight: {hit['highlight'].get('content', [''])[0][:100]}...")


def main():
    # Configuration from environment
    es_url = os.getenv("ELASTICSEARCH_HOST", "http://localhost:9201")
    index_name = os.getenv("ELASTICSEARCH_INDEX", "techmech_confluence_kb")
    embed_model = os.getenv("EMBED_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
    data_dir = os.getenv("CONFLUENCE_DATA_DIR", "../confluence/generated_confluence")

    # Resolve data directory
    if not os.path.isabs(data_dir):
        script_dir = Path(__file__).parent
        data_dir = script_dir / data_dir

    data_dir = Path(data_dir)

    if not data_dir.exists():
        print(f"Error: Data directory not found: {data_dir}")
        sys.exit(1)

    print("TechMech Confluence Markdown Indexer (Enhanced)")
    print("=" * 60)
    print(f"Data directory: {data_dir}")
    print(f"Elasticsearch: {es_url}")
    print(f"Index name: {index_name}")
    print(f"Embedding model: {embed_model}")
    print("=" * 60)
    print()

    # Create indexer
    indexer = MarkdownIndexer(es_url, index_name, embed_model)

    # Create index with German analyzers
    indexer.create_index()

    # Index documents
    success_count = indexer.index_documents(data_dir)

    if success_count > 0:
        # Verify
        indexer.verify_indexing()
        # Test search
        indexer.test_search()
        print()
        print("Indexing complete!")
        sys.exit(0)
    else:
        print("No documents were indexed")
        sys.exit(1)


if __name__ == "__main__":
    main()
