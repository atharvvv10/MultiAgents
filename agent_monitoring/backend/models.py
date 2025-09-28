from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AgentLog(Base):
    __tablename__ = "agent_logs"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, index=True)
    step = Column(Integer)
    event_type = Column(String)
    content = Column(Text)
    timestamp = Column(DateTime, server_default=func.now())
