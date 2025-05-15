from flask import Flask, render_template_string
import requests

app = Flask(__name__)

URLS_TO_CHECK = [
    "https://example.com",
    "https://httpstat.us/200",
    "https://httpstat.us/503"
]


HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Uptime Monitor</title>
    <style>
        body { font-family: sans-serif; padding: 2rem; }
        .up { color: green; font-weight: bold; }
        .down { color: red; font-weight: bold; }
    </style>
</head>
<body>
    <h1>Uptime Monitor</h1>
    <table>
        <tr><th>URL</th><th>Status</th></tr>
        {% for url, status in statuses.items() %}
        <tr>
            <td>{{ url }}</td>
            <td class="{{ 'up' if status == 'UP' else 'down' }}">{{ status }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

def check_url(url):
    try:
        response = requests.get(url, timeout=5)
        return "UP" if response.status_code == 200 else "DOWN"
    except requests.RequestException:
        return "DOWN"

@app.route("/")
def index():
    statuses = {url: check_url(url) for url in URLS_TO_CHECK}
    return render_template_string(HTML_TEMPLATE, statuses=statuses)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)