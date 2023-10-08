#creates database
import sqlite3
conn = sqlite3.connect("information.db")
cur = conn.cursor()

#creates table with login details if it does not exist
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE, -- UNIQUE constraint
    password VARCHAR(255) NOT NULL       
)            
""")

conn.commit()
