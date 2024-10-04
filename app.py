import webbrowser
from flask import Flask
from flask_cors import CORS
from routes import job_routes
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import Job  


app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

# Setup SQLAlchemy
db = SQLAlchemy(app)


# Register routes
app.register_blueprint(job_routes)

# Function to run the app
def run_app():
    app.run(debug=True)  # Ensure it's running in debug mode

if __name__ == "__main__":
    # Open the browser first
    webbrowser.open('http://127.0.0.1:5000/jobs')  # Opens in the default web browser
    run_app()  # Start the Flask app
