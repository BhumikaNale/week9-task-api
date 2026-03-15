from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from flask_bcrypt import Bcrypt
from flask_cors import CORS

from config import Config
from models import db, User, Task


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
CORS(app)


# Create database
with app.app_context():
    db.create_all()


# -----------------------------
# REGISTER
# -----------------------------
@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if User.query.filter_by(email=email).first():
        return jsonify({"message": "User already exists"}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

    new_user = User(
        username=username,
        email=email,
        password=hashed_password
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"})


# -----------------------------
# LOGIN
# -----------------------------
@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()

    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({"message": "Invalid credentials"}), 401

    access_token = create_access_token(identity=str(user.id))

    return jsonify({"access_token": access_token})


# -----------------------------
# CREATE TASK
# -----------------------------
@app.route("/tasks", methods=["POST"])
@jwt_required()
def create_task():

    user_id = get_jwt_identity()

    data = request.get_json()

    task = Task(
        title=data.get("title"),
        description=data.get("description"),
        status=data.get("status", "pending"),
        priority=data.get("priority", "medium"),
        user_id=user_id
    )

    db.session.add(task)
    db.session.commit()

    return jsonify({"message": "Task created"})


# -----------------------------
# GET TASKS
# -----------------------------
@app.route("/tasks", methods=["GET"])
@jwt_required()
def get_tasks():

    user_id = get_jwt_identity()

    tasks = Task.query.filter_by(user_id=user_id).all()

    output = []

    for task in tasks:
        task_data = {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "status": task.status,
            "priority": task.priority
        }
        output.append(task_data)

    return jsonify(output)


# -----------------------------
# GET SINGLE TASK
# -----------------------------
@app.route("/tasks/<int:id>", methods=["GET"])
@jwt_required()
def get_task(id):

    user_id = get_jwt_identity()

    task = Task.query.filter_by(id=id, user_id=user_id).first()

    if not task:
        return jsonify({"message": "Task not found"}), 404

    return jsonify({
        "title": task.title,
        "description": task.description,
        "status": task.status,
        "priority": task.priority
    })


# -----------------------------
# UPDATE TASK
# -----------------------------
@app.route("/tasks/<int:id>", methods=["PUT"])
@jwt_required()
def update_task(id):

    user_id = get_jwt_identity()

    task = Task.query.filter_by(id=id, user_id=user_id).first()

    if not task:
        return jsonify({"message": "Task not found"}), 404

    data = request.get_json()

    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.status = data.get("status", task.status)
    task.priority = data.get("priority", task.priority)

    db.session.commit()

    return jsonify({"message": "Task updated"})


# -----------------------------
# DELETE TASK
# -----------------------------
@app.route("/tasks/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_task(id):

    user_id = get_jwt_identity()

    task = Task.query.filter_by(id=id, user_id=user_id).first()

    if not task:
        return jsonify({"message": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "Task deleted"})


if __name__ == "__main__":
    app.run(debug=True)