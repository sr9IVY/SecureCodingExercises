from flask import Flask, request, jsonify, abort
from werkzeug.security import generate_password_hash
import requests
import re

app = Flask(__name__)

print("Exercise 2 - Broken Access Control")
@app.route('/account/<user_id>')
def get_account(user_id):
    if user_id != str(request.user.id):
        abort(403)
    user = db.query(User).filter_by(id=user_id).first()
    return jsonify(user.to_dict())

print("Exercise 4 - Cryptographic Failures")
def hash_password(password):
    return generate_password_hash(password)

print("Exercise 7 - Insecure Design")
@app.route('/reset-password', methods=['POST'])
def reset_password():
    token = request.form['token']
    new_password = request.form['new_password']
    user = verify_token(token)
    if not user:
        abort(403)
    user.password = generate_password_hash(new_password)
    db.session.commit()
    return 'Password reset'

print("Exercise 9 - Server-Side Request Forgery")
def fetch_url():
    url = input("Enter URL: ")
    if not re.match(r'^https?://[^/]+$', url):
        print("Invalid URL")
        return
    try:
        response = requests.get(url, timeout=5)
        print(response.text)
    except:
        print("Request failed")

# Uncomment below to run Flask app if needed
# if __name__ == '__main__':
#     app.run()
