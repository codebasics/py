from flask import Flask, jsonify, request
import util

app = Flask(__name__)


def _set_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


@app.get("/get_location_names")
def get_location_names():
    return _set_cors(jsonify({"locations": util.get_location_names()}))


@app.route("/predict_home_price", methods=["GET", "POST"])
def predict_home_price():
    data = request.form if request.form else request.args

    try:
        total_sqft = float(data["total_sqft"])
        bhk = int(data["bhk"])
        bath = int(data["bath"])
        location = data["location"].strip()
    except (KeyError, TypeError, ValueError):
        return _set_cors(jsonify({
            "error": "Provide valid total_sqft, bhk, bath, and location values."
        })), 400

    if total_sqft <= 0 or bhk <= 0 or bath <= 0 or not location:
        return _set_cors(jsonify({
            "error": "total_sqft, bhk, bath, and location must contain valid positive values."
        })), 400

    try:
        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
    except RuntimeError as exc:
        return _set_cors(jsonify({"error": str(exc)})), 503

    return _set_cors(jsonify({"estimated_price": estimated_price}))


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(host="0.0.0.0", port=5000)
