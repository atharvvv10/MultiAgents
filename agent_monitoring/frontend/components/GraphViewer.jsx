import ReactFlow from 'reactflow'

const nodes = [{ id: 'AgentA', data: { label: 'AgentA' }, position: { x: 0, y: 0 } },
               { id: 'AgentB', data: { label: 'AgentB' }, position: { x: 200, y: 0 } }]
const edges = [{ id: 'e1', source: 'AgentA', target: 'AgentB' }]

export default function GraphViewer() {
  return <ReactFlow nodes={nodes} edges={edges} fitView />
}
