export default function ReplayControls() {
  const handleReplay = () => fetch("/api/replay", { method: "POST" })

  return (
    <div>
      <button onClick={handleReplay}>Replay Last Trace</button>
    </div>
  )
}
