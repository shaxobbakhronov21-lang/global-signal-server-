from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
import hmac, hashlib, json, time

app = FastAPI()

SECRET_KEY = b"e78682f1b80ca6dc503269964b4bb8b5171fa502be83c5d175bb53f205975238  "

clients = []
used_nonces = {}

def verify_signature(payload, signature):
    message = json.dumps(payload, sort_keys=True).encode()
    expected = hmac.new(SECRET_KEY, message, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature)

def is_replay(nonce):
    now = time.time()
    for n in list(used_nonces.keys()):
        if now - used_nonces[n] > 60:
            del used_nonces[n]
    if nonce in used_nonces:
        return True
    used_nonces[nonce] = now
    return False

@app.post("/signal")
async def receive_signal(request: Request):
    payload = await request.json()
    signature = request.headers.get("X-Signature")

    if not signature or not verify_signature(payload, signature):
        return {"status": "invalid signature"}

    if is_replay(payload["nonce"]):
        return {"status": "replay detected"}

    for ws in clients:
        await ws.send_json(payload)

    return {"status": "broadcasted"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        clients.remove(websocket)
