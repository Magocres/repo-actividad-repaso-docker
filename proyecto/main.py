import os
import psycopg


query_create_table = """
CREATE TABLE IF NOT EXISTS characters (
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
    'Earth (C-137)', 
    'Citadel of Ricks', 
    'https://rickandmortyapi.com/api/character/avatar/2.jpeg', 
    'https://rickandmortyapi.com/api/character/2', 
    '2017-11-04T18:48:46.250Z'
),
(
    3, 
    'Summer Smith', 
    'Alive', 
    'Human', 
    '', 
    'Female', 
    'Earth (C-137)', 
    'Earth (Replacement Dimension)', 
    'https://rickandmortyapi.com/api/character/avatar/3.jpeg', 
    'https://rickandmortyapi.com/api/character/3', 
    '2017-11-04T18:48:46.250Z'
),
(
    4, 
    'Beth Smith', 
    'Alive', 
    'Human', 
    '', 
    'Female', 
    'Earth (C-137)', 
    'Earth (Replacement Dimension)', 
    'https://rickandmortyapi.com/api/character/avatar/4.jpeg', 
    'https://rickandmortyapi.com/api/character/4', 
    '2017-11-04T18:48:46.250Z'
),
(
    5, 
    'Jerry Smith', 
    'Alive', 
    'Human', 
    '', 
    'Male', 
    'Earth (C-137)', 
    'Earth (Replacement Dimension)', 
    'https://rickandmortyapi.com/api/character/avatar/5.jpeg', 
    'https://rickandmortyapi.com/api/character/5', 
    '2017-11-04T18:48:46.250Z'
),
(
    6, 
    'Abadango Cluster Princess', 
    'Alive', 
    'Alien', 
    '', 
    'Female', 
    'Abadango', 
    'Abadango', 
    'https://rickandmortyapi.com/api/character/avatar/6.jpeg', 
    'https://rickandmortyapi.com/api/character/6', 
    '2017-11-04T19:26:56.301Z'
),
(
    7, 
    'Abradolf Lincler', 
    'Dead', 
    'Human', 
    'Genetic experiment', 
    'Male', 
    'Earth (C-137)', 
    'Testicle Monster Dimension', 
    'https://rickandmortyapi.com/api/character/avatar/7.jpeg', 
    'https://rickandmortyapi.com/api/character/7', 
    '2017-11-04T19:26:56.301Z'
),
(
    8, 
    'Adjudicator Rick', 
    'Dead', 
    'Human', 
    '', 
    'Male', 
    'unknown', 
    'Citadel of Ricks', 
    'https://rickandmortyapi.com/api/character/avatar/8.jpeg', 
    'https://rickandmortyapi.com/api/character/8', 
    '2017-11-04T19:29:56.745Z'
),
(
    9, 
    'Agency Director', 
    'Dead', 
    'Human', 
    '', 
    'Male', 
    'Earth (C-137)', 
    'Earth (C-137)', 
    'https://rickandmortyapi.com/api/character/avatar/9.jpeg', 
    'https://rickandmortyapi.com/api/character/9', 
    '2017-11-04T19:30:31.940Z'
),
(
    10, 
    'Alan Rails', 
    'Dead', 
    'Human', 
    'Superhuman (Ghost trainsinda power)', 
    'Male', 
    'unknown', 
    'Worldender''s lair',
    'https://rickandmortyapi.com/api/character/avatar/10.jpeg',
    'https://rickandmortyapi.com/api/character/10',
    '2017-11-04T19:31:30.419Z'
)
ON CONFLICT (id) DO NOTHING
RETURNING id, name;
"""

query_select_first_ten = """
SELECT id, name, species
FROM characters
ORDER BY id
LIMIT 10;
"""

query_count = """
SELECT COUNT(*) FROM characters;
"""

query_delete_table = """
DROP TABLE IF EXISTS characters;
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
                inserted = cur.fetchall()

                print(f"Inserciones realizadas: {len(inserted)}")
                for character_id, name in inserted:
                    print(f"  - id={character_id}, name={name}")

                cur.execute(query_select_first_ten)
                rows = cur.fetchall()
                print("Primeros 10 personajes:")
                for character_id, name, species in rows:
                    print(f"  - id={character_id}, name={name}, species={species}")

                cur.execute(query_count)
                total = cur.fetchone()[0]
                print(f"Total de personajes guardados: {total}")
    except Exception as e:
        print(f"Error: {e}")

check_database_connection()