from backend.logger import log_agent_activity
from trace_store import get_trace

def replay_last_trace():
    last_trace_id = "last"
    trace_logs = get_trace(last_trace_id)
    log_agent_activity(
        session_id="replay",
        step="replay_last_trace",
        event_type="replay",
        content=str(trace_logs)
    )
    return {"status": "success", "trace": trace_logs}
