import pandas as pd
from database import execute_query,establish_connection

def read_csv(file_path):
    return pd.read_csv(file_path)

def format_value(value):
    return str(value).replace("'", "''")

def generate_movie_insert_queries(df_movie):
    formatted_rows = []
    formatted_row_movie_genres = []

    for _, row in df_movie.iterrows():
        formatted_row = "({}, '{}', {}, '{}', '{}', {}, '{}')".format(
            row['id'],
            format_value(row['title']),
            row['year'],
            format_value(row['country']),
            format_value(row['director']),
            row['minutes'],
            format_value(row['poster'])
        )
        formatted_rows.append(formatted_row)

        for genre in str(row['genre']).split(","):
            formatted_row_movie_genre = "({}, '{}')".format(
                row['id'],
                format_value(genre)
            )
            formatted_row_movie_genres.append(formatted_row_movie_genre)

    insert_movie_genre_query = "INSERT INTO MovieGenre (movie_id, genre) VALUES {}".format(', '.join(formatted_row_movie_genres))
    
    insert_query_movie = "INSERT INTO Movie (id, title, year, country, director, minutes, poster) VALUES {}".format(', '.join(formatted_rows))

    return insert_query_movie, insert_movie_genre_query

def generate_rating_insert_query(df_rating):
    formatted_rows = ["({}, {}, {}, {})".format(
        row['rater_id'], row['movie_id'], row['rating'], row['time']
    ) for _, row in df_rating.iterrows()]
    return "INSERT INTO Rating (rater_id, movie_id, rating, time) VALUES {}".format(', '.join(formatted_rows))

def create_table_query(table_name, columns):
    return """
    CREATE TABLE IF NOT EXISTS {} (
        {}
    );
    """.format(table_name, ', '.join(columns))


def fetch_and_print_data(cursor, query, message):
    cursor.execute(query)
    data = cursor.fetchall()
    print(f"\n{message}:")
    for row in data:
        print(row)

def generate_drop_table_query():
    return """
    DROP TABLE IF EXISTS Movie;
    DROP TABLE IF EXISTS Rating;
    DROP TABLE IF EXISTS MovieGenre;
    """

def create_table_and_insert_csv(cursor):
    csv_file_path_movie = 'data/movies.csv'
    csv_file_path_rating = 'data/ratings.csv'

    df_movie = read_csv(csv_file_path_movie)
    df_rating = read_csv(csv_file_path_rating)

    execute_query(cursor, generate_drop_table_query())
    print("Tables dropped....")

    # Execute the SQL statements to create tables
    execute_query(cursor, create_table_query("Movie", ["id SERIAL PRIMARY KEY", "title VARCHAR(2000)", "year INTEGER", "country VARCHAR(2000)", "director VARCHAR(2000)", "minutes INTEGER", "poster VARCHAR(2000)"]))
    execute_query(cursor, create_table_query("Rating", ["rater_id INTEGER", "movie_id INTEGER", "rating INTEGER", "time INTEGER"]))
    execute_query(cursor, create_table_query("MovieGenre", ["movie_id INTEGER", "genre VARCHAR(250)"]))

    # Generate insert queries
    insert_query_movie, insert_movie_genre_query = generate_movie_insert_queries(df_movie)
    insert_query_rating = generate_rating_insert_query(df_rating)
   
    # Insert data from csv file
    execute_query(cursor, insert_query_movie)
    execute_query(cursor, insert_query_rating)
    execute_query(cursor, insert_movie_genre_query)

def main():
    connection = establish_connection()

    if connection:
        try:
            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # create table and insert data
            create_table_and_insert_csv(cursor)

            # Commit the changes to the database
            connection.commit()

            # Fetch and print movie data
            fetch_and_print_data(cursor, "SELECT * FROM Movie;", "Movie Data")

            # Fetch and print rating data
            fetch_and_print_data(cursor, "SELECT * FROM Rating;", "Rating Data")

        except Exception as e:
            print("Something went wrong!")
            print(e)


if __name__ == "__main__":
    main()
