import json

# List of input files to combine
input_files = [
    'tickets_10.jsonl',
    'tickets_restructured.jsonl',
    'tickets_NHR-Support.jsonl',
    'tickets_HPC_Admins.jsonl'
]

# Set to keep track of unique ticket IDs
seen_ticket_ids = set()
total_tickets = 0
duplicates = 0

with open('total_tickets.jsonl', 'w', encoding='utf-8') as outfile:
    for input_file in input_files:
        try:
            with open(input_file, 'r', encoding='utf-8') as infile:
                print(f"Processing {input_file}...")
                for line in infile:
                    ticket = json.loads(line.strip())
                    ticket_id = ticket.get('TicketID')
                    
                    if ticket_id not in seen_ticket_ids:
                        outfile.write(line)
                        seen_ticket_ids.add(ticket_id)
                        total_tickets += 1
                    else:
                        duplicates += 1
        except FileNotFoundError:
            print(f"Warning: {input_file} not found, skipping...")
            continue

print(f"\nCombination complete!")
print(f"Total unique tickets: {total_tickets}")
print(f"Duplicate tickets skipped: {duplicates}")
