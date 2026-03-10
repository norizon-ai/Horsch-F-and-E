#!/usr/bin/env python3
"""
Test script to verify Elasticsearch ingestion and vector search functionality.
"""

import json
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer

ELASTICSEARCH_URL = "http://localhost:9200"
INDEX_NAME = "knowledge_articles"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def test_elasticsearch_connection():
    """Test connection to Elasticsearch."""
    es = Elasticsearch(ELASTICSEARCH_URL)
    
    if not es.ping():
        print("❌ Cannot connect to Elasticsearch")
        return None
        
    print("✅ Connected to Elasticsearch")
    
    # Get cluster info
    info = es.info()
    print(f"   Version: {info['version']['number']}")
    
    return es


def test_index_exists(es):
    """Check if the index exists and get stats."""
    if not es.indices.exists(index=INDEX_NAME):
        print(f"❌ Index '{INDEX_NAME}' does not exist")
        return False
        
    print(f"✅ Index '{INDEX_NAME}' exists")
    
    # Get index stats
    stats = es.indices.stats(index=INDEX_NAME)
    doc_count = stats['_all']['primaries']['docs']['count']
    print(f"   Document count: {doc_count}")
    
    # Get mapping
    mapping = es.indices.get_mapping(index=INDEX_NAME)
    if 'content_vector' in mapping[INDEX_NAME]['mappings']['properties']:
        vector_props = mapping[INDEX_NAME]['mappings']['properties']['content_vector']
        print(f"   Vector field configured: dims={vector_props.get('dims', 'unknown')}")
    
    return True


def test_sample_documents(es):
    """Retrieve and display sample documents."""
    print("\n📄 Sample Documents:")
    
    # Get 3 random documents
    response = es.search(
        index=INDEX_NAME,
        body={
            "size": 3,
            "query": {"match_all": {}},
            "_source": ["document_id", "metadata.title", "source.uri", "content"]
        }
    )
    
    if response['hits']['total']['value'] == 0:
        print("   No documents found in index")
        return
        
    for i, hit in enumerate(response['hits']['hits'], 1):
        doc = hit['_source']
        print(f"\n   Document {i}:")
        print(f"   - ID: {doc.get('document_id', 'N/A')}")
        print(f"   - Title: {doc.get('metadata', {}).get('title', 'N/A')}")
        print(f"   - URL: {doc.get('source', {}).get('uri', 'N/A')}")
        print(f"   - Content preview: {doc.get('content', '')[:200]}...")


def test_vector_search(es):
    """Test vector similarity search."""
    print("\n🔍 Testing Vector Search:")
    
    # Initialize embedding model
    model = SentenceTransformer(EMBEDDING_MODEL)
    
    # Test queries
    test_queries = [
        "Wie kann ich mich für Kurse anmelden?",
        "Einführungsveranstaltungen für neue Studierende",
        "Praktikum im Ausland"
    ]
    
    for query in test_queries:
        print(f"\n   Query: '{query}'")
        
        # Generate query embedding
        query_vector = model.encode(query).tolist()
        
        # Perform vector search
        response = es.search(
            index=INDEX_NAME,
            body={
                "size": 3,
                "query": {
                    "script_score": {
                        "query": {"match_all": {}},
                        "script": {
                            "source": "cosineSimilarity(params.query_vector, 'content_vector') + 1.0",
                            "params": {"query_vector": query_vector}
                        }
                    }
                },
                "_source": ["metadata.title", "source.uri"]
            }
        )
        
        # Display results
        for hit in response['hits']['hits']:
            score = hit['_score']
            title = hit['_source'].get('metadata', {}).get('title', 'N/A')
            print(f"   - Score: {score:.3f} | {title[:60]}...")


def test_text_search(es):
    """Test traditional text search."""
    print("\n📝 Testing Text Search:")
    
    test_queries = [
        "Studienstart",
        "Einführungsveranstaltung",
        "BAföG"
    ]
    
    for query in test_queries:
        print(f"\n   Query: '{query}'")
        
        response = es.search(
            index=INDEX_NAME,
            body={
                "size": 3,
                "query": {
                    "multi_match": {
                        "query": query,
                        "fields": ["content", "metadata.title^2", "metadata.description"]
                    }
                },
                "_source": ["metadata.title"]
            }
        )
        
        # Display results
        total = response['hits']['total']['value']
        print(f"   Found {total} matching documents")
        for hit in response['hits']['hits']:
            title = hit['_source'].get('metadata', {}).get('title', 'N/A')
            print(f"   - {title[:70]}...")


def main():
    """Run all tests."""
    print("=" * 60)
    print("Elasticsearch Ingestion Test Suite")
    print("=" * 60)
    
    # Test connection
    es = test_elasticsearch_connection()
    if not es:
        print("\n⚠️  Cannot proceed without Elasticsearch connection")
        print("Please ensure Elasticsearch is running:")
        print("  docker-compose -f services/database/docker-compose.yml up -d elasticsearch")
        return
    
    # Test index
    if not test_index_exists(es):
        print("\n⚠️  Index not found. Please run the ingestion script first:")
        print("  python services/ingestion_worker/src/direct_ingest.py")
        return
    
    # Test documents
    test_sample_documents(es)
    
    # Test search capabilities
    try:
        test_vector_search(es)
    except Exception as e:
        print(f"\n⚠️  Vector search test failed: {e}")
        print("Make sure the embedding model is installed")
    
    test_text_search(es)
    
    print("\n" + "=" * 60)
    print("✅ Test suite completed")
    print("=" * 60)


if __name__ == "__main__":
    main()