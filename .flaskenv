# The .flaskenv file is used to set environment variables specifically for Flask applications when using the Flask development server

# Set the flask_app to main, so the application will find and run from main.py. It is the entry point of my application.
FLASK_APP=main

# When this variable is set to 1, it enables the Flask debugger. Flask debugger is a useful tool that helps debug and diagnose errors
# development via error messages and traceback. 
FLASK_DEBUG=1

# Sets the port to 8080, so that localhost will run on port 8080.
FLASK_RUN_PORT=8080