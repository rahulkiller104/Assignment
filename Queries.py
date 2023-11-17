from database import establish_connection
from operations import HighestAverageRatingForGenre, TopMovies, TopRatedMovies, TopRaters, countHighRatedMovies, countUniqueRaters, favoriateGenre, secondHighestActionYear


if __name__ == "__main__":
    connection = establish_connection()

    while True:
        print("\nOptions Menu:")
        print("a. Top 5 Movie Titles:")
        print("   Sort and print the top 5 movie titles based on the following criteria:")
        print("   - Duration")
        print("   - Year of Release")
        print("   - Average rating (consider movies with minimum 5 ratings)")
        print("   - Number of ratings given")

        print("b. Number of Unique Raters:")
        print("   Determine and print the count of unique rater IDs.")

        print("c. Top 5 Rater IDs:")
        print("   Sort and print the top 5 rater IDs based on:")
        print("   - Most movies rated")
        print("   - Highest Average rating given (consider raters with min 5 ratings)")

        print("d. Top Rated Movie:")
        print("   Find and print the top-rated movies by:")
        print("   - Director 'Michael Bay'")
        print("   - 'Comedy'")
        print("   - In the year 2013")
        print("   - In India (consider movies with a minimum of 5 ratings).")

        print("e. Favorite Movie Genre of Rater ID 1040:")
        print("   Determine and print the favorite movie genre for the rater with ID 1040.")
        
        print("f. Highest Average Rating for a Movie Genre by Rater ID 1040:")
        print("   Find and print the highest average rating for a movie genre given by the rater with ID 1040.")
        
        print("g. Year with Second-Highest Number of Action Movies:")
        print("   Identify and print the year with the second-highest number of action movies from the USA that received an average rating of 6.5 or higher and had a runtime of less than 120 minutes.")

        print("h. Count of Movies with High Ratings:")
        print("   Count and print the number of movies that have received at least five reviews with a rating of 7 or higher.")

        print("x. Exit")

        option = input("Enter option: ").lower()

        if option == 'a':
            TopMovies(connection)
        elif option == 'b':
            countUniqueRaters(connection)
        elif option == 'c':
            TopRaters(connection)
        elif option == 'd':
            TopRatedMovies(connection)
        elif option == 'e':
            favoriateGenre(connection)
        elif option == 'f':
            HighestAverageRatingForGenre(connection)
        elif option == 'g':
            secondHighestActionYear(connection)
        elif option == 'h':
            countHighRatedMovies(connection)
        elif option == 'x':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please choose a valid option (a, b, c, d, e, f, g, h, x).")



