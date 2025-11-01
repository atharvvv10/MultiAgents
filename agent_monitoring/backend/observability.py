from .database import SessionLocal
from .models import AgentLog
from sqlalchemy import desc, and_
from datetime import datetime

def get_recent_logs(limit=200):
    db = SessionLocal()
    rows = db.query(AgentLog).order_by(desc(AgentLog.id)).limit(limit).all()
    db.close()
    return rows

def filter_logs(agent=None, event_type=None, start_ts=None, end_ts=None, limit=500):
    db = SessionLocal()
    q = db.query(AgentLog)
    if agent:
        q = q.filter(AgentLog.agent == agent)
    if event_type:
        q = q.filter(AgentLog.event_type == event_type)
    if start_ts:
        q = q.filter(AgentLog.timestamp >= start_ts)
    if end_ts:
        q = q.filter(AgentLog.timestamp <= end_ts)
    rows = q.order_by(desc(AgentLog.id)).limit(limit).all()
    db.close()
    return rows
