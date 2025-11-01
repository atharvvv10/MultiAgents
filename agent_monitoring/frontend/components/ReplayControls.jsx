import React, { useState } from "react";

export default function ReplayControls() {
  const [status, setStatus] = useState("");

  const handleReplay = () => {
    setStatus("Replaying...");
    fetch("http://localhost:8000/replay", { method: "POST" })
      .then((r) => r.json())
      .then((data) => setStatus(JSON.stringify(data)))
      .catch((err) => setStatus("error"));
  };

  return (
    <div style={{ marginTop: 12 }}>
      <button onClick={handleReplay}>Replay Last Trace</button>
      <div style={{ marginTop: 8, fontSize: 12 }}>{status}</div>
    </div>
  );
}

