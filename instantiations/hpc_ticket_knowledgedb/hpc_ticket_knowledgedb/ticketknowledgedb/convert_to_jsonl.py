import json
import glob
import re
from datetime import datetime

def parse_ticket_file(file_path):
    with open(file_path, 'r', encoding='latin-1') as f:
        content = f.read()

    # Split by the double line separator
    tickets_raw = content.split('=====================================================================')
    tickets = []

    required_fields = ['TicketNumber', 'TicketID', 'Title', 'Created', 'Queue', 'State']

    for ticket_raw in tickets_raw:
        if not ticket_raw.strip():
            continue

        ticket = {}
        sections = ticket_raw.split('---------------------------------------------------------------------')
        
        # Parse header section
        header = sections[0]
        header_lines = [line.strip() for line in header.split('\n') if line.strip()]
        for line in header_lines:
            if ':' in line:
                key, value = line.split(':', 1)
                ticket[key.strip()] = value.strip()

        # Check if all required fields are present
        has_required_fields = all(field in ticket for field in required_fields)
        if not has_required_fields:
            continue

        # Parse conversations
        conversations = []
        current_message = None

        try:
            for section in sections[1:]:
                if not section.strip():
                    continue

                lines = [line.strip() for line in section.split('\n') if line.strip()]
                if not lines:
                    continue

                # Check if this section starts with metadata (contains ':')
                if ':' in lines[0]:
                    # If we have a previous message, try to add it if it's valid
                    if current_message is not None:
                        # Determine role based on SenderType or email domain
                        if 'SenderType' in current_message:
                            if current_message['SenderType'] == 'customer':
                                current_message['role'] = 'user'
                            elif current_message['SenderType'] == 'agent':
                                current_message['role'] = 'system'
                        elif 'Sender' in current_message:
                            sender_email = current_message['Sender'].lower()
                            if '@rrze.uni-erlangen.de' in sender_email or 'hpc@rrze.uni-erlangen.de' in sender_email:
                                current_message['role'] = 'system'
                            else:
                                current_message['role'] = 'user'
                        if 'role' in current_message and ('content' in current_message or 'Subject' in current_message):
                            conversations.append(current_message)

                    # Start a new message
                    current_message = {}
                    content_lines = []

                    # Parse metadata
                    for line in lines:
                        if ':' in line:
                            key, value = line.split(':', 1)
                            current_message[key.strip()] = value.strip()
                        else:
                            content_lines.append(line)

                    if content_lines:
                        current_message['content'] = '\n'.join(content_lines)
                else:
                    # This section is content for the previous message
                    if current_message is not None:
                        content = '\n'.join(lines)
                        if 'content' in current_message:
                            current_message['content'] += '\n' + content
                        else:
                            current_message['content'] = content

            # Add the last message if valid
            if current_message is not None:
                # Determine role based on SenderType or email domain
                if 'SenderType' in current_message:
                    if current_message['SenderType'] == 'customer':
                        current_message['role'] = 'user'
                    elif current_message['SenderType'] == 'agent':
                        current_message['role'] = 'system'
                elif 'Sender' in current_message:
                    sender_email = current_message['Sender'].lower()
                    if '@rrze.uni-erlangen.de' in sender_email or 'hpc@rrze.uni-erlangen.de' in sender_email:
                        current_message['role'] = 'system'
                    else:
                        current_message['role'] = 'user'
                if 'role' in current_message and ('content' in current_message or 'Subject' in current_message):
                    conversations.append(current_message)

            # Only add tickets with valid conversations
            if conversations:
                # Verify all conversations have required fields
                valid = True
                for conv in conversations:
                    if not ('role' in conv and 
                           'Sender' in conv and 
                           ('content' in conv or 'Subject' in conv)):
                        valid = False
                        break

                if valid:
                    ticket['conversations'] = conversations
                    tickets.append(ticket)

        except Exception as e:
            # Skip tickets with parsing errors
            continue

    return tickets

def save_to_jsonl(tickets, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for ticket in tickets:
            # Convert latin-1 encoded strings to unicode
            for conv in ticket.get('conversations', []):
                if 'content' in conv:
                    conv['content'] = conv['content'].encode('latin-1').decode('utf-8', errors='replace')
            f.write(json.dumps(ticket, ensure_ascii=False) + '\n')

if __name__ == '__main__':
    # Find all .txt files in the current directory
    txt_files = glob.glob('*.txt')
    
    if not txt_files:
        print("No .txt files found in the current directory")
        exit()
    
    # Process each .txt file
    for input_file in txt_files:
        # Generate output filename by replacing .txt with .jsonl
        output_file = input_file.rsplit('.', 1)[0] + '.jsonl'
        
        # Convert the file
        tickets = parse_ticket_file(input_file)
        save_to_jsonl(tickets, output_file)
        print(f"Converted {len(tickets)} tickets from {input_file} to {output_file}")
