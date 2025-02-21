#!/usr/bin/env python3
"""
Module for API Security and Authentication Techniques.

"""

from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1",
              "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1",
               "password": generate_password_hash("password"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    """
    The function receives the username and password sent by the client.
    If the credentials belong to a user,
    then the function should return the user object.
    If the credentials are invalid the function can return None or False.
    """
    if username in users and \
            check_password_hash(users.get(username)["password"], password):
        return username
    else:
        return None


@app.route("/basic-protected", methods=['GET'])
@auth.login_required
def basic_protected():
    """
    Function that checks if the user provides
    valid basic authentication credentials.
    """
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """
    Function that checks if the user provides
    valid JWT authentication credentials.
    """
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    is_logged = verify_password(username, password)

    if is_logged is not None:
        access_token = create_access_token(identity={
            "username": username,
            "role": users[username]["role"]
        })
        return jsonify(access_token=access_token)
    else:
        return "Unauthorized response", 401


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """
    Function that checks if the user provides a valid JWT token.
    """
    current_user = get_jwt_identity()
    return ("JWT Auth: Access Granted")


@app.route("/admin-only", methods=["GET"])
@auth.login_required(role=["admin", "user"])
def admin_only():
    """
    Function that checks if the user is an admin.
    """
    current_user = get_jwt_identity()
    if current_user["role"] ==  "admin":
        return "Admin Access: Granted"
    else:
        return jsonify("error: Admin access required"), 403


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run()
