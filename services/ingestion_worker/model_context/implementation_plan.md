## Phase 1: Infrastructure and Environment Setup

  This phase focuses on creating the container definitions and basic files needed to run the service.


   1. ✅ Create `docker-compose.yml` at Project Root: Create a docker-compose.yml file in the root directory of the tierzero project. This file
      will define the RabbitMQ message bus and the new ingestion worker service.
       * Action: Create the file and add the rabbitmq service definition exactly as described in queue_architecture.md. Also, add a skeleton
         definition for the ingestion-worker service.


   2. ✅ Create the Worker's `Dockerfile`: Inside the services/ingestion_worker/ directory, create a file named Dockerfile.
       * Action: This file will define the container for our worker. It should:
           * Start from a Python base image (e.g., python:3.11-slim).
           * Set a working directory.
           * Copy the worker's requirements.txt file.
           * Install the Python dependencies.
           * Copy the rest of the worker's source code.
           * Define the command to run the worker script.


   3. ✅ Create the Worker's `requirements.txt`: Inside services/ingestion_worker/, create a requirements.txt file.
       * Action: Add the necessary Python libraries. To start, this will be:

   1         pika
   2         pydantic



   4. ✅ Create the Worker's Source Directory: Inside services/ingestion_worker/, create a src directory to hold the Python source code, keeping
      the project organized.

  ## Phase 2: Worker Application Logic

  This phase focuses on writing the Python code for the worker itself.


   5. ✅ Create the Main Application File: Inside services/ingestion_worker/src/, create a main.py file. This will be the entry point for the
      worker.


   6. ✅ Implement the RabbitMQ Consumer: In main.py, write the boilerplate code to:
       * Connect to the RabbitMQ server using the pika library.
       * Declare the queue it will listen to (e.g., content.raw.received, as per the workflow).
       * Set up a consumer to listen for messages on this queue.


   7. ✅ Define the Message Data Model: Inside services/ingestion_worker/src/, create a models.py file.
       * Action: Copy the CrawledContentMessage Pydantic model from the documentation into this file. The worker will use this to validate
         and parse incoming messages from the queue.


   8. ✅ Implement the Core Processing Callback: In main.py, create the callback function that the pika consumer will execute for each message.
      This function is the "Assembly Line" from your workflow document.
       * Action: Inside this function, implement the following logic:
          a.  Parse the message body using the CrawledContentMessage model.
          b.  (Placeholder) Add a function call for chunk_content().
          c.  (Placeholder) Add a function call for generate_embeddings().
          d.  (Placeholder) Add a function call for save_to_database().
          e.  Implement message acknowledgment (ack) to properly remove the message from the queue after it has been processed.

  ## Phase 3: Configuration and Finalization

  This phase connects everything together.


   9. ✅ Add a Configuration Module: Inside services/ingestion_worker/src/, create a config.py file.
       * Action: Use this file to load settings from environment variables (e.g., RABBITMQ_URL, DATABASE_URL). This keeps credentials and
         settings out of the source code.


   10. ✅ Finalize `docker-compose.yml`: Update the ingestion-worker service definition in the root docker-compose.yml file.
       * Action:
           * Set the build context to point to the services/ingestion_worker directory.
           * Add a depends_on clause to ensure RabbitMQ starts before the worker.
           * Pass the required environment variables (like RABBITMQ_URL) to the worker container, as shown in the architecture sketch.
