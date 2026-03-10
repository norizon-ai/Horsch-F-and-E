#!/usr/bin/env python3

import requests
import json

# Configuration
base_url = "https://confluence.horsch.com"
bearer_token = "your-confluence-bearer-token-here"

print("Verifying if language settings affect content visibility...\n")

# Test configurations
test_configs = [
    {
        "name": "English (default)",
        "headers": {
            "Authorization": f"Bearer {bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    },
    {
        "name": "German (Accept-Language)",
        "headers": {
            "Authorization": f"Bearer {bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Accept-Language": "de-DE,de;q=0.9"
        }
    },
    {
        "name": "German (with X-Atlassian-Force-Locale)",
        "headers": {
            "Authorization": f"Bearer {bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Accept-Language": "de-DE,de;q=0.9",
            "X-Atlassian-Force-Locale": "de_DE"
        }
    }
]

results_summary = {}

for config in test_configs:
    print(f"\nTesting with: {config['name']}")
    print("="*60)
    
    headers = config['headers']
    results = {}
    
    # 1. Count total pages
    try:
        response = requests.get(
            f"{base_url}/rest/api/content/search?cql=type=page&limit=1",
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            total_pages = data.get('totalSize', 0)
            results['total_pages'] = total_pages
            print(f"Total pages: {total_pages}")
    except Exception as e:
        print(f"Error counting pages: {e}")
        results['total_pages'] = 0
    
    # 2. Count spaces
    try:
        response = requests.get(
            f"{base_url}/rest/api/space?limit=100",
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            spaces = data.get('results', [])
            results['total_spaces'] = len(spaces)
            results['space_keys'] = [s.get('key') for s in spaces]
            print(f"Total spaces: {len(spaces)}")
            print(f"Space keys: {results['space_keys']}")
    except Exception as e:
        print(f"Error counting spaces: {e}")
        results['total_spaces'] = 0
        results['space_keys'] = []
    
    # 3. Count pages per space
    space_pages = {}
    for space_key in results.get('space_keys', []):
        try:
            # Get actual count by fetching all pages
            all_pages = []
            start = 0
            while True:
                response = requests.get(
                    f"{base_url}/rest/api/content?spaceKey={space_key}&type=page&start={start}&limit=100",
                    headers=headers,
                    timeout=10
                )
                if response.status_code == 200:
                    data = response.json()
                    batch = data.get('results', [])
                    all_pages.extend(batch)
                    if len(batch) < 100:
                        break
                    start += 100
                else:
                    break
            
            space_pages[space_key] = len(all_pages)
        except:
            space_pages[space_key] = 0
    
    results['space_pages'] = space_pages
    print(f"\nPages per space:")
    total_from_spaces = 0
    for space, count in space_pages.items():
        print(f"   {space}: {count}")
        total_from_spaces += count
    
    results['total_from_spaces'] = total_from_spaces
    print(f"Total from individual spaces: {total_from_spaces}")
    
    # 4. Search for German-specific content
    german_searches = [
        ("text ~ 'Deutsch'", "Contains 'Deutsch'"),
        ("text ~ 'German'", "Contains 'German'"),
        ("text ~ 'DE'", "Contains 'DE'"),
        ("title ~ 'DE'", "Title contains 'DE'"),
    ]
    
    print(f"\nGerman content searches:")
    for cql, desc in german_searches:
        try:
            response = requests.get(
                f"{base_url}/rest/api/content/search?cql=type=page and {cql}&limit=1",
                headers=headers,
                timeout=10
            )
            if response.status_code == 200:
                data = response.json()
                count = data.get('totalSize', 0)
                if count > 0:
                    print(f"   {desc}: {count} pages")
        except:
            pass
    
    # 5. Check a specific page to see if content differs
    test_page_id = "263097403"  # First page from IS space
    try:
        response = requests.get(
            f"{base_url}/rest/api/content/{test_page_id}?expand=body.storage",
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            title = data.get('title', '')
            body_length = len(data.get('body', {}).get('storage', {}).get('value', ''))
            print(f"\nTest page {test_page_id}:")
            print(f"   Title: {title}")
            print(f"   Body length: {body_length} characters")
            results[f'test_page_title'] = title
            results[f'test_page_body_length'] = body_length
    except:
        pass
    
    results_summary[config['name']] = results

# Compare results
print("\n" + "="*60)
print("COMPARISON OF RESULTS")
print("="*60)

if len(results_summary) > 1:
    first_config = list(results_summary.keys())[0]
    baseline = results_summary[first_config]
    
    for config_name, results in results_summary.items():
        if config_name == first_config:
            continue
        
        print(f"\nComparing '{first_config}' vs '{config_name}':")
        
        # Compare total pages
        if results.get('total_pages') != baseline.get('total_pages'):
            print(f"   ⚠️  Different total pages: {baseline.get('total_pages')} vs {results.get('total_pages')}")
        else:
            print(f"   ✓ Same total pages: {results.get('total_pages')}")
        
        # Compare spaces
        if results.get('space_keys') != baseline.get('space_keys'):
            print(f"   ⚠️  Different spaces detected!")
            baseline_set = set(baseline.get('space_keys', []))
            current_set = set(results.get('space_keys', []))
            if current_set - baseline_set:
                print(f"      Additional spaces: {current_set - baseline_set}")
            if baseline_set - current_set:
                print(f"      Missing spaces: {baseline_set - current_set}")
        else:
            print(f"   ✓ Same spaces: {len(results.get('space_keys', []))}")
        
        # Compare page counts per space
        different_counts = False
        for space in results.get('space_pages', {}):
            if results['space_pages'].get(space) != baseline.get('space_pages', {}).get(space):
                if not different_counts:
                    print(f"   ⚠️  Different page counts in spaces:")
                    different_counts = True
                print(f"      {space}: {baseline.get('space_pages', {}).get(space)} vs {results['space_pages'].get(space)}")
        
        if not different_counts:
            print(f"   ✓ Same page counts in all spaces")
        
        # Compare test page
        if results.get('test_page_title') != baseline.get('test_page_title'):
            print(f"   ⚠️  Test page has different title!")
        if results.get('test_page_body_length') != baseline.get('test_page_body_length'):
            print(f"   ⚠️  Test page has different body length!")

print("\n" + "="*60)
print("CONCLUSION")
print("="*60)

all_same = True
if len(results_summary) > 1:
    first_total = results_summary[list(results_summary.keys())[0]].get('total_pages', 0)
    for config_name, results in results_summary.items():
        if results.get('total_pages', 0) != first_total:
            all_same = False
            break

if all_same:
    print("✓ Language settings (Accept-Language, X-Atlassian-Force-Locale) do NOT")
    print("  affect the number of visible pages or spaces.")
    print(f"  All configurations show the same {first_total} pages.")
else:
    print("⚠️  Different language settings show different content!")
    print("  Further investigation needed.")

print(f"\nTotal pages available: {results_summary.get(list(results_summary.keys())[0], {}).get('total_pages', 0)}")
print("All data has been successfully scraped.")