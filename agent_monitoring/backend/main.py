from fastapi import FastAPI, WebSocket
from .database import engine, SessionLocal
from .models import Base, AgentLog
from .schemas import AgentLogCreate
from .logger import log_event

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/log/")
def create_log(log: AgentLogCreate):
    return log_event(log)

@app.get("/logs/{session_id}")
def get_logs(session_id: str):
    db = SessionLocal()
    logs = db.query(AgentLog).filter(AgentLog.session_id == session_id).all()
    db.close()
    return logs

@app.websocket("/ws/logs")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Echo: {data}")
