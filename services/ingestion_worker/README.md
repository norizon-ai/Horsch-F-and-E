# Ingestion Worker Service

## Overview

The Ingestion Worker is a core component of the tierzero pipeline, responsible for processing raw content received from various connectors. It operates as a consumer, listening to a RabbitMQ queue for incoming messages containing raw data.

Its primary responsibilities, as outlined in the "Assembly Line" phase of the architecture, are:
1.  **Chunking:** Breaking down large documents into smaller, more manageable pieces suitable for semantic search.
2.  **Embedding:** Converting the text chunks into numerical vector representations using an embedding model.
3.  **Storing:** Saving the processed chunks, their embeddings, and associated metadata to the central database.

This service is designed to be highly scalable and generic; it does not need to know the original source of the data it processes.

---

## Development & Testing

Follow these steps to run the worker locally for development and testing.

### 1. Start the Services

The Ingestion Worker and its RabbitMQ message broker are managed via the main `docker-compose.yml` file at the project root.

To build and start the containers, run the following command from the **root of the `tierzero` project**:

```bash
docker-compose up --build
```

This command will:
- Build the `ingestion_worker` Docker image.
- Start the `ingestion_worker` container.
- Start the `rabbitmq` container that it depends on.

You will see logs from the worker indicating it has successfully connected to RabbitMQ and is "waiting for messages".

### 2. Send Test Messages

To test that the worker is consuming messages correctly, you can use the provided publisher script. This script sends three sample messages, formatted according to `src/models.py`, directly to the queue.

First, ensure you have the required Python library installed on your local machine:
```bash
pip install pika
```

Then, in a **new terminal**, run the script from the **project root directory**:
```bash
python services/ingestion_worker/test_scripts/test_publisher.py
```

### 3. Verify the Results

- **Check the Logs:** In your original `docker-compose` terminal, you will see real-time logs from the `ingestion_worker` as it receives, processes (using the placeholder functions), and acknowledges each message.
- **Check RabbitMQ UI:** You can also inspect the queue directly via the RabbitMQ Management UI.
  - **URL:** [http://localhost:15672](http://localhost:15672)
  - **Login:** `guest` / `guest`
  - Navigate to the "Queues" tab. You should see the `content.raw.received` queue. You can click on it to see message rates and consumer details.

---

## Completing the Implementation

The current service contains a fully functional skeleton. To make it production-ready, the placeholder functions in `src/main.py` must be replaced with real implementations.

#### `chunk_content(text)`
- **Goal:** Implement robust text splitting.
- **Recommendation:** Use a library designed for this purpose, such as `langchain.text_splitter.RecursiveCharacterTextSplitter` or the Natural Language Toolkit (`nltk`). Add the chosen library to `requirements.txt`.

#### `generate_embeddings(chunks)`
- **Goal:** Convert text chunks to vector embeddings.
- **Recommendation:**
  - For local embeddings, use a library like `sentence-transformers`. You will need to select a pre-trained model (e.g., `all-MiniLM-L6-v2`).
  - For API-based embeddings, use clients from providers like `openai` or `cohere`.
  - Add the required libraries to `requirements.txt`.

#### `save_to_database(...)`
- **Goal:** Persist the processed data to the PostgreSQL database.
- **Recommendation:**
  - Add a database service (e.g., Postgres) to the root `docker-compose.yml`.
  - Use a robust database library like `SQLAlchemy` (as an ORM) or `psycopg2` (as a driver).
  - Implement the logic to connect to the database using the `DATABASE_URL` from `src/config.py` and insert the data.
  - Add the chosen library to `requirements.txt`.

---

## Configuration

The service is configured via environment variables, which are loaded in `src/config.py`.

- `RABBITMQ_URL`: The connection string for the RabbitMQ server.
- `RAW_CONTENT_QUEUE`: The name of the queue to consume from.
- `DATABASE_URL`: The connection string for the PostgreSQL database.
- `LOG_LEVEL`: The logging level for the application.

These are set in the `docker-compose.yml` file for containerized deployment.
