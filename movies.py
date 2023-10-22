import sqlite3
# Connection between python and the database (create a .db file)
conn = sqlite3.connect('movies.db')
# This allows me to execute the statements. 
cursor = conn.cursor()

# cursor.execute("""CREATE TABLE movies(
#                name text,
#                date integer,
#                genre text,
#                rate text,
#                duration integer,
#                overview text, 
#                cast text,
#                revenue integer
#                )""")

# cursor.execute("INSERT INTO movies VALUES ('Whispers of the Heart0, '1995', 'Romance', 'PG', '2', 'Best movie ever', 'Issei Takahashi', '34.9' ')")


# Basic SELECT statement, one line only. 
cursor.execute("SELECT * FROM movies")
print(cursor.fetchall) # Grab everything from that query. 

# I dunno know what this is, I was told to put it there, I'll figure it our. 
conn.commit()

# Important. 
conn.close()

# The Movie Database 

