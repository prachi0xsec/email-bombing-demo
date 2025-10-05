# demo_app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

REQUEST_COUNT = {}
RATE_LIMIT = 10  # after 10 requests we return 429 for demonstration

@app.route("/forgot-password", methods=["POST"])
def forgot_password():
    email = request.form.get("email") or (request.json and request.json.get("email"))
    if not email:
        return jsonify({"error":"missing email"}), 400
    cnt = REQUEST_COUNT.get(email, 0) + 1
    REQUEST_COUNT[email] = cnt
    if email == "forbidden@example.test":
        return jsonify({"error":"forbidden"}), 403
    if cnt > RATE_LIMIT:
        return jsonify({"error":"rate limited"}), 429
    return jsonify({"result":"reset_email_sent", "attempt": cnt}), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
