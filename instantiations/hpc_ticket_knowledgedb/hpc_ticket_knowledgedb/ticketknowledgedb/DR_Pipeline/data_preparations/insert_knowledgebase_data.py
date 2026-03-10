#!/usr/bin/env python3
"""
Script to insert knowledgebase data (ticket data) into Elasticsearch
Based on insert_inform_data.py but adapted for ticket knowledgebase structure
"""

import json
import os
import sys
import time
from typing import Dict, Any, List, Generator
import requests
from datetime import datetime
from pathlib import Path

# Configuration
ELASTIC_URL = os.getenv("ELASTIC_URL", "http://localhost:9200")
INDEX_NAME = "tickets"
DEFAULT_BATCH_SIZE = 1000
MAX_RETRIES = 3
RETRY_DELAY = 5

class TicketsElasticsearchInserter:
    """Handle Elasticsearch operations for ticket knowledgebase data insertion"""
    
    def __init__(self, elastic_url: str = ELASTIC_URL, index_name: str = INDEX_NAME, batch_size: int = DEFAULT_BATCH_SIZE):
        self.elastic_url = elastic_url
        self.index_name = index_name
        self.batch_size = batch_size
        self.session = requests.Session()
        
    def check_connection(self) -> bool:
        """Check if Elasticsearch is accessible"""
        try:
            response = self.session.get(f"{self.elastic_url}/_cluster/health", timeout=10)
            if response.status_code == 200:
                health = response.json()
                print(f"✓ Elasticsearch cluster status: {health.get('status', 'unknown')}")
                return True
            else:
                print(f"✗ Elasticsearch health check failed: {response.status_code}")
                return False
        except Exception as e:
            print(f"✗ Cannot connect to Elasticsearch: {e}")
            return False
    
    def create_index(self) -> bool:
        """Create the index with appropriate mappings for ticket knowledgebase data"""
        mapping = {
            "mappings": {
                "properties": {
                    "id": {
                        "type": "keyword"
                    },
                    "ticket_id": {
                        "type": "keyword"
                    },
                    "filename": {
                        "type": "keyword"
                    },
                    "title": {
                        "type": "text",
                        "analyzer": "standard",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        }
                    },
                    "keywords": {
                        "type": "text",
                        "analyzer": "standard"
                    },
                    "summary": {
                        "type": "text",
                        "analyzer": "standard"
                    },
                    "problem_description": {
                        "type": "text",
                        "analyzer": "standard"
                    },
                    "root_cause": {
                        "type": "text",
                        "analyzer": "standard"
                    },
                    "solution": {
                        "type": "text",
                        "analyzer": "standard"
                    },
                    "actions_taken": {
                        "type": "text",
                        "analyzer": "standard"
                    },
                    "general_learnings": {
                        "type": "text",
                        "analyzer": "standard"
                    },
                    "text": {
                        "type": "text",
                        "analyzer": "standard",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        }
                    },
                    "indexed_at": {
                        "type": "date"
                    },
                    "text_length": {
                        "type": "integer"
                    },
                    "source": {
                        "type": "keyword"
                    }
                }
            },
            "settings": {
                "number_of_shards": 1,
                "number_of_replicas": 0,
                "analysis": {
                    "analyzer": {
                        "standard_analyzer": {
                            "type": "standard",
                            "stopwords": "_english_"
                        },
                        "german_analyzer": {
                            "type": "standard",
                            "stopwords": "_german_"
                        }
                    }
                }
            }
        }
        
        try:
            # Check if index already exists
            response = self.session.head(f"{self.elastic_url}/{self.index_name}")
            if response.status_code == 200:
                print(f"ℹ️  Index '{self.index_name}' already exists")
                return True
            
            # Create the index
            response = self.session.put(
                f"{self.elastic_url}/{self.index_name}",
                json=mapping,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code in [200, 201]:
                print(f"✓ Created index '{self.index_name}'")
                return True
            else:
                print(f"✗ Failed to create index: {response.status_code} - {response.text}")
                return False
                
        except Exception as e:
            print(f"✗ Error creating index: {e}")
            return False
    
    def delete_index(self) -> bool:
        """Delete the index (useful for fresh start)"""
        try:
            response = self.session.delete(f"{self.elastic_url}/{self.index_name}")
            if response.status_code in [200, 404]:
                print(f"✓ Deleted index '{self.index_name}' (or it didn't exist)")
                return True
            else:
                print(f"✗ Failed to delete index: {response.status_code}")
                return False
        except Exception as e:
            print(f"✗ Error deleting index: {e}")
            return False
    
    def read_jsonl_file(self, file_path: str) -> Generator[Dict[str, Any], None, None]:
        """Read JSONL file and yield documents"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    if not line:
                        continue
                    
                    try:
                        doc = json.loads(line)
                        
                        # Ensure required fields exist
                        if 'id' not in doc or 'text' not in doc:
                            print(f"⚠️  Skipping line {line_num}: missing required fields")
                            continue
                        
                        # Add metadata
                        doc['indexed_at'] = datetime.utcnow().isoformat()
                        doc['text_length'] = len(doc.get('text', ''))
                        if 'source' not in doc:
                            doc['source'] = 'knowledgebase'
                        
                        yield doc
                        
                    except json.JSONDecodeError as e:
                        print(f"⚠️  Skipping line {line_num}: JSON decode error - {e}")
                        continue
                        
        except FileNotFoundError:
            print(f"✗ File not found: {file_path}")
            return
        except Exception as e:
            print(f"✗ Error reading file: {e}")
            return
    
    def bulk_insert(self, documents: List[Dict[str, Any]]) -> bool:
        """Insert documents using Elasticsearch bulk API"""
        if not documents:
            return True
        
        # Prepare bulk request body
        bulk_body = []
        for doc in documents:
            # Index action
            bulk_body.append(json.dumps({
                "index": {
                    "_index": self.index_name,
                    "_id": doc.get('id')
                }
            }))
            # Document source
            bulk_body.append(json.dumps(doc))
        
        bulk_data = '\n'.join(bulk_body) + '\n'
        
        # Send bulk request
        for attempt in range(MAX_RETRIES):
            try:
                response = self.session.post(
                    f"{self.elastic_url}/_bulk",
                    data=bulk_data,
                    headers={"Content-Type": "application/x-ndjson"},
                    timeout=60
                )
                
                if response.status_code == 200:
                    result = response.json()
                    
                    # Check for errors in bulk response
                    errors = []
                    for item in result.get('items', []):
                        if 'index' in item and item['index'].get('error'):
                            errors.append(item['index']['error'])
                    
                    if errors:
                        print(f"⚠️  Bulk insert had {len(errors)} errors")
                        for error in errors[:5]:  # Show first 5 errors
                            print(f"   - {error}")
                        return len(errors) < len(documents) / 2  # Success if < 50% errors
                    else:
                        return True
                else:
                    print(f"✗ Bulk insert failed: {response.status_code} - {response.text}")
                    
            except Exception as e:
                print(f"✗ Bulk insert attempt {attempt + 1} failed: {e}")
                
            if attempt < MAX_RETRIES - 1:
                print(f"Retrying in {RETRY_DELAY} seconds...")
                time.sleep(RETRY_DELAY)
        
        return False
    
    def get_index_stats(self) -> Dict[str, Any]:
        """Get index statistics"""
        try:
            response = self.session.get(f"{self.elastic_url}/{self.index_name}/_stats")
            if response.status_code == 200:
                return response.json()
            else:
                return {}
        except Exception:
            return {}
    
    def insert_from_file(self, file_path: str, recreate_index: bool = False) -> bool:
        """Insert all documents from a JSONL file"""
        print(f"Starting insertion from: {file_path}")
        
        if not os.path.exists(file_path):
            print(f"✗ File does not exist: {file_path}")
            return False
        
        # Check connection
        if not self.check_connection():
            return False
        
        # Recreate index if requested
        if recreate_index:
            self.delete_index()
        
        # Create index
        if not self.create_index():
            return False
        
        # Process file in batches
        batch = []
        total_processed = 0
        total_inserted = 0
        start_time = time.time()
        
        print(f"Processing file in batches of {self.batch_size}...")
        
        for doc in self.read_jsonl_file(file_path):
            batch.append(doc)
            total_processed += 1
            
            if len(batch) >= self.batch_size:
                if self.bulk_insert(batch):
                    total_inserted += len(batch)
                    print(f"✓ Inserted batch: {total_inserted:,} documents")
                else:
                    print(f"✗ Failed to insert batch at document {total_processed}")
                
                batch = []
                
                # Show progress every 10 batches
                if total_processed % (self.batch_size * 10) == 0:
                    elapsed = time.time() - start_time
                    rate = total_processed / elapsed
                    print(f"Progress: {total_processed:,} processed ({rate:.1f} docs/sec)")
        
        # Insert remaining documents
        if batch:
            if self.bulk_insert(batch):
                total_inserted += len(batch)
                print(f"✓ Inserted final batch: {total_inserted:,} documents")
        
        # Final statistics
        elapsed = time.time() - start_time
        print(f"\n=== Insertion Complete ===")
        print(f"Total processed: {total_processed:,}")
        print(f"Total inserted: {total_inserted:,}")
        print(f"Time taken: {elapsed:.2f} seconds")
        print(f"Average rate: {total_processed/elapsed:.1f} docs/sec")
        
        # Get final index stats
        stats = self.get_index_stats()
        if stats:
            doc_count = stats.get('indices', {}).get(self.index_name, {}).get('total', {}).get('docs', {}).get('count', 0)
            print(f"Final document count in index: {doc_count:,}")
        
        return total_inserted > 0

def main():
    """Main function with command line interface"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Insert ticket knowledgebase data into Elasticsearch")
    parser.add_argument("file_path", nargs='?', 
                       default="/Users/sebastian/Downloads/ticketknowledgedb/knowledgebase_data.jsonl",
                       help="Path to JSONL file")
    parser.add_argument("--elastic-url", default=ELASTIC_URL, help="Elasticsearch URL")
    parser.add_argument("--index-name", default=INDEX_NAME, help="Index name")
    parser.add_argument("--recreate", action="store_true", help="Recreate index (delete existing)")
    parser.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE, help="Batch size for bulk operations")
    
    args = parser.parse_args()
    
    # Create inserter with specified batch size
    inserter = TicketsElasticsearchInserter(args.elastic_url, args.index_name, args.batch_size)
    
    # Insert data
    success = inserter.insert_from_file(args.file_path, args.recreate)
    
    if success:
        print(f"\n🎉 Successfully inserted ticket knowledgebase data into '{args.index_name}' index!")
        print(f"You can now search using: curl -X POST {args.elastic_url}/{args.index_name}/_search")
    else:
        print(f"\n❌ Failed to insert data")
        sys.exit(1)

if __name__ == "__main__":
    main()
