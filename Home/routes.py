#!/usr/bin/env python3 

# Importing the necessary modules 
import os
import sqlite3
import bcrypt 
from base64 import b64encode
from flask import request 
from flask import Blueprint 
from datetime import datetime 
from flask import session, flash
from flask import render_template, redirect, url_for 

# Creating the blueprint object 
home = Blueprint('home', __name__, template_folder="templates", static_folder="static"); 

# Getting the path to the database 
db_path = os.path.sep.join(["Database", "database.db"])

# Creating a function for reading images 
def convertToBinaryData(file_path):
    # Execute the block of code below to read images 
    with open(file_path, 'rb') as file:
        blobData = file.read()
    
    # Return the blob data 
    return blobData; 


# Creating the home page 
@home.route("/", methods=["GET"])
def HomePage():
    # Checking if the user is logged in 
    if "email" in session:
        # Execute the block below if the user is logged in 
        return render_template("home.html")
    
    else:
        # Creating the home page for the cars route 
        return render_template("index.html")

# Creating the sign in route 
@home.route('/signin', methods=["GET", "POST"])
def SignIn():
    # Checking the request 
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Verify the user on sqlite database, connecting to into the 
        # database to pull out the hash value 
        conn = sqlite3.connect(db_path)

        # Extracting the emails only from the users table
        sql_statement = """
            SELECT PASSWORD_HASH FROM users WHERE EMAIL_ADDRESS=?
        """; 
        cursor = conn.execute(sql_statement, (email,))
        result = cursor.fetchall(); 

        # If the user exists, execute this block of code below. 
        if result:
            # If the user with the email address is present, verify the hash value 
            for pass_hash in result[0]:
                # Converting the pass_hash, and the password into a byte type. 
                # pass_hash = pass_hash.encode("utf-8") 
                password = password.encode("utf-8")

                # Checking if the password is correct. 
                condition = bcrypt.checkpw(password, pass_hash);
                

                # if the conditions is True, add a new session for the user 
            if condition == True:
                # 
                session["email"] = email
                return redirect(url_for("home.UserHome")) 

            
            # if the condition is False
            if condition is False:
                # 
                flash("The email address or password is incorrect!", "info")
                return render_template("signin.html") 


    elif request.method == "GET":
        # Checking if the user is loggen in firstly 
        if "email" in session:
            return redirect(url_for("home.UserHome"))

        # Else, if the user is not logged in, execute the block of 
        # code below 
        return render_template("signin.html")

# Creating a route for the user home 
@home.route("/user_home", methods=["GET", "POST"])
def UserHome():
    # This route can only be accessed by the logged in users 
    if "email" in session:
        email = session["email"]

        # If the request is a post request 
        if request.method == "POST":
            # Verify the user on sqlite database, by connecting to into the 
            # database to pull out the hash value 
            conn = sqlite3.connect(db_path)

            # Extracting the emails only from the users table
            sql_statement = """
                SELECT USERNAME FROM users WHERE EMAIL_ADDRESS=?
            """; 
            cursor = conn.execute(sql_statement, (email,))
            result = cursor.fetchall();

            # 
            for name in result[0]:
                name = name

            # executet the block of code if the request is a post request, read the values, and 
            # save them into the data 
            username = request.form.get("username")
            email = request.form.get("email-value") 
            date = request.form.get("date")
            car_name = request.form.get("car-name")
            car_model = request.form.get("car-model")
            car_description = request.form.get("car-description")
            car_price = request.form.get('car-price')
            version_number = request.form.get("version-number")

            # Working with files 
            file = request.files['image_file']

            # Using a try catch block for the image check 
            try:
                # Getting the file exetensions 
                file_extensions =  ["JPG","JPEG","PNG","GIF"]
                uploaded_file_extension = file.filename.split(".")[-1]

                # If the file uploaded was an image file
                if (uploaded_file_extension.upper() in file_extensions):
                    # Getting the current date 
                    now = datetime.now()
                    dt_string = now.strftime("%d-%m-%Y-%H:%M:%S")
                    image_path= f"static/Uploads/{dt_string}.jpg"
                    file.save(image_path) 
                    image_path= f"/static/Uploads/{dt_string}.jpg"

                    # # Saving into the database 
                    # image_data = convertToBinaryData(destination_path)
                    # Connecting into the database 
                    conn = sqlite3.connect(db_path)
                    cursor = conn.cursor()

                    # 
                    sql_statement = """
                        INSERT INTO cars (
                            USERNAME, EMAIL_ADDRESS, DATE, CAR_NAME, MODEL, VERSION_NUMBER, 
                            CAR_DESCRIPTION, CAR_PRICE, IMAGE_PATH
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?) 
                    """; 

                    # insert the data 
                    data_tuple = (
                        username, email, date, car_name, car_model, 
                        version_number, car_description, car_price, image_path
                        )

                    # saving the data 
                    cursor.execute(sql_statement, data_tuple)
                    conn.commit() 

                    # Saving the data 
                    flash("Data Saved!")
                    return render_template('userHome.html', username=name)

                # If the image was not an image file 
                else:
                    flash("only images are accepted")
                    return render_template('userHome.html', username=name)
            # Except 
            except Exception as e:
                # 
                flash("Only images are accepted")
                return render_template('userHome.html', username=name)

        # If the request is a get request, execute the block of code 
        # below. 
        else:
            # Verify the user on sqlite database, by connecting to into the 
            # database to pull out the hash value 
            conn = sqlite3.connect(db_path)

            # Extracting the emails only from the users table
            sql_statement = """
                SELECT USERNAME FROM users WHERE EMAIL_ADDRESS=?
            """; 
            cursor = conn.execute(sql_statement, (email,))
            result = cursor.fetchall();

            # 
            for name in result[0]:
                name = name

            # Return the home user 
            return render_template("userHome.html", username=name); 

    
    # If the user is not logged in, redirect the user to the sign page 
    else:
        return redirect(url_for("home.SignIn"))

# Creating the sign up route 
@home.route("/signup", methods=["GET", "POST"])
def SignUp():
    # Checking if the request is a post request 
    if request.method == "POST":
        # execute the block of code below for a post request, and register 
        # the user 
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        # Verify if the email is registered on the database
        # Making a connection to the sql database 
        conn = sqlite3.connect(db_path)

        # Extracting the emails only from the users table
        sql_statement = """
            SELECT EMAIL_ADDRESS FROM users WHERE EMAIL_ADDRESS=?
        """; 
        cursor = conn.execute(sql_statement, (email,))
        result = cursor.fetchall(); 

        # If the user exists, execute this block of code below. 
        if result:
            flash("The user with the email address is already registered!", "info")
            return render_template("signup.html") 
            

        # If the user is not registered, register the user and redirect the 
        # user to a login page. 
        else:
            # Register the user convert the user password into an encoded data string 
            # of type "UTF-8" encoding, hash the password, and save the value 
            # inside the database 
            password = password.encode("utf-8")
            password = bcrypt.hashpw(password, bcrypt.gensalt(5)); 

            # Save the hash file into the database 
            sql_statement = """
                INSERT INTO users (
                    USERNAME, EMAIL_ADDRESS, PASSWORD_HASH
                ) VALUES (?, ?, ?)
            """; 

            # Getting the users data 
            data = (username, email, password)

            # Executing the sql statement, and then save the data 
            cursor.execute(sql_statement, data); 
            conn.commit() 

            # Return the user back to the signin page
            flash("Registered successfully!", "info")
            return redirect(url_for("home.SignIn"))

    # if the request method is a get request, execute the block of code 
    # below 
    if request.method == "GET":
        # Execute the block of code if the request is a get request 
        return render_template("signup.html")

# Creating the sign out route 
@home.route("/signout", methods=["GET", "POST"])
def SignOut():
    session.pop("email", None); 
    return redirect(url_for("home.HomePage"))