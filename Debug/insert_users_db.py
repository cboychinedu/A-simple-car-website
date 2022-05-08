#!/usr/bin/env python3 

# Importing the necessary modules 
import sqlite3 

# Making a connection 
conn = sqlite3.connect("database.db"); 
cursor = conn.cursor()
print("Connected to Sqlite3 successfully")

# Creating the cursor object 
sql_statement = """
    INSERT INTO users (
        USERNAME, EMAIL_ADDRESS, PASSWORD_HASH
        ) VALUES (?, ?, ?)
"""; 
# cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
# Insert the data 
data_tuple = ("cmbonu", "cboy.chinedu@gmail.com", "4edudieiieei")

# Saving the data 
cursor.execute(sql_statement, data_tuple)
conn.commit(); 