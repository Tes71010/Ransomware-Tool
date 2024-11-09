from detection import monitor_directory

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/start-monitoring")
def start_monitoring():
    result = monitor_directory("/path/to/monitor")
    return result


if __name__ == "__main__":
    app.run(debug=True)
