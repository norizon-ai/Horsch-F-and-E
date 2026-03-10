import requests
import time
import random
import logging
from typing import Dict, Any, Optional, List
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from requests.exceptions import RequestException, HTTPError


class RateLimitExceeded(Exception):
    pass


class ConfluenceAPIClient:
    def __init__(self, config):
        self.config = config
        self.base_url = config.base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.logger = logging.getLogger(__name__)
        self.request_count = 0
        self.last_request_time = 0
        
    def _add_jitter(self):
        jitter = random.uniform(0.1, 0.5)
        time.sleep(jitter)
    
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=2, min=4, max=60),
        retry=retry_if_exception_type((RequestException, RateLimitExceeded))
    )
    def _make_request(self, method: str, endpoint: str, params: Dict = None, 
                     json_data: Dict = None, stream: bool = False) -> requests.Response:
        
        self._add_jitter()
        
        url = f"{self.base_url}{endpoint}"
        
        self.logger.debug(f"Making {method} request to {url}")
        self.request_count += 1
        
        try:
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                json=json_data,
                timeout=self.config.request_timeout,
                stream=stream
            )
            
            if response.status_code == 429:
                retry_after = int(response.headers.get("Retry-After", 60))
                self.logger.warning(f"Rate limit hit. Waiting {retry_after} seconds...")
                time.sleep(retry_after)
                raise RateLimitExceeded(f"Rate limit exceeded. Retry after {retry_after} seconds")
            
            response.raise_for_status()
            return response
            
        except HTTPError as e:
            if e.response.status_code == 403:
                self.logger.warning(f"Access forbidden for {url}")
                return None
            elif e.response.status_code == 404:
                self.logger.warning(f"Resource not found: {url}")
                return None
            else:
                self.logger.error(f"HTTP error occurred: {e}")
                raise
        except RequestException as e:
            self.logger.error(f"Request error occurred: {e}")
            raise
    
    def get(self, endpoint: str, params: Dict = None) -> Optional[Dict]:
        response = self._make_request("GET", endpoint, params=params)
        if response and response.content:
            try:
                return response.json()
            except Exception as e:
                self.logger.debug(f"Response content: {response.text[:500]}")
                self.logger.error(f"Failed to parse JSON response: {e}")
                raise
        return None
    
    def post(self, endpoint: str, json_data: Dict = None, params: Dict = None) -> Optional[Dict]:
        response = self._make_request("POST", endpoint, params=params, json_data=json_data)
        if response and response.content:
            return response.json()
        return None
    
    def download_file(self, url: str, output_path: str) -> bool:
        try:
            response = self._make_request("GET", url, stream=True)
            if response:
                with open(output_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                return True
        except Exception as e:
            self.logger.error(f"Failed to download file from {url}: {e}")
        return False
    
    def get_paginated(self, endpoint: str, params: Dict = None, 
                     expand: List[str] = None) -> List[Dict]:
        
        if params is None:
            params = {}
        
        # Check if endpoint already has parameters
        if "?" in endpoint:
            # Parameters already in endpoint, need to be careful
            base_endpoint = endpoint
            params_copy = params.copy()
        else:
            base_endpoint = endpoint
            params_copy = params.copy()
        
        params_copy["limit"] = self.config.page_size
        
        if expand:
            params_copy["expand"] = ",".join(expand)
        
        all_results = []
        start = 0
        
        while True:
            params_copy["start"] = start
            
            response_data = self.get(base_endpoint, params_copy)
            
            if not response_data:
                break
            
            if "results" in response_data:
                results = response_data["results"]
                all_results.extend(results)
                self.logger.info(f"Retrieved {len(results)} items from {endpoint}")
                
                # Check if there are more results
                size = response_data.get("size", 0)
                limit = response_data.get("limit", self.config.page_size)
                
                if size < limit:
                    # No more results
                    break
                
                start += size
            else:
                # Single result, not paginated
                all_results.append(response_data)
                break
        
        return all_results
    
    def test_connection(self) -> bool:
        try:
            # Try v2 API first
            response = self.get("/api/v2/spaces?limit=1")
            if response:
                self.logger.info("Successfully connected to Confluence API v2")
                return True
        except Exception as e:
            self.logger.warning(f"API v2 failed, trying v1: {e}")
            
        try:
            # Fallback to v1 API
            response = self.get("/rest/api/space?limit=1")
            if response:
                self.logger.info("Successfully connected to Confluence API v1")
                self.logger.warning("Note: Using API v1. Some features may be limited.")
                return True
        except Exception as e:
            self.logger.error(f"Failed to connect to Confluence API: {e}")
        
        return False