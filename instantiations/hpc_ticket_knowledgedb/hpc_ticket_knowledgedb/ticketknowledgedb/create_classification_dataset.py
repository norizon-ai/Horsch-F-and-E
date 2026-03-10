import json
import pandas as pd
import glob
from collections import defaultdict

def get_initial_request(ticket):
    """Extract the initial user request from a ticket."""
    if 'conversations' not in ticket or not ticket['conversations']:
        return None
    
    # Find the first user message
    for conv in ticket['conversations']:
        if conv.get('role') == 'user':
            # Combine subject and content if both exist
            message = ""
            if 'Subject' in conv:
                message += conv['Subject']
            if 'content' in conv:
                if message:
                    message += " | "
                message += conv['content']
            return message.strip()
    return None

def load_tickets(jsonl_files):
    """Load tickets from multiple JSONL files."""
    all_data = []
    queue_counts = defaultdict(int)
    
    for file_path in jsonl_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                ticket = json.loads(line)
                initial_request = get_initial_request(ticket)
                if initial_request:
                    queue = ticket.get('Queue')
                    if queue:
                        all_data.append({
                            'prompt': initial_request,
                            'completion': queue
                        })
                        queue_counts[queue] += 1
    
    return all_data, queue_counts

def balance_dataset(data, min_samples=None):
    """Balance the dataset by queue."""
    # Group data by queue
    queue_groups = defaultdict(list)
    for item in data:
        queue_groups[item['completion']].append(item)
    
    # If min_samples not specified, use the smallest queue size
    if min_samples is None:
        min_samples = min(len(group) for group in queue_groups.values())
    
    # Balance the dataset
    balanced_data = []
    for queue, items in queue_groups.items():
        # Take min_samples items from each queue
        balanced_data.extend(items[:min_samples])
    
    return balanced_data

def main():
    # Find all JSONL files
    jsonl_files = glob.glob('*.jsonl')
    
    # Load and process tickets
    print("Loading tickets...")
    all_data, queue_counts = load_tickets(jsonl_files)
    
    print("\nInitial queue distribution:")
    for queue, count in queue_counts.items():
        print(f"{queue}: {count} tickets")
    
    # Balance the dataset
    balanced_data = balance_dataset(all_data)
    
    # Convert to DataFrame and save
    df = pd.DataFrame(balanced_data)
    
    print("\nFinal dataset shape:", df.shape)
    print("\nSample of the dataset:")
    print(df.head())
    
    # Save to JSONL
    output_file = 'classification_dataset.jsonl'
    df.to_json(output_file, orient='records', lines=True)
    print(f"\nDataset saved to {output_file}")
    
    # Show final distribution
    print("\nFinal queue distribution:")
    print(df['completion'].value_counts())

if __name__ == '__main__':
    main()
