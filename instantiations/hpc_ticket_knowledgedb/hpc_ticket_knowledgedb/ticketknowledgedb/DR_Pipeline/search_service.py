#!/usr/bin/env python3
"""
Search service for HPC knowledge base using Elasticsearch
"""

import asyncio
import requests
import time
from typing import List, Optional, Tuple

# Try absolute imports first (for direct execution), then relative imports (for package use)
try:
    from dr_models import SearchResult, HPCSearchRequest, HPCSearchResponse
    from dr_config import config
except ImportError:
    from .dr_models import SearchResult, HPCSearchRequest, HPCSearchResponse
    from .dr_config import config


class SearchService:
    """Service for searching HPC knowledge base"""
    
    def __init__(self):
        self.elastic_url = config.elastic_url
        self.docs_index = config.docs_index
        self.tickets_index = config.tickets_index
        self.timeout = config.search_timeout
        # Retry tuning (use config if present, else defaults)
        self.max_retries = getattr(config, "search_max_retries", 3)
        self.backoff_base = getattr(config, "search_backoff_base", 0.75)  # seconds
        self.backoff_factor = getattr(config, "search_backoff_factor", 2.0)
    
    async def search(self, request: HPCSearchRequest) -> HPCSearchResponse:
        """Perform search based on request type"""
        start_time = time.time()
        
        try:
            if request.search_type == "docs":
                results, total = await self._search_index(request.query, self.docs_index, request.max_results)
            elif request.search_type == "tickets":
                results, total = await self._search_index(request.query, self.tickets_index, request.max_results)
            elif request.search_type == "both":
                docs_results, docs_total = await self._search_index(request.query, self.docs_index, request.max_results // 2)
                tickets_results, tickets_total = await self._search_index(request.query, self.tickets_index, request.max_results // 2)
                results = docs_results + tickets_results
                total = docs_total + tickets_total
                # Sort combined results by score
                results.sort(key=lambda x: x.score, reverse=True)
                results = results[:request.max_results]
            else:
                raise ValueError(f"Invalid search type: {request.search_type}")
            
            search_time = time.time() - start_time
            
            return HPCSearchResponse(
                query=request.query,
                results=results,
                total_found=total,
                search_time=search_time,
                error=None
            )
            
        except Exception as e:
            search_time = time.time() - start_time
            return HPCSearchResponse(
                query=request.query,
                results=[],
                total_found=0,
                search_time=search_time,
                error=str(e)
            )
    
    async def _search_index(self, query: str, index_name: str, max_results: int) -> Tuple[List[SearchResult], int]:
        """Search a specific Elasticsearch index"""
        try:
            # Configure search fields based on index
            if index_name == self.docs_index:
                fields = ["title^3", "text"]  # Simplified field list
                source_fields = ["id", "title", "text", "url"]
            else:  # tickets index
                fields = ["problem_description^5", "solution^4", "root_cause^3", "title^3", "keywords^2", "summary^2", "text"]
                source_fields = ["id", "ticket_id", "title", "text", "keywords", "summary", "problem_description", "root_cause", "solution"]
            
            # Single optimized query - fast and reliable
            search_data = {
                "query": {
                    "multi_match": {
                        "query": query,
                        "fields": fields,
                        "type": "best_fields",
                        "fuzziness": "0",  # No fuzziness for consistent performance
                        "operator": "or"   # More lenient matching
                    }
                },
                "size": max(1, min(max_results, 20)),  # Cap results for performance
                "_source": source_fields,
                "highlight": {
                    "fields": {
                        "title": {"number_of_fragments": 0},  # Highlight entire title
                        "text": {"fragment_size": 120, "number_of_fragments": 1}  # Single small fragment
                    },
                    "max_analyzed_offset": 5000  # Limit analysis for performance
                },
                "sort": [{"_score": {"order": "desc"}}],
                "timeout": f"{max(10, int(self.timeout-5))}s"  # Conservative timeout
            }

            search_url = f"{self.elastic_url}/{index_name}/_search"
            headers = {"Content-Type": "application/json"}
            
            raw_response = self._request_with_retries(
                method="POST",
                url=search_url,
                json=search_data,
                headers=headers,
                timeout=self.timeout,
                what=f"search index '{index_name}'"
            )
            
            if raw_response.status_code == 200:
                raw_results = raw_response.json()
                hits = raw_results.get("hits", {}).get("hits", [])
                total = raw_results.get("hits", {}).get("total", {}).get("value", 0)
                
                results = []
                for hit in hits:
                    source = hit.get("_source", {})
                    highlight = hit.get("highlight", {})
                    
                    # Combine highlights efficiently
                    highlight_parts = []
                    if "title" in highlight:
                        highlight_parts.extend(highlight["title"])
                    if "text" in highlight:
                        highlight_parts.extend(highlight["text"])
                    highlight_text = " ... ".join(highlight_parts) if highlight_parts else None
                    
                    # For tickets, create richer content from multiple fields
                    if index_name == self.tickets_index:
                        content_parts = []
                        if source.get("problem_description"):
                            content_parts.append(f"Problem: {source['problem_description'][:400]}")
                        if source.get("root_cause"):
                            content_parts.append(f"Root Cause: {source['root_cause'][:300]}")
                        if source.get("solution"):
                            content_parts.append(f"Solution: {source['solution'][:400]}")
                        if source.get("text") and not content_parts:  # Fallback to text if no structured fields
                            content_parts.append(source["text"][:1200])
                        content = "\n\n".join(content_parts) if content_parts else source.get("text", "")[:1200]
                    else:
                        content = source.get("text", "")[:1200]
                    
                    result = SearchResult(
                        id=source.get("id", ""),
                        title=source.get("title", ""),
                        content=content,
                        score=hit.get("_score", 0.0),
                        source_type=index_name,
                        url=source.get("url") if index_name == self.docs_index else None,
                        ticket_id=source.get("ticket_id") if index_name == self.tickets_index else None,
                        keywords=source.get("keywords") if index_name == self.tickets_index else None,
                        highlight=highlight_text
                    )
                    
                    results.append(result)
                
                return results, total
            else:
                raise Exception(f"Elasticsearch error: {raw_response.status_code} - {raw_response.text}")
                
        except Exception as e:
            raise Exception(f"Search error: {str(e)}")
    
    def _request_with_retries(self, method: str, url: str, json: dict, headers: dict, timeout: float, what: str):
        """Make an HTTP request with retries and exponential backoff."""
        last_err = None
        for attempt in range(1, self.max_retries + 1):
            try:
                resp = requests.request(method=method, url=url, json=json, headers=headers, timeout=timeout)
                return resp
            except requests.exceptions.ReadTimeout as e:
                last_err = e
                if attempt < self.max_retries:
                    delay = self.backoff_base * (self.backoff_factor ** (attempt - 1))
                    print(f"    [!] Elasticsearch {what} timed out (attempt {attempt}/{self.max_retries}, timeout={timeout}s). Retrying in {delay:.1f}s...")
                    time.sleep(delay)
                    continue
                else:
                    raise Exception(f"Read timeout after {self.max_retries} attempts for {what} at {url}")
            except requests.exceptions.ConnectionError as e:
                last_err = e
                if attempt < self.max_retries:
                    delay = self.backoff_base * (self.backoff_factor ** (attempt - 1))
                    print(f"    [!] Elasticsearch connection error for {what} (attempt {attempt}/{self.max_retries}). Retrying in {delay:.1f}s...")
                    time.sleep(delay)
                    continue
                else:
                    raise Exception(f"Connection error after {self.max_retries} attempts for {what} at {url}: {e}")
            except Exception as e:
                last_err = e
                break
        # If we break out due to unexpected exception, raise a descriptive error
        raise Exception(f"Unexpected error during {what} at {url}: {last_err}")
    
    def test_connection(self) -> bool:
        """Test connection to Elasticsearch"""
        try:
            resp = requests.get(f"{self.elastic_url}/_cluster/health", timeout=min(5, self.timeout))
            if resp.status_code == 200:
                return True
            print(f"    [!] Elasticsearch health check returned {resp.status_code}: {resp.text[:120]}")
            return False
        except requests.exceptions.ReadTimeout:
            print("    [!] Elasticsearch health check timed out")
            return False
        except Exception as e:
            print(f"    [ERROR] Elasticsearch health check failed: {e}")
            return False


# Global search service instance
search_service = SearchService()
