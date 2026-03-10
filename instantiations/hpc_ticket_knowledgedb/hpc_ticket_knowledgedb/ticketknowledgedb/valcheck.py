#!/usr/bin/env python3
import json
import sys
from typing import Dict, List, Any

def validate_content(content: str) -> List[str]:
    """
    Validate content string for common issues.
    Returns a list of issues found, empty list if content is valid.
    """
    issues = []
    
    # Check for null bytes
    if '\x00' in content:
        issues.append("Contains null bytes")
    
    # Check for broken unicode
    try:
        content.encode('utf-8').decode('utf-8')
    except UnicodeError:
        issues.append("Invalid Unicode encoding")
    
    # Check for incomplete escape sequences
    if content.count('\\') != content.count('\\\\') * 2:
        issues.append("Potentially incomplete escape sequences")
        
    # Check for broken HTML/XML entities
    if '&' in content and not all(e.endswith(';') for e in content.split('&')[1:] if any(c.isalpha() for c in e)):
        issues.append("Potentially broken HTML/XML entities")
        
    # Check for control characters (except common ones like newline, tab)
    control_chars = ''.join(chr(i) for i in range(32) if i not in [9, 10, 13])
    if any(c in content for c in control_chars):
        issues.append("Contains unexpected control characters")
        
    return issues

def check_jsonl_file(filepath: str) -> Dict[str, List[Dict[str, Any]]]:
    """
    Check each line in the JSONL file and validate conversation content.
    Returns a dictionary of issues found.
    """
    issues_by_line = {
        "parsing_errors": [],
        "content_issues": []
    }
    
    with open(filepath, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            try:
                record = json.loads(line.strip())
                if 'conversations' in record:
                    for conv_idx, conv in enumerate(record['conversations']):
                        if 'content' in conv:
                            content_issues = validate_content(conv['content'])
                            if content_issues:
                                issues_by_line["content_issues"].append({
                                    "line": line_num,
                                    "conversation_index": conv_idx,
                                    "issues": content_issues
                                })
            except json.JSONDecodeError as e:
                issues_by_line["parsing_errors"].append({
                    "line": line_num,
                    "error": str(e)
                })
                
    return issues_by_line

def main():
    if len(sys.argv) != 2:
        print("Usage: python valcheck.py <jsonl_file>")
        sys.exit(1)
        
    filepath = sys.argv[1]
    issues = check_jsonl_file(filepath)
    
    if not any(issues.values()):
        print("No issues found!")
        return
        
    if issues["parsing_errors"]:
        print("\nJSON Parsing Errors:")
        for error in issues["parsing_errors"]:
            print(f"Line {error['line']}: {error['error']}")
            
    if issues["content_issues"]:
        print("\nContent Issues:")
        for issue in issues["content_issues"]:
            print(f"Line {issue['line']}, Conversation {issue['conversation_index']}:")
            for problem in issue['issues']:
                print(f"  - {problem}")

if __name__ == "__main__":
    main()
