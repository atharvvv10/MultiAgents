from backend.logger import log_agent_activity

# Inside workflow step
log_agent_activity(agent_name="AgentA", step="Step1", event_type="start", content="Workflow started")

