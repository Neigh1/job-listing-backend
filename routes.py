from flask import Blueprint, jsonify

job_routes = Blueprint('job_routes', __name__)

# Sample route
@job_routes.route('/jobs', methods=['GET'])
def get_jobs():
    return jsonify({"jobs": "This is where jobs will be listed"})
