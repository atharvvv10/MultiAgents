import React from "react";

export default function MetricsCard({ title, value }) {
  return (
    <div style={{ border: "1px solid #ddd", padding: 12, margin: 8, borderRadius: 6, minWidth: 150 }}>
      <div style={{ fontSize: 12, color: "#666" }}>{title}</div>
      <div style={{ fontSize: 20, fontWeight: "600" }}>{value}</div>
    </div>
  );
}
