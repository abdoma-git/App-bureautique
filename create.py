
import sqlite3

# Step 2: Establish a connection to the SQLite database (or create one if it doesn't exist)
conn = sqlite3.connect('db2')

# Step 3: Create a cursor object to interact with the database
cursor = conn.cursor()

# Step 4: Execute the SQL query to create the "match" table
create_table_query = '''
CREATE TABLE IF NOT EXISTS match (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    team1 TEXT,
    team2 TEXT,
    date_debut TEXT,
    date_fin TEXT,
    status TEXT,
    cote1 TEXT,
    cote2 TEXT,
    commentaires TEXT
);
'''
cursor.execute(create_table_query)

conn.commit()

conn.close()