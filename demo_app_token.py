from flask import Flask, request, jsonify
app = Flask(__name__)

TOKEN_COUNT = {}
RATE_LIMIT = 10

@app.route("/password-reset", methods=["POST"])
def password_reset():
    token = request.args.get("tbtoken")
    email = request.form.get("email") or (request.json and request.json.get("email"))
    if not token:
        return jsonify({"error":"missing token"}), 400
    if not email:
        return jsonify({"error":"missing email"}), 400
    key = f"{token}:{email}"
    cnt = TOKEN_COUNT.get(key, 0) + 1
    TOKEN_COUNT[key] = cnt
    if token == "forbidden-token-demo":
        return jsonify({"error":"forbidden"}), 403
    if cnt > RATE_LIMIT:
        return jsonify({"error":"rate limited"}), 429
    return jsonify({"result":"reset_queued","attempt":cnt}), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
