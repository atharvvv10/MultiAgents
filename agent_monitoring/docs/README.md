# 🧠 MultiAgents: Agent Monitoring Module

Real-time observability for multi-agent systems

## 📥 Installation

Clone the repository:
```bash
git clone https://github.com/atharvvv10/MultiAgents.git
cd MultiAgents/agent_monitoring
```

Launch the Monitoring Dashboard:
```bash
python demo/launch_monitor.py
```

Open in your browser:
```bash
http://localhost:6006

or via CLI:

xdg-open http://localhost:6006
```
## 📦 Key Features

1.📡 Live agent activity stream – Track agent actions in real-time.

2.🕸️ Interactive communication graph – Visualize agent interactions using LangGraph for clear branching and relationships.

3.📈 Performance metrics – Monitor CPU, latency, throughput, and memory usage.

4.🔍 Searchable message logs – Filter and query historical logs for debugging.

5.🧑‍💻 Agent health and diagnostics – Detect errors, anomalies, and agent status.

6.🌿 Branch-based support – Handle multiple agent branches, versions, or deployments seamlessly.

## 🖥️ Dashboard Routes

1./graph ->	Interactive agent communication graph

2./agents -> Agent statistics and health overview

3./logs	-> Message history with search & filters

4./metrics -> System performance charts

## ⚙️ Configuration (Python)
```bash
Default configuration:

from agent_monitoring.core import MonitorManager

monitor = MonitorManager()
monitor.launch_dashboard(port=6006)


Custom configuration:

from agent_monitoring.config import MonitorConfig
from agent_monitoring.core import MonitorManager

config = MonitorConfig(
    port=7000,
    enable_logging=True,
    verbosity="DEBUG"
)

monitor = MonitorManager(config)
monitor.launch_dashboard()
```

## 🔗 Integrations

1.✅ LangChain-compatible

2.✅ Extendable logging backends

3.✅ Plug-and-play with custom agents

4.📚 Documentation & References:
```bash
monitoring_guide.md → Setup & usage

api_reference.md → API details

agent_patterns.md → Design best practices
```
## 🧪 Run Tests
```bash
pytest tests/
```
## 🛠️ Contributing

1.Fork the repository →

2.Add feature or improvement →

3.Create a Pull Request →

## 🚀 Celebrate your contribution!

## Made with ❤️ by Atharv
