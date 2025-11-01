from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AgentLogCreate(BaseModel):
    session_id: Optional[str]
    agent: str
    step: Optional[str]
    event_type: str
    content: Optional[str]
    target_agent: Optional[str]
    status: Optional[str]
    latency_ms: Optional[int]

class AgentLogOut(BaseModel):
    id: int
    session_id: Optional[str]
    agent: str
    step: Optional[str]
    event_type: str
    content: Optional[str]
    target_agent: Optional[str]
    status: Optional[str]
    latency_ms: Optional[int]
    timestamp: datetime

    class Config:
        orm_mode = True
