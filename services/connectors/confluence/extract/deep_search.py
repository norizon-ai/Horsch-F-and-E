#!/usr/bin/env python3

import requests
import json
from collections import defaultdict

# Configuration
base_url = "https://confluence.horsch.com"
bearer_token = "your-confluence-bearer-token-here"

headers = {
    "Authorization": f"Bearer {bearer_token}",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Accept-Language": "de-DE,de;q=0.9"
}

print("Deep search for all available content...\n")

# Collect all unique page IDs
all_page_ids = set()
page_details = {}

print("1. Fetching all pages with pagination:")
start = 0
while True:
    try:
        response = requests.get(
            f"{base_url}/rest/api/content?type=page&start={start}&limit=100&expand=space,version,ancestors",
            headers=headers,
            timeout=15
        )
        if response.status_code == 200:
            data = response.json()
            results = data.get('results', [])
            
            if not results:
                break
                
            for page in results:
                page_id = page.get('id')
                all_page_ids.add(page_id)
                page_details[page_id] = {
                    'title': page.get('title'),
                    'space': page.get('space', {}).get('key'),
                    'created': page.get('version', {}).get('when'),
                    'creator': page.get('version', {}).get('by', {}).get('displayName'),
                    'ancestors': len(page.get('ancestors', []))
                }
            
            print(f"   Fetched {start} to {start + len(results)} (total so far: {len(all_page_ids)})")
            
            # Check if there are more pages
            if len(results) < 100:
                break
            start += 100
        else:
            print(f"   Error: Status {response.status_code}")
            break
    except Exception as e:
        print(f"   Error: {e}")
        break

print(f"\nTotal unique pages found: {len(all_page_ids)}")

# 2. Analyze pages by space
print("\n2. Page distribution by space:")
space_counts = defaultdict(int)
for details in page_details.values():
    space_counts[details['space']] += 1

for space, count in sorted(space_counts.items()):
    print(f"   {space}: {count} pages")

# 3. Search for child pages that might not be in main results
print("\n3. Checking for child pages:")
child_pages_found = set()
sample_pages = list(all_page_ids)[:20]  # Check first 20 pages

for page_id in sample_pages:
    try:
        response = requests.get(
            f"{base_url}/rest/api/content/{page_id}/child/page?limit=100",
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            children = data.get('results', [])
            for child in children:
                child_id = child.get('id')
                if child_id not in all_page_ids:
                    child_pages_found.add(child_id)
                    print(f"   Found additional child page: {child.get('title')} (ID: {child_id})")
    except:
        pass

if child_pages_found:
    print(f"   Found {len(child_pages_found)} additional child pages not in main results!")
else:
    print("   No additional child pages found")

# 4. Check for different content types
print("\n4. Checking all content types:")
content_types = ['page', 'blogpost', 'comment', 'attachment', 'label']
for content_type in content_types:
    try:
        response = requests.get(
            f"{base_url}/rest/api/content?type={content_type}&limit=1",
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            # Get more accurate count
            response2 = requests.get(
                f"{base_url}/rest/api/content?type={content_type}&limit=500",
                headers=headers,
                timeout=10
            )
            if response2.status_code == 200:
                count = len(response2.json().get('results', []))
                if count > 0:
                    print(f"   {content_type}: {count} items")
    except:
        pass

# 5. Search with expanded criteria
print("\n5. Search with special criteria:")
special_searches = [
    "type=page AND space.key IN (IS,PNKB,ITKB,DPPO,DFEDOCU3PUB)",
    "type=page ORDER BY created DESC",
    "type=page AND ancestor != 0",  # Pages with parents
    "type=page AND ancestor = 0",   # Root pages only
]

for search_cql in special_searches:
    try:
        response = requests.get(
            f"{base_url}/rest/api/content/search?cql={search_cql}&limit=500",
            headers=headers,
            timeout=15
        )
        if response.status_code == 200:
            data = response.json()
            total = data.get('totalSize', 0)
            actual = len(data.get('results', []))
            print(f"   '{search_cql}':")
            print(f"      Total reported: {total}, Actual in response: {actual}")
    except Exception as e:
        print(f"   '{search_cql}': Error - {e}")

# 6. Check if there are draft or historical versions
print("\n6. Checking for drafts and versions:")
sample_check = list(all_page_ids)[:5]  # Check first 5 pages
for page_id in sample_check:
    try:
        # Check for drafts
        response = requests.get(
            f"{base_url}/rest/api/content/{page_id}?status=draft",
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            print(f"   Page {page_id} has a draft version")
        
        # Check version history
        response = requests.get(
            f"{base_url}/rest/api/content/{page_id}/version",
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            versions = data.get('results', [])
            if len(versions) > 1:
                details = page_details.get(page_id, {})
                print(f"   Page '{details.get('title', 'Unknown')}' has {len(versions)} versions")
    except:
        pass

# 7. Final verification with direct space content count
print("\n7. Direct count from each space (bypassing search):")
total_direct = 0
for space_key in ['IS', 'PNKB', 'ITKB', 'DPPO', 'DFEDOCU3PUB']:
    all_space_pages = []
    start = 0
    
    while True:
        try:
            response = requests.get(
                f"{base_url}/rest/api/content?spaceKey={space_key}&type=page&start={start}&limit=100",
                headers=headers,
                timeout=10
            )
            if response.status_code == 200:
                data = response.json()
                results = data.get('results', [])
                all_space_pages.extend(results)
                
                if len(results) < 100:
                    break
                start += 100
            else:
                break
        except:
            break
    
    print(f"   {space_key}: {len(all_space_pages)} pages")
    total_direct += len(all_space_pages)

print(f"\nTotal pages from direct space queries: {total_direct}")
print(f"Total pages from general search: {len(all_page_ids)}")

if total_direct != len(all_page_ids):
    print(f"\n⚠️  Discrepancy found! Direct: {total_direct} vs Search: {len(all_page_ids)}")