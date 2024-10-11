from flask import Flask, jsonify
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
with app.app_context():
    db.create_all()

# API route to fetch all jobs
@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()  # Fetch all jobs from the Job table
    job_list = []
    for job in jobs:
        job_data = {
            'id': job.id,
            'title': job.title,
            'description': job.description,
            'username': job.user.username  # Include user information
        }
        job_list.append(job_data)
    
    return jsonify(job_list)  # Return the jobs as a JSON response

@app.route('/')
def home():
    return "Welcome to the Job Listing System!"

if __name__ == '__main__':
    app.run(debug=True)
