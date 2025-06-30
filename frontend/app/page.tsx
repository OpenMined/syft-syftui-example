'use client'

import { useEffect, useState } from 'react'

interface HelloResponse {
  message: string
  timestamp: string
  status: string
  user_email: string
}

interface StatusResponse {
  app: string
  version: string
  timestamp: string
  syftbox: {
    status: string
    user_email: string
  }
  components: {
    backend: string
    frontend: string
    cron: string
  }
}

export default function Home() {
  const [hello, setHello] = useState<HelloResponse | null>(null)
  const [status, setStatus] = useState<StatusResponse | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8001'

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true)
        
        // Fetch hello message
        const helloResponse = await fetch(`${apiUrl}/api/hello`)
        if (!helloResponse.ok) throw new Error('Failed to fetch hello message')
        const helloData = await helloResponse.json()
        setHello(helloData)

        // Fetch status
        const statusResponse = await fetch(`${apiUrl}/api/status`)
        if (!statusResponse.ok) throw new Error('Failed to fetch status')
        const statusData = await statusResponse.json()
        setStatus(statusData)

      } catch (err) {
        setError(err instanceof Error ? err.message : 'Unknown error')
      } finally {
        setLoading(false)
      }
    }

    fetchData()
  }, [apiUrl])

  if (loading) {
    return (
      <div style={{ textAlign: 'center', padding: '2rem' }}>
        <h1>🚀 SyftUI Example</h1>
        <p>Loading...</p>
      </div>
    )
  }

  if (error) {
    return (
      <div style={{ textAlign: 'center', padding: '2rem' }}>
        <h1>🚀 SyftUI Example</h1>
        <p style={{ color: 'red' }}>Error: {error}</p>
        <p>Make sure the backend is running on {apiUrl}</p>
      </div>
    )
  }

  return (
    <div style={{ 
      maxWidth: '800px', 
      margin: '0 auto', 
      textAlign: 'center',
      backgroundColor: 'white',
      padding: '2rem',
      borderRadius: '8px',
      boxShadow: '0 2px 10px rgba(0,0,0,0.1)'
    }}>
      <h1 style={{ 
        color: '#333',
        marginBottom: '2rem',
        fontSize: '2.5rem'
      }}>
        🚀 SyftUI Example
      </h1>
      
      {hello && (
        <div style={{ 
          marginBottom: '2rem',
          padding: '1rem',
          backgroundColor: '#e8f5e8',
          borderRadius: '6px'
        }}>
          <h2 style={{ color: '#2d5d2d' }}>
            {hello.message}
          </h2>
          <p style={{ color: '#666', fontSize: '0.9rem' }}>
            User: {hello.user_email}
          </p>
          <p style={{ color: '#666', fontSize: '0.9rem' }}>
            Received at: {new Date(hello.timestamp).toLocaleString()}
          </p>
        </div>
      )}

      {status && (
        <div style={{
          padding: '1rem',
          backgroundColor: '#f0f8ff',
          borderRadius: '6px',
          marginBottom: '2rem'
        }}>
          <h3 style={{ color: '#1e3a8a' }}>Application Status</h3>
          <p><strong>App:</strong> {status.app} v{status.version}</p>
          
          {/* SyftBox Status */}
          <div style={{
            margin: '1rem 0',
            padding: '0.75rem',
            backgroundColor: status.syftbox.status === 'connected' ? '#dcfce7' : '#fef3c7',
            borderRadius: '4px'
          }}>
            <strong>SyftBox:</strong> 
            <span style={{ 
              color: status.syftbox.status === 'connected' ? 'green' : 'orange',
              marginLeft: '0.5rem'
            }}>
              {status.syftbox.status}
            </span>
            {status.syftbox.status === 'connected' && (
              <div style={{ fontSize: '0.9rem', marginTop: '0.25rem' }}>
                Logged in as: {status.syftbox.user_email}
              </div>
            )}
          </div>

          <div style={{ 
            display: 'grid', 
            gridTemplateColumns: 'repeat(auto-fit, minmax(120px, 1fr))',
            gap: '1rem',
            marginTop: '1rem'
          }}>
            <div>
              <strong>Backend:</strong> 
              <span style={{ 
                color: status.components.backend === 'running' ? 'green' : 'red',
                marginLeft: '0.5rem'
              }}>
                {status.components.backend}
              </span>
            </div>
            <div>
              <strong>Frontend:</strong> 
              <span style={{ 
                color: status.components.frontend === 'available' ? 'green' : 'red',
                marginLeft: '0.5rem'
              }}>
                {status.components.frontend}
              </span>
            </div>
            <div>
              <strong>Cron:</strong> 
              <span style={{ 
                color: status.components.cron === 'available' ? 'green' : 'red',
                marginLeft: '0.5rem'
              }}>
                {status.components.cron}
              </span>
            </div>
          </div>
        </div>
      )}

      <div style={{ 
        fontSize: '0.9rem', 
        color: '#666',
        borderTop: '1px solid #eee',
        paddingTop: '1rem'
      }}>
        <p>This is a minimal SyftUI example with:</p>
        <ul style={{ 
          listStyle: 'none', 
          padding: 0,
          display: 'flex',
          justifyContent: 'center',
          gap: '2rem',
          flexWrap: 'wrap'
        }}>
          <li>✅ Next.js Frontend</li>
          <li>✅ FastAPI Backend</li>
          <li>✅ SyftBox Integration</li>
          <li>✅ Cron Job Component</li>
        </ul>
      </div>
    </div>
  )
} 