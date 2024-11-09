import os
import threading
import time

from flask import Flask
from flask import jsonify
from flask import render_template

app = Flask(__name__)

# Global variable to store monitoring status
monitoring_active = False
monitoring_result = ""


def monitor_directory(path):
    global monitoring_result
    before = set(os.listdir(path))
    while monitoring_active:
        time.sleep(10)  # Check every 10 seconds
        after = set(os.listdir(path))
        added = after - before
        if added:
            monitoring_result = f"New files added: {added}"
            before = after  # Update the before set


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/start-monitoring")
def start_monitoring():
    global monitoring_active
    if not monitoring_active:
        monitoring_active = True
        # Start the monitoring in a separate thread
        thread = threading.Thread(target=monitor_directory, args=("/path/to/monitor",))
        thread.start()
        return "Monitoring started."
    else:
        return "Monitoring is already active."


@app.route("/stop-monitoring")
def stop_monitoring():
    global monitoring_active
    monitoring_active = False
    return "Monitoring stopped."


@app.route("/status")
def status():
    return jsonify({"status": monitoring_result})


if __name__ == "__main__":
    app.run(debug=True)
