from replay_engine import replay_trace

def replay_from_id(trace_id):
    trace = load_trace_by_id(trace_id)
    return replay_trace(trace)
