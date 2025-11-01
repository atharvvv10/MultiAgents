from .database import SessionLocal
from .models import AgentLog
from .logger import log_agent_activity

def _get_last_trace_session_id():
    db = SessionLocal()
    row = db.query(AgentLog).order_by(AgentLog.id.desc()).first()
    db.close()
    return row.session_id if row else None

def replay_last_trace():
    session_id = _get_last_trace_session_id()
    if not session_id:
        return {"status": "no_trace"}
    db = SessionLocal()
    trace_logs = db.query(AgentLog).filter(AgentLog.session_id == session_id).order_by(AgentLog.id.asc()).all()
    db.close()
    log_agent_activity(session_id="replay", agent="ReplayEngine", step="replay_last_trace", event_type="replay", content=f"replayed session {session_id}")
    return {"status": "success", "session_id": session_id, "trace_count": len(trace_logs)}
