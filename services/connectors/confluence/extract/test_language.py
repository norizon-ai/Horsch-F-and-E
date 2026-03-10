#!/usr/bin/env python3

import requests
import json

# Configuration
base_url = "https://confluence.horsch.com"
bearer_token = "your-confluence-bearer-token-here"

print("Testing Confluence API with different language settings...\n")

# Test with different language headers
language_tests = [
    {"Accept-Language": "en-US,en;q=0.9", "name": "English"},
    {"Accept-Language": "de-DE,de;q=0.9", "name": "German"},
    {"Accept-Language": "de", "name": "German (simple)"},
]

for lang_header in language_tests:
    print(f"\n{'='*60}")
    print(f"Testing with {lang_header['name']}: {lang_header['Accept-Language']}")
    print('='*60)
    
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Accept-Language": lang_header["Accept-Language"]
    }
    
    # Test spaces endpoint
    print("\n1. Testing /rest/api/space endpoint:")
    try:
        response = requests.get(f"{base_url}/rest/api/space?limit=25", headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            spaces = data.get('results', [])
            print(f"   Found {len(spaces)} spaces")
            print("   Space keys:", [s.get('key') for s in spaces])
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test content search with CQL
    print("\n2. Testing content search:")
    try:
        # Search for all content
        response = requests.get(
            f"{base_url}/rest/api/content/search?cql=type=page&limit=250", 
            headers=headers, 
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            total_size = data.get('totalSize', 0)
            results = data.get('results', [])
            print(f"   Total pages found: {total_size}")
            print(f"   Results in response: {len(results)}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test specific spaces for German content
    print("\n3. Testing individual spaces for content count:")
    for space_key in ['IS', 'PNKB', 'ITKB', 'DPPO', 'DFEDOCU3PUB']:
        try:
            response = requests.get(
                f"{base_url}/rest/api/content?spaceKey={space_key}&type=page&limit=1",
                headers=headers,
                timeout=10
            )
            if response.status_code == 200:
                data = response.json()
                total = data.get('size', 0)
                # Get actual total if available
                if '_links' in data and 'base' in data['_links']:
                    # Try to get more accurate count
                    response2 = requests.get(
                        f"{base_url}/rest/api/content?spaceKey={space_key}&type=page&limit=500",
                        headers=headers,
                        timeout=10
                    )
                    if response2.status_code == 200:
                        data2 = response2.json()
                        actual_count = len(data2.get('results', []))
                        print(f"   {space_key}: {actual_count} pages")
                    else:
                        print(f"   {space_key}: {total}+ pages")
                else:
                    print(f"   {space_key}: {total} pages")
        except Exception as e:
            print(f"   {space_key}: Error - {e}")

print("\n" + "="*60)
print("Testing for hidden or language-specific content...")
print("="*60)

# Test with user locale parameter
headers_de = {
    "Authorization": f"Bearer {bearer_token}",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Accept-Language": "de-DE,de;q=0.9"
}

# Try various CQL queries to find more content
cql_queries = [
    "type=page",
    "type=page and language=de",
    "type=page and language=en",
    "type=blogpost",
    "type=page order by created desc",
    "type=page and space.type=global",
    "type=page and space.type=personal",
]

print("\nTesting different CQL queries:")
for cql in cql_queries:
    try:
        response = requests.get(
            f"{base_url}/rest/api/content/search?cql={cql}&limit=1",
            headers=headers_de,
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            total = data.get('totalSize', 0)
            print(f"   '{cql}': {total} results")
    except Exception as e:
        print(f"   '{cql}': Error - {e}")

# Check for user-specific content
print("\n4. Checking current user info and permissions:")
try:
    response = requests.get(
        f"{base_url}/rest/api/user/current?expand=personalSpace",
        headers=headers_de,
        timeout=10
    )
    if response.status_code == 200:
        user_data = response.json()
        print(f"   Username: {user_data.get('username')}")
        print(f"   Display Name: {user_data.get('displayName')}")
        if 'personalSpace' in user_data:
            print(f"   Personal Space: {user_data['personalSpace']}")
except Exception as e:
    print(f"   Error: {e}")

# Test with different expand parameters
print("\n5. Testing with content expansion for multilingual content:")
try:
    response = requests.get(
        f"{base_url}/rest/api/content?type=page&expand=metadata.labels,version,translations&limit=5",
        headers=headers_de,
        timeout=10
    )
    if response.status_code == 200:
        data = response.json()
        for page in data.get('results', []):
            title = page.get('title')
            page_id = page.get('id')
            
            # Check for translations
            if 'translations' in page.get('_expandable', {}):
                print(f"   Page '{title}' (ID: {page_id}) has translations available")
            
            # Check metadata
            if 'metadata' in page and 'labels' in page['metadata']:
                labels = page['metadata']['labels'].get('results', [])
                if labels:
                    label_names = [l.get('name') for l in labels]
                    if any('de' in l.lower() or 'german' in l.lower() for l in label_names):
                        print(f"   Page '{title}' has German-related labels: {label_names}")
except Exception as e:
    print(f"   Error: {e}")