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
        print(result); 

        # Return the results to the client 
        return {"data": result[0]}

    # Else if the request is a get request
    else:
        # Checking if the user is loggen in 
        if "email" in session: 
            # If the user is logged in redirect the user to the home 
            # view cars page 
            return render_template("view_cars_user.html")

        # Else 
        else: 
            # Creating a route for viewing all the posted cars 
            return render_template("view_cars.html")

    

# Creating a route for posting cars 
@cars.route("/post_cars", methods=["POST"])
def PostCars():
    # Creating a route for posting cars 
    return "POST CARS"; 

# Creating a route for deleting the cars 
@cars.route("/delete_cars", methods=["DELETE"])
def DeleteCars():
    # Creating a route for deleting cars 
    return "Delete Cars"; 