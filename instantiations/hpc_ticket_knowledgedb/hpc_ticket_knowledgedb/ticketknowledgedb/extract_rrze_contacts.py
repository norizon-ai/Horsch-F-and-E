import json
import re
from collections import defaultdict

def extract_name_from_field(field):
    """Extract name from a field like 'Name <email@domain.com>' or just 'Name'"""
    # Try to match name with email pattern first
    email_pattern = r'(.*?)\s*<.*?>'
    match = re.match(email_pattern, field)
    if match:
        return match.group(1).strip()
    # If no email pattern, return the whole field
    return field.strip()

def process_ticket_file(file_path):
    # Set to store unique agent names
    agent_names = set()
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            ticket = json.loads(line)
            
            # Process conversations
            for conv in ticket.get('conversations', []):
                # Check if this is an agent message
                if conv.get('SenderType') == 'agent':
                    # Extract name from From field if it exists
                    if 'From' in conv:
                        name = extract_name_from_field(conv['From'])
                        if name:
                            agent_names.add(name)
    
    return sorted(agent_names)

def main():
    file_path = 'tickets_10.jsonl'
    agent_names = process_ticket_file(file_path)
    
    print("Names of agents from ticket conversations:")
    print("-" * 50)
    
    for name in agent_names:
        print(f"- {name}")
    
    print(f"\nTotal unique agents found: {len(agent_names)}")

if __name__ == '__main__':
    main()