import React, { useEffect, useState } from "react";
import GraphViewer from "../components/GraphViewer";
import ReplayControls from "../components/ReplayControls";
import MetricsCard from "../components/MetricsCard";
import FilterPanel from "../components/FilterPanel";

export default function Observability() {
  const [metrics, setMetrics] = useState({ total_events: 0, error_count: 0, avg_latency_ms: 0 });

  const loadMetrics = () => {
    fetch("http://localhost:8000/metrics")
      .then((r) => r.json())
      .then((d) => setMetrics(d))
      .catch(() => {});
  };

  useEffect(() => {
    loadMetrics();
    const t = setInterval(loadMetrics, 5000);
    return () => clearInterval(t);
  }, []);

  const handleFilter = ({ agent, event_type }) => {
    const q = new URLSearchParams();
    if (agent) q.set("agent", agent);
    if (event_type) q.set("event_type", event_type);
    fetch(`http://localhost:8000/logs/filter?${q.toString()}`)
      .then((r) => r.json())
      .then((data) => {
        // For simplicity just reload page components by refreshing window - or you can implement a prop-driven GraphViewer
        window.location.reload();
      });
  };

  return (
    <div style={{ padding: 12 }}>
      <h1>Agent Observability Dashboard</h1>
      <div style={{ display: "flex", gap: 8 }}>
        <MetricsCard title="Total events" value={metrics.total_events} />
        <MetricsCard title="Errors" value={metrics.error_count} />
        <MetricsCard title="Avg latency ms" value={Math.round(metrics.avg_latency_ms)} />
      </div>
      <FilterPanel onFilter={handleFilter} />
      <GraphViewer />
      <ReplayControls />
    </div>
  );
}
