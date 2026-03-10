
import psycopg2
import json
import random
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))

from config import DATABASE_URL

def insert_mock_data():
    """
    Connects to the database and inserts a mock document and its chunks.
    """
    conn = None
    try:
        print("Connecting to the database...")
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        print("Connection successful.")

        # 1. Create a mock user and source
        cur.execute("INSERT INTO users (email, full_name) VALUES (%s, %s) ON CONFLICT (email) DO NOTHING RETURNING id;",
                    ('mock.user@example.com', 'Mock User'))
        user_id = cur.fetchone()
        if user_id:
            user_id = user_id[0]
        else: # If user already exists, get their ID
            cur.execute("SELECT id FROM users WHERE email = %s;", ('mock.user@example.com',))
            user_id = cur.fetchone()[0]


        cur.execute("INSERT INTO sources (source_type, name) VALUES (%s, %s) ON CONFLICT (name) DO NOTHING RETURNING id;",
                    ('manual', 'Mock Manual Entry'))
        source_id = cur.fetchone()
        if source_id:
            source_id = source_id[0]
        else: # If source already exists, get its ID
            cur.execute("SELECT id FROM sources WHERE name = %s;", ('Mock Manual Entry',))
            source_id = cur.fetchone()[0]


        # 2. Insert a mock document
        source_uri = "mock://manual/entry/1"
        title = "The Ultimate Guide to Mocking Data"
        metadata = {"version": "1.0", "author": "Mock User"}
        cur.execute(
            """
            INSERT INTO documents (source_id, creator_id, source_uri, title, metadata)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (source_uri) DO UPDATE SET title = EXCLUDED.title, updated_at = NOW()
            RETURNING id;
            """,
            (source_id, user_id, source_uri, title, json.dumps(metadata))
        )
        document_id = cur.fetchone()[0]
        print(f"Inserted or updated document with ID: {document_id}")

        # 3. Insert mock document chunks
        chunks = [
            "This is the first chunk of the ultimate guide.",
            "It explains why mocking is essential for robust testing.",
            "The final chunk discusses advanced mocking techniques."
        ]
        # Generate dummy embeddings of the correct dimension (768)
        embeddings = [[random.uniform(-1, 1) for _ in range(768)] for _ in chunks]

        for i, (content, embedding) in enumerate(zip(chunks, embeddings)):
            cur.execute(
                """
                INSERT INTO document_chunks (document_id, content, embedding, chunk_index)
                VALUES (%s, %s, %s, %s);
                """,
                (document_id, content, embedding, i)
            )
        print(f"Inserted {len(chunks)} chunks for document ID: {document_id}")

        # Commit the transaction
        conn.commit()
        print("Successfully inserted mock data.")

    except psycopg2.Error as e:
        print(f"Database error: {e}", file=sys.stderr)
        if conn:
            conn.rollback()
    finally:
        if conn:
            cur.close()
            conn.close()
            print("Database connection closed.")

if __name__ == "__main__":
    insert_mock_data()
