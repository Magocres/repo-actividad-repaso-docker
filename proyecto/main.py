import os
import psycopg


query_create_table = """
CREATE TABLE characters IF NOT EXISTS (
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

query_insert_data = """
INSERT INTO characters (
    id, name, status, species, type, gender, origin_name, location_name, image, url, created
) VALUES 
(
    1, 
    'Rick Sanchez', 
    'Alive', 
    'Human', 
    '', 
    'Male', 
    'Earth (C-137)', 
    'Citadel of Ricks', 
    'https://rickandmortyapi.com/api/character/avatar/1.jpeg', 
    'https://rickandmortyapi.com/api/character/1', 
    '2017-11-04T18:48:46.250Z'
),
(
    2, 
    'Morty Smith', 
    'Alive', 
    'Human', 
    '', 
    'Male', 
    'unknown', 
    'Citadel of Ricks', 
    'https://rickandmortyapi.com/api/character/avatar/2.jpeg', 
    'https://rickandmortyapi.com/api/character/2', 
    '2017-11-04T18:48:46.250Z'
);
"""

def check_database_connection():
    database_url = os.getenv("DATABASE_URL")

    try:
        with psycopg.connect(database_url) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT version();")
                db_version = cur.fetchone()
                print("¡Conexión establecida con éxito a PostgreSQL!")
                print(f"Versión del servidor: {db_version[0]}")

                cur.execute(query_create_table)
                cur.execute(query_insert_data)
    except Exception as e:
        print(f"Error: {e}")

check_database_connection()