# Ex1 Broken Access Control FixedNodejs.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated user database
users_db = {
    "123": {"id": "123", "name": "Alice"},
    "456": {"id": "456", "name": "Bob"}
}

# Simulated logged-in user
current_user_id = "123"  # Replace with dynamic auth in real apps

@app.route('/profile/<user_id>', methods=['GET'])
def get_profile(user_id):
    if user_id != current_user_id:
        print(f"Access denied for user_id: {user_id}")
        return jsonify({"error": "Access denied"}), 403

    user = users_db.get(user_id)
    if not user:
        print(f"User not found: {user_id}")
        return jsonify({"error": "User not found"}), 404

    print("Ex1sc ran successfully")
    return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)





