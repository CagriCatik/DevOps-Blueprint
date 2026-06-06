from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Shopping Frontend!"


@app.route("/health")
def health():
    # A health endpoint is handy for deployment checks and load balancers.
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
