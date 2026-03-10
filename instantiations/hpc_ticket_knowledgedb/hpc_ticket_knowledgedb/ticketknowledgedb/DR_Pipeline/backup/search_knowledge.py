#!/usr/bin/env python3
"""
Unified search script for both documentation and ticket knowledgebase
Allows searching across both indices or specific ones
"""

import json
import os
import sys
import requests
from typing import Dict, Any, List, Optional
import argparse

# Configuration
ELASTIC_URL = os.getenv("ELASTIC_URL", "http://localhost:9200")
DOCS_INDEX = "docs"
TICKETS_INDEX = "tickets"

class KnowledgeSearcher:
    """Search across documentation and ticket knowledgebase"""
    
    def __init__(self, elastic_url: str = ELASTIC_URL):
        self.elastic_url = elastic_url
        self.session = requests.Session()
    
    def check_connection(self) -> bool:
        """Check if Elasticsearch is accessible"""
        try:
            response = self.session.get(f"{self.elastic_url}/_cluster/health", timeout=10)
            return response.status_code == 200
        except Exception:
            return False
    
    def search_index(self, query: str, index_name: str, size: int = 10, 
                    fields: Optional[List[str]] = None) -> Dict[str, Any]:
        """Search a specific index"""
        
        # Default fields to search
        if not fields:
            if index_name == DOCS_INDEX:
                fields = ["title^2", "text", "titles"]
            else:  # tickets index
                fields = ["title^2", "summary^1.5", "keywords^1.5", "text", 
                         "problem_description", "solution", "actions_taken"]
        
        search_body = {
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": fields,
                    "type": "best_fields",
                    "fuzziness": "AUTO"
                }
            },
            "highlight": {
                "fields": {
                    "text": {"fragment_size": 150, "number_of_fragments": 3},
                    "title": {},
                    "summary": {},
                    "solution": {"fragment_size": 200, "number_of_fragments": 2}
                }
            },
            "size": size,
            "_source": {
                "excludes": ["text"] if index_name == DOCS_INDEX else []
            }
        }
        
        try:
            response = self.session.post(
                f"{self.elastic_url}/{index_name}/_search",
                json=search_body,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Search failed for {index_name}: {response.status_code}")
                return {}
        except Exception as e:
            print(f"Error searching {index_name}: {e}")
            return {}
    
    def search_all(self, query: str, size: int = 5) -> Dict[str, Any]:
        """Search both documentation and tickets"""
        results = {
            "docs": self.search_index(query, DOCS_INDEX, size),
            "tickets": self.search_index(query, TICKETS_INDEX, size),
            "query": query
        }
        return results
    
    def format_doc_result(self, hit: Dict[str, Any]) -> str:
        """Format a documentation search result"""
        source = hit.get("_source", {})
        highlight = hit.get("highlight", {})
        score = hit.get("_score", 0)
        
        result = f"\n📄 **Documentation** (Score: {score:.2f})\n"
        result += f"**Title:** {source.get('title', 'N/A')}\n"
        result += f"**URL:** {source.get('url', 'N/A')}\n"
        
        # Show highlights if available
        if highlight:
            if "text" in highlight:
                result += f"**Relevant Content:**\n"
                for fragment in highlight["text"][:2]:
                    result += f"  • {fragment}\n"
        
        return result
    
    def format_ticket_result(self, hit: Dict[str, Any]) -> str:
        """Format a ticket search result"""
        source = hit.get("_source", {})
        highlight = hit.get("highlight", {})
        score = hit.get("_score", 0)
        
        result = f"\n🎫 **Ticket** (Score: {score:.2f})\n"
        result += f"**Ticket ID:** {source.get('ticket_id', 'N/A')}\n"
        result += f"**Title:** {source.get('title', 'N/A')}\n"
        
        if source.get('keywords'):
            keywords = source['keywords']
            if isinstance(keywords, list):
                result += f"**Keywords:** {', '.join(keywords)}\n"
            else:
                result += f"**Keywords:** {keywords}\n"
        
        if source.get('summary'):
            result += f"**Summary:** {source['summary'][:200]}...\n"
        
        # Show highlights if available
        if highlight:
            if "solution" in highlight:
                result += f"**Solution Highlights:**\n"
                for fragment in highlight["solution"][:1]:
                    result += f"  • {fragment}\n"
            elif "text" in highlight:
                result += f"**Relevant Content:**\n"
                for fragment in highlight["text"][:2]:
                    result += f"  • {fragment}\n"
        
        return result
    
    def print_results(self, results: Dict[str, Any], show_docs: bool = True, show_tickets: bool = True):
        """Print formatted search results"""
        query = results.get("query", "")
        print(f"\n🔍 Search Results for: '{query}'\n")
        print("=" * 60)
        
        total_results = 0
        
        # Show documentation results
        if show_docs and "docs" in results:
            docs_data = results["docs"]
            docs_hits = docs_data.get("hits", {}).get("hits", [])
            if docs_hits:
                print(f"\n📚 DOCUMENTATION RESULTS ({len(docs_hits)} found)")
                print("-" * 40)
                for hit in docs_hits:
                    print(self.format_doc_result(hit))
                total_results += len(docs_hits)
        
        # Show ticket results
        if show_tickets and "tickets" in results:
            tickets_data = results["tickets"]
            tickets_hits = tickets_data.get("hits", {}).get("hits", [])
            if tickets_hits:
                print(f"\n🎫 TICKET RESULTS ({len(tickets_hits)} found)")
                print("-" * 40)
                for hit in tickets_hits:
                    print(self.format_ticket_result(hit))
                total_results += len(tickets_hits)
        
        if total_results == 0:
            print("\n❌ No results found. Try different keywords or check your spelling.")
        else:
            print(f"\n✅ Total results shown: {total_results}")
    
    def get_index_info(self) -> Dict[str, Any]:
        """Get information about available indices"""
        info = {}
        
        for index_name in [DOCS_INDEX, TICKETS_INDEX]:
            try:
                response = self.session.get(f"{self.elastic_url}/{index_name}/_stats")
                if response.status_code == 200:
                    stats = response.json()
                    doc_count = stats.get('indices', {}).get(index_name, {}).get('total', {}).get('docs', {}).get('count', 0)
                    info[index_name] = {
                        'exists': True,
                        'doc_count': doc_count
                    }
                else:
                    info[index_name] = {'exists': False, 'doc_count': 0}
            except Exception:
                info[index_name] = {'exists': False, 'doc_count': 0}
        
        return info

def main():
    """Main function with command line interface"""
    parser = argparse.ArgumentParser(description="Search HPC knowledge base (docs + tickets)")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--elastic-url", default=ELASTIC_URL, help="Elasticsearch URL")
    parser.add_argument("--size", type=int, default=5, help="Number of results per index")
    parser.add_argument("--docs-only", action="store_true", help="Search only documentation")
    parser.add_argument("--tickets-only", action="store_true", help="Search only tickets")
    parser.add_argument("--info", action="store_true", help="Show index information")
    
    args = parser.parse_args()
    
    searcher = KnowledgeSearcher(args.elastic_url)
    
    # Check connection
    if not searcher.check_connection():
        print(f"❌ Cannot connect to Elasticsearch at {args.elastic_url}")
        sys.exit(1)
    
    # Show index info if requested
    if args.info:
        info = searcher.get_index_info()
        print("\n📊 Index Information:")
        print("-" * 30)
        for index_name, data in info.items():
            status = "✅ Available" if data['exists'] else "❌ Not found"
            print(f"{index_name}: {status} ({data['doc_count']:,} documents)")
        print()
    
    # Perform search
    if args.docs_only:
        results = {"docs": searcher.search_index(args.query, DOCS_INDEX, args.size), "query": args.query}
        searcher.print_results(results, show_docs=True, show_tickets=False)
    elif args.tickets_only:
        results = {"tickets": searcher.search_index(args.query, TICKETS_INDEX, args.size), "query": args.query}
        searcher.print_results(results, show_docs=False, show_tickets=True)
    else:
        results = searcher.search_all(args.query, args.size)
        searcher.print_results(results)

if __name__ == "__main__":
    main()
