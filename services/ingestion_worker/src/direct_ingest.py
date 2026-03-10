#!/usr/bin/env python3
"""
Direct ingestion script for crawled articles into Elasticsearch.
Reads JSON files from crawler output and indexes them with vector embeddings.
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any
import uuid

from elasticsearch import Elasticsearch, helpers
from sentence_transformers import SentenceTransformer
import numpy as np

# Configuration
ELASTICSEARCH_URL = "http://localhost:9200"
INDEX_NAME = "knowledge_articles"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"  # 384-dim model, fast and efficient
BATCH_SIZE = 10  # Number of documents to process at once

class ArticleIngester:
    def __init__(self, es_url: str = ELASTICSEARCH_URL, index_name: str = INDEX_NAME):
        """Initialize the ingester with Elasticsearch connection and embedding model."""
        self.es = Elasticsearch(es_url)
        self.index_name = index_name
        self.embedding_model = SentenceTransformer(EMBEDDING_MODEL)
        
        # Check connection
        if not self.es.ping():
            raise ConnectionError("Cannot connect to Elasticsearch")
        print(f"Connected to Elasticsearch at {es_url}")
        
    def create_index(self):
        """Create the Elasticsearch index with proper mapping for vectors."""
        # Check if index exists
        if self.es.indices.exists(index=self.index_name):
            print(f"Index '{self.index_name}' already exists")
            return
            
        # Define mapping with vector field
        mapping = {
            "mappings": {
                "properties": {
                    "document_id": {"type": "keyword"},
                    "content": {"type": "text"},
                    "content_vector": {
                        "type": "dense_vector",
                        "dims": 384,  # Dimension of all-MiniLM-L6-v2
                        "index": True,
                        "similarity": "cosine"
                    },
                    "source": {
                        "properties": {
                            "id": {"type": "keyword"},
                            "uri": {"type": "keyword"},
                            "module": {"type": "keyword"},
                            "ingested_at": {"type": "date"}
                        }
                    },
                    "author": {
                        "properties": {
                            "name": {"type": "text"}
                        }
                    },
                    "access_control": {
                        "properties": {
                            "users": {"type": "keyword"},
                            "groups": {"type": "keyword"}
                        }
                    },
                    "metadata": {
                        "properties": {
                            "created_at": {"type": "date"},
                            "updated_at": {"type": "date"},
                            "version": {"type": "integer"},
                            "language": {"type": "keyword"},
                            "is_verified": {"type": "boolean"},
                            "is_obsolete": {"type": "boolean"},
                            "title": {"type": "text"},
                            "description": {"type": "text"},
                            "keywords": {"type": "text"}
                        }
                    },
                    "tags": {"type": "keyword"},
                    "engagement": {
                        "properties": {
                            "upvotes": {"type": "integer"},
                            "downvotes": {"type": "integer"},
                            "retrieval_count": {"type": "integer"}
                        }
                    },
                    "comments": {
                        "type": "nested",
                        "properties": {
                            "user": {"type": "text"},
                            "timestamp": {"type": "date"},
                            "comment": {"type": "text"}
                        }
                    }
                }
            }
        }
        
        # Create index
        self.es.indices.create(index=self.index_name, body=mapping)
        print(f"Created index '{self.index_name}' with vector mapping")
        
    def generate_embedding(self, text: str) -> List[float]:
        """Generate embedding vector for the given text."""
        # Truncate very long texts to avoid memory issues
        max_length = 5000  # Characters
        if len(text) > max_length:
            text = text[:max_length]
            
        # Generate embedding
        embedding = self.embedding_model.encode(text, convert_to_numpy=True)
        return embedding.tolist()
        
    def process_crawled_file(self, file_path: Path) -> Dict[str, Any]:
        """Process a single crawled JSON file and prepare it for indexing."""
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        # Generate unique document ID
        doc_id = str(uuid.uuid4())
        
        # Extract content and generate embedding
        content = data.get('content', '')
        content_vector = self.generate_embedding(content)
        
        # Extract metadata
        source_data = data.get('source', {})
        metadata = data.get('metadata', {})
        
        # Prepare document for Elasticsearch
        document = {
            "document_id": doc_id,
            "content": content,
            "content_vector": content_vector,
            "source": {
                "id": data.get('source_document_id', ''),
                "uri": source_data.get('uri', ''),
                "module": source_data.get('module', 'Intranet Connector'),
                "ingested_at": source_data.get('retrieved_at', datetime.utcnow().isoformat())
            },
            "author": {
                "name": data.get('author', {}).get('name', 'Unknown') if data.get('author') else 'Unknown'
            },
            "access_control": {
                "users": [p for p in data.get('permissions', []) if p.startswith('user:')],
                "groups": [p for p in data.get('permissions', []) if p.startswith('group:')]
            },
            "metadata": {
                "created_at": datetime.utcnow().isoformat(),
                "updated_at": datetime.utcnow().isoformat(),
                "version": 1,
                "language": "de",  # German content from FAU
                "is_verified": False,
                "is_obsolete": False,
                "title": metadata.get('og:title', metadata.get('title', '')),
                "description": metadata.get('og:description', metadata.get('description', '')),
                "keywords": metadata.get('keywords', '')
            },
            "tags": data.get('tags', []),
            "engagement": {
                "upvotes": 0,
                "downvotes": 0,
                "retrieval_count": 0
            },
            "comments": []
        }
        
        return document
        
    def ingest_directory(self, directory_path: str):
        """Ingest all JSON files from a directory structure."""
        base_path = Path(directory_path)
        
        if not base_path.exists():
            print(f"Directory {directory_path} does not exist")
            return
            
        # Find all JSON files
        json_files = list(base_path.rglob("*.json"))
        
        # Filter out index.jsonl and other non-article files
        article_files = [
            f for f in json_files 
            if f.name not in ['index.jsonl', 'statistics.json', 'error_statistics.json']
            and not f.name.endswith('.jsonl')
        ]
        
        print(f"Found {len(article_files)} article files to process")
        
        # Process in batches
        documents = []
        for i, file_path in enumerate(article_files, 1):
            try:
                print(f"Processing file {i}/{len(article_files)}: {file_path.name}")
                doc = self.process_crawled_file(file_path)
                documents.append({
                    "_index": self.index_name,
                    "_id": doc["document_id"],
                    "_source": doc
                })
                
                # Bulk index when batch is full
                if len(documents) >= BATCH_SIZE:
                    self._bulk_index(documents)
                    documents = []
                    
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
                continue
                
        # Index remaining documents
        if documents:
            self._bulk_index(documents)
            
        print(f"Ingestion complete. Indexed {len(article_files)} documents")
        
    def _bulk_index(self, documents: List[Dict]):
        """Bulk index documents to Elasticsearch."""
        try:
            success, failed = helpers.bulk(self.es, documents, stats_only=True)
            print(f"Bulk indexed {success} documents successfully")
            if failed:
                print(f"Failed to index {failed} documents")
        except Exception as e:
            print(f"Bulk indexing error: {e}")
            
    def search_similar(self, query_text: str, k: int = 5):
        """Search for similar documents using vector similarity."""
        # Generate query embedding
        query_vector = self.generate_embedding(query_text)
        
        # Perform vector search
        script_query = {
            "script_score": {
                "query": {"match_all": {}},
                "script": {
                    "source": "cosineSimilarity(params.query_vector, 'content_vector') + 1.0",
                    "params": {"query_vector": query_vector}
                }
            }
        }
        
        response = self.es.search(
            index=self.index_name,
            body={
                "size": k,
                "query": script_query,
                "_source": ["document_id", "metadata.title", "source.uri"]
            }
        )
        
        return response['hits']['hits']


def main():
    """Main function to run the ingestion process."""
    # Initialize ingester
    print("Initializing Article Ingester...")
    ingester = ArticleIngester()
    
    # Create index if needed
    print("Setting up Elasticsearch index...")
    ingester.create_index()
    
    # Define data directory
    data_dir = "/Users/lisaschmidt/Documents/GitHub/rag-server/services/connectors/intranet_connector/src/dev_crawled_data"
    
    # Ingest all articles
    print(f"Starting ingestion from {data_dir}")
    ingester.ingest_directory(data_dir)
    
    # Test with a sample search
    print("\nTesting vector search...")
    results = ingester.search_similar("Studienstart FAU Einführungsveranstaltungen", k=3)
    
    print("\nTop 3 similar documents:")
    for hit in results:
        source = hit['_source']
        print(f"- Score: {hit['_score']:.3f}")
        print(f"  Title: {source.get('metadata', {}).get('title', 'N/A')}")
        print(f"  URL: {source.get('source', {}).get('uri', 'N/A')}")
        print()


if __name__ == "__main__":
    main()