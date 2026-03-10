#!/usr/bin/env python3

import requests
import json

# Configuration
base_url = "https://confluence.horsch.com"
bearer_token = "your-confluence-bearer-token-here"

headers = {
    "Authorization": f"Bearer {bearer_token}",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Accept-Language": "de-DE,de;q=0.9,en;q=0.8"
}

print("Comprehensive search for all Confluence spaces and content...\n")

# 1. Get ALL spaces with pagination
print("1. Fetching ALL spaces (including archived):")
all_spaces = []
start = 0
limit = 100

while True:
    try:
        # Include all types and statuses
        response = requests.get(
            f"{base_url}/rest/api/space?start={start}&limit={limit}&type=global&status=current",
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            results = data.get('results', [])
            all_spaces.extend(results)
            
            if len(results) < limit:
                break
            start += limit
        else:
            break
    except Exception as e:
        print(f"Error fetching spaces: {e}")
        break

print(f"   Found {len(all_spaces)} current global spaces")

# Try archived spaces
try:
    response = requests.get(
        f"{base_url}/rest/api/space?status=archived&limit=100",
        headers=headers,
        timeout=10
    )
    if response.status_code == 200:
        data = response.json()
        archived = data.get('results', [])
        if archived:
            print(f"   Found {len(archived)} archived spaces:")
            for space in archived:
                print(f"      - {space.get('key')}: {space.get('name')}")
except:
    pass

# Try personal spaces
try:
    response = requests.get(
        f"{base_url}/rest/api/space?type=personal&limit=100",
        headers=headers,
        timeout=10
    )
    if response.status_code == 200:
        data = response.json()
        personal = data.get('results', [])
        if personal:
            print(f"   Found {len(personal)} personal spaces:")
            for space in personal[:5]:  # Show first 5
                print(f"      - {space.get('key')}: {space.get('name')}")
except:
    pass

print("\n2. Detailed space analysis:")
for space in all_spaces:
    space_key = space.get('key')
    space_name = space.get('name')
    
    # Get detailed space info with expansion
    try:
        response = requests.get(
            f"{base_url}/rest/api/space/{space_key}?expand=description,permissions,settings,metadata.labels",
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            space_data = response.json()
            
            # Count all content types
            content_counts = {}
            for content_type in ['page', 'blogpost', 'comment', 'attachment']:
                try:
                    resp = requests.get(
                        f"{base_url}/rest/api/content?spaceKey={space_key}&type={content_type}&limit=1",
                        headers=headers,
                        timeout=5
                    )
                    if resp.status_code == 200:
                        count_data = resp.json()
                        # Try to get more accurate count
                        resp2 = requests.get(
                            f"{base_url}/rest/api/content?spaceKey={space_key}&type={content_type}&limit=500",
                            headers=headers,
                            timeout=5
                        )
                        if resp2.status_code == 200:
                            actual_count = len(resp2.json().get('results', []))
                            if actual_count > 0:
                                content_counts[content_type] = actual_count
                except:
                    pass
            
            print(f"\n   {space_key} - {space_name}")
            print(f"      Type: {space.get('type', 'unknown')}")
            print(f"      Status: {space.get('status', 'unknown')}")
            
            if content_counts:
                print(f"      Content: {content_counts}")
            
            # Check for language-specific settings
            if 'settings' in space_data.get('_expandable', {}):
                print(f"      Has settings (may include language)")
            
            # Check metadata
            if 'metadata' in space_data:
                if 'labels' in space_data['metadata']:
                    labels = space_data['metadata'].get('labels', {}).get('results', [])
                    if labels:
                        print(f"      Labels: {[l.get('name') for l in labels[:5]]}")
                        
    except Exception as e:
        print(f"   Error getting details for {space_key}: {e}")

print("\n3. Search for content with different parameters:")

# Test various search strategies
search_params = [
    {"cql": "type=page", "desc": "All pages"},
    {"cql": "type=page and text ~ german", "desc": "Pages containing 'german'"},
    {"cql": "type=page and text ~ deutsch", "desc": "Pages containing 'deutsch'"},
    {"cql": "type=page and text ~ de", "desc": "Pages containing 'de'"},
    {"cql": "type=page and creator != currentUser()", "desc": "Pages by other users"},
    {"cql": "type=page and lastModified > -365d", "desc": "Pages modified in last year"},
    {"cql": "type=page and label = de", "desc": "Pages with 'de' label"},
    {"cql": "type=page and label = german", "desc": "Pages with 'german' label"},
    {"cql": "type=page and title ~ DE", "desc": "Pages with 'DE' in title"},
]

for search in search_params:
    try:
        response = requests.get(
            f"{base_url}/rest/api/content/search?cql={search['cql']}&limit=1",
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            total = data.get('totalSize', 0)
            if total > 0:
                print(f"   {search['desc']}: {total} results")
                
                # Show first result as example
                if data.get('results'):
                    first = data['results'][0]
                    print(f"      Example: '{first.get('title')}' in space {first.get('space', {}).get('key')}")
    except Exception as e:
        print(f"   {search['desc']}: Error - {e}")

print("\n4. Check for restricted content:")
try:
    # Try to access content with different permission levels
    response = requests.get(
        f"{base_url}/rest/api/content?expand=restrictions&limit=10",
        headers=headers,
        timeout=10
    )
    if response.status_code == 200:
        data = response.json()
        for content in data.get('results', []):
            if 'restrictions' in content:
                restrictions = content.get('restrictions', {})
                if restrictions:
                    print(f"   Page '{content.get('title')}' has restrictions: {restrictions}")
except Exception as e:
    print(f"   Error checking restrictions: {e}")

print("\n5. Testing space permissions endpoint:")
for space_key in all_spaces[:3]:  # Test first 3 spaces
    try:
        response = requests.get(
            f"{base_url}/rest/api/space/{space_key.get('key')}/permission",
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            print(f"   {space_key.get('key')}: Has accessible permissions")
    except:
        pass