from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/greet", methods=["GET"])
def greet():
    name = request.args.get("name", "stranger")
    return jsonify({"message": f"Hello  {name}"})

@app.route("/add", methods=["GET"])
def add():
    try:
        a = parse_float_params("a", request.args.get("a"))
        b = parse_float_params("b", request.args.get("b"))
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    return jsonify({"sum": a + b})


def parse_float_params(name, value):
    if value is None or value.strip() == "":
        raise ValueError(f"{name} is required")
    try:
        return float(value)
    except  ValueError:
        raise ValueError(f"'{name}' must be a valid number")


if __name__ == "__main__":
    app.run(debug=True, port=5000)