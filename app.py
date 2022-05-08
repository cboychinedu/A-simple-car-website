#!/usr/bin/env python3 

#!/usr/bin/env python3 

# importing the necessary modules 
import os 
import logging
from flask import Flask, url_for, session  
from flask_cors import CORS
from datetime import timedelta

# Importing the views 
from Home.routes import home 
from Cars.routes import cars 

# Creating the flask application 
app = Flask(__name__) 
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = "kdsd8*DEKFE!@$#$$REDKDNI*(KEHE&E&^^$D"
app.permanent_session_lifetime = timedelta(days=24)

#
CORS(app)

# Register the views using the "app.register" function 
app.register_blueprint(home, url_prefix="/")
app.register_blueprint(cars, url_prefix="/api")


# Logging the configurations to a file on disk 
logging.basicConfig(filename="requests.log", level=logging.DEBUG,
                        format='%(asctime)s %(message)s %(filename)s %(module)s %(pathname)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')

# Handling custom error pages
@app.errorhandler(404)
def page_not_found(e):
    # Execute this route if the user navigates to a route that does not exist
    # return render_template('404.html'), 404;
    return "Error 404", 404; 

# Handling error request 500
@app.errorhandler(500)
def internal_server_error(e):
    # Execute this route if the request generated gives an internal server error
    # return render_template('500.html'), 500;
    return "Bad Request, try again", 500; 

# Setting the session timeout
# @app.before_request
# def make_session_permanent():
#     session.permanent = True
#     app.permanent_session_lifetime = timedelta(days=24)

# Adding functions for updating the web application on reload
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

# Creating a function called dated url for tracking the changes made
def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


# Running the flask application 
if __name__ == "__main__":
    app.run(port=5001, 
            host="localhost",
            debug=True)