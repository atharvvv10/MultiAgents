# 📖 MultiProdigy Observability User Guide
## 🚀 Quick Start
## 1. Enable Observability in Your Agents

Observability is automatically enabled when you use BaseAgent. No additional setup required.
```bash
from MultiProdigy.agents.agent_base import BaseAgent
from MultiProdigy.bus.message_bus import MessageBus

# Your agents automatically get tracing
class MyAgent(BaseAgent):
    def on_message(self, message):
        # This will be automatically traced
        return f"Processed: {message.content}"

# Usage
bus = MessageBus()
agent = MyAgent("MyAgent", bus)
```

## 2. Start the Observability Dashboard
```bash
from MultiProdigy.observability.dashboard import ObservabilityDashboard

# Start the dashboard server
dashboard = ObservabilityDashboard()
dashboard.run(host='localhost', port=5000)


Then open 👉 http://localhost:5000
 in your browser.
```

## 3. View the Agent Network Graph
```bash
Visit 👉 http://localhost:5000/static/graph.html
```

## 📊 Features Overview
## Dashboard Features

## Timeline View: Chronological flow of agent messages

-> Sending and receiving events

-> Processing duration per agent

-> Error tracking and status indicators

## Metrics Panel: Key performance indicators

-> Total messages processed

-> Average processing duration

-> Error rates and counts

-> Active agent status

## Trace Details: Drill-down into interactions

-> Individual message content

-> Metadata and context

-> Error stack traces

## Network Graph Features

-> Interactive Visualization

-> Drag, zoom, and pan

-> Click nodes for details

## Real-time Updates

-> Refresh every 5 seconds

-> Message flow animations

## Agent Status Indicators

-> 🟢 Active

-> 🟡 Processing

-> 🔴 Error

-> ⚫ Idle

## ⚙️ Configuration Options
Custom Log File
```bash
from MultiProdigy.observability.tracer import AgentTracer
tracer = AgentTracer(log_file="my_custom_traces.jsonl")

Dashboard Config
from MultiProdigy.observability.dashboard import ObservabilityDashboard
dashboard = ObservabilityDashboard(log_file="my_custom_traces.jsonl")
dashboard.run(host='0.0.0.0', port=8080, debug=False)

Graph Time Window
from MultiProdigy.observability.graph_builder import AgentGraphBuilder
builder = AgentGraphBuilder()
graph_data = builder.build_graph_data(time_window_minutes=30)
```

## 🔧 Advanced Usage
```bash 
Custom Tracing
from MultiProdigy.observability.tracer import tracer

class MyAgent(BaseAgent):
    def on_message(self, message):
        trace_id = tracer.start_trace(
            agent_name=self.name,
            event_type="custom_processing",
            metadata={"input_type": type(message.content).__name__}
        )
        try:
            result = self.complex_processing(message.content)
            tracer.end_trace(trace_id, result={"output_length": len(result)})
            return result
        except Exception as e:
            tracer.end_trace(trace_id, error=str(e))
            raise
```

## Filtering & Search
```bash
http://localhost:5000/api/traces?agent=TaskManager

http://localhost:5000/api/timeline?status=error

http://localhost:5000/api/metrics?time_window=3600

Export Data
from MultiProdigy.observability.dashboard import ObservabilityDashboard
dashboard = ObservabilityDashboard()
traces = dashboard._load_traces()
# Export to CSV, send to external monitoring, etc.
```

## 🛠️ Troubleshooting

## No Data in Dashboard?

-> Ensure agents are active (traces only created during activity).

-> Verify log file path.

-> Confirm agents inherit from BaseAgent.

## Empty Graph?

-> Make sure agents communicated recently (default window = 60 min).

-> Check browser console for JS errors.

-> Verify /api/graph returns data.

## Performance Issues?

-> Large logs → slow dashboard. Rotate logs.

-> Use smaller time windows.

-> Disable graph animations if needed.

## Enable Debug Mode
```bash
import logging
logging.basicConfig(level=logging.DEBUG)

from MultiProdigy.observability.dashboard import ObservabilityDashboard
dashboard = ObservabilityDashboard()
dashboard.run(debug=True)
```
## 📂 Log File Format (JSONL)
```bash
{"trace_id": "abc123", "timestamp": "2025-01-22T10:30:00Z", "event_type": "message_sent", "sender": "UserAgent", "receiver": "TaskManager", "content_preview": "Hello"}
{"trace_id": "def456", "agent_name": "TaskManager", "event_type": "message_received", "start_time": "2025-01-22T10:30:01Z", "duration_ms": 150, "status": "completed"}
```
## 🌍 Integration with External Tools
```bash
Prometheus Metrics
from prometheus_client import Counter, Histogram, start_http_server

message_counter = Counter('multiprodigy_messages_total', 'Total messages', ['sender', 'receiver'])
processing_time = Histogram('multiprodigy_processing_seconds', 'Processing time', ['agent'])

start_http_server(8000)

ELK Stack Integration
import json
from elasticsearch import Elasticsearch

es = Elasticsearch(['localhost:9200'])
def forward_to_elk(trace_data):
    es.index(index='multiprodigy-traces', body=trace_data)
```
1.Grafana Dashboards

2.Configure Prometheus as a data source

3.Import dashboard templates

4.Set up alerts (errors, latency, throughput)

## ✅ Best Practices

-> Monitor resource usage (~5% overhead).

-> Rotate log files regularly.

-> Use time windows for efficiency.

-> Add domain-specific custom metrics.

-> Always handle tracing errors gracefully.

## 📡 API Reference
-> Tracer Methods
```bash
start_trace(agent_name, event_type, metadata=None) → trace_id

end_trace(trace_id, result=None, error=None) → None

log_message_event(sender, receiver, content, message_id=None) → message_id
```

-> Dashboard Endpoints
```bash
GET /api/traces → List all traces

GET /api/traces/<trace_id> → Trace details

GET /api/timeline → Timeline data

GET /api/metrics → Performance metrics

GET /api/graph → Graph visualization
```
-> Graph Builder Methods
```bash
build_graph_data(time_window_minutes=60) → graph_data

get_agent_details(agent_name) → agent_details
```
