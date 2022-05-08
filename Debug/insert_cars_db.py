#!/usr/bin/env python3 

# This module wass created for inserting image files into sql database 
# Importing the necessary modules 
import sqlite3 

# Creating a function for reading images 
def convertToBinaryData(file_path):
    # Execute the block of code below to read images 
    with open(file_path, 'rb') as file:
        blobData = file.read()
    
    # Return the blob data 
    return blobData; 



# 
conn = sqlite3.connect("database.db")
cursor = conn.cursor() 
print('Connected to SQlite')

# 
sql_statement = """
    INSERT INTO cars ( 
        USERNAME, EMAIL_ADDRESS, DATE, CAR_NAME, MODEL, VERSION_NUMBER, IMAGE
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
"""; 

#
# insert the data 
blobData = convertToBinaryData("car.jpg")
data_tuple = ("kelvin", "kev@gmail.com", "22-11-1995", "MSH-BMW", "V6", "Mh-876", blobData)

# Saving the data 
cursor.execute(sql_statement, data_tuple)
conn.commit()