# 🧠 MultiAgents

Multi-Agent System • Monitoring • Replay • Observability

A modular full-stack framework for building, monitoring, and visualizing multi-agent workflows.  
Includes backend orchestration, real-time monitoring, replay timeline, workflow graphs, and a frontend dashboard.

---

## 📁 Project Structure
```bash
MultiAgents/
│
├── backend/
│ ├── broadcaster.py # Real-time event broadcasting to frontend subscribers
│ ├── database.py # Storage of traces, metrics, snapshots, and replay data
│ ├── graph_builder.py # Builds LangGraph-style agent workflow graphs (nodes, edges, routing)
│ ├── logger.py # Central structured logging system for events, traces, and agent states
│ ├── main.py # Backend entrypoint — starts API server, monitoring, replay engine
│ ├── metrics.py # Captures latency, token usage, error rates, and agent performance stats
│ ├── models.py # Typed data models: events, states, traces, graph nodes, snapshots
│ ├── observability.py # Tracks system health, agent behavior anomalies, state transitions
│ ├── replay.py # Reconstructs full history of agent runs for interactive timeline replay
│ └── schemas.py # API + internal data schemas for requests, events, and trace records
│
├── docs/
│ ├── README.md # Documentation root
│ ├── feature_spec.md # Feature-level architecture specifications
│ ├── graph_visualization.md# Workflow visualization details
│ ├── langsmith_features.md # LangGraph/LangSmith integration overview
│ ├── logging_research.md # Internal logging and tracing research notes
│ └── user_guide.md # Step-by-step operational guide
│
├── frontend/
│ ├── components/ # UI elements like replay controls, graph views, agent state cards
│ ├── pages/ # Dashboard pages: Observability, Replay, Monitor
│ ├── app.js # Frontend app logic, routing, global state management
│ ├── index.html # Root HTML page for the dashboard
│ └── style.css # Styling for layout, colors, and theme
│
├── config.yaml # Environment configurations: logging, workflow definitions, ports
├── langgraph_workflow.py # Defines agent interactions and workflow graph
├── reply_engine.py # LLM response pipeline: generation, validation, routing
├── requirements.txt # Python dependencies for the whole project
└── trace_store.py # Trace persistence layer for logging and replay
```
---

## 📝 Description

MultiAgents provides everything required to run and observe complex multi-agent execution:  
- Agent workflow orchestration  
- Real-time monitoring & visualization  
- Replay of past agent runs  
- Graph-based workflow representation  
- Metrics and performance insights  
- Frontend dashboard for observability  
- Strong backend architecture for agent logic  

Designed for debugging, research, and production-oriented agent ecosystems.

---

## 🖥️ Backend Modules

- **broadcaster.py**: Real-time event broadcasting to frontend subscribers  
- **database.py**: Storage of traces, metrics, snapshots, and replay data  
- **graph_builder.py**: Builds LangGraph-style agent workflow graphs (nodes, edges, and routing)  
- **logger.py**: Central structured logging system for events, traces, and agent states  
- **main.py**: Backend entrypoint — starts API server, monitoring, and replay engine  
- **metrics.py**: Captures latency, token usage, error rates, and agent performance statistics  
- **models.py**: Typed data models including events, states, traces, graph nodes, and snapshots  
- **observability.py**: Tracks system health, agent behavior anomalies, and state transitions  
- **replay.py**: Reconstructs full history of agent runs into an interactive timeline for replay  
- **schemas.py**: Defines API and internal data schemas for requests, events, and trace records  

---

## 📚 Documentation

Key documents to explore:  
- **README.md** — Root project documentation  
- **feature_spec.md** — Detailed architecture and feature specifications  
- **graph_visualization.md** — Details of workflow graph visualization  
- **langsmith_features.md** — LangGraph and LangSmith platform integrations  
- **logging_research.md** — Insights and research on logging and tracing methodologies  
- **user_guide.md** — Step-by-step operational manual for users  

---

## 🎨 Frontend (Observability Dashboard)

- **components/** — UI elements like replay controls, graph view, agent state cards  
- **pages/** — Dashboard pages including Observability, Replay, and Monitor interfaces  
- **app.js** — Frontend application logic managing routing and state  
- **index.html** — Root HTML page of the dashboard  
- **style.css** — Dashboard styles for layout, colors, and theming  

---

## ⚙️ Configuration & Supporting Files

- **config.yaml** — Environment setup, logging options, workflow definitions, and backend/frontend ports  
- **langgraph_workflow.py** — Workflow graph defining agent interactions and routing  
- **reply_engine.py** — Language Model (LLM) response pipeline including generation, validation, and routing  
- **trace_store.py** — Provides trace persistence layer used by logging and replay functionalities  

---

## 📦 Installation
```bash
git clone https://github.com/atharvvv10/MultiAgents.git
cd MultiAgents
pip install -r requirements.txt
```
---

## ▶️ Run Backend
```bash
python backend/main.py
```
---

## 🌐 Run Frontend
```bash
Option 1 — Open directly:  
Open `frontend/index.html` in a web browser.

Option 2 — Serve the frontend folder:  
npx serve frontend
```
---

## ✨ Features

- Real-time multi-agent monitoring  
- Replay timeline viewer for past agent runs  
- Workflow graph visualization  
- Full trace logging and persistent storage  
- Metrics and performance statistics  
- Frontend dashboard for comprehensive observability  
- Modular and scalable backend architecture  
- Ideal tooling for debugging, research, and production  

---

## 🎯 Ideal Use Cases

- AI agent research  
- Multi-agent system debugging  
- Workflow visualization and tracing  
- Performance and metrics analysis  
- Production-grade multi-agent orchestration  

---

Thank you for exploring MultiAgents — empowering you with full observability and control over complex multi-agent workflows! 🚀
