import flask
import re

# TODO: change this to your academic email
AUTHOR = "amyzheng@sas.upenn.edu"

app = flask.Flask(__name__)

# Simple route to test your server
@app.route("/")
def hello():
    return f"Hello from my Password Validator! &mdash; <tt>{AUTHOR}</tt>"

# Password validation function based on Policy EIGHT
def is_valid_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not any(c.isupper() for c in password):
        return False, "Password must contain at least one uppercase letter."
    if not any(c.isdigit() for c in password):
        return False, "Password must contain at least one digit."
    if not any(c in "!@#$%^&*" for c in password):
        return False, "Password must contain at least one special character (!@#$%^&*)."
    
    return True, "Password meets all requirements."

# Password validator endpoint
@app.route("/v1/checkPassword", methods=["POST"])
def check_password():
    data = flask.request.get_json() or {}
    pw = data.get("password", "")

    valid, reason = is_valid_password(pw)

    return flask.jsonify({"valid": valid, "reason": reason}), 200 if valid else 400

if __name__ == "__main__":
    app.run(debug=True)
