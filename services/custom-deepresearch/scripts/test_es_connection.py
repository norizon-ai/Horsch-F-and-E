#!/usr/bin/env python3
"""
Test script for Elasticsearch agent connectivity.

Tests:
1. Direct Elasticsearch connectivity via HTTP
2. ElasticsearchBackend search functionality
3. ElasticsearchSearchTool execution

Usage:
    python scripts/test_es_connection.py

    # Or with custom ES URL
    ES_URL=http://localhost:9200 python scripts/test_es_connection.py
"""

import asyncio
import os
import sys
from pathlib import Path

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))


async def test_direct_connection(es_url: str, index: str) -> bool:
    """Test 1: Direct HTTP connection to Elasticsearch."""
    print("\n" + "=" * 60)
    print("TEST 1: Direct Elasticsearch Connection")
    print("=" * 60)

    import httpx

    try:
        async with httpx.AsyncClient() as client:
            # Test cluster health
            response = await client.get(f"{es_url}/_cluster/health")
            if response.status_code != 200:
                print(f"FAIL: Health check returned {response.status_code}")
                return False

            health = response.json()
            print(f"Cluster: {health['cluster_name']}")
            print(f"Status: {health['status']}")
            print(f"Nodes: {health['number_of_nodes']}")

            # Test index exists
            response = await client.head(f"{es_url}/{index}")
            if response.status_code == 200:
                print(f"Index '{index}': EXISTS")
            else:
                print(f"FAIL: Index '{index}' does not exist (status {response.status_code})")
                return False

            # Test document count
            response = await client.get(f"{es_url}/{index}/_count")
            if response.status_code == 200:
                count = response.json()["count"]
                print(f"Document count: {count}")
            else:
                print(f"FAIL: Count returned {response.status_code}")
                return False

            print("PASS: Direct connection successful")
            return True

    except Exception as e:
        print(f"FAIL: {e}")
        return False


async def test_backend(es_url: str, index: str) -> bool:
    """Test 2: ElasticsearchBackend search functionality."""
    print("\n" + "=" * 60)
    print("TEST 2: ElasticsearchBackend Search")
    print("=" * 60)

    try:
        from deepsearch.retrievers.search_backends.elasticsearch import (
            ElasticsearchBackend,
            ElasticsearchConfig,
        )

        config = ElasticsearchConfig(
            url=es_url,
            index=index,
            search_fields=["title^3", "content"],
        )

        backend = ElasticsearchBackend(config)

        # Test search
        test_queries = ["roboter", "wartung", "sicherheit"]

        for query in test_queries:
            result = await backend.search(query=query, max_results=3)

            if result.error:
                print(f"FAIL: Search for '{query}' returned error: {result.error}")
                await backend.close()
                return False

            print(f"\nQuery: '{query}'")
            print(f"  Found: {result.total_found} results")
            for i, doc in enumerate(result.results[:3], 1):
                print(f"  {i}. {doc.title[:50]}... (score: {doc.score:.2f})")

        await backend.close()
        print("\nPASS: Backend search successful")
        return True

    except Exception as e:
        print(f"FAIL: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_tool(es_url: str, index: str) -> bool:
    """Test 3: ElasticsearchSearchTool execution."""
    print("\n" + "=" * 60)
    print("TEST 3: ElasticsearchSearchTool Execution")
    print("=" * 60)

    try:
        from deepsearch.agents.elasticsearch.tools import ElasticsearchSearchTool

        tool = ElasticsearchSearchTool(
            es_url=es_url,
            index=index,
            search_fields=["title^3", "content"],
        )

        print(f"Tool name: {tool.name}")
        print(f"Tool description: {tool.description}")

        # Test execute
        result = await tool.execute(query="RC-3000 Wartung", max_results=5)

        if not result.success:
            print(f"FAIL: Tool execution failed: {result.error}")
            await tool.close()
            return False

        print(f"\nSearch results:")
        print(f"  Total found: {result.data['total_found']}")
        for i, doc in enumerate(result.data['results'][:3], 1):
            print(f"  {i}. {doc['title'][:50]}... (score: {doc['score']:.2f})")

        # Verify sources are returned in data dict
        if result.data.get("sources"):
            print(f"\nSources returned: {len(result.data['sources'])}")
        else:
            print(f"\nWARNING: No sources returned in data")

        await tool.close()
        print("\nPASS: Tool execution successful")
        return True

    except Exception as e:
        print(f"FAIL: {e}")
        import traceback
        traceback.print_exc()
        return False


async def main():
    """Run all tests."""
    es_url = os.getenv("ES_URL", "http://localhost:9200")
    index = os.getenv("ES_INDEX", "demo_confluence_kb")

    print("=" * 60)
    print("Elasticsearch Agent Connection Tests")
    print("=" * 60)
    print(f"ES URL: {es_url}")
    print(f"Index: {index}")

    results = []

    # Test 1: Direct connection
    results.append(("Direct Connection", await test_direct_connection(es_url, index)))

    # Test 2: Backend search
    results.append(("Backend Search", await test_backend(es_url, index)))

    # Test 3: Tool execution
    results.append(("Tool Execution", await test_tool(es_url, index)))

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    all_passed = True
    for name, passed in results:
        status = "PASS" if passed else "FAIL"
        print(f"  {name}: {status}")
        if not passed:
            all_passed = False

    print()
    if all_passed:
        print("All tests passed!")
        return 0
    else:
        print("Some tests failed!")
        return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
