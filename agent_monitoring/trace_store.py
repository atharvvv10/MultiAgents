logs = []

def log_event(agent_name, step, event_type, content, target_agent=None):
    logs.append({
        "agent": agent_name,
        "step": step,
        "event_type": event_type,
        "content": content,
        "target_agent": target_agent
    })
    return logs[-1]

def get_recent_logs(limit=100):
    return logs[-limit:]

def get_trace(trace_id):
    return logs
