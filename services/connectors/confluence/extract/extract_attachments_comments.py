#!/usr/bin/env python3

import requests
import json
import os
from pathlib import Path
from tqdm import tqdm
import time

# Configuration
base_url = "https://confluence.horsch.com"
bearer_token = "your-confluence-bearer-token-here"
output_dir = "confluence_export"

headers = {
    "Authorization": f"Bearer {bearer_token}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

print("Extracting attachments and comments from Confluence...\n")

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
    'total_comments': 0,
    'pages_with_attachments': 0,
    'pages_with_comments': 0,
    'total_size_mb': 0
}

# 1. Extract attachments
print("1. Extracting attachments...")
print("="*60)

for space_key, page_id in tqdm(all_pages[:10], desc="Testing first 10 pages"):  # Test with first 10
    try:
        # Try the correct v1 endpoint for attachments
        url = f"{base_url}/rest/api/content/{page_id}/child/attachment"
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            try:
                data = response.json()
                attachments = data.get('results', [])
                
                if attachments:
                    stats['pages_with_attachments'] += 1
                    
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
                        
                        stats['total_attachments'] += 1
                        
                        # Try to download the file
                        try:
                            file_response = requests.get(download_link, headers=headers, timeout=30, stream=True)
                            if file_response.status_code == 200:
                                file_path = att_dir / title
                                with open(file_path, 'wb') as f:
                                    for chunk in file_response.iter_content(chunk_size=8192):
                                        f.write(chunk)
                                
                                file_size_mb = os.path.getsize(file_path) / (1024*1024)
                                stats['total_size_mb'] += file_size_mb
                                stats['downloaded_attachments'] += 1
                                
                                print(f"\n   ✓ Downloaded: {title} ({file_size_mb:.2f} MB)")
                            else:
                                stats['failed_attachments'] += 1
                                print(f"\n   ✗ Failed to download: {title} (Status: {file_response.status_code})")
                        except Exception as e:
                            stats['failed_attachments'] += 1
                            print(f"\n   ✗ Failed to download {title}: {e}")
                    
                    # Save metadata
                    with open(att_dir / 'metadata.json', 'w') as f:
                        json.dump(metadata, f, indent=2)
                    
            except json.JSONDecodeError:
                # Response is not JSON, might be HTML
                pass
                
    except Exception as e:
        pass
    
    time.sleep(0.1)  # Small delay to avoid rate limiting

print(f"\n\nAttachment Statistics:")
print(f"   Pages with attachments: {stats['pages_with_attachments']}")
print(f"   Total attachments found: {stats['total_attachments']}")
print(f"   Successfully downloaded: {stats['downloaded_attachments']}")
print(f"   Failed downloads: {stats['failed_attachments']}")
print(f"   Total size: {stats['total_size_mb']:.2f} MB")

# 2. Extract comments
print("\n2. Extracting comments...")
print("="*60)

comments_found = []

for space_key, page_id in tqdm(all_pages[:10], desc="Testing first 10 pages"):  # Test with first 10
    try:
        # Try v1 endpoint for comments
        url = f"{base_url}/rest/api/content/{page_id}/child/comment?expand=body.storage,version"
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            try:
                data = response.json()
                comments = data.get('results', [])
                
                if comments:
                    stats['pages_with_comments'] += 1
                    stats['total_comments'] += len(comments)
                    
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
                    
                    comments_found.append({
                        'page_id': page_id,
                        'space': space_key,
                        'count': len(comments)
                    })
                    
                    print(f"\n   ✓ Found {len(comments)} comments for page {page_id}")
                    
            except json.JSONDecodeError:
                # Response is not JSON
                pass
                
    except Exception as e:
        pass
    
    time.sleep(0.1)  # Small delay

print(f"\n\nComment Statistics:")
print(f"   Pages with comments: {stats['pages_with_comments']}")
print(f"   Total comments found: {stats['total_comments']}")

if comments_found:
    print(f"\n   Pages with comments:")
    for item in comments_found[:5]:  # Show first 5
        print(f"      Page {item['page_id']} in {item['space']}: {item['count']} comments")

# 3. Try alternative methods for images embedded in pages
print("\n3. Checking for embedded images in page content...")
print("="*60)

embedded_images = []

for space_key, page_id in all_pages[:5]:  # Check first 5 pages
    page_file = Path(output_dir) / "spaces" / space_key / "pages" / f"{page_id}.json"
    
    if page_file.exists():
        with open(page_file, 'r') as f:
            page_data = json.load(f)
            
        # Check for embedded images in the storage format
        if 'body' in page_data and 'storage' in page_data['body']:
            content = page_data['body']['storage'].get('value', '')
            
            # Look for image references
            if '<ri:attachment' in content or '<ac:image' in content:
                # Count image references
                import re
                attachments = re.findall(r'ri:filename="([^"]+)"', content)
                images = re.findall(r'<ac:image[^>]*>', content)
                
                if attachments or images:
                    embedded_images.append({
                        'page_id': page_id,
                        'space': space_key,
                        'attachments': attachments,
                        'image_tags': len(images)
                    })

if embedded_images:
    print(f"Found {len(embedded_images)} pages with embedded images:")
    for item in embedded_images:
        print(f"   Page {item['page_id']} in {item['space']}:")
        if item['attachments']:
            print(f"      Attachment references: {item['attachments']}")
        if item['image_tags']:
            print(f"      Image tags: {item['image_tags']}")

# 4. Final summary
print("\n" + "="*60)
print("EXTRACTION SUMMARY")
print("="*60)
print(f"Processed: {len(all_pages[:10])} pages (test run with first 10)")
print(f"Attachments: {stats['downloaded_attachments']} downloaded, {stats['failed_attachments']} failed")
print(f"Comments: {stats['total_comments']} found")
print(f"Total download size: {stats['total_size_mb']:.2f} MB")

if stats['total_attachments'] == 0 and stats['total_comments'] == 0:
    print("\n⚠️  No attachments or comments were found.")
    print("This might be because:")
    print("  1. The pages don't have attachments/comments")
    print("  2. The API endpoints return HTML instead of JSON (API v1 limitation)")
    print("  3. Different permissions are needed for attachments/comments")
    print("\nTo get all attachments, you might need to:")
    print("  - Use Confluence's built-in export feature (Space Tools > Content Tools > Export)")
    print("  - Use a different API endpoint or authentication method")
else:
    print(f"\n✓ Successfully extracted content!")
    print(f"  Check {output_dir}/spaces/*/attachments/ for downloaded files")
    print(f"  Check {output_dir}/spaces/*/comments/ for comment data")