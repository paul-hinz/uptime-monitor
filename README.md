# Uptime Monitor

Ein kleiner Uptime-Monitor in Python & Flask als Beispiel für automatisierte CI/CD Pipeline

![Tests](https://github.com/paul-hinz/uptime-monitor/actions/workflows/deploy.yml/badge.svg) &nbsp;&nbsp; 

Currently live on: http://3.64.200.96/


## Features

- Sendet regelmäßig Anfragen an definierte URLs
- Meldet, ob die Seiten erreichbar sind
- In Docker verpackt, auf mit Terraform definierte AWS Infrastruktur deployt
- Tests via Pytest und GitHub Actions 
