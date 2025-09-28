from trace_store import load_traces
from langgraph_workflow import app

def replay_trace(trace):
    return app.invoke(trace["inputs"])

def replay_all():
    return [replay_trace(t) for t in load_traces()]
