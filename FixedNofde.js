# secure_code_combined.py

def ex1_secure():
    # Example fix for input validation
    user_input = input("Enter a number: ")
    try:
        number = int(user_input)
        return f"Valid number: {number}"
    except ValueError:
        return "Invalid input. Please enter a number."

def ex2_secure():
    # Example fix for command injection
    import subprocess
    filename = input("Enter filename to list: ")
    if filename.isalnum():
        result = subprocess.run(["ls", filename], capture_output=True, text=True)
        return result.stdout
    else:
        return "Invalid filename."

def ex_vulnerability_fixed():
    # This is the one marked as 'Ex # Vulnerability'
    # Example fix for insecure deserialization
    import json
    data = '{"user": "admin", "access": "limited"}'
    try:
        parsed = json.loads(data)
        return f"Parsed safely: {parsed}"
    except json.JSONDecodeError:
        return "Failed to parse JSON."

def main():
    print("Running Ex # Vulnerability:")
    print(ex_vulnerability_fixed())

if __name__ == "__main__":
    main()
