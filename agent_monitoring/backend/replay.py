from trace_store import get_trace

def replay_last_trace():
    last_trace_id = "last"  # placeholder logic for last trace
    trace_logs = get_trace(last_trace_id)
    return {"status": "success", "trace": trace_logs}
