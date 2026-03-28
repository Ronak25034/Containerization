from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to my updated CI/CD Pipeline!"

@app.route("/status")
def status():
    return jsonify({
        "status": "running",
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

@app.route("/user/<name>")
def greet_user(name):
    return f"Hello, {name}! Your CI/CD pipeline is working perfectly."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
