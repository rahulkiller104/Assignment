# Movie Database Query Tool

This project is a Python-based tool for querying and analyzing a movie database stored in a PostgreSQL database. The tool allows users to perform various queries and retrieve information about movies, raters, and ratings.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- PostgreSQL


## Setup

1. Clone the repository:
2. Navigate to the project directory:

    ```bash
    cd Assignment
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the PostgreSQL database:
    - Create a database and update the connection string in `database.py` with your database credentials.

5. Run the main script to create the table and upload the data:

    ```bash
    python main.py
    ```
    Queries.py is using the function defined in Operations.py.
    ```bash
    python Queries.py
    ```
## Usage

1. Upon running `Query.py`, you will see an options menu with various query functionalities.

2. Choose an option by entering the corresponding letter:
    - `a`: Top 5 Movie Titles
    - `b`: Number of Unique Raters
    - `c`: Top 5 Rater IDs
    - `d`: Top Rated Movies
    - `e`: Favorite Movie Genre of Rater ID 1040
    - `f`: Highest Average Rating for a Movie Genre by Rater ID 1040
    - `g`: Year with Second-Highest Number of Action Movies
    - `h`: Count of Movies with High Ratings
    - `x`: Exit

3. Follow the on-screen instructions to interact with the tool.



