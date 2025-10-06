# FixedJavacodes.py
import hashlib

def hash_password(password: str) -> str:
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    return sha256.hexdigest()

# Example usage
if __name__ == "__main__":
    hashed = hash_password("mySecurePassword123")
    print("EX 3 RAN SUCCESSFULLY")
import sqlite3

def initialize_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT
        )
    """)
    # Insert sample user if not already present
    cursor.execute("SELECT COUNT(*) FROM users WHERE username = ?", ("alice",))
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", ("alice", "alice@example.com"))
    conn.commit()
    conn.close()

def get_user_by_username(username: str):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    result = cursor.fetchall()
    conn.close()
    return result

# Example usage
if __name__ == "__main__":
    initialize_db()
    users = get_user_by_username("alice")
    print("EX 5 RAN SUCCESSFULLY")
    print("Query result:", users)


import bcrypt

def verify_password(input_password: str, stored_hash: bytes) -> bool:
    return bcrypt.checkpw(input_password.encode('utf-8'), stored_hash)

# Example usage
if __name__ == "__main__":
    # Simulate stored hash (normally from DB)
    password = "mySecurePassword123"
    stored_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Verify login
    if verify_password("mySecurePassword123", stored_hash):
        print("EX 10 RAN SUCCESSFULLY")
    else:
        print("EX 10 FAILED")
