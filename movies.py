import sqlite3

conn = sqlite3.connect('movies.db')

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

cursor.execute("SELECT * FROM movies")
print(cursor.fetchall)

conn.commit()

conn.close()