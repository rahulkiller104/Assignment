# database.py
import psycopg2

def establish_connection():
    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect("postgres://moviedb_m9w3_user:HykbOxafVKKsPFtdM4ILl3aOGtIr9qcl@dpg-clats4u16hkc7380rv60-a.oregon-postgres.render.com/moviedb_m9w3")
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
