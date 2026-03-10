#!/usr/bin/env python3
import json
import random

def sample_jsonl(input_file, output_file, sample_size=100):
    """
    Sample random entries from a JSONL file.
    
    Args:
        input_file (str): Path to the input JSONL file
        output_file (str): Path to save the sampled data
        sample_size (int): Number of samples to extract
    """
    # Read all lines from the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Get total number of entries
    total_entries = len(lines)
    print(f"Total entries in the file: {total_entries}")
    
    # If sample size is greater than total entries, adjust it
    if sample_size > total_entries:
        print(f"Sample size {sample_size} is greater than total entries {total_entries}")
        print(f"Adjusting sample size to {total_entries}")
        sample_size = total_entries
    
    # Randomly select sample_size entries
    sampled_indices = random.sample(range(total_entries), sample_size)
    sampled_lines = [lines[i] for i in sampled_indices]
    
    # Write sampled entries to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in sampled_lines:
            f.write(line)
    
    print(f"Successfully sampled {sample_size} entries and saved to {output_file}")

if __name__ == "__main__":
    input_file = "/Users/sebastian/Downloads/ticketknowledgedb/dedup_total_tickets.jsonl"
    output_file = "/Users/sebastian/Downloads/ticketknowledgedb/ticketsampledata.jsonl"
    
    sample_jsonl(input_file, output_file)
