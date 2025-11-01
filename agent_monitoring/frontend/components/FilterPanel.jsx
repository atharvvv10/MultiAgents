import React, { useState } from "react";

export default function FilterPanel({ onFilter }) {
  const [agent, setAgent] = useState("");
  const [eventType, setEventType] = useState("");

  const apply = () => {
    onFilter({ agent: agent || undefined, event_type: eventType || undefined });
  };

  return (
    <div style={{ display: "flex", gap: 8, alignItems: "center", margin: "8px 0" }}>
      <input placeholder="Agent" value={agent} onChange={(e) => setAgent(e.target.value)} />
      <input placeholder="Event Type" value={eventType} onChange={(e) => setEventType(e.target.value)} />
      <button onClick={apply}>Apply</button>
    </div>
  );
}
