from .database import SessionLocal, engine
from .models import AgentLog, Base
from .schemas import AgentLogCreate
from datetime import datetime
from . import broadcaster
import asyncio

Base.metadata.create_all(bind=engine)

def _to_dict(db_obj):
    return {
        "id": db_obj.id,
        "session_id": db_obj.session_id,
        "agent": db_obj.agent,
        "step": db_obj.step,
        "event_type": db_obj.event_type,
        "content": db_obj.content,
        "target_agent": db_obj.target_agent,
        "status": db_obj.status,
        "latency_ms": db_obj.latency_ms,
        "timestamp": db_obj.timestamp.isoformat()
    }

def log_event_from_schema(log: AgentLogCreate):
    db = SessionLocal()
    db_obj = AgentLog(
        session_id=log.session_id,
        agent=log.agent,
        step=log.step,
        event_type=log.event_type,
        content=log.content,
        target_agent=log.target_agent,
        status=log.status,
        latency_ms=log.latency_ms,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    db.close()
    payload = _to_dict(db_obj)
    try:
        asyncio.create_task(broadcaster.broadcast(payload))
    except Exception:
        pass
    return payload

def log_agent_activity(session_id, agent, step, event_type, content=None, target_agent=None, status=None, latency_ms=None):
    schema = AgentLogCreate(
        session_id=session_id,
        agent=agent,
        step=step,
        event_type=event_type,
        content=content,
        target_agent=target_agent,
        status=status,
        latency_ms=latency_ms
    )
    return log_event_from_schema(schema)

