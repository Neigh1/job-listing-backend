from .app import app
from .models import db  # Import db from models

# Initialize the database with the Flask app
db.init_app(app)
