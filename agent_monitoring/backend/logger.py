from .database import SessionLocal
from .models import AgentLog
from .schemas import AgentLogCreate

def log_event(log: AgentLogCreate):
    db = SessionLocal()
    db_log = AgentLog(
        session_id=log.session_id,
        step=log.step,
        event_type=log.event_type,
        content=log.content,
    )
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    db.close()
    return db_log

def log_agent_activity(session_id, step, event_type, content):
    log = AgentLogCreate(
        session_id=session_id,
        step=step,
        event_type=event_type,
        content=content
    )
    return log_event(log)
