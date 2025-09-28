# 🧠 MultiAgents: Agent Monitoring Module

Real-time observability for multi-agent systems

## 📥 Installation
# Clone the repository
```bash
git clone https://github.com/atharvvv10/MultiAgents.git
cd MultiAgents/agent_monitoring
```

## 🚀 Launch the Monitoring Dashboard
```bash
python demo/launch_monitor.py
```

## Open in your browser:
```bash
http://localhost:6006

or use:

xdg-open http://localhost:6006
```

## 📦 Key Features

1.📡 Live agent activity stream

2.🕸️ Interactive communication graph

3.📈 Performance metrics (CPU, latency, throughput)

4.🔍 Searchable message logs

5.🧑‍💻 Agent health and diagnostics

## 🖥️ Dashboard Routes


/graph ->	Agent communication graph
/agents	-> Agent stats and health
/logs ->	Message history and filters
/metrics ->	System performance charts

## ⚙️ Configuration (Python)
```bash
from agent_monitoring.core import MonitorManager
```
## Launch dashboard on default port
```bash
monitor = MonitorManager()
monitor.launch_dashboard(port=6006)

Custom Configuration
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

4.📚 Documentation & References

5.📄 monitoring_guide.md → Setup & usage

6.📄 api_reference.md → API details

7.📄 agent_patterns.md → Design best practices

## 🧪 Run Tests
```bash
pytest tests/
```
## 🛠️ Contributing

Fork → Feature → Pull Request → 🚀

## Made with ❤️ by Atharv
