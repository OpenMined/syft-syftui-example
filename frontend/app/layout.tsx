import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'SyftUI Example',
  description: 'Minimal SyftUI Example Application',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body style={{ 
        fontFamily: 'system-ui, -apple-system, sans-serif',
        margin: 0,
        padding: '2rem',
        backgroundColor: '#f5f5f5'
      }}>
        {children}
      </body>
    </html>
  )
} 