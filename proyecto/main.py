import os
import psycopg


query = """
CREATE TABLE characters (
    id              INTEGER PRIMARY KEY,
    name            TEXT NOT NULL,
    status          TEXT,
    species         TEXT,
    type            TEXT,
    gender          TEXT,
    origin_name     TEXT,
    location_name   TEXT,
    image           TEXT,
    url             TEXT,
    created         TIMESTAMPTZ
);
"""

def check_database_connection():
    database_url = os.getenv("DATABASE_URL")

    try:
        with psycopg.connect(database_url) as conn:
            with conn.cursor() as cur:
                cur.execute(query) # AQUI VA LA QUERY
                db_version = cur.fetchone()

                print("¡Conexión establecida con éxito a PostgreSQL!")
                print(f"Versión del servidor: {db_version[0]}")

    except Exception as e:
        print(f"Error: {e}")
        
