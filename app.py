from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  # SQLite database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

# Define the User model (table)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary Key
    username = db.Column(db.String(80), unique=True, nullable=False)  # Username field
    email = db.Column(db.String(120), unique=True, nullable=False)  # Email field

    def __repr__(self):
        return f'<User {self.username}>'

# Define the Job model (table)
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary Key
    title = db.Column(db.String(200), nullable=False)  # Job title
    description = db.Column(db.Text, nullable=False)  # Job description
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign Key

    user = db.relationship('User', backref='jobs')  # Relationship to User

    def __repr__(self):
        return f'<Job {self.title}>'

# Create the database tables
if __name__ == '__main__':
    with app.app_context():  # Set up an application context
        db.create_all()  # This will create the User and Job tables based on the models

    @app.route('/')
    def home():
        return "Welcome to the Job Listing System!"

    app.run(debug=True)
