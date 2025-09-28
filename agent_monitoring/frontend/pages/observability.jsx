import GraphViewer from '../components/GraphViewer'
import ReplayControls from '../components/ReplayControls'

export default function Observability() {
  return (
    <div>
      <h1>Agent Observability Dashboard</h1>
      <GraphViewer />
      <ReplayControls />
    </div>
  )
}
