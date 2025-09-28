from fastapi import APIRouter
from trace_store import load_traces

router = APIRouter()

@router.get("/logs")
def get_logs(): return load_traces()

@router.get("/agents")
def get_agents(): return ["AgentA", "AgentB"]

@router.get("/graph")
def get_graph(): return {"nodes": ["AgentA", "AgentB"], "edges": [("AgentA", "AgentB")]}

@router.post("/replay")
def replay(trace): return replay_trace(trace)
