import time
import requests
import os

# server URL
SERVER_URL = os.environ.get("SERVER_URL", "https://global-signal-server-3.onrender.com/signal")
SENDER = "@Kaktus_bol12"

while True:
    data = {
        "message": "Jonli global signal 🔥",
        "sender": SENDER
    }
    try:
        r = requests.post(SERVER_URL, json=data)
        print("Signal yuborildi:", r.status_code)
    except Exception as e:
        print("Xato:", e)
    time.sleep(5)
