#!/usr/bin/python3
"""
Web server 
"""
from api.v1.views import app_views
from flask import Flask, jsonify, make_response

app = Flask(__name__)

# Define the route for the status
@app.route('/api/v1/status', methods=['GET'])
def get_status():
    return jsonify({"status": "API is up and running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
