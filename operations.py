from database import execute_query

def top_movies(cursor, criterion, limit=5):

    # Define SQL queries for each criterion
    duration_query = """
    SELECT title, minutes FROM Movie
    ORDER BY minutes DESC
    LIMIT {};
    """.format(limit)

    year_query = """
    SELECT title, year FROM Movie
    ORDER BY year DESC
    LIMIT {};
    """.format(limit)

    avg_rating_query = """
    SELECT m.title,  CAST(ROUND(AVG(r.rating), 2) AS VARCHAR(10)) as avg_rating
    FROM Movie m
    INNER JOIN Rating r ON m.id = r.movie_id
    GROUP BY m.id, m.title
    HAVING COUNT(r.rating) >= 5
    ORDER BY avg_rating DESC
    LIMIT {};
    """.format(limit)

    num_ratings_query = """
    SELECT m.id, m.title, COUNT(r.rating) as num_ratings
    FROM Movie m
    INNER JOIN Rating r ON m.id = r.movie_id
    GROUP BY m.id, m.title
    ORDER BY num_ratings DESC
    LIMIT {};
    """.format(limit)

    # Choose the appropriate query based on the criterion
    if criterion == 'duration':
        query = duration_query
    elif criterion == 'year':
        query = year_query
    elif criterion == 'avg_rating':
        query = avg_rating_query
    elif criterion == 'num_ratings':
        query = num_ratings_query
    else:
        print("Invalid criterion.")
        return

    # Execute the chosen query and fetch results
    results = execute_query(cursor, query)

    # Print the results
    print("\nTop 5 Movies based on {}: ".format(criterion.capitalize()))
    for row in results:
        print(row)


def TopMovies(connection):
    if connection:
        try:
           # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # Get top 5 movies based on duration
            top_movies(cursor, 'duration')

            # # Get top 5 movies based on year of release
            top_movies(cursor, 'year')

            # Get top 5 movies based on average rating (minimum 5 ratings)
            top_movies(cursor, 'avg_rating')

            # Get top 5 movies based on the number of ratings given
            top_movies(cursor, 'num_ratings')

        except Exception as e:
           print("something went wrong in TopMovies!")
           print(e)




def countUniqueRaters(connection):
  try:
    cursor = connection.cursor()
    unique_raters_query = """
            SELECT COUNT(DISTINCT rater_id) FROM Rating;
            """
    results = execute_query(cursor, unique_raters_query)[0][0]
    print("\nNumber of Unique Raters: {}".format(results))
  except Exception as e:
      print("something went wrong in countUniqueRaters!")
      print(e)



def top_raters(cursor, criterion, limit=5):
    # Define SQL queries for each criterion
    most_movies_rated_query = """
    SELECT rater_id, COUNT(movie_id) as num_movies_rated
    FROM Rating
    GROUP BY rater_id
    ORDER BY num_movies_rated DESC
    LIMIT {};
    """.format(limit)

    highest_avg_rating_query = """
    SELECT rater_id, CAST(ROUND(AVG(rating), 2) AS VARCHAR(10)) as avg_rating
    FROM Rating
    GROUP BY rater_id
    HAVING COUNT(rating) >= 5
    ORDER BY avg_rating DESC
    LIMIT {};
    """.format(limit)

    # Choose the appropriate query based on the criterion
    if criterion == 'most_movies_rated':
        query = most_movies_rated_query
    elif criterion == 'highest_avg_rating':
        query = highest_avg_rating_query
    else:
        print("Invalid criterion.")
        return

    # Execute the chosen query and fetch results
    results = execute_query(cursor, query)

    # Print the results
    print("\nTop 5 Raters based on {}: ".format(criterion.capitalize()))
    for row in results:
        print(row)

def TopRaters(connection):
    if connection:
        try:
           # Create a cursor object to execute SQL queries
            cursor = connection.cursor()
            # Get top 5 raters based on most movies rated
            top_raters(cursor, 'most_movies_rated')

            # Get top 5 raters based on highest average rating (minimum 5 ratings)
            top_raters(cursor, 'highest_avg_rating')

        except Exception as e:
            print("something went wrong in TopRaters")
            print(e)


def top_rated_movies(cursor, criterion, limit=5):
    # Define SQL queries for each criterion
    top_rated_by_director_query = """
    SELECT m.id, m.title,  CAST(ROUND(AVG(r.rating), 2) AS VARCHAR(10)) as avg_rating
    FROM Movie m
    INNER JOIN Rating r ON m.id = r.movie_id
    WHERE m.director = 'Michael Bay'
    GROUP BY m.id, m.title
    HAVING COUNT(r.rating) >= 5
    ORDER BY avg_rating DESC
    LIMIT {};
    """.format(limit)

    top_rated_comedy_query = """
    SELECT m.id, m.title,  CAST(ROUND(AVG(r.rating), 2) AS VARCHAR(10)) as avg_rating
    FROM Movie m
    INNER JOIN Rating r ON m.id = r.movie_id
    INNER JOIN MovieGenre mg ON m.id = mg.movie_id
    WHERE mg.genre = 'Comedy'
    GROUP BY m.id, m.title
    HAVING COUNT(r.rating) >= 5
    ORDER BY avg_rating DESC
    LIMIT {};
    """.format(limit)


    top_rated_2013_query = """
    SELECT m.id, m.title,  CAST(ROUND(AVG(r.rating), 2) AS VARCHAR(10)) as avg_rating
    FROM Movie m
    INNER JOIN Rating r ON m.id = r.movie_id
    WHERE m.year = 2013
    GROUP BY m.id, m.title
    HAVING COUNT(r.rating) >= 5
    ORDER BY avg_rating DESC
    LIMIT {};
    """.format(limit)

    top_rated_india_query = """
    SELECT m.id, m.title,  CAST(ROUND(AVG(r.rating), 2) AS VARCHAR(10)) as avg_rating
    FROM Movie m
    INNER JOIN Rating r ON m.id = r.movie_id
    WHERE m.country = 'India'
    GROUP BY m.id, m.title
    HAVING COUNT(r.rating) >= 5
    ORDER BY avg_rating DESC
    LIMIT {};
    """.format(limit)

    # Choose the appropriate query based on the criterion
    if criterion == 'director':
        query = top_rated_by_director_query
    elif criterion == 'comedy':
        query = top_rated_comedy_query
    elif criterion == 'year':
        query = top_rated_2013_query
    elif criterion == 'india':
        query = top_rated_india_query
    else:
        print("Invalid criterion.")
        return

    # Execute the chosen query and fetch results
    results = execute_query(cursor, query)

    # Print the results
    print("\nTop Rated Movies based on {}: ".format(criterion.capitalize()))
    for row in results:
        print(row)


def TopRatedMovies(connection):
    if connection:
        try:
           # Create a cursor object to execute SQL queries
            cursor = connection.cursor()
            # Get top rated movies by director 'Michael Bay'
            top_rated_movies(cursor, 'director')

            # Get top rated comedy movies
            top_rated_movies(cursor, 'comedy')

            # Get top rated movies in the year 2013
            top_rated_movies(cursor, 'year')

            # Get top rated movies in India
            top_rated_movies(cursor, 'india')
        except Exception as e:
            print("somthing went wrong in TopRatedMovies")
            print(e)

def countHighRatedMovies(connection):
       if connection:
        try:
           # Create a cursor object to execute SQL queries
            cursor = connection.cursor()
            # Define SQL query to count movies with at least five reviews and a rating of 7 or higher
            high_rated_movies_query = """
            SELECT COUNT(DISTINCT m.id)
            FROM Movie m
            INNER JOIN Rating r ON m.id = r.movie_id
            WHERE r.rating >= 7
            GROUP BY  m.id
            HAVING COUNT(r.rating) >= 5;
            """

            # Execute the query and fetch results
            result = execute_query(cursor, high_rated_movies_query)

            # Print the result
            if result:
                num_high_rated_movies = result[0][0]
                print("\nNumber of Movies with High Ratings (at least five reviews with a rating of 7 or higher): {}".format(num_high_rated_movies))
            else:
                print("\nNo movies meet the criteria.")
        except Exception as e:
            print(e)


def favoriateGenre(connection):
          # Create a cursor
         cursor = connection.cursor()

         favorite_genre_query = """
            SELECT r.rater_id, mg.genre, COUNT(*) as genre_count
            FROM Rating r
            INNER JOIN MovieGenre mg ON r.movie_id = mg.movie_id
            WHERE r.rater_id = {rater_id}
            GROUP BY r.rater_id, mg.genre
            ORDER BY genre_count DESC
            LIMIT 1;
        """.format(rater_id=1040)
         
         cursor.execute(favorite_genre_query)

         # Fetch the result
         result = cursor.fetchone()

         if result:
            print("Favorite Movie Genre for Rater ID {rater_id}: {genre}".format(rater_id=result[0], genre=result[1]))
         else:
            print("No data found for Rater ID {rater_id}".format(rater_id=1040))

def secondHighestActionYear(connection):
          # Create a cursor
        cursor = connection.cursor()

        # Define the SELECT query
        second_highest_action_year_query = """
            SELECT m.year, COUNT(*) as num_action_movies
            FROM Movie m
            JOIN MovieGenre mg ON m.id = mg.movie_id
            JOIN Rating r ON m.id = r.movie_id
            WHERE mg.genre = 'Action'
                AND m.country = 'USA'
                AND m.minutes < 120
            GROUP BY m.year
            HAVING AVG(r.rating) >= 6.5
            ORDER BY num_action_movies DESC
            LIMIT 2;
        """

        # Execute the query
        cursor.execute(second_highest_action_year_query)

        # Fetch the result
        result = cursor.fetchone()

        if result:
            print("Year with the Second-Highest Number of Action Movies:", result[0])
        else:
            print("No data found meeting the criteria.")

def HighestAverageRatingForGenre(connection):
        # Create a cursor
        cursor = connection.cursor()

        # Define the SELECT query
        highest_avg_rating_for_genre_query = """
            SELECT mg.genre,  CAST(ROUND(AVG(r.rating), 2) AS VARCHAR(10)) as avg_rating
            FROM Rating r
            JOIN MovieGenre mg ON r.movie_id = mg.movie_id
            WHERE r.rater_id = {rater_id}
            GROUP BY mg.genre
            HAVING COUNT(r.rating) >= 5
            ORDER BY avg_rating DESC
            LIMIT 1;
        """.format(rater_id=1040)

        # Execute the query
        cursor.execute(highest_avg_rating_for_genre_query)

        # Fetch the result
        result = cursor.fetchone()

        if result:
            print("Highest Average Rating for a Movie Genre by Rater ID {rater_id}: Genre = {genre}, Average Rating = {avg_rating}".format(
                rater_id=1040, genre=result[0], avg_rating=result[1]))
        else:
            print("No data found meeting the criteria.")

