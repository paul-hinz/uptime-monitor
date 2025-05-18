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

    if not history:
        for url in URLS_TO_CHECK:
            history.insert(0, check_url(url))


    if request.method == "POST":
        user_input = request.form["url"]

        if not user_input.startswith(("http://", "https://")):
            url = "https://" + user_input
        else:
            url = user_input

        result = check_url(url)
        history.insert(0, result)

    return render_template("index.html", result=result, history=history[:10])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)