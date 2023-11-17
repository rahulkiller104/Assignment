# database.py
import psycopg2

def establish_connection():
    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect("your_database_connection_string")
        return connection
    except psycopg2.Error as e:
        print("Error connecting to the PostgreSQL database:", e)
        return None

def execute_query(cursor, query):
    try:
        # Execute the query
        cursor.execute(query)
        # Fetch and return the results
        return cursor.fetchall()
    except psycopg2.Error as e:
        print("Error executing query:", e)
