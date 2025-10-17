from trace_store import load_traces
from langgraph_workflow import app
from backend.logger import log_agent_activity

def replay_trace(trace):
    result = app.invoke(trace["inputs"])
    log_agent_activity(
        agent_name="ReplayEngine",
        step="replay_trace",
        event_type="replay",
        content=str(trace["inputs"])
    )
    return result

def replay_all():
    results = []
    for t in load_traces():
        results.append(replay_trace(t))
    return results
