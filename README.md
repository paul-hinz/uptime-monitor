# Uptime Monitor

Ein kleiner Uptime-Monitor in Python & Flask als Beispiel für automatisierte CI/CD Pipeline

## Features

- Sendet regelmäßig Anfragen an definierte URLs
- Meldet, ob die Seiten erreichbar sind
- In Docker verpackt
- Tests via Pytest und GitHub Actions ![Tests](https://github.com/paul-hinz/uptime-monitor/actions/workflows/test.yml/badge.svg)

## Setup

```bash
docker build -t uptime-monitor .
docker run -p 5000:5000 uptime-monitor