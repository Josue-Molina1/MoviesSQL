import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("movie_database.db")

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table to store movies
cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        year INTEGER,
        genre TEXT
    )
''')

# Function that allows me to add movies with a Title, year, and a genre, will add more rows in the future. 
def add_movie(title, year, genre):
    conn = sqlite3.connect("movie_database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO movies (title, year, genre) VALUES (?, ?, ?)", (title, year, genre))
    conn.commit()
    conn.close()

# Function that queries all my movies on the databases, so user can now the ID number and edit more functions. 
def get_movies():
    conn = sqlite3.connect("movie_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies")
    movies = cursor.fetchall()
    conn.close()
    return movies

# Update movie, this will allow user to edit data for when more actions are possible. 
# Future features. Gross Income, Director, Cast, etc. 
def update_movie(movie_id, title, year, genre, rating):
    conn = sqlite3.connect("movie_database.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE movies SET title = ?, director = ?, year = ?, genre = ?, rating = ? WHERE id = ?", (title, year, genre, rating, movie_id))
    conn.commit()
    conn.close()

def add_comment(movie_id, comment):
    conn = sqlite3.connect("movie_database.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE movies SET comment = ? WHERE id = ?", (comment, movie_id))
    conn.commit()
    conn.close()

# Delete a movie from the table movies.
def delete_movie(movie_id):
    conn = sqlite3.connect("movie_database.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
    conn.commit()
    conn.close()


# Menu for future interface. Using functios defined above. 
while True:
    print("Movie Database Menu:")
    print("1. Add Movies Seen")
    print("2. View Movies")
    print("3. Rate Movies")
    print("4. Delete a Movie")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        title = input("Enter the movie title: ")
        year = int(input("Enter the release year: "))
        genre = input("Enter the genre: ")
        add_movie(title, year, genre)
        print("Movie added successfully!")
    
    elif choice == "2":
        movies = get_movies()
        for movie in movies:
            print(movie)
        
        view_movie_id = int(input("Enter the movie ID to add a comment: "))
        
        if view_movie_id in [movie[0] for movie in movies]:
            comment = input("Enter your comment for this movie: ")
            add_comment(view_movie_id, comment)
            print("Comment added successfully!")

        else:
            print("Invalid movie ID. Please try again.")

    
    elif choice == "3":
        movie_id = int(input("Enter the movie ID to update: "))
        title = input("Enter the updated title: ")
        year = int(input("Enter the updated release year: "))
        genre = input("Enter the updated genre: ")
        rating = float(input("Enter the updated rating (1-10): "))
        update_movie(movie_id, title, year, genre, rating)
        print("Movie updated, thanks!")
    
    elif choice == "4":
        movie_id = int(input("Enter the movie ID to delete: "))
        delete_movie(movie_id)
        print("Movie deleted successfully!")

    elif choice == "5":
        print("Exiting the Movie Database. See you later alligator!")
        break



# Commit the changes and close the connection ALWAYS! 
conn.commit()
conn.close()
