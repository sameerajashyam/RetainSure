from flask import Blueprint, request, jsonify
from models import user_model
from utils.security import hash_password, verify_password

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/', methods=['GET'])
def health():
    return jsonify({"message": "User Management System"}), 200

@user_routes.route('/users', methods=['GET'])
def get_users():
    users = user_model.get_all_users()
    return jsonify([dict(user) for user in users]), 200

@user_routes.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_model.get_user_by_id(user_id)
    if user:
        return jsonify(dict(user)), 200
    return jsonify({"error": "User not found"}), 404

@user_routes.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not all([name, email, password]):
        return jsonify({"error": "Missing fields"}), 400

    hashed_pw = hash_password(password)
    try:
        user_model.create_user(name, email, hashed_pw)
        return jsonify({"message": "User created"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@user_routes.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not all([name, email]):
        return jsonify({"error": "Missing fields"}), 400

    user_model.update_user(user_id, name, email)
    return jsonify({"message": "User updated"}), 200

@user_routes.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_model.delete_user(user_id)
    return jsonify({"message": f"User {user_id} deleted"}), 200

@user_routes.route('/search', methods=['GET'])
def search():
    name = request.args.get('name')
    if not name:
        return jsonify({"error": "Please provide name"}), 400

    users = user_model.search_users_by_name(name)
    return jsonify([dict(user) for user in users]), 200

@user_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = user_model.get_user_by_email(email)
    if user and verify_password(user['password'], password):
        return jsonify({"status": "success", "user_id": user['id']}), 200

    return jsonify({"status": "failed"}), 401
