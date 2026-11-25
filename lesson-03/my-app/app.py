import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    env = os.getenv("APP_ENV", "dev")
    return f"Hello from Docker Environment: {env}\n"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
