#!/usr/bin/env python3

import requests
import json
import os
from pathlib import Path
from tqdm import tqdm
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# Configuration
base_url = "https://confluence.horsch.com"
bearer_token = "your-confluence-bearer-token-here"
output_dir = "confluence_export"

headers = {
    "Authorization": f"Bearer {bearer_token}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

print("Extracting ALL attachments from Confluence pages...\n")

# Load existing pages from checkpoint
checkpoint_file = os.path.join(output_dir, "checkpoint.json")
with open(checkpoint_file, 'r') as f:
    checkpoint = json.load(f)

all_pages = []
for space_key, page_ids in checkpoint['completed_pages'].items():
    for page_id in page_ids:
        all_pages.append((space_key, page_id))

print(f"Found {len(all_pages)} pages to process\n")

# Statistics
stats = {
    'total_attachments': 0,
    'downloaded_attachments': 0,
    'failed_attachments': 0,
    'pages_with_attachments': 0,
    'total_size_mb': 0,
    'processed_pages': 0
}

def process_page_attachments(space_key, page_id):
    local_stats = {
        'attachments': 0,
        'downloaded': 0,
        'failed': 0,
        'size_mb': 0,
        'has_attachments': False
    }
    
    try:
        # Try the v1 endpoint for attachments
        url = f"{base_url}/rest/api/content/{page_id}/child/attachment"
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            try:
                data = response.json()
                attachments = data.get('results', [])
                
                if attachments:
                    local_stats['has_attachments'] = True
                    
                    # Create directory for attachments
                    att_dir = Path(output_dir) / "spaces" / space_key / "attachments" / page_id
                    att_dir.mkdir(parents=True, exist_ok=True)
                    
                    # Save metadata
                    metadata = []
                    
                    for att in attachments:
                        att_id = att.get('id')
                        title = att.get('title', f'attachment_{att_id}')
                        
                        # Get download link
                        download_link = att.get('_links', {}).get('download')
                        if not download_link:
                            download_link = f"/download/attachments/{page_id}/{title}"
                        
                        # Full URL
                        if not download_link.startswith('http'):
                            download_link = base_url + download_link
                        
                        metadata.append({
                            'id': att_id,
                            'title': title,
                            'mediaType': att.get('metadata', {}).get('mediaType'),
                            'fileSize': att.get('extensions', {}).get('fileSize'),
                            'created': att.get('version', {}).get('when'),
                            'creator': att.get('version', {}).get('by', {}).get('displayName'),
                            'download_link': download_link
                        })
                        
                        local_stats['attachments'] += 1
                        
                        # Try to download the file
                        file_path = att_dir / title
                        if not file_path.exists():  # Skip if already downloaded
                            try:
                                file_response = requests.get(download_link, headers=headers, timeout=30, stream=True)
                                if file_response.status_code == 200:
                                    with open(file_path, 'wb') as f:
                                        for chunk in file_response.iter_content(chunk_size=8192):
                                            f.write(chunk)
                                    
                                    file_size_mb = os.path.getsize(file_path) / (1024*1024)
                                    local_stats['size_mb'] += file_size_mb
                                    local_stats['downloaded'] += 1
                                else:
                                    local_stats['failed'] += 1
                            except Exception as e:
                                local_stats['failed'] += 1
                        else:
                            # File already exists
                            file_size_mb = os.path.getsize(file_path) / (1024*1024)
                            local_stats['size_mb'] += file_size_mb
                            local_stats['downloaded'] += 1
                    
                    # Save metadata
                    with open(att_dir / 'metadata.json', 'w') as f:
                        json.dump(metadata, f, indent=2)
                    
            except json.JSONDecodeError:
                pass
                
    except Exception as e:
        pass
    
    return local_stats

print("Processing all pages for attachments...")
print("="*60)

# Process pages in parallel with progress bar
with ThreadPoolExecutor(max_workers=5) as executor:
    # Submit all tasks
    futures = {executor.submit(process_page_attachments, space_key, page_id): (space_key, page_id) 
               for space_key, page_id in all_pages}
    
    # Process completed tasks with progress bar
    with tqdm(total=len(all_pages), desc="Extracting attachments") as pbar:
        for future in as_completed(futures):
            space_key, page_id = futures[future]
            try:
                result = future.result()
                
                # Update global stats
                stats['processed_pages'] += 1
                if result['has_attachments']:
                    stats['pages_with_attachments'] += 1
                stats['total_attachments'] += result['attachments']
                stats['downloaded_attachments'] += result['downloaded']
                stats['failed_attachments'] += result['failed']
                stats['total_size_mb'] += result['size_mb']
                
                # Update progress bar
                if result['has_attachments']:
                    pbar.set_postfix({
                        'Attachments': stats['total_attachments'],
                        'Downloaded': stats['downloaded_attachments'],
                        'Size': f"{stats['total_size_mb']:.1f}MB"
                    })
                
            except Exception as e:
                pass
            
            pbar.update(1)

# 2. Now extract comments similarly
print("\n\nExtracting comments from all pages...")
print("="*60)

comment_stats = {
    'total_comments': 0,
    'pages_with_comments': 0
}

def process_page_comments(space_key, page_id):
    local_stats = {
        'comments': 0,
        'has_comments': False
    }
    
    try:
        # Try v1 endpoint for comments
        url = f"{base_url}/rest/api/content/{page_id}/child/comment?expand=body.storage,version"
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            try:
                data = response.json()
                comments = data.get('results', [])
                
                if comments:
                    local_stats['has_comments'] = True
                    local_stats['comments'] = len(comments)
                    
                    # Create directory for comments
                    comment_dir = Path(output_dir) / "spaces" / space_key / "comments"
                    comment_dir.mkdir(parents=True, exist_ok=True)
                    
                    # Process comments
                    comment_data = []
                    for comment in comments:
                        comment_data.append({
                            'id': comment.get('id'),
                            'title': comment.get('title'),
                            'body': comment.get('body', {}).get('storage', {}).get('value', ''),
                            'created': comment.get('version', {}).get('when'),
                            'creator': comment.get('version', {}).get('by', {}).get('displayName'),
                            'page_id': page_id
                        })
                    
                    # Save comments
                    comment_file = comment_dir / f"{page_id}_comments.json"
                    with open(comment_file, 'w', encoding='utf-8') as f:
                        json.dump(comment_data, f, indent=2, ensure_ascii=False)
                    
            except json.JSONDecodeError:
                pass
                
    except Exception as e:
        pass
    
    return local_stats

# Process comments in parallel
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = {executor.submit(process_page_comments, space_key, page_id): (space_key, page_id) 
               for space_key, page_id in all_pages}
    
    with tqdm(total=len(all_pages), desc="Extracting comments") as pbar:
        for future in as_completed(futures):
            try:
                result = future.result()
                
                if result['has_comments']:
                    comment_stats['pages_with_comments'] += 1
                comment_stats['total_comments'] += result['comments']
                
                pbar.set_postfix({
                    'Comments': comment_stats['total_comments'],
                    'Pages with comments': comment_stats['pages_with_comments']
                })
                
            except Exception as e:
                pass
            
            pbar.update(1)

# Final summary
print("\n" + "="*60)
print("EXTRACTION COMPLETE")
print("="*60)
print(f"Processed: {len(all_pages)} pages")
print(f"\nAttachments:")
print(f"   Pages with attachments: {stats['pages_with_attachments']}")
print(f"   Total attachments found: {stats['total_attachments']}")
print(f"   Successfully downloaded: {stats['downloaded_attachments']}")
print(f"   Failed downloads: {stats['failed_attachments']}")
print(f"   Total size: {stats['total_size_mb']:.2f} MB")
print(f"\nComments:")
print(f"   Pages with comments: {comment_stats['pages_with_comments']}")
print(f"   Total comments found: {comment_stats['total_comments']}")

if stats['total_attachments'] > 0:
    print(f"\n✓ Attachments saved to: {output_dir}/spaces/*/attachments/")
if comment_stats['total_comments'] > 0:
    print(f"✓ Comments saved to: {output_dir}/spaces/*/comments/")

# Save extraction report
report = {
    'extraction_date': time.strftime('%Y-%m-%d %H:%M:%S'),
    'pages_processed': len(all_pages),
    'attachments': {
        'pages_with_attachments': stats['pages_with_attachments'],
        'total_found': stats['total_attachments'],
        'downloaded': stats['downloaded_attachments'],
        'failed': stats['failed_attachments'],
        'total_size_mb': stats['total_size_mb']
    },
    'comments': {
        'pages_with_comments': comment_stats['pages_with_comments'],
        'total_found': comment_stats['total_comments']
    }
}

with open(Path(output_dir) / 'attachments_comments_report.json', 'w') as f:
    json.dump(report, f, indent=2)

print(f"\nReport saved to: {output_dir}/attachments_comments_report.json")