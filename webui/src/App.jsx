import { useState } from "react"
import axios from "axios"

const API = "http://localhost:8000"

export default function App() {
  const [target, setTarget] = useState("")
  const [result, setResult] = useState(null)
  const [system, setSystem] = useState(null)

  const startScan = async () => {
    const res = await axios.post(`${API}/scan/quick`, {
      target
    })

    setResult(res.data)
  }

  const getSystemInfo = async () => {
    const res = await axios.get(`${API}/system/info`)
    setSystem(res.data)
  }

  return (
    <div className="container">
      <h1>0x-Scan Recon Platform</h1>

      <div className="card">
        <h2>Start Scan</h2>

        <input
          placeholder="example.com"
          value={target}
          onChange={e => setTarget(e.target.value)}
        />

        <button onClick={startScan}>
          Scan Target
        </button>
      </div>

      {result && (
        <div className="card">
          <h2>Scan Result</h2>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}

      <div className="card">
        <h2>System Info</h2>

        <button onClick={getSystemInfo}>
          Fetch System Info
        </button>

        {system && (
          <pre>{JSON.stringify(system, null, 2)}</pre>
        )}
      </div>
    </div>
  )
}
