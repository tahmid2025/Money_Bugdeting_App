import sqlite3

# Connect to the database
conn = sqlite3.connect('Students.db')

# Create a cursor
c = conn.cursor()

# Create the Students table only if it doesn't already exist
c.execute('''CREATE TABLE IF NOT EXISTS Students (
             student_id INTEGER PRIMARY KEY,
             name TEXT,
             surname TEXT, 
             username TEXT, 
             password TEXT
           )''')

# Create the Items table only if it doesn't already exist
c.execute('''CREATE TABLE IF NOT EXISTS Items (
            item_id INTEGER PRIMARY KEY,
            student_id INTEGER,
            month TEXT,
            food REAL,
            household_expenses REAL, 
            travel REAL,
            shopping REAL,
            self_care REAL,
            other REAL,
            FOREIGN KEY (student_id) REFERENCES Students(student_id)  -- Define the foreign key relationship
          )''')



# Commit the changes to the database
conn.commit()