import json
import asyncio
import aiohttp
import os
import sys
import logging
from threading import TIMEOUT_MAX
from urllib.parse import quote
from typing import List, Dict
from datetime import datetime
from tqdm import tqdm

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stderr)]
)
logger = logging.getLogger(__name__)

# API configuration from worker.py
API_KEY = 'xFhGltj52Gn'
base_url = 'http://10.28.89.46:6000'
MODEL = '/anvme/workspace/unrz103h-helma/base_models/MistralAWQ'
MAX_WORKERS = 10
REQUEST_TIMEOUT = TIMEOUT_MAX  # Use same timeout as worker.py
headers = {'content-type': 'application/json', 'Authorization': f'Bearer {API_KEY}'}

# Prompt template
PROMPT_TEMPLATE = """What can be learned from following HPC-Support Ticket conversation:
{ticket_content}
Add keywords to the output and whats to be learned generally, it can be vague. Don't use peoples names. The role system are employees of the hpc site (Thomas, Michael Meier, Anna Kahler, Katrin Nusser, Johannes Veh are HPC Admins, refer to them as HPC Admins). The 2nd Level Support team consists of Lacey, Dane (fo36fizy), Kuckuk, Sebastian (sisekuck), Lange, Florian (ow86apyf), Ernst, Dominik (te42kyfo), and Mayr, Martin. Gehard Wellein is Head of the Datacenter and Georg Hager Training and Support Group Leader. Harald Lanig is caring about NHR Rechenzeit Support and Applications for Grants. Jan Eitzinger and Gruber are Software and Tools developer. Keep it very short. Sometimes its not clear what is done. Extract the root cause of the problem from the user. Add the solution if found. Your report will later be used to solve similar errors of they appear again so write it in a style like a documentation for support employees to look up help. Write it in Markdown. Only respond with the Markdown report infomation."""

def format_ticket_content(ticket: Dict) -> str:
    """Format ticket content for the prompt."""
    content = f"Subject: {ticket['Title']}\n\n"
    
    for conv in ticket['conversations']:
        if 'content' not in conv:
            logger.debug(f"Skipping conversation without content in ticket {ticket['TicketNumber']}, ArticleID: {conv.get('ArticleID', 'unknown')}")
            continue
            
        role = 'HPC Admin' if conv['role'] == 'system' else 'User'
        content += f"{role}: {conv['content']}\n\n"
    
    return content

def get_safe_filename(ticket: Dict) -> str:
    """Generate a safe filename from ticket subject and number."""
    subject = quote(ticket['Title'].replace('/', '_'))
    return f"{ticket['TicketNumber']}_{subject[:100]}.md"

async def process_ticket(session: aiohttp.ClientSession, ticket: Dict, semaphore: asyncio.Semaphore) -> None:
    """Process a single ticket with the API and save the result."""
    async with semaphore:  # Control concurrent requests
        try:
            ticket_content = format_ticket_content(ticket)
            prompt = PROMPT_TEMPLATE.format(ticket_content=ticket_content)
            
            payload = {
                'model': MODEL,
                'messages': [
                    {'role': 'system', 'content': 'You are a helpful HPC support knowledge base assistant.'},
                    {'role': 'user', 'content': prompt}
                ],
                'temperature': 0.2,
                'top_p': 0.95,
                'max_tokens': 4096
            }
            
            url = f'{base_url}/v1/chat/completions'
            logger.debug(f"Sending request for ticket {ticket['TicketNumber']} to {url}")
            async with session.post(url, headers=headers, json=payload, timeout=REQUEST_TIMEOUT) as response:
                response_text = await response.text()
                logger.debug(f"Response for ticket {ticket['TicketNumber']}: {response.status} - {response_text[:200]}")
                
                if response.status == 200:
                    try:
                        result = json.loads(response_text)
                        logger.debug(f"Full API response for ticket {ticket['TicketNumber']}: {json.dumps(result, indent=2)}")
                        
                        if 'choices' not in result:
                            print(f"✗ Error processing ticket {ticket['TicketNumber']}: No 'choices' in response")
                            logger.error(f"Response structure invalid: {result}")
                            return
                            
                        if not result['choices']:
                            print(f"✗ Error processing ticket {ticket['TicketNumber']}: Empty choices list")
                            logger.error(f"Empty choices list in response: {result}")
                            return
                            
                        message = result['choices'][0].get('message', {})
                        if not message:
                            print(f"✗ Error processing ticket {ticket['TicketNumber']}: No message in first choice")
                            logger.error(f"No message in first choice: {result['choices'][0]}")
                            return
                            
                        content = message.get('content', '')
                        if content:
                            markdown_content = f"# Ticket {ticket['TicketNumber']}\n\n{content}"
                            
                            filename = get_safe_filename(ticket)
                            filepath = os.path.join('knowledgebase', filename)
                            
                            with open(filepath, 'w', encoding='utf-8') as f:
                                f.write(markdown_content)
                                
                            print(f"✓ Processed ticket {ticket['TicketNumber']}")
                        else:
                            print(f"✗ Error processing ticket {ticket['TicketNumber']}: Empty content in response")
                            logger.error(f"Empty content in message: {message}")
                    except json.JSONDecodeError as e:
                        print(f"✗ Error processing ticket {ticket['TicketNumber']}: Invalid JSON response - {str(e)}")
                else:
                    print(f"✗ Error processing ticket {ticket['TicketNumber']}: {response.status} - {response_text[:100]}")
                    
        except Exception as e:
            print(f"✗ Error processing ticket {ticket['TicketNumber']}: {str(e)}")

async def process_tickets(tickets: List[Dict]) -> None:
    """Process multiple tickets in parallel with rate limiting."""
    # Create a semaphore to limit concurrent requests
    semaphore = asyncio.Semaphore(MAX_WORKERS)
    
    # Create progress bar
    pbar = tqdm(total=len(tickets), desc='Processing tickets', unit='ticket')
    
    async with aiohttp.ClientSession() as session:
        tasks = []
        for ticket in tickets:
            task = asyncio.create_task(process_ticket(session, ticket, semaphore))
            tasks.append(task)
        
        # Process all tasks
        for task in asyncio.as_completed(tasks):
            await task
            pbar.update(1)
        
        pbar.close()

def main():
    if not API_KEY:
        print("Error: OPENAI_API_KEY environment variable not set")
        return
    
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(description='Process HPC support tickets')
    parser.add_argument('--start-from', type=int, default=0,
                        help='Start processing from this ticket index (0-based)')
    args = parser.parse_args()
    
    # Ensure the knowledgebase directory exists
    os.makedirs('knowledgebase', exist_ok=True)
    
    # Read tickets from the combined file
    tickets = []
    with open('dedup_total_tickets.jsonl', 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i >= args.start_from:  # Only load tickets from the starting point
                tickets.append(json.loads(line))
    
    total_tickets = args.start_from + len(tickets)
    print(f"Starting processing from ticket {args.start_from}/{total_tickets} ({len(tickets)} tickets remaining)...")
    
    try:
        # Run the async processing
        asyncio.run(process_tickets(tickets))
        print("\nProcessing complete! Knowledge base files have been created in the 'knowledgebase' directory.")
    except KeyboardInterrupt:
        print("\nProcessing interrupted by user. You can resume from the last processed ticket.")
    except Exception as e:
        print(f"\nError occurred: {str(e)}")
        print("You can resume processing from the last successful ticket.")

if __name__ == "__main__":
    main()
