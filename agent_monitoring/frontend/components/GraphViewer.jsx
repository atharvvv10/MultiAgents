import React, { useState, useEffect } from "react";
import ReactFlow from "reactflow";

export default function GraphViewer() {
  const [nodes, setNodes] = useState([]);
  const [edges, setEdges] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/logs")
      .then((res) => res.json())
      .then((data) => {
        const agentNodes = [];
        const agentEdges = [];

        data.forEach((log, index) => {
          if (!agentNodes.find((n) => n.id === log.agent)) {
            agentNodes.push({
              id: log.agent,
              data: { label: log.agent },
              position: { x: 200 * index, y: 0 },
            });
          }

          if (log.target_agent) {
            agentEdges.push({
              id: `e-${log.agent}-${log.target_agent}-${index}`,
              source: log.agent,
              target: log.target_agent,
            });
          }
        });

        setNodes(agentNodes);
        setEdges(agentEdges);
      })
      .catch((err) => console.error(err));
  }, []);

  return <ReactFlow nodes={nodes} edges={edges} fitView />;
}
