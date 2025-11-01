from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Query
from fastapi.responses import JSONResponse
from .observability import get_recent_logs, filter_logs
from .replay import replay_last_trace
from .logger import log_agent_activity
from . import broadcaster
from .schemas import AgentLogOut
from typing import List, Optional
import asyncio

app = FastAPI()

@app.get("/logs", response_model=List[AgentLogOut])
def read_logs(limit: int = 200):
    rows = get_recent_logs(limit)
    return rows

@app.get("/logs/filter", response_model=List[AgentLogOut])
def read_filtered(agent: Optional[str] = None, event_type: Optional[str] = None, start_ts: Optional[str] = None, end_ts: Optional[str] = None, limit: int = 500):
    start = None
    end = None
    from datetime import datetime
    if start_ts:
        start = datetime.fromisoformat(start_ts)
    if end_ts:
        end = datetime.fromisoformat(end_ts)
    rows = filter_logs(agent=agent, event_type=event_type, start_ts=start, end_ts=end, limit=limit)
    return rows

@app.post("/replay")
def replay():
    return replay_last_trace()

@app.post("/log_event")
def log_event_api(session_id: str = None, agent: str = Query(...), step: str = None, event_type: str = Query(...), content: str = None, target_agent: str = None, status: str = None, latency_ms: int = None):
    payload = log_agent_activity(session_id=session_id, agent=agent, step=step, event_type=event_type, content=content, target_agent=target_agent, status=status, latency_ms=latency_ms)
    return JSONResponse(content=payload)

@app.websocket("/ws/logs")
async def websocket_logs_endpoint(websocket: WebSocket):
    await websocket.accept()
    await broadcaster.register(websocket)
    try:
        while True:
            await asyncio.sleep(10)
    except WebSocketDisconnect:
        await broadcaster.unregister(websocket)
