#!/usr/bin/env python3 

# This Module was created for user posting cars. 
# Fields-- 
# Tablename => cars
# id, date, car_name, model, version_number, image 

# Importing the necessary modules 
import sqlite3 

# 
conn = sqlite3.connect("database.db")

# sql statement 
sql_statement = """
    create table cars(
        USERNAME CHAR(255),
        EMAIL_ADDRESS CHAR(255),
        DATE CHAR(255), 
        CAR_NAME CHAR(255), 
        MODEL CHAR(255), 
        VERSION_NUMBER CHAR(255), 
        CAR_DESCRIPTION CHAR(355),
        CAR_PRICE CHAR(255), 
        IMAGE_PATH CHAR(255)
    ); 
"""

# second statement 
sql_statement2 = """
    CREATE TABLE users (
        USERNAME CHAR(255), 
        EMAIL_ADDRESS CHAR(255), 
        PASSWORD_HASH CHAR(255)
    )
"""; 

# Create the table 
conn.execute(sql_statement); 
conn.execute(sql_statement2); 
conn.commit(); 

# close the connection 
conn.close(); 
