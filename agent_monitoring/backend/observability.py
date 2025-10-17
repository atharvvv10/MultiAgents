from trace_store import get_recent_logs

def get_logs_for_visualization(limit=100):
    return get_recent_logs(limit)
