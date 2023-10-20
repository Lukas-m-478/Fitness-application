#creates database
import sqlite3
conn = sqlite3.connect("information.db")
cur = conn.cursor()

#create table with login details if it does not exist
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE, -- UNIQUE constraint
    password VARCHAR(255) NOT NULL       
)            
""")

#create table with upper body exercises if it does not exist
cur.execute("""
CREATE TABLE IF NOT EXISTS upper_body_exercises (
    id INTEGER PRIMARY KEY,
    exercise VARCHAR(255) NOT NULL      
)            
""")

#create table with lower body exercises if it does not exist 
cur.execute("""
CREATE TABLE IF NOT EXISTS lower_body_exercises (
    id INTEGER PRIMARY KEY,
    exercise VARCHAR(255) NOT NULL      
)            
""")

#create table with core exercises if it does not exist 
cur.execute("""
CREATE TABLE IF NOT EXISTS core_exercises (
    id INTEGER PRIMARY KEY,
    exercise VARCHAR(255) NOT NULL      
)            
""")

#create table with compound exercises if it does not exist 
cur.execute("""
CREATE TABLE IF NOT EXISTS compound_exercises (
    id INTEGER PRIMARY KEY,
    exercise VARCHAR(255) NOT NULL      
)            
""")

#create table with cardio exercises if it does not exist 
cur.execute("""
CREATE TABLE IF NOT EXISTS cardio (
    id INTEGER PRIMARY KEY,
    exercise VARCHAR(255) NOT NULL      
)            
""")

#insert upper body exercises
cur.execute("INSERT INTO upper_body_exercises (exercise) VALUES (?)", ("push ups",))
cur.execute("INSERT INTO upper_body_exercises (exercise) VALUES (?)", ("bicep curls",))
cur.execute("INSERT INTO upper_body_exercises (exercise) VALUES (?)", ("hammer curls",))
cur.execute("INSERT INTO upper_body_exercises (exercise) VALUES (?)", ("preacher curls",))
cur.execute("INSERT INTO upper_body_exercises (exercise) VALUES (?)", ("barbell curls",))
cur.execute("INSERT INTO upper_body_exercises (exercise) VALUES (?)", ("shoulder press",))
cur.execute("INSERT INTO upper_body_exercises (exercise) VALUES (?)", ("lateral raise",))
cur.execute("INSERT INTO upper_body_exercises (exercise) VALUES (?)", ("lateral pull-down",))
cur.execute("INSERT INTO upper_body_exercises (exercise) VALUES (?)", ("rows",))
cur.execute("INSERT INTO upper_body_exercises (exercise) VALUES (?)", ("tricep extensions",))
cur.execute("INSERT INTO upper_body_exercises (exercise) VALUES (?)", ("rear delts",))
cur.execute("INSERT INTO upper_body_exercises (exercise) VALUES (?)", ("pec fly",))

#insert lower body exercises
cur.execute("INSERT INTO lower_body_exercises (exercise) VALUES (?)", ("leg extensions",))
cur.execute("INSERT INTO lower_body_exercises (exercise) VALUES (?)", ("leg press",))
cur.execute("INSERT INTO lower_body_exercises (exercise) VALUES (?)", ("leg curls",))
cur.execute("INSERT INTO lower_body_exercises (exercise) VALUES (?)", ("lunges",))
cur.execute("INSERT INTO lower_body_exercises (exercise) VALUES (?)", ("calf raises",))

#insert compound exercises
cur.execute("INSERT INTO compound_exercises (exercise) VALUES (?)", ("pull ups",))
cur.execute("INSERT INTO compound_exercises (exercise) VALUES (?)", ("dips",))
cur.execute("INSERT INTO compound_exercises (exercise) VALUES (?)", ("squats",))
cur.execute("INSERT INTO compound_exercises (exercise) VALUES (?)", ("deadlift",))
cur.execute("INSERT INTO compound_exercises (exercise) VALUES (?)", ("bench press",))


#insert cardio exercises
cur.execute("INSERT INTO cardio (exercise) VALUES (?)", ("running",))
cur.execute("INSERT INTO cardio (exercise) VALUES (?)", ("burpees",))
cur.execute("INSERT INTO cardio (exercise) VALUES (?)", ("skipping rope",))
cur.execute("INSERT INTO cardio (exercise) VALUES (?)", ("biking",))
cur.execute("INSERT INTO cardio (exercise) VALUES (?)", ("stairs",))

#insert core exercises
cur.execute("INSERT INTO core_exercises (exercise) VALUES (?)", ("crunches",))
cur.execute("INSERT INTO core_exercises (exercise) VALUES (?)", ("sit ups",))
cur.execute("INSERT INTO core_exercises (exercise) VALUES (?)", ("plank",))
cur.execute("INSERT INTO core_exercises (exercise) VALUES (?)", ("hanging leg raise",))
cur.execute("INSERT INTO core_exercises (exercise) VALUES (?)", ("hollow hold",))

#execute queries
conn.commit()
