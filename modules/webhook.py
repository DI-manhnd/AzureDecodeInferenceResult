import json
import os

import requests


def send_teams(title, msg):
    url = os.getenv("WEBHOOK_URL")
    headers = {"Content-Type": "application/json"}
    data = {
        "title": title,
        "text": msg,
    }
    requests.post(url, headers=headers, data=json.dumps(data))
