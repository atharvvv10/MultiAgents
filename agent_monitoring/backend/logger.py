from trace_store import log_event

def log_agent_activity(agent_name, event_type, message, target_agent=None):
    log_event(agent_name, event_type, message, target_agent)
