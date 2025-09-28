from langgraph.graph import StateGraph

def agent_a(state): return {"output": f"A processed {state['input']}"}
def agent_b(state): return {"output": f"B processed {state['input']}"}

def condition(state): return "yes" if "go" in state["input"] else "no"

graph = StateGraph()
graph.add_node("AgentA", agent_a)
graph.add_node("AgentB", agent_b)
graph.add_conditional_edges("AgentA", condition, {"yes": "AgentB", "no": "AgentA"})

app = graph.compile()
