from flask import Flask, Response
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "DevOps Monitoring Demo App"

@app.route("/metrics")
def metrics():
    value = random.randint(1,100)

    data = f'''
# HELP random_metric Random metric value
# TYPE random_metric gauge
random_metric {value}
'''
    return Response(data, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)