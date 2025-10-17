import React from "react";

export default function ReplayControls() {
  const handleReplay = () => {
    fetch("http://localhost:8000/replay", { method: "POST" })
      .then((res) => res.json())
      .then((data) => console.log("Replay result:", data))
      .catch((err) => console.error(err));
  };

  return (
    <div>
      <button onClick={handleReplay}>Replay Last Trace</button>
    </div>
  );
}
