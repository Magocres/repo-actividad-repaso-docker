import os
import psycopg


def check_database_connection():
    database_url = os.getenv("DATABASE_URL")

    try:
        with psycopg.connect(database_url) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT version();")
                db_version = cur.fetchone()

                print("¡Conexión establecida con éxito a PostgreSQL!")
                print(f"Versión del servidor: {db_version[0]}")

    except Exception as e:
        print(f"Error: {e}")
        
