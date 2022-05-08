#!/usr/bin/env python3 

# Importing the necessary modules 
import os 
from flask import Blueprint, session
from flask import render_template, redirect, url_for 

# Creating the blueprint object 
cars = Blueprint("cars", __name__, template_folder="templates", static_folder="static"); 

# Creating the home page route for the cars 
@cars.route("/cars", methods=["GET"])
def ViewCars():
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