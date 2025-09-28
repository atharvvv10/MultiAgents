from pydantic import BaseModel
from datetime import datetime

class AgentLogCreate(BaseModel):
    session_id: str
    step: int
    event_type: str
    content: str

class AgentLogOut(BaseModel):
    id: int
    session_id: str
    step: int
    event_type: str
    content: str
    timestamp: datetime

    class Config:
        orm_mode = True
