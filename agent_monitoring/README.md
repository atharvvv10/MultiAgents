# 🧠 MultiAgents: Agent Monitoring Module
# Real-time observability for multi-agent systems

$ git clone https://github.com/atharvvv10/MultiAgents.git
$ cd MultiAgents/agent_monitoring

# 🚀 Launch the Monitoring Dashboard
$ python demo/launch_monitor.py

# 🌐 Open in browser
$ xdg-open http://localhost:6006
# or manually visit: http://localhost:6006

# 📦 Key Features
# ──────────────────────────────────────────────
# 📡 Live agent activity stream
# 🕸️ Interactive communication graph
# 📈 Performance metrics (CPU, latency, throughput)
# 🔍 Searchable message logs
# 🧑‍💻 Agent health and diagnostics

# 🖥️ Dashboard Routes
# ──────────────────────────────────────────────
# /           → Main dashboard
# /graph      → Agent communication graph
# /agents     → Agent stats and health
# /logs       → Message history and filters
# /metrics    → System performance charts

# ⚙️ Configuration (Python)
$ python
>>> from agent_monitoring.core import MonitorManager
>>> monitor = MonitorManager()
>>> monitor.launch_dashboard(port=6006)

# Custom config
>>> from agent_monitoring.config import MonitorConfig
>>> config = MonitorConfig(
...     port=7000,
...     enable_logging=True,
...     verbosity="DEBUG"
... )
>>> monitor = MonitorManager(config)

# 🔗 Integrations
# ──────────────────────────────────────────────
# ✅ LangChain-compatible
# ✅ Extendable logging backends
# ✅ Plug-and-play with custom agents

# 📚 Docs & References
# ──────────────────────────────────────────────
# 📄 monitoring_guide.md → Setup & usage
# 📄 api_reference.md    → API details
# 📄 agent_patterns.md   → Design best practices

# 🧪 Run tests
$ pytest tests/

# 🛠️ Contribute
# Fork → Feature → PR → 🚀

# Made with ❤️ by Atharv
