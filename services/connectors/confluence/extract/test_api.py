#!/usr/bin/env python3

import requests
import json

# Configuration
base_url = "https://confluence.horsch.com"
bearer_token = "your-confluence-bearer-token-here"

# Set up headers
headers = {
    "Authorization": f"Bearer {bearer_token}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

print("Testing Confluence API endpoints...\n")

# Test different endpoints
endpoints = [
    "/rest/api/space",
    "/rest/api/space?limit=1",
    "/rest/api/content",
    "/rest/api/content?limit=1",
    "/rest/api/content/search?cql=type=page&limit=1",
    "/rest/api/user/current",
]

for endpoint in endpoints:
    url = f"{base_url}{endpoint}"
    print(f"Testing: {url}")
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        print(f"  Status: {response.status_code}")
        
        if response.status_code == 200:
            try:
                data = response.json()
                if "results" in data:
                    print(f"  Results found: {len(data['results'])}")
                else:
                    print(f"  Response keys: {list(data.keys())[:5]}")
            except json.JSONDecodeError:
                print(f"  Response (first 200 chars): {response.text[:200]}")
        else:
            print(f"  Error response: {response.text[:200]}")
    except Exception as e:
        print(f"  Error: {e}")
    
    print()

print("\nTrying without expand parameters...")
url = f"{base_url}/rest/api/space?limit=5"
try:
    response = requests.get(url, headers=headers, timeout=10)
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"Success! Found {len(data.get('results', []))} spaces")
        
        if data.get('results'):
            print("\nFirst space:")
            space = data['results'][0]
            print(f"  Key: {space.get('key')}")
            print(f"  Name: {space.get('name')}")
            print(f"  Type: {space.get('type')}")
except Exception as e:
    print(f"Error: {e}")