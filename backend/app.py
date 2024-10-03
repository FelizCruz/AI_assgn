from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = []
workouts = [{"id": 1, "name": "Push-up", "level": "Beginner"}]
meals = [{"id": 1, "name": "Keto Avocado Salad", "type": "Keto"}]

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the AI-Based Fitness and Diet Planner!"})

@app.route('/register', methods=['POST'])
def register():
    user_data = request.json
    users.append(user_data)
    return jsonify({"message": "User registered successfully!"}), 201

@app.route('/login', methods=['POST'])
def login():
    login_data = request.json
    for user in users:
        if user['username'] == login_data['username'] and user['password'] == login_data['password']:
            return jsonify({"message": "Login successful!"}), 200
    return jsonify({"message": "Invalid credentials!"}), 401

@app.route('/workouts', methods=['GET'])
def get_workouts():
    return jsonify(workouts), 200

@app.route('/meals', methods=['GET'])
def get_meals():
    return jsonify(meals), 200

if __name__ == '__main__':
    app.run(debug=True)
