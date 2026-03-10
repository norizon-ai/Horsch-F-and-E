import json
from collections import defaultdict
from thefuzz import fuzz
import tqdm
import re

def load_tickets(filename):
    tickets = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                tickets.append(json.loads(line))
    return tickets

def save_tickets(tickets, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for ticket in tickets:
            f.write(json.dumps(ticket, ensure_ascii=False) + '\n')

def normalize_title(title):
    # Remove ticket IDs in square brackets
    title = re.sub(r'\[[a-z0-9]+\]', '', title)
    # Remove common variations
    title = title.lower().strip()
    
    # Normalize common HPC account variations
    title = re.sub(r'hpc-account', 'hpc account', title)
    title = re.sub(r'hpc[- ]zugang', 'hpc access', title)
    title = re.sub(r'hpc[- ]kennung', 'hpc account', title)
    title = re.sub(r'tier\d+-access', 'tier-access', title)
    
    return title

def contains_special_keywords(title):
    special_keywords = [
        'tier-access',
        'job on alex does not use',
        'job on alex does not use allocated gpu',
        'gpu allocated but not utilized',
        'gpus allocated but not utilized'
    ]
    
    account_keywords = [
        'hpc account',
        'hpc access',
        'hpc-berechtigung',
        'hpc zugang'
    ]
    
    title_lower = title.lower()
    
    # Check for special keywords
    if any(keyword in title_lower for keyword in special_keywords):
        return True
        
    # Check for account-related combinations
    account_matches = sum(1 for keyword in account_keywords if keyword in title_lower)
    return account_matches > 0

def find_similar_groups(tickets, similarity_threshold=85):
    # Dictionary to store groups of similar tickets
    groups = defaultdict(list)
    # Keep track of processed tickets
    processed = set()
    # Special counter for "Antrag" titles
    antrag_count = 0
    
    print("Grouping similar tickets...")
    for i, ticket in enumerate(tqdm.tqdm(tickets)):
        if i in processed:
            continue
            
        current_title = ticket['Title']
        normalized_title = normalize_title(current_title)
        
        # Check if this is a special case that should be grouped differently
        if contains_special_keywords(current_title):
            # For special cases, use more specific grouping
            for j, other_ticket in enumerate(tickets[i+1:], start=i+1):
                if j in processed:
                    continue
                
                other_title = other_ticket['Title']
                # Group tickets with same base pattern (ignoring IDs)
                if contains_special_keywords(other_title) and normalize_title(other_title) == normalized_title:
                    groups[normalized_title].append(other_ticket)
                    processed.add(j)
            
            groups[normalized_title].append(ticket)
            processed.add(i)
            continue
        
        # Handle "Antrag" titles separately with a counter
        if 'antrag' in normalized_title:
            if antrag_count >= 100:
                processed.add(i)
                continue
            antrag_count += 1
        
        current_group = [ticket]
        processed.add(i)
        
        # Compare with remaining tickets
        for j, other_ticket in enumerate(tickets[i+1:], start=i+1):
            if j in processed:
                continue
                
            other_title = other_ticket['Title']
            other_normalized = normalize_title(other_title)
            
            # Calculate similarity ratio
            similarity = fuzz.ratio(normalized_title, other_normalized)
            
            if similarity >= similarity_threshold:
                if 'antrag' in normalized_title and antrag_count >= 100:
                    continue
                current_group.append(other_ticket)
                processed.add(j)
                if 'antrag' in normalized_title:
                    antrag_count += 1
        
        # Use the normalized title as the group key
        group_key = normalized_title
        groups[group_key].extend(current_group)
    
    return groups

def deduplicate_tickets(input_file, output_file, max_duplicates=7):
    print(f"Loading tickets from {input_file}...")
    tickets = load_tickets(input_file)
    print(f"Loaded {len(tickets)} tickets")
    
    # Group similar tickets
    groups = find_similar_groups(tickets)
    
    # Select tickets to keep
    deduplicated_tickets = []
    print("\nDeduplicating tickets...")
    for group_key, group_tickets in groups.items():
        # For special cases, keep more examples
        max_keep = max_duplicates
        if contains_special_keywords(group_key):
            max_keep = 15  # Keep more examples for special cases
        
        # Keep up to max_keep tickets from each group
        kept_tickets = group_tickets[:max_keep]
        deduplicated_tickets.extend(kept_tickets)
        
        reduction = len(group_tickets) - len(kept_tickets)
        if reduction > 0:
            print(f"Group '{group_key}': Reduced from {len(group_tickets)} to {len(kept_tickets)} tickets")
    
    print(f"\nTotal tickets reduced from {len(tickets)} to {len(deduplicated_tickets)}")
    
    # Save deduplicated tickets
    print(f"Saving deduplicated tickets to {output_file}...")
    save_tickets(deduplicated_tickets, output_file)
    print("Done!")

if __name__ == "__main__":
    input_file = "total_tickets.jsonl"
    output_file = "dedup_total_tickets.jsonl"
    deduplicate_tickets(input_file, output_file)
