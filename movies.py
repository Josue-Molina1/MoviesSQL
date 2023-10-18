import sqlite3

def create_connection():
    #Connection object
    connect_obj = sqlite3.connect("Movies")
    # Cursor Object 
    cursor_obj = connect_obj.cursor()
    # Create table
    table = """CREATE table MOVIES (
               MOVIE VARCHAR(255), 
               YEAR INT(4),
               GENRE CHARO(25)
             );
            """

print(table)
