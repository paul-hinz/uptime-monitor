from flask import Flask, render_template, request
import requests

app = Flask(__name__)

history = []

URLS_TO_CHECK = [
    "https://github.com",
    "https://httpstat.us/200",
    "https://httpstat.us/503"
]

def check_url(url):
    try:
        response = requests.get(url, timeout=5)
        return {
            "url": url,
            "status": "UP" if response.ok else "DOWN",
            "code": response.status_code
        }
    except requests.RequestException:
        return {
            "url": url,
            "status": "DOWN",
            "code": "N/A"
        }

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        url = request.form["url"]
        try:
            response = requests.get(url, timeout=5)
            status = "UP" if response.ok else "DOWN"
            code = response.status_code
        except requests.RequestException:
            status = "DOWN"
            code = "N/A"

        result = {"url": url, "status": status, "code": code}
        history.insert(0, result)  # neueste zuerst

    return render_template("index.html", result=result, history=history[:10])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)