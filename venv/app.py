# app.py
from flask import Flask
from flask_cors import CORS
from routes import job_routes  # Import the routes from routes.py

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Register the routes blueprint
app.register_blueprint(job_routes)

if __name__ == "__main__":
    app.run(debug=True)  # Runs the Flask app in debug mode
