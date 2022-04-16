from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def hello_world():
    now = datetime.now()
    return f"Hello world from Stephanie Liu on {now.strftime('%B %d, %Y %H:%M:%S')}"


if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)

