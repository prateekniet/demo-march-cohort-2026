from flask import Flask, jsonify, request

app = Flask(__name__)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


@app.route("/add", methods=["GET"])
def add_api():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))

    return jsonify({
        "operation": "addition",
        "a": a,
        "b": b,
        "result": add(a, b)
    })


@app.route("/subtract", methods=["GET"])
def subtract_api():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))

    return jsonify({
        "operation": "subtraction",
        "a": a,
        "b": b,
        "result": subtract(a, b)
    })


@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    return response


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
