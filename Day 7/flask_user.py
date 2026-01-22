from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Raja"},
    {"id": 2, "name": "Rama"}
]

@app.route("/", methods=["GET"])
def home():
    return "Welcome"

# GET + POST (handles /users and /users/)
@app.route("/users", methods=["GET", "POST"])
@app.route("/users/", methods=["GET", "POST"])
def users_handler():
    # GET all users
    if request.method == "GET":
        return jsonify(users), 200

    # POST create user
    if request.method == "POST":
        data = request.get_json()

        if not data or "name" not in data:
            return jsonify({"message": "name is required"}), 400

        new_user = {
            "id": users[-1]["id"] + 1 if users else 1,
            "name": data["name"]
        }
        users.append(new_user)

        return jsonify(new_user), 201

# PUT, PATCH, DELETE
@app.route("/users/<int:user_id>", methods=["PUT", "PATCH", "DELETE"])
@app.route("/users/<int:user_id>/", methods=["PUT", "PATCH", "DELETE"])
def user_handler(user_id):
    user = next((u for u in users if u["id"] == user_id), None)

    if not user:
        return jsonify({"message": "user not found"}), 404

    # PUT / PATCH
    if request.method in ["PUT", "PATCH"]:
        data = request.get_json()

        if not data:
            return jsonify({"message": "no data provided"}), 400

        user["name"] = data.get("name", user["name"])
        return jsonify(user), 200

    # DELETE
    if request.method == "DELETE":
        users.remove(user)
        return jsonify({"message": "user deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True)
