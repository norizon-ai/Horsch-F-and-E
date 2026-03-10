import json
import glob
import os
from datetime import datetime

def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        return False

def validate_ticket(ticket):
    # Required ticket fields
    required_fields = ['TicketNumber', 'TicketID', 'Title', 'Created', 'Queue', 'State']
    missing_fields = [field for field in required_fields if field not in ticket]
    if missing_fields:
        return False, f"Missing required fields: {', '.join(missing_fields)}"
    
    # Validate Created date
    if not validate_date(ticket['Created']):
        return False, f"Invalid Created date format: {ticket['Created']}"
    
    # Validate conversations
    if 'conversations' not in ticket:
        return False, "Missing conversations array"
    
    if not isinstance(ticket['conversations'], list):
        return False, "Conversations is not an array"
    
    for idx, conv in enumerate(ticket['conversations']):
        # Validate CreateTime if present
        if 'CreateTime' in conv and not validate_date(conv['CreateTime']):
            return False, f"Invalid CreateTime in conversation {idx}: {conv['CreateTime']}"
    
    return True, "Valid"

def validate_jsonl_file(file_path):
    print(f"\nValidating {file_path}")
    errors = []
    valid_count = 0
    total_count = 0
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                total_count += 1
                try:
                    ticket = json.loads(line)
                    is_valid, message = validate_ticket(ticket)
                    if is_valid:
                        valid_count += 1
                    else:
                        errors.append(f"Line {line_num}: {message}")
                except json.JSONDecodeError as e:
                    errors.append(f"Line {line_num}: Invalid JSON - {str(e)}")
                except Exception as e:
                    errors.append(f"Line {line_num}: Unexpected error - {str(e)}")
    except Exception as e:
        errors.append(f"File error: {str(e)}")
    
    return valid_count, total_count, errors

def main():
    jsonl_files = glob.glob('*.jsonl')
    
    if not jsonl_files:
        print("No JSONL files found in the current directory")
        return
    
    total_valid = 0
    total_tickets = 0
    
    for file_path in jsonl_files:
        valid_count, total_count, errors = validate_jsonl_file(file_path)
        total_valid += valid_count
        total_tickets += total_count
        
        print(f"\nResults for {file_path}:")
        print(f"Valid tickets: {valid_count}/{total_count} ({(valid_count/total_count*100):.2f}%)")
        
        if errors:
            print("\nErrors found:")
            for error in errors:
                print(f"- {error}")
        else:
            print("No errors found")
    
    print(f"\nOverall Summary:")
    print(f"Total valid tickets: {total_valid}/{total_tickets} ({(total_valid/total_tickets*100):.2f}%)")

if __name__ == '__main__':
    main()
