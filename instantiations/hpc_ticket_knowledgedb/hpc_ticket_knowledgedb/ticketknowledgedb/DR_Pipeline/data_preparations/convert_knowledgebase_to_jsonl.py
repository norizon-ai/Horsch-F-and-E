#!/usr/bin/env python3
"""
Script to convert knowledgebase markdown files to JSONL format for Elasticsearch insertion
"""

import json
import os
import re
import hashlib
from pathlib import Path
from typing import Dict, List, Any

def extract_ticket_id(filename: str) -> str:
    """Extract ticket ID from filename"""
    # Remove .md extension and extract the ticket ID (first part before underscore)
    base_name = filename.replace('.md', '')
    if '_' in base_name:
        return base_name.split('_')[0]
    return base_name

def parse_markdown_content(content: str) -> Dict[str, Any]:
    """Parse markdown content and extract structured information"""
    lines = content.split('\n')
    
    # Initialize data structure
    data = {
        'keywords': [],
        'summary': '',
        'problem_description': '',
        'root_cause': '',
        'solution': '',
        'actions_taken': '',
        'general_learnings': '',
        'full_text': content
    }
    
    current_section = None
    current_content = []
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines and markdown code blocks
        if not line or line.startswith('```'):
            continue
            
        # Check for section headers
        if line.startswith('## '):
            # Save previous section
            if current_section and current_content:
                section_text = '\n'.join(current_content).strip()
                if current_section == 'keywords':
                    # Extract keywords from bullet points
                    keywords = []
                    for content_line in current_content:
                        if content_line.strip().startswith('- '):
                            keywords.append(content_line.strip()[2:])
                    data['keywords'] = keywords
                else:
                    data[current_section] = section_text
            
            # Start new section
            section_name = line[3:].lower().replace(' ', '_').replace('/', '_')
            if 'keyword' in section_name:
                current_section = 'keywords'
            elif 'summary' in section_name:
                current_section = 'summary'
            elif 'problem' in section_name or 'description' in section_name:
                current_section = 'problem_description'
            elif 'root_cause' in section_name or 'cause' in section_name:
                current_section = 'root_cause'
            elif 'solution' in section_name:
                current_section = 'solution'
            elif 'actions' in section_name or 'taken' in section_name:
                current_section = 'actions_taken'
            elif 'learning' in section_name or 'general' in section_name:
                current_section = 'general_learnings'
            else:
                current_section = None
            
            current_content = []
        else:
            # Add content to current section
            if current_section:
                current_content.append(line)
    
    # Save last section
    if current_section and current_content:
        section_text = '\n'.join(current_content).strip()
        if current_section == 'keywords':
            keywords = []
            for content_line in current_content:
                if content_line.strip().startswith('- '):
                    keywords.append(content_line.strip()[2:])
            data['keywords'] = keywords
        else:
            data[current_section] = section_text
    
    return data

def process_knowledgebase_files(knowledgebase_dir: str, output_file: str):
    """Process all markdown files in knowledgebase directory and create JSONL"""
    
    knowledgebase_path = Path(knowledgebase_dir)
    if not knowledgebase_path.exists():
        print(f"Error: Knowledgebase directory not found: {knowledgebase_dir}")
        return
    
    processed_count = 0
    error_count = 0
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Process all .md files
        for md_file in knowledgebase_path.glob('*.md'):
            try:
                # Read markdown file
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract ticket ID
                ticket_id = extract_ticket_id(md_file.name)
                
                # Parse content
                parsed_data = parse_markdown_content(content)
                
                # Create document
                doc = {
                    'id': hashlib.md5(f"{ticket_id}_{md_file.name}".encode()).hexdigest(),
                    'ticket_id': ticket_id,
                    'filename': md_file.name,
                    'title': f"Ticket {ticket_id}",
                    'keywords': parsed_data['keywords'],
                    'summary': parsed_data['summary'],
                    'problem_description': parsed_data['problem_description'],
                    'root_cause': parsed_data['root_cause'],
                    'solution': parsed_data['solution'],
                    'actions_taken': parsed_data['actions_taken'],
                    'general_learnings': parsed_data['general_learnings'],
                    'text': parsed_data['full_text'],
                    'text_length': len(parsed_data['full_text']),
                    'source': 'knowledgebase'
                }
                
                # Write to JSONL
                outfile.write(json.dumps(doc, ensure_ascii=False) + '\n')
                processed_count += 1
                
                if processed_count % 100 == 0:
                    print(f"Processed {processed_count} files...")
                    
            except Exception as e:
                print(f"Error processing {md_file.name}: {e}")
                error_count += 1
                continue
    
    print(f"\n=== Conversion Complete ===")
    print(f"Processed: {processed_count} files")
    print(f"Errors: {error_count} files")
    print(f"Output: {output_file}")

def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Convert knowledgebase markdown files to JSONL")
    parser.add_argument("--knowledgebase-dir", 
                       default="/Users/sebastian/Downloads/ticketknowledgedb/knowledgebase",
                       help="Path to knowledgebase directory")
    parser.add_argument("--output", 
                       default="/Users/sebastian/Downloads/ticketknowledgedb/knowledgebase_data.jsonl",
                       help="Output JSONL file path")
    
    args = parser.parse_args()
    
    process_knowledgebase_files(args.knowledgebase_dir, args.output)

if __name__ == "__main__":
    main()
