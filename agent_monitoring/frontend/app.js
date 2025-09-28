document.addEventListener("DOMContentLoaded", function () {
  var cy = cytoscape({
    container: document.getElementById("cy"),
    elements: [
      { data: { id: "start", label: "Start" } },
      { data: { id: "step1", label: "Prompt Sent" } },
      { data: { id: "step2", label: "LLM Response" } },
      { data: { id: "end", label: "End" } },
      { data: { source: "start", target: "step1" } },
      { data: { source: "step1", target: "step2" } },
      { data: { source: "step2", target: "end" } }
    ],
    style: [
      { selector: "node", style: { "background-color": "#007bff", "label": "data(label)", "color": "#fff", "text-valign": "center", "text-halign": "center" } },
      { selector: "edge", style: { "width": 2, "line-color": "#ccc", "target-arrow-color": "#ccc", "target-arrow-shape": "triangle" } }
    ],
    layout: { name: "breadthfirst" }
  });
});
