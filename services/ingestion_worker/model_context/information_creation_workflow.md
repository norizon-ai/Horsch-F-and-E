Here is the flow, using the example of an Admin wanting to sync a Confluence space:


  Step 1: The Job Order (Ingestion Orchestrator)


   1. The Trigger: An administrator goes to the tierzero web UI and clicks the "Sync Confluence Space" button.
   2. The API Call: The frontend sends a simple, lightweight request to the Ingestion Orchestrator service. For example: POST 
      /api/v1/ingest/confluence.
   3. The Command: The Ingestion Orchestrator's only job is to receive this request and translate it into a formal command message. It does
      not know how to crawl Confluence itself. It simply creates a message like:
      { "source": "confluence", "space_id": "ENG", "crawl_type": "full" }
   4. Publishing the Command: The Orchestrator then publishes this command message to a specific topic on the Message Bus, let's call it the
      crawl.requested topic. Its job is now done.

  Step 2: The Conveyor Belt (Message Bus)


   1. Holding the Job: The Message Bus (e.g., RabbitMQ) receives the message from the Orchestrator and holds it in the crawl.requested queue.
   2. Decoupling: This is the most critical role of the bus. The Orchestrator doesn't know or care which service will handle the job. If the
      relevant connector service is down, the message simply waits safely in the queue until a consumer is available. This ensures fault 
      tolerance.

  Step 3: The Specialized Work (Connector Services - A type of Worker)


   1. Listening for Work: A specialized service, the Confluence Connector, is subscribed to the crawl.requested topic. It's constantly
      listening for messages that are relevant to it.
   2. Claiming the Job: It sees the Confluence job message, picks it up from the queue, and begins its work.
   3. Fetching Data: The connector holds all the logic to talk to the external Confluence API. It fetches the pages from the "ENG" space one
      by one.
   4. Publishing Raw Material: For each page it successfully fetches, the connector wraps the raw content, metadata (title, author), and
      permissions into a standardized message format. It then publishes this new message to a different topic on the Message Bus, such as
      content.raw.received.

  Step 4: The Assembly Line (Processing Workers)


   1. Generic Work: A pool of identical Processing Workers is subscribed to the content.raw.received topic. These workers are generic; they
      don't care if the content came from Confluence, Slack, or the Intranet.
   2. The Pipeline: When a worker picks up a raw content message, it performs a series of sequential, CPU-intensive tasks:
       * Chunking: It breaks the large document text into smaller, searchable chunks.
       * Enriching: It might scan for PII (PermSec04) or perform other transformations.
       * Embedding: It calls an embedding model (like one from OpenAI or a local model) to generate a vector embedding for each chunk.
   3. Scalability: If there is a large influx of documents (e.g., a full site crawl), the content.raw.received queue will grow. To handle
      this, we can simply scale up the number of Processing Worker replicas. They will work in parallel to clear the queue faster, without
      affecting any other part of the system.

  Step 5: The Warehouse (Database)


   1. The Final Step: Once a Processing Worker has a fully processed chunk (with its text, metadata, and vector embedding), it performs the
      final action.
   2. Writing the Data: The worker connects to the central Database (PostgreSQL) and inserts the data into the appropriate tables (documents
      and chunks).

  The data is now fully ingested, indexed, and immediately available to the Search Service for user queries.

  Summary of the Interaction


   - Orchestrator creates the job order.
   - Message Bus acts as the decoupled delivery system for job orders and raw materials.
   - Connectors are specialists that fetch raw materials from external sources.
   - Processing Workers are generic laborers that turn raw materials into finished, searchable products.
   - Database is the final warehouse where the finished products are stored, ready for retrieval.