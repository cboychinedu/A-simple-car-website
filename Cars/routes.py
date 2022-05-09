#!/usr/bin/env python3 

# Importing the necessary modules 
import os 
import sqlite3
from flask import request 
from flask import Blueprint, session
from flask import render_template, redirect, url_for 

# Creating the blueprint object 
cars = Blueprint("cars", __name__, template_folder="templates", static_folder="static"); 

# Getting the path to the database 
db_path = os.path.sep.join(["Database", "database.db"]); 

# Creating the home page route for the cars 
@cars.route("/cars", methods=["GET", "POST"])
def ViewCars():
    list = []
    # Checking if the request is a post request 
    # Checking if the request is a post request 
    if request.method == "POST":
        # Connect to the database and extract all the cars saved 
        conn = sqlite3.connect(db_path)

        # Set up the sqlstatement 
        sql_statement = """
            SELECT * FROM cars
        """;  
        cursor = conn.execute(sql_statement)
        result = cursor.fetchall(); 

        # 
        for values in result:
            list.append(values); 

        # Return the results to the client 
        return {"data": list}

    # Else if the request is a get request
    else:
        # Checking if the user is loggen in 
        if "email" in session:
            # Connect to the database and extract all the cars saved 
            conn = sqlite3.connect(db_path)

            # Set up the sqlstatement 
            sql_statement = """
                SELECT * FROM cars
            """;  
            cursor = conn.execute(sql_statement)
            result = cursor.fetchall();  

            # If the user is logged in redirect the user to the home 
            # view cars page 
      
            return render_template("view_cars_user.html", result=result, var="hello")

        # Else 
        else: 
            # Connect to the database and extract all the cars saved 
            conn = sqlite3.connect(db_path)

            # Set up the sqlstatement 
            sql_statement = """
                SELECT * FROM cars
            """;  
            cursor = conn.execute(sql_statement)
            result = cursor.fetchall(); 
            
            # Creating a route for viewing all the posted cars 
            return render_template("view_cars.html", result=result)

    

# Creating a route for posting cars 
@cars.route("/post_cars", methods=["POST"])
def PostCars():
    # Creating a route for posting cars 
    return "POST CARS"; 


# Creating a route for deleting the cars 
@cars.route("/delete-car", methods=["DELETE"])
def DeleteCars():
    # Get the car name 
    if "email" in session:
        # Execute the block of code below 
        data = request.get_json()
        image_name = data["image_name"]

        # Connecting into the database 
        conn = sqlite3.connect(db_path); 

        # Setting up the sql statement 
        sql_statement = """
            DELETE FROM cars where IMAGE_PATH=?
        """

        # Setting up the full image path 
        full_path = f"/static/Uploads/{image_name}"

        # Delete the specific image file 
        cursor = conn.execute(sql_statement, (full_path, ))
        conn.commit(); 

        # Removing the file 
        os.remove(f"static/Uploads/{image_name}"); 

        # Sending back the status message to the client
        return { "message": "Car Data Deleted." , "status": "success"}

    # If the data was not found
    else:
        # The user is not logged in 
        return {"message": "Cannot delete, when not logged in.", "status": "error" }