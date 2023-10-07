import sqlite3
conn = sqlite3.connect("logindetails.db")

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL       
)            
""")

conn.commit()
