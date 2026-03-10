import argparse
import asyncio
import sys
import json
import logging
import os
from threading import TIMEOUT_MAX
from typing import List, Dict, Optional

import aiohttp
from aiofiles import open as aio_open
from openai import AsyncOpenAI
from pydantic import BaseModel

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stderr)
    ]
)

# Create logger
logger = logging.getLogger(__name__)

# Enable OpenAI debug logging
logging.getLogger("openai").setLevel(logging.DEBUG)
logging.getLogger("httpx").setLevel(logging.DEBUG)
logging.getLogger("httpcore").setLevel(logging.DEBUG)

# Print all OpenAI loggers
loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
openai_loggers = [logger for logger in loggers if logger.name.startswith("openai")]


MAX_REQUEST_ATTEMPTS = 3
REQUEST_TIMEOUT = TIMEOUT_MAX  # Use threading.TIMEOUT_MAX like worker.py
ON_THE_FLY_REQUESTS = 10
base_url = None
headers = {'content-type': 'application/json', 'Authorization': 'Bearer xFhGltj52Gn'}
API_KEY = 'xFhGltj52Gn'

logger.debug(f"Initialized with: MAX_REQUEST_ATTEMPTS={MAX_REQUEST_ATTEMPTS}, REQUEST_TIMEOUT={REQUEST_TIMEOUT}s, ON_THE_FLY_REQUESTS={ON_THE_FLY_REQUESTS}")

client = None

# MODEL = "AMead10/Llama-3.2-3B-Instruct-AWQ"
MODEL = "/anvme/workspace/unrz103h-helma/base_models/MistralAWQ"


class QnA(BaseModel):
    question: str
    answer: str


class ResponseDescription(BaseModel):
    pairs: list[QnA]


json_schema = ResponseDescription.model_json_schema()

def get_usr_msg(text: str, themengebiet: str, topic_filter: str, titel: str, autor: str, volltext: str):
    logger.debug(f"get_usr_msg inputs: text='{text[:100]}...', themengebiet='{themengebiet}', topic_filter='{topic_filter}', titel='{titel}', autor='{autor}', volltext='{volltext[:100]}...'")

    # Escape any % in the template string itself
    template = """
Du bist ein Experte für Steuerberatung und sollst eine Konversation basierend auf steuerrechtlichen Themen generieren. Dir werden die folgenden Informationen zu einem Textchunk gegeben:

- Themengebiet: {themengebiet}
- TopicFilter: {topic_filter}
- Titel: {titel}
- Autor: {autor}
- Volltext: {volltext}

Erstelle basierend auf diesen Informationen:
1. **Rote Linie (Chain of Thought)**: Eine kurze Beschreibung des Gesprächsverlaufs. Diese sollte die Hauptpunkte des Dialogs zusammenfassen und den logischen Fluss des Gesprächs skizzieren. Sie dient als Plan für den Dialog.
2. **Konversation**: Eine realistische und thematisch kohärente Unterhaltung zwischen einem Nutzer (user), der steuerrechtliche Fragen stellt, und einer KI (assistant), die als Steuerberater fungiert. Die Länge der Konversation hängt von der Komplexität des Themas im Volltext ab und kann flexibel sein (mindestens 1, aber auch mehr als 2 Interaktionen).

**Wichtige Hinweise zur Konversation**:
- **Variation**: Stelle sicher, dass die Formulierungen der Nutzerfragen abwechslungsreich und natürlich sind. Vermeide häufige Einleitungen wie "Ich habe eine Frage" oder "Ich habe gehört, dass". Stattdessen soll der Nutzer auch präzisere oder spezifischere Fragen stellen (z. B. direkt auf ein Szenario eingehen oder eine Regelung hinterfragen).
- **Natürlichkeit**: Die Fragen und Antworten sollen realistische Dialoge widerspiegeln, wie sie in einer echten Steuerberatungssituation vorkommen könnten.
- **Flexibilität**: Die Länge der Konversation hängt von der Komplexität des Themas im Volltext ab und kann flexibel sein (mindestens 1, aber auch mehr als 2 Interaktionen).

Gib die Konversation im JSON-Format aus. Jede Interaktion soll durch ein Objekt dargestellt werden. 

**Format**:
json '''
[
  {{ "content": "string", "role": "user" }},
  {{ "content": "string", "role": "assistant" }},
  ...
]
'''

**Beispiel für eine rote Linie**:
"Der Nutzer stellt Fragen zu steuerrechtlichen Konsequenzen einer neuen Gesetzgebung im Bereich {themengebiet}. Die KI erläutert die Regelung, gibt Beispiele und erklärt mögliche Auswirkungen auf Unternehmen und Privatpersonen. Es folgen spezifische Fragen zur praktischen Umsetzung."

Erstelle zuerst eine "rote Linie" für den gegebenen Textchunk. Nutze diese, um die Konversation zu strukturieren, und generiere dann die vollständige Unterhaltung. Achte darauf, dass der Dialog nachvollziehbar bleibt, auch ohne direkten Zugriff auf den Volltext. Beachte die erwähnte Flexibitlät der Fragenstellung.
""".replace('%', '%%')

    try:
        # Use str.format() instead of f-string to avoid format specifier issues
        result = template.format(
            themengebiet=themengebiet,
            topic_filter=topic_filter,
            titel=titel,
            autor=autor,
            volltext=volltext
        )
        logger.debug(f"get_usr_msg generated message (first 200 chars): {result[:200]}")
        return result
    except Exception as e:
        logger.error(f"Error formatting message template: {str(e)}")
        # Return a safe fallback that still includes the content but without formatting
        return f"""
Error in formatting. Raw inputs:
Text: {text}
Themengebiet: {themengebiet}
TopicFilter: {topic_filter}
Titel: {titel}
Autor: {autor}
Volltext: {volltext}
"""


def get_sys_msg():
    return """Du bist ein hochspezialisierter virtueller Steuerexperte, der sich darauf spezialisiert hat, steuerrechtliche Themen klar, präzise und für Laien verständlich zu erklären. Deine Aufgabe ist es, realistische, thematisch kohärente und nachvollziehbare Konversationen zu erstellen. 

Folgende Richtlinien musst du einhalten:
1. **Zielgruppe**: Die Nutzer (user) stellen Fragen, die sowohl von Laien als auch von steuerrechtlich versierten Personen stammen können. Deine Antworten sollten immer professionell und fachlich korrekt sein, aber auch leicht verständlich bleiben.
2. **Konversation**: Erstelle ein realistisches Gespräch basierend auf vorgegebenen Themen und Inhalten. Die Länge der Konversation richtet sich nach der Komplexität des Themas und kann flexibel sein.
3. **Formatierung**: Die Konversation wird in einem JSON-Format dargestellt, mit klaren Rollen (user und assistant) und verständlichen Inhalten. Nutze ein iteratives Frage-Antwort-Muster.
4. **Zusammenhänge**: Gib den Nutzern genügend Kontext, damit sie die Konversation nachvollziehen können, auch ohne direkten Zugriff auf die Originalquelle (den Textchunk).
5. **Chain of Thought**: Generiere immer eine "rote Linie", um die Hauptpunkte und den logischen Fluss des Gesprächs vorab zu skizzieren. Nutze diese als Grundlage für den Dialog.
6. **Stil der Fragen**: Benutze keine Floskeln wie "Ich habe eine Frage" oder "Ich habe gehört, dass". Stelle sicher, dass die Fragen abwechslungsreich und natürlich sind.

Bleibe sachlich und thematisch genau, aber auch flexibel, um auf spezifische Szenarien einzugehen.
"""


class RequestQueue:
    successful_requests = 0
    failed_requests = 0

    def __init__(self, max_concurrent_requests: int):
        """
        Initialize the request queue with a max number of concurrent requests.

        :param max_concurrent_requests: Maximum number of requests to process concurrently
        """
        self.max_concurrent_requests = max_concurrent_requests
        self.pending_queue = asyncio.Queue()
        self.active_requests = set()
        self.semaphore = asyncio.Semaphore(max_concurrent_requests)

    async def add_request(self, data: Dict):
        """
        Add a request to the queue.

        :param data: Request data to be processed
        """
        record_id = data['_recordid']
        data['attempt'] += 1  # keep track of attempt
        if data['attempt'] <= MAX_REQUEST_ATTEMPTS:
            logger.warning(f"Timeout for request id: {record_id}. Requeueing attempt {data['attempt']}.")
            await self.pending_queue.put(data)
            await self.process_queue()
        else:
            RequestQueue.failed_requests += 1
            logger.error(f"Max retries reached. Dropping the request: id: {record_id}.")

    async def process_queue(self):
        """
        Process the queue by sending requests up to the max concurrent limit.
        """
        tasks = []
        while (not self.pending_queue.empty() and
               len(self.active_requests) < self.max_concurrent_requests):
            try:
                # Get a request from the queue without blocking
                data = self.pending_queue.get_nowait()

                # Create a task for the request
                task = asyncio.create_task(self.process_request(data))
                self.active_requests.add(task)
                tasks.append(task)

                # Remove the request from active set when it's done
                task.add_done_callback(self.active_requests.discard)
            except asyncio.QueueEmpty:
                break

        # Wait for all tasks to complete
        if tasks:
            await asyncio.gather(*tasks)

    async def process_request(self, data: Dict):
        """
        Process a single request with retry logic.
        """
        try:
            async with self.semaphore:
                record_id = data.get('_recordid', 'unknown')
                logger.debug(f"Processing request {record_id}")

                # Only validate Volltext as required
                if not data.get('volltext'):
                    logger.error(f"Request {record_id} missing required field: volltext")
                    self.failed_requests += 1
                    return

                try:
                    # Prepare message with proper escaping
                    messages = [
                        {"role": "system", "content": get_sys_msg()},
                        {"role": "user", "content": get_usr_msg(
                            data.get('text', ''),
                            data.get('themengebiet', ''),
                            data.get('topic_filter', ''),
                            data.get('titel', ''),
                            data.get('autor', ''),
                            data['volltext']
                        )}
                    ]

                    request_body = {
                        "model": MODEL,
                        "messages": messages,
                        "temperature": 0.3,
                        "top_p": 0.8
                    }

                    logger.debug(f"Request {record_id} - API Configuration:")
                    logger.debug(f"  Base URL: {base_url}")
                    logger.debug(f"  Model: {MODEL}")
                    logger.debug(f"  System message length: {len(messages[0]['content'])}")
                    logger.debug(f"  User message length: {len(messages[1]['content'])}")
                    logger.debug(f"  Total request size: {len(str(request_body))} bytes")

                    try:
                        logger.debug("Making API call now...")
                        completion = await asyncio.wait_for(
                            client.chat.completions.create(**request_body),
                            timeout=REQUEST_TIMEOUT
                        )
                        
                        logger.debug(f"Got response: {completion}")
                        content = completion.choices[0].message.content.strip()
                        logger.debug(f"Raw content: {content}")
                        
                        # Extract JSON content
                        try:
                            # First try direct JSON parsing
                            json_content = json.loads(content)
                        except json.JSONDecodeError:
                            # If that fails, try to extract JSON from markdown code blocks
                            if "```json" in content:
                                # Extract content between ```json and ```
                                json_content = content.split("```json")[1].split("```")[0].strip()
                                logger.debug(f"Extracted JSON content: {json_content}")
                                json_content = json.loads(json_content)
                            else:
                                raise ValueError("Response does not contain valid JSON or ```json``` block")
                        
                        # Convert the conversation array into our expected format
                        processed_content = {
                            '_recordid': record_id,
                            'conversation': json_content
                        }
                        
                        logger.debug(f"Final processed content: {json.dumps(processed_content, indent=2)}")
                        
                        async with aio_open(output_file, mode='a', encoding='utf-8') as fout:
                            await fout.write(json.dumps(processed_content) + '\n')
                        
                        logger.debug(f"Request {record_id} completed successfully")
                        self.successful_requests += 1
                        return processed_content
                            
                    except asyncio.TimeoutError:
                        logger.warning(f"Timeout for request {record_id}. Requeueing.")
                        if data['attempt'] < MAX_REQUEST_ATTEMPTS - 1:
                            data['attempt'] += 1
                            await self.add_request(data)
                        else:
                            logger.error(f"Max retries reached for request {record_id}")
                            self.failed_requests += 1
                            
                    except Exception as e:
                        logger.error(f"API call failed for request {record_id}: {str(e)}")
                        if data['attempt'] < MAX_REQUEST_ATTEMPTS - 1:
                            data['attempt'] += 1
                            await self.add_request(data)
                        else:
                            logger.error(f"Max retries reached for request {record_id}")
                            self.failed_requests += 1

                except Exception as e:
                    logger.error(f"Error processing request for _recordid:{record_id}: {str(e)}")
                    if data['attempt'] < MAX_REQUEST_ATTEMPTS - 1:
                        data['attempt'] += 1
                        await self.add_request(data)
                    else:
                        logger.error(f"Max retries reached for request {record_id}")
                        self.failed_requests += 1

        except Exception as final_error:
            logger.critical(f"Unhandled error in process_request: {str(final_error)}")
            self.failed_requests += 1
            return None


async def load_processed_records(output_path: str) -> set:
    """
    Load already processed record IDs from the output file.
    
    :param output_path: Path to the output JSONL file
    :return: Set of processed record IDs
    """
    processed_records = set()
    try:
        if os.path.exists(output_path):
            async with aio_open(output_path, 'r') as file:
                async for line in file:
                    try:
                        record = json.loads(line)
                        if '_recordid' in record:
                            processed_records.add(record['_recordid'])
                    except json.JSONDecodeError:
                        continue
            logger.info(f"Found {len(processed_records)} already processed records in {output_path}")
    except Exception as e:
        logger.error(f"Error loading processed records from {output_path}: {str(e)}")
    
    return processed_records

async def parse_file(file_path: str, request_queue: RequestQueue, processed_records: set):
    """
    Parse the file asynchronously and add each item from the JSON list to the request queue.

    :param file_path: Path to the input file
    :param request_queue: Queue to add parsed data
    :param processed_records: Set of already processed record IDs
    """
    try:
        async with aio_open(file_path, 'r') as file:
            content = await file.read()
            try:
                data = json.loads(content)
                for index, chunk in enumerate(data):
                    try:
                        # Check if record has already been processed
                        if chunk['_recordid'] in processed_records:
                            logger.info(f"Skipping already processed record {chunk['_recordid']} in {file_path}")
                            continue

                        # Check for required Volltext field
                        if 'Volltext' not in chunk or not chunk['Volltext']:
                            logger.error(f"Skipping chunk {index} in {file_path} due to missing required field: Volltext")
                            continue

                        # Get all other fields with empty string defaults
                        request_data = {
                            '_recordid': chunk['_recordid'],  # Use the original _recordid
                            'text': chunk.get('text', ''),
                            'themengebiet': chunk.get('Themengebiet', ''),
                            'topic_filter': chunk.get('TopicFilter', ''),
                            'titel': chunk.get('Titel', ''),
                            'autor': chunk.get('Autor', ''),
                            'volltext': chunk['Volltext'],  # Required field
                            'attempt': 0
                        }

                        # Log any missing optional fields
                        optional_fields = ['text', 'Themengebiet', 'TopicFilter', 'Titel', 'Autor']
                        missing_fields = [field for field in optional_fields if not chunk.get(field)]
                        if missing_fields:
                            logger.info(f"Initializing missing optional fields as empty in chunk {index} of {file_path}: {', '.join(missing_fields)}")

                        await request_queue.add_request(request_data)
                    except Exception as e:
                        logger.error(f"Error processing chunk {index} in {file_path}: {str(e)}")
                        continue
            except json.JSONDecodeError as e:
                logger.error(f"Error decoding JSON from {file_path}: {str(e)}")
    except Exception as e:
        logger.error(f"Error reading file {file_path}: {str(e)}")


async def main(input_files: str, output_dir: str, max_concurrent: int = ON_THE_FLY_REQUESTS):
    """
    Main function to coordinate file parsing and sending HTTP requests.

    :param input_files: Comma-separated list of input files
    :param output_dir: Directory path where output files will be stored
    :param max_concurrent: Maximum number of concurrent requests
    """
    # Create request queue with max concurrent requests
    request_queue = RequestQueue(max_concurrent)
    
    # Parse input files and add to queue
    file_list = input_files.split(',')
    for file_path in file_list:
        file_path = file_path.strip()
        # Get the base name of the input file and create output path
        input_basename = os.path.basename(file_path)
        input_name = os.path.splitext(input_basename)[0]
        output_path = os.path.join(output_dir, f"{input_name}.jsonl")
        
        # Set the global output file for this input file
        global output_file
        output_file = output_path
        
        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)
        
        # Load already processed records
        processed_records = await load_processed_records(output_path)
        
        await parse_file(file_path, request_queue, processed_records)
    
    # Process the queue
    await request_queue.process_queue()
    
    # Print statistics
    total = request_queue.successful_requests + request_queue.failed_requests
    if total > 0:
        success_rate = (request_queue.successful_requests / total) * 100
        logger.info(f"Processing complete. Total chunks: {total}, Success rate: {success_rate:.2f}%")
    else:
        logger.warning("No chunks were processed. Please check your input files and required fields.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Asynchronous file parser and HTTP sender")
    parser.add_argument(
        '--input-files',
        required=True,
        help='Comma-separated list of input files'
    )
    parser.add_argument(
        '--output-dir',
        required=True,
        help='Directory path where output files will be stored'
    )
    parser.add_argument(
        '--endpoint',
        type=str, 
        required=True,
        help="ip address of the AI assistant"
    )
    parser.add_argument(
        '--max-concurrent',
        type=int,
        default=ON_THE_FLY_REQUESTS,
        help='Maximum number of concurrent requests'
    )

    args = parser.parse_args()

    # Set up base URL and client
    base_url = f"http://{args.endpoint}:6000/v1/"
    client = AsyncOpenAI(
        base_url=base_url,
        api_key="Bearer xFhGltj52Gn",
        timeout=REQUEST_TIMEOUT  # Set the client timeout to match our desired timeout
    )

    logger.info(f"Base URL: {base_url}")
    logger.info(f"Max Concurrent Requests: {args.max_concurrent}")

    # Run the asyncio program
    asyncio.run(main(args.input_files, args.output_dir, args.max_concurrent))

    total = RequestQueue.successful_requests+RequestQueue.failed_requests

    if total > 0:
        success_rate = (RequestQueue.successful_requests / total) * 100
        print(f"Total chunks: {total}, Success rate: {success_rate:.2f}%")
    else:
        print("No chunks were processed. Please check your input files and required fields.")
