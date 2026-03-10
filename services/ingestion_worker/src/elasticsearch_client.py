"""
Elasticsearch client for storing processed chunks and embeddings.
"""
import json
from typing import List, Dict, Any, Optional
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


class ElasticsearchClient:
    """
    Handles all Elasticsearch operations for the ingestion worker.
    """
    
    def __init__(self, es_host: str = "localhost", es_port: int = 9200, 
                 es_user: Optional[str] = None, es_password: Optional[str] = None):
        """
        Initialize Elasticsearch client.
        """
        if es_user and es_password:
            self.es = Elasticsearch(
                [{'host': es_host, 'port': es_port}],
                http_auth=(es_user, es_password),
                http_compress=True,
                request_timeout=30,
                max_retries=3,
                retry_on_timeout=True
            )
        else:
            self.es = Elasticsearch(
                [{'host': es_host, 'port': es_port}],
                http_compress=True,
                request_timeout=30,
                max_retries=3,
                retry_on_timeout=True
            )
        
        self.index_name = "tier-zero-documents"
        self._ensure_index_exists()
    
    def _ensure_index_exists(self):
        """
        Create the index with proper mapping if it doesn't exist.
        """
        if not self.es.indices.exists(index=self.index_name):
            mapping = {
                "mappings": {
                    "properties": {
                        "source_uri": {
                            "type": "keyword"
                        },
                        "source_type": {
                            "type": "keyword"
                        },
                        "content": {
                            "type": "text",
                            "analyzer": "standard"
                        },
                        "content_vector": {
                            "type": "dense_vector",
                            "dims": 768,
                            "index": True,
                            "similarity": "cosine"
                        },
                        "metadata": {
                            "type": "object",
                            "properties": {
                                "title": {"type": "text"},
                                "author": {"type": "keyword"},
                                "content_type": {"type": "keyword"},
                                "chunk_index": {"type": "integer"},
                                "total_chunks": {"type": "integer"},
                                "chunk_size": {"type": "integer"},
                                "headings": {
                                    "type": "nested",
                                    "properties": {
                                        "level": {"type": "integer"},
                                        "text": {"type": "text"}
                                    }
                                }
                            }
                        },
                        "permissions": {
                            "type": "keyword"
                        },
                        "ingested_at": {
                            "type": "date"
                        },
                        "document_id": {
                            "type": "keyword"
                        }
                    }
                },
                "settings": {
                    "number_of_shards": 1,
                    "number_of_replicas": 0,
                    "analysis": {
                        "analyzer": {
                            "standard": {
                                "type": "standard",
                                "stopwords": "_english_"
                            }
                        }
                    }
                }
            }
            
            self.es.indices.create(index=self.index_name, body=mapping)
            print(f"Created Elasticsearch index: {self.index_name}")
    
    def generate_document_id(self, source_uri: str, chunk_index: int) -> str:
        """
        Generate a unique document ID for a chunk.
        """
        import hashlib
        content = f"{source_uri}#{chunk_index}"
        return hashlib.md5(content.encode()).hexdigest()
    
    def store_chunks(self, source_uri: str, source_type: str, chunks: List[Dict[str, Any]], 
                    embeddings: List[List[float]], permissions: List[str], 
                    document_metadata: Dict[str, Any]) -> bool:
        """
        Store processed chunks with their embeddings in Elasticsearch.
        
        Args:
            source_uri: Original URI of the document
            source_type: Type of source (e.g., 'intranet', 'web')
            chunks: List of chunk dictionaries with content and metadata
            embeddings: List of embedding vectors for each chunk
            permissions: List of permission strings
            document_metadata: Metadata for the entire document
        
        Returns:
            bool: True if successful, False otherwise
        """
        if len(chunks) != len(embeddings):
            raise ValueError("Number of chunks must match number of embeddings")
        
        # Prepare documents for bulk indexing
        documents = []
        ingested_at = datetime.utcnow().isoformat()
        
        for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
            doc_id = self.generate_document_id(source_uri, chunk['metadata'].get('chunk_index', i))
            
            # Merge chunk metadata with document metadata
            merged_metadata = document_metadata.copy()
            merged_metadata.update(chunk['metadata'])
            
            document = {
                "_index": self.index_name,
                "_id": doc_id,
                "_source": {
                    "document_id": doc_id,
                    "source_uri": source_uri,
                    "source_type": source_type,
                    "content": chunk['content'],
                    "content_vector": embedding,
                    "metadata": merged_metadata,
                    "permissions": permissions,
                    "ingested_at": ingested_at
                }
            }
            documents.append(document)
        
        try:
            # Use bulk API for efficient indexing
            success, failed = bulk(self.es, documents, refresh=True)
            
            if failed:
                print(f"Failed to index {len(failed)} documents: {failed}")
                return False
            
            print(f"Successfully indexed {success} chunks from {source_uri}")
            return True
            
        except Exception as e:
            print(f"Error storing chunks in Elasticsearch: {e}")
            return False
    
    def search_similar(self, query_vector: List[float], size: int = 10, 
                      filters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        Search for similar documents using vector similarity.
        
        Args:
            query_vector: Query embedding vector
            size: Number of results to return
            filters: Optional filters (e.g., permissions, source_type)
        
        Returns:
            List of matching documents with scores
        """
        query = {
            "knn": {
                "field": "content_vector",
                "query_vector": query_vector,
                "k": size,
                "num_candidates": size * 2
            }
        }
        
        # Add filters if provided
        if filters:
            query["filter"] = []
            for field, value in filters.items():
                if isinstance(value, list):
                    query["filter"].append({"terms": {field: value}})
                else:
                    query["filter"].append({"term": {field: value}})
        
        try:
            response = self.es.search(
                index=self.index_name,
                body={"query": query, "size": size}
            )
            
            results = []
            for hit in response['hits']['hits']:
                result = hit['_source']
                result['_score'] = hit['_score']
                results.append(result)
            
            return results
            
        except Exception as e:
            print(f"Error searching Elasticsearch: {e}")
            return []
    
    def search_text(self, query: str, size: int = 10, 
                   filters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        Search for documents using text search.
        
        Args:
            query: Text query
            size: Number of results to return
            filters: Optional filters
        
        Returns:
            List of matching documents with scores
        """
        search_query = {
            "multi_match": {
                "query": query,
                "fields": ["content^2", "metadata.title^3", "metadata.description"],
                "type": "best_fields",
                "fuzziness": "AUTO"
            }
        }
        
        # Add filters if provided
        if filters:
            search_query = {
                "bool": {
                    "must": [search_query],
                    "filter": []
                }
            }
            
            for field, value in filters.items():
                if isinstance(value, list):
                    search_query["bool"]["filter"].append({"terms": {field: value}})
                else:
                    search_query["bool"]["filter"].append({"term": {field: value}})
        
        try:
            response = self.es.search(
                index=self.index_name,
                body={
                    "query": search_query,
                    "size": size,
                    "highlight": {
                        "fields": {
                            "content": {},
                            "metadata.title": {}
                        }
                    }
                }
            )
            
            results = []
            for hit in response['hits']['hits']:
                result = hit['_source']
                result['_score'] = hit['_score']
                if 'highlight' in hit:
                    result['_highlight'] = hit['highlight']
                results.append(result)
            
            return results
            
        except Exception as e:
            print(f"Error searching Elasticsearch: {e}")
            return []
    
    def delete_document(self, source_uri: str) -> bool:
        """
        Delete all chunks for a specific document.
        
        Args:
            source_uri: URI of the document to delete
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            query = {"term": {"source_uri": source_uri}}
            response = self.es.delete_by_query(
                index=self.index_name,
                body={"query": query},
                refresh=True
            )
            
            deleted_count = response.get('deleted', 0)
            print(f"Deleted {deleted_count} chunks for document: {source_uri}")
            return True
            
        except Exception as e:
            print(f"Error deleting document from Elasticsearch: {e}")
            return False
    
    def health_check(self) -> bool:
        """
        Check if Elasticsearch is healthy and accessible.
        
        Returns:
            bool: True if healthy, False otherwise
        """
        try:
            health = self.es.cluster.health()
            return health['status'] in ['green', 'yellow']
        except Exception as e:
            print(f"Elasticsearch health check failed: {e}")
            return False
