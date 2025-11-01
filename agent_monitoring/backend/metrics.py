from .database import SessionLocal
from .models import AgentLog
from sqlalchemy import func

def get_basic_metrics():
    db = SessionLocal()
    total = db.query(func.count(AgentLog.id)).scalar() or 0
    errors = db.query(func.count(AgentLog.id)).filter(AgentLog.event_type == "error").scalar() or 0
    avg_latency = db.query(func.avg(AgentLog.latency_ms)).scalar() or 0
    db.close()
    return {"total_events": int(total), "error_count": int(errors), "avg_latency_ms": float(avg_latency or 0)}
