from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from datetime import datetime
import json
import os

app = FastAPI()
LOG_FILE = "signals_log.json"

# Agar log fayl yo'q bo'lsa, uni yarating
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as f:
        json.dump([], f)

@app.post("/signal")
async def receive_signal(request: Request):
    data = await request.json()
    data["timestamp"] = datetime.utcnow().isoformat()

    with open(LOG_FILE, "r+") as f:
        logs = json.load(f)
        logs.append(data)
        f.seek(0)
        json.dump(logs, f, indent=4)

    print("Signal qabul qilindi:", data)
    return JSONResponse({"status": "ok", "received": data})

@app.get("/signals")
async def get_signals():
    with open(LOG_FILE, "r") as f:
        logs = json.load(f)
    return JSONResponse(logs)
