from fastapi import FastAPI
from backend.logger import log_agent_activity
from backend.replay import replay_last_trace
from backend.observability import get_logs_for_visualization

app = FastAPI()

@app.get("/logs")
def read_logs(limit: int = 100):
    return get_logs_for_visualization(limit)

@app.post("/replay")
def replay():
    return replay_last_trace()

@app.post("/log_event")
def log_event_api(agent_name: str, step: str, event_type: str, content: str, target_agent: str = None):
    return log_agent_activity(agent_name, step, event_type, content)

