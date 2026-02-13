from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Global Signal Server")

# Signal modeli: message + sender (@Kaktus_bol12)
class Signal(BaseModel):
    message: str
    sender: str

@app.get("/")
async def root():
    return {"status": "Server is running"}

@app.post("/signal")
async def send_signal(signal: Signal):
    # Logda kim yuborganini ko‘rsatadi
    print(f"New signal received from {signal.sender}: {signal.message}")
    return {
        "status": "Signal received",
        "message": signal.message,
        "sender": signal.sender
    }
