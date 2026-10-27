import psycopg2
import config

conn = psycopg2.connect(
    dbname=config.DB_NAME,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    host=config.DB_HOST,
    port=config.DB_PORT
)

print("Connected to PostgreSQL successfully!")

conn.close()