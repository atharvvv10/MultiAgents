from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy import func
from .database import Base

class AgentLog(Base):
    __tablename__ = "agent_logs"
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(128), index=True, nullable=True)
    agent = Column(String(128), index=True, nullable=False)
    step = Column(String(128), nullable=True)
    event_type = Column(String(64), index=True, nullable=False)
    content = Column(Text, nullable=True)
    target_agent = Column(String(128), nullable=True)
    status = Column(String(32), nullable=True)
    latency_ms = Column(Integer, nullable=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
