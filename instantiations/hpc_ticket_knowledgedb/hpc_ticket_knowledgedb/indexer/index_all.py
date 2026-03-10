#!/usr/bin/env python3
"""
Unified indexer for HPC Knowledge Database
Indexes docs, tickets, and knowledgebase into Elasticsearch
"""

import os
import sys
import glob
import json
from pathlib import Path

# Import the existing indexing scripts
sys.path.insert(0, '/app/data/DR_Pipeline/data_preparations')

from insert_docs_data import DocsElasticsearchInserter
from insert_knowledgebase_data import TicketsElasticsearchInserter

# Configuration from environment
ELASTIC_URL = os.getenv("ELASTIC_URL", "http://localhost:9200")
DOCS_INDEX = os.getenv("DOCS_INDEX", "docs")
TICKETS_INDEX = os.getenv("TICKETS_INDEX", "tickets")
DATA_DIR = "/app/data"


def index_docs():
    """Index documentation data"""
    print("=" * 80)
    print("INDEXING DOCUMENTATION")
    print("=" * 80)

    docs_jsonl = f"{DATA_DIR}/docsmd/docs_data.jsonl"

    if not os.path.exists(docs_jsonl):
        print(f"[!] Warning: {docs_jsonl} not found, skipping docs indexing")
        return False

    try:
        inserter = DocsElasticsearchInserter(
            elastic_url=ELASTIC_URL,
            index_name=DOCS_INDEX
        )

        if not inserter.check_connection():
            print("[ERROR] Failed to connect to Elasticsearch")
            return False

        # Create index
        inserter.create_index()

        # Insert data
        with open(docs_jsonl, 'r') as f:
            docs = [json.loads(line) for line in f]

        print(f"Found {len(docs)} documentation entries")

        # Use the inserter's bulk insert method
        # Note: You may need to adapt this based on the actual method signature
        success_count = 0
        batch_size = 1000

        for i in range(0, len(docs), batch_size):
            batch = docs[i:i+batch_size]
            try:
                if inserter.bulk_insert(batch):
                    success_count += len(batch)
                    print(f"  Indexed {success_count}/{len(docs)} docs")
                else:
                    print(f"  [ERROR] Batch failed")
            except Exception as e:
                print(f"  [ERROR] Batch failed: {e}")

        if success_count > 0:
            print(f"Successfully indexed {success_count} documentation entries")
            return True
        else:
            print(f"[ERROR] Failed to index any documentation entries")
            return False

    except Exception as e:
        print(f"[ERROR] Documentation indexing failed: {e}")
        return False


def index_tickets():
    """Index ticket knowledgebase data"""
    print("\n" + "=" * 80)
    print("INDEXING TICKETS")
    print("=" * 80)

    # Look for knowledgebase markdown files
    kb_dir = f"{DATA_DIR}/knowledgebase"

    if not os.path.exists(kb_dir):
        print(f"[!] Warning: {kb_dir} not found, skipping tickets indexing")
        return False

    try:
        inserter = TicketsElasticsearchInserter(
            elastic_url=ELASTIC_URL,
            index_name=TICKETS_INDEX
        )

        if not inserter.check_connection():
            print("[ERROR] Failed to connect to Elasticsearch")
            return False

        # Create index
        inserter.create_index()

        # Read all markdown files from knowledgebase
        md_files = glob.glob(f"{kb_dir}/*.md")
        print(f"Found {len(md_files)} ticket markdown files")

        # Convert to documents for indexing
        documents = []
        for md_file in md_files:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                filename = os.path.basename(md_file)

                # Create document
                doc = {
                    "id": filename.replace('.md', ''),
                    "filename": filename,
                    "title": filename.replace('.md', '').replace('_', ' '),
                    "text": content,
                    "source": "knowledgebase",
                    "text_length": len(content)
                }
                documents.append(doc)

        # Insert in batches
        success_count = 0
        batch_size = 100

        for i in range(0, len(documents), batch_size):
            batch = documents[i:i+batch_size]
            try:
                if inserter.bulk_insert(batch):
                    success_count += len(batch)
                    print(f"  Indexed {success_count}/{len(documents)} tickets")
                else:
                    print(f"  [ERROR] Batch failed")
            except Exception as e:
                print(f"  [ERROR] Batch failed: {e}")

        if success_count > 0:
            print(f"Successfully indexed {success_count} tickets")
            return True
        else:
            print(f"[ERROR] Failed to index any tickets")
            return False

    except Exception as e:
        print(f"[ERROR] Tickets indexing failed: {e}")
        return False


def index_topic_clusters():
    """Index topic clusters (optional)"""
    print("\n" + "=" * 80)
    print("INDEXING TOPIC CLUSTERS")
    print("=" * 80)

    clusters_dir = f"{DATA_DIR}/topic_clusters"

    if not os.path.exists(clusters_dir):
        print(f"[INFO] {clusters_dir} not found, skipping topic clusters")
        return True  # Not critical

    try:
        # Index topic clusters into tickets index
        inserter = TicketsElasticsearchInserter(
            elastic_url=ELASTIC_URL,
            index_name=TICKETS_INDEX
        )

        md_files = glob.glob(f"{clusters_dir}/*.md")
        print(f"Found {len(md_files)} topic cluster files")

        documents = []
        for md_file in md_files:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                filename = os.path.basename(md_file)

                doc = {
                    "id": f"cluster_{filename.replace('.md', '')}",
                    "filename": filename,
                    "title": filename.replace('topic_', 'Topic: ').replace('.md', '').replace('_', ' '),
                    "text": content,
                    "source": "topic_cluster",
                    "text_length": len(content)
                }
                documents.append(doc)

        if documents:
            batch_size = 50
            success_count = 0
            for i in range(0, len(documents), batch_size):
                batch = documents[i:i+batch_size]
                try:
                    if inserter.bulk_insert(batch):
                        success_count += len(batch)
                except Exception as e:
                    print(f"  [ERROR] Batch failed: {e}")

            if success_count > 0:
                print(f"Successfully indexed {success_count} topic clusters")
            else:
                print(f"[!] Failed to index any topic clusters")

        return True  # Not critical, don't fail the whole process

    except Exception as e:
        print(f"[!] Topic clusters indexing failed: {e}")
        return True  # Not critical


def main():
    """Main indexing workflow"""
    print("\n" + "=" * 80)
    print("HPC KNOWLEDGE DATABASE INDEXER")
    print("=" * 80)
    print(f"Elasticsearch URL: {ELASTIC_URL}")
    print(f"Docs Index: {DOCS_INDEX}")
    print(f"Tickets Index: {TICKETS_INDEX}")
    print(f"Data Directory: {DATA_DIR}")
    print("=" * 80)

    results = {
        "docs": False,
        "tickets": False,
        "clusters": False
    }

    # Index docs
    results["docs"] = index_docs()

    # Index tickets
    results["tickets"] = index_tickets()

    # Index topic clusters (optional)
    results["clusters"] = index_topic_clusters()

    # Summary
    print("\n" + "=" * 80)
    print("INDEXING SUMMARY")
    print("=" * 80)
    print(f"  Documentation: {'[OK]' if results['docs'] else '[FAILED]'}")
    print(f"  Tickets: {'[OK]' if results['tickets'] else '[FAILED]'}")
    print(f"  Topic Clusters: {'[OK]' if results['clusters'] else '[!] (optional)'}")
    print("=" * 80)

    # Exit code based on critical components
    if results["docs"] or results["tickets"]:
        print("Indexing completed successfully")
        sys.exit(0)
    else:
        print("[ERROR] Indexing failed - no data indexed")
        sys.exit(1)


if __name__ == "__main__":
    main()
