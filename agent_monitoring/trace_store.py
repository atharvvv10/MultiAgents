from agent_monitoring.backend.database import SessionLocal
from agent_monitoring.backend.models import AgentLog

def load_traces():
    db = SessionLocal()
    rows = db.query(AgentLog).order_by(AgentLog.id.desc()).limit(100).all()
    db.close()
    traces = []
    for r in rows:
        traces.append({
            "id": r.id,
            "session_id": r.session_id,
            "agent": r.agent,
            "step": r.step,
            "event_type": r.event_type,
            "content": r.content,
            "timestamp": r.timestamp.isoformat()
        })
    return traces

def get_recent_logs(limit=200):
    return load_traces()[:limit]
