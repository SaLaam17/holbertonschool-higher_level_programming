#!/usr/bin/env python3
"""

"""

from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)

users = {"jane": {
        "username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"
    }, "john": {
        "username": "john", "name": "John", "age": 30, "city": "New York"
    }
    }


@app.route("/")
# Define a route for the root URL (“/”).
def home():
    """
    Function to handle this route (“/”).
    """
    return "<p>Welcome to the Flask API!</p>"


@app.route("/data")
# Define a route for the root URL (“/”).
def get_users():
    """
    Function to handle data route.
    """
    username = list(users.keys())
    return jsonify(username)


@app.route("/status")
# Define a route for the root URL (“/”).
def get_status():
    """
    Function to return status.
    """
    return "<p>OK</p>"


@app.route("/users/<username>")
# Define a dynamic route for the root URL ("/users/<username>").
def get_username_obj(username):
    """
    Function that returns the full object
    corresponding to the provided username
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"})


@app.route("/add_user", methods=['POST'])
def add_user():
    """
    Function that adds new user.
    """
    new_user = request.get_json()
    username = new_user.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    users[username] = new_user
    return jsonify({"message": "User added"}), 201


if __name__ == "__main__":
    app.run()
