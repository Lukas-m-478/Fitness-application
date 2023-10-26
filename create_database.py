#sqlite3 was learned from https://www.youtube.com/watch?v=pd-0G0MigUA&t=706s
#import sql library
import sqlite3
#creates database
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
cur.execute("INSERT INTO upper_body_exercises (exercise) VALUES (?)", ("bicep curls",))
cur.execute("INSERT INTO upper_body_exercises (exercise) VALUES (?)", ("hammer curls",))
cur.execute("INSERT INTO upper_body_exercises (exercise) VALUES (?)", ("preacher curls",))
cur.execute("INSERT INTO upper_body_exercises (exercise) VALUES (?)", ("barbell curls",))
cur.execute("INSERT INTO upper_body_exercises (exercise) VALUES (?)", ("lateral raise",))
cur.execute("INSERT INTO upper_body_exercises (exercise) VALUES (?)", ("tricep extensions",))
cur.execute("INSERT INTO upper_body_exercises (exercise) VALUES (?)", ("rear delts",))

#insert lower body exercises
cur.execute("INSERT INTO lower_body_exercises (exercise) VALUES (?)", ("leg extensions",))
cur.execute("INSERT INTO lower_body_exercises (exercise) VALUES (?)", ("leg curls",))
cur.execute("INSERT INTO lower_body_exercises (exercise) VALUES (?)", ("calf raises",))

#insert compound exercises
cur.execute("INSERT INTO compound_exercises (exercise) VALUES (?)", ("pull ups",))
cur.execute("INSERT INTO compound_exercises (exercise) VALUES (?)", ("dips",))
cur.execute("INSERT INTO compound_exercises (exercise) VALUES (?)", ("squats",))
cur.execute("INSERT INTO compound_exercises (exercise) VALUES (?)", ("deadlift",))
cur.execute("INSERT INTO compound_exercises (exercise) VALUES (?)", ("bench press",))
cur.execute("INSERT INTO compound_exercises (exercise) VALUES (?)", ("push ups",))
cur.execute("INSERT INTO compound_exercises (exercise) VALUES (?)", ("shoulder press",))
cur.execute("INSERT INTO compound_exercises (exercise) VALUES (?)", ("lateral pull-down",))
cur.execute("INSERT INTO compound_exercises (exercise) VALUES (?)", ("pec fly",))
cur.execute("INSERT INTO compound_exercises (exercise) VALUES (?)", ("rows",))
cur.execute("INSERT INTO compound_exercises (exercise) VALUES (?)", ("leg press",))
cur.execute("INSERT INTO compound_exercises (exercise) VALUES (?)", ("lunges",))
cur.execute("INSERT INTO compound_exercises (exercise) VALUES (?)", ("burpees",))

#insert cardio exercises
cur.execute("INSERT INTO cardio (exercise) VALUES (?)", ("running",))
cur.execute("INSERT INTO cardio (exercise) VALUES (?)", ("jogging",))
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

#add exercise_day column to upper and lower body exercise tables (it stores "Push", "Pull" or "Legs")
#add exercise_days column and target_muscles column to compound exercise table
cur.execute("ALTER TABLE upper_body_exercises ADD COLUMN exercise_day VARCHAR(255)")
cur.execute("ALTER TABLE lower_body_exercises ADD COLUMN exercise_day VARCHAR(255)")
cur.execute("ALTER TABLE compound_exercises ADD COLUMN exercise_day VARCHAR(255)")
cur.execute("ALTER TABLE compound_exercises ADD COLUMN target_muscles VARCHAR(255)")
cur.execute("ALTER TABLE upper_body_exercises ADD COLUMN target_muscle VARCHAR(255)")
cur.execute("ALTER TABLE lower_body_exercises ADD COLUMN target_muscle VARCHAR(255)")

#add "Push", "Pull" or "Legs" to upper body exercises table to specify what exercise fits where
cur.execute("UPDATE upper_body_exercises SET exercise_day = ? WHERE exercise = ?", ("Pull", "bicep curls"))
cur.execute("UPDATE upper_body_exercises SET exercise_day = ? WHERE exercise = ?", ("Pull", "hammer curls"))
cur.execute("UPDATE upper_body_exercises SET exercise_day = ? WHERE exercise = ?", ("Pull", "preacher curls"))
cur.execute("UPDATE upper_body_exercises SET exercise_day = ? WHERE exercise = ?", ("Pull", "barbell curls"))
cur.execute("UPDATE upper_body_exercises SET exercise_day = ? WHERE exercise = ?", ("Push", "lateral raise"))
cur.execute("UPDATE upper_body_exercises SET exercise_day = ? WHERE exercise = ?", ("Push", "tricep extensions"))
cur.execute("UPDATE upper_body_exercises SET exercise_day = ? WHERE exercise = ?", ("Push", "rear delts"))

#add "Push", "Pull" or "Legs" to lower body exercises table to specify what exercise fits where
cur.execute("UPDATE lower_body_exercises SET exercise_day = ? WHERE exercise = ?", ("Legs", "leg extensions"))
cur.execute("UPDATE lower_body_exercises SET exercise_day = ? WHERE exercise = ?", ("Legs", "leg curls"))
cur.execute("UPDATE lower_body_exercises SET exercise_day = ? WHERE exercise = ?", ("Legs", "calf raises"))

#add "Push", "Pull" or "Legs" to compound exercises table to specify what exercise fits where
cur.execute("UPDATE compound_exercises SET exercise_day = ? WHERE exercise = ?", ("Pull", "pull ups"))
cur.execute("UPDATE compound_exercises SET exercise_day = ? WHERE exercise = ?", ("Push", "dips"))
cur.execute("UPDATE compound_exercises SET exercise_day = ? WHERE exercise = ?", ("Legs", "squats"))
cur.execute("UPDATE compound_exercises SET exercise_day = ? WHERE exercise = ?", ("Legs,Pull", "deadlift"))
cur.execute("UPDATE compound_exercises SET exercise_day = ? WHERE exercise = ?", ("Push", "bench press"))
cur.execute("UPDATE compound_exercises SET exercise_day = ? WHERE exercise = ?", ("Push", "push ups"))
cur.execute("UPDATE compound_exercises SET exercise_day = ? WHERE exercise = ?", ("Push", "shoulder press"))
cur.execute("UPDATE compound_exercises SET exercise_day = ? WHERE exercise = ?", ("Pull", "lateral pull-down"))
cur.execute("UPDATE compound_exercises SET exercise_day = ? WHERE exercise = ?", ("Push", "pec fly"))
cur.execute("UPDATE compound_exercises SET exercise_day = ? WHERE exercise = ?", ("Pull", "rows"))
cur.execute("UPDATE compound_exercises SET exercise_day = ? WHERE exercise = ?", ("Legs", "leg press"))
cur.execute("UPDATE compound_exercises SET exercise_day = ? WHERE exercise = ?", ("Legs", "lunges"))
cur.execute("UPDATE compound_exercises SET exercise_day = ? WHERE exercise = ?", ("Legs,Push", "burpees"))

#add muscle name to target_muscle column in upper body exercise table to specify what muscle each exercise works
cur.execute("UPDATE upper_body_exercises SET target_muscle = ? WHERE exercise = ?", ("biceps", "bicep curls"))
cur.execute("UPDATE upper_body_exercises SET target_muscle = ? WHERE exercise = ?", ("biceps", "hammer curls"))
cur.execute("UPDATE upper_body_exercises SET target_muscle = ? WHERE exercise = ?", ("biceps", "preacher curls"))
cur.execute("UPDATE upper_body_exercises SET target_muscle = ? WHERE exercise = ?", ("biceps", "barbell curls"))
cur.execute("UPDATE upper_body_exercises SET target_muscle = ? WHERE exercise = ?", ("shoulders,traps", "lateral raise"))
cur.execute("UPDATE upper_body_exercises SET target_muscle = ? WHERE exercise = ?", ("triceps", "tricep extensions"))
cur.execute("UPDATE upper_body_exercises SET target_muscle = ? WHERE exercise = ?", ("shoulders", "rear delts"))

#add muscle name to target_muscle column in lower body exercise table to specify what muscle each exercise works
cur.execute("UPDATE lower_body_exercises SET target_muscle = ? WHERE exercise = ?", ("quads", "leg extensions"))
cur.execute("UPDATE lower_body_exercises SET target_muscle = ? WHERE exercise = ?", ("hamstrings", "leg curls"))
cur.execute("UPDATE lower_body_exercises SET target_muscle = ? WHERE exercise = ?", ("calves", "calf raises"))

#add muscle names to target_muscles column in compound exercise table to specify what muscles each exercise works
cur.execute("UPDATE compound_exercises SET target_muscles = ? WHERE exercise = ?", ("back,shoulders,biceps,traps", "pull ups"))
cur.execute("UPDATE compound_exercises SET target_muscles = ? WHERE exercise = ?", ("triceps,chest", "dips"))
cur.execute("UPDATE compound_exercises SET target_muscles = ? WHERE exercise = ?", ("quads,hamstrings,calves,glutes", "squats"))
cur.execute("UPDATE compound_exercises SET target_muscles = ? WHERE exercise = ?", ("hamstrings,back,glutes,traps", "deadlift"))
cur.execute("UPDATE compound_exercises SET target_muscles = ? WHERE exercise = ?", ("chest,shoulders,triceps", "bench press"))
cur.execute("UPDATE compound_exercises SET target_muscles = ? WHERE exercise = ?", ("triceps,chest,shoulders", "push ups"))
cur.execute("UPDATE compound_exercises SET target_muscles = ? WHERE exercise = ?", ("shoulders,triceps,chest", "shoulder press"))
cur.execute("UPDATE compound_exercises SET target_muscles = ? WHERE exercise = ?", ("lats,biceps,shoulders,traps", "lateral pull-down"))
cur.execute("UPDATE compound_exercises SET target_muscles = ? WHERE exercise = ?", ("chest,shoulders,triceps,biceps", "pec fly"))
cur.execute("UPDATE compound_exercises SET target_muscles = ? WHERE exercise = ?", ("lats,shoulders,back,biceps", "rows"))
cur.execute("UPDATE compound_exercises SET target_muscles = ? WHERE exercise = ?", ("quads,glutes,hamstrings,calves", "leg press"))
cur.execute("UPDATE compound_exercises SET target_muscles = ? WHERE exercise = ?", ("glutes,hamstrings,quads,calves", "lunges"))
cur.execute("UPDATE compound_exercises SET target_muscles = ? WHERE exercise = ?", ("chest,triceps,shoulders,quads,hamstrings,glutes,calves", "burpees"))

#execute queries
conn.commit()
