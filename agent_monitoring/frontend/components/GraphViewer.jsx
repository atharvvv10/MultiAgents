import React, { useState, useEffect, useRef } from "react";
import ReactFlow from "reactflow";

export default function GraphViewer() {
  const [nodes, setNodes] = useState([]);
  const [edges, setEdges] = useState([]);
  const wsRef = useRef(null);

  useEffect(() => {
    fetch("http://localhost:8000/logs")
      .then((r) => r.json())
      .then((data) => {
        const agentMap = new Map();
        const n = [];
        const e = [];
        data.forEach((log, i) => {
          if (!agentMap.has(log.agent)) {
            const idx = agentMap.size;
            agentMap.set(log.agent, true);
            n.push({ id: log.agent, data: { label: log.agent }, position: { x: 250 * idx, y: 0 } });
          }
          if (log.target_agent) {
            e.push({ id: `e-${log.id}`, source: log.agent, target: log.target_agent });
          }
        });
        setNodes(n);
        setEdges(e);
      })
      .catch((_) => {});

    wsRef.current = new WebSocket("ws://localhost:8000/ws/logs");
    wsRef.current.onmessage = (evt) => {
      try {
        const log = JSON.parse(evt.data);
        setNodes((prev) => {
          if (prev.find((p) => p.id === log.agent)) return prev;
          return [...prev, { id: log.agent, data: { label: log.agent }, position: { x: 250 * prev.length, y: 0 } }];
        });
        if (log.target_agent) {
          setEdges((prev) => [...prev, { id: `e-${log.id}`, source: log.agent, target: log.target_agent }]);
        }
      } catch (e) {}
    };

    return () => {
      if (wsRef.current) wsRef.current.close();
    };
  }, []);

  return <ReactFlow nodes={nodes} edges={edges} fitView />;
}
