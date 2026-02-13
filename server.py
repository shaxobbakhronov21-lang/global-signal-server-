from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Global Signal Server")

# Signal modeli
class Signal(BaseModel):
    message: str
    sender: Optional[str] = None  # ixtiyoriy

@app.get("/")
async def root():
    return {"status": "Server is running"}

@app.post("/signal")
async def send_signal(signal: Signal):
    # Agar sender yuborilmasa avtomatik qo‘shiladi
    sender_name = signal.sender if signal.sender else "@Kaktus_bol12"

    print(f"🌍 New signal from {sender_name}: {signal.message}")

    return {
        "status": "Signal received",
        "message": signal.message,
        "sender": sender_name
    }
