#!/usr/bin/env python3 

# Importing the necessary modules 
import sqlite3 

# making a connection 
conn = sqlite3.connect("database.db"); 
print("Connected to Sqlite3 successfully")

# Creating the cursor object 
sql_statement = """
    SELECT * FROM cars
"""; 
cursor = conn.execute(sql_statement)
result = cursor.fetchall(); 

# 
for value in result:
    print(value); 
    break;  