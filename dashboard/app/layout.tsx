import type { Metadata } from "next"
import "./globals.css"

export const metadata: Metadata = {
  title: "Podcast Summaries | AI-Powered Weekly Insights",
  description: "Automated podcast episode summaries powered by Claude AI. Stay informed with key insights from your favorite podcasts.",
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="en">
      <body>
        <header style={{
          background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
          boxShadow: '0 2px 10px rgba(0, 0, 0, 0.1)'
        }} className="text-white py-4 sticky top-0 z-50">
          <nav className="container-custom">
            <div className="flex items-center justify-between">
              <a href="/" className="flex items-center space-x-2 hover:opacity-80 transition-opacity">
                <svg className="w-8 h-8" fill="currentColor" viewBox="0 0 20 20">
                  <path d="M18 3a1 1 0 00-1.196-.98l-10 2A1 1 0 006 5v9.114A4.369 4.369 0 005 14c-1.657 0-3 .895-3 2s1.343 2 3 2 3-.895 3-2V7.82l8-1.6v5.894A4.37 4.37 0 0015 12c-1.657 0-3 .895-3 2s1.343 2 3 2 3-.895 3-2V3z" />
                </svg>
                <span className="text-xl font-bold hidden sm:inline">Podcast Summaries</span>
                <span className="text-xl font-bold sm:hidden">Summaries</span>
              </a>
              <div className="flex items-center space-x-1 sm:space-x-4">
                <a
                  href="/"
                  className="px-3 py-2 rounded-lg hover:bg-white/20 transition-colors font-medium text-sm sm:text-base"
                >
                  Home
                </a>
                <a
                  href="/summaries"
                  className="px-3 py-2 rounded-lg hover:bg-white/20 transition-colors font-medium text-sm sm:text-base"
                >
                  Archive
                </a>
              </div>
            </div>
          </nav>
        </header>

        <main className="min-h-screen">
          {children}
        </main>

        <footer style={{ background: 'var(--surface)', borderTop: '1px solid var(--border)' }} className="py-12 mt-20">
          <div className="container-custom">
            <div className="text-center">
              <div className="flex items-center justify-center space-x-2 mb-4">
                <svg className="w-6 h-6" style={{ color: 'var(--primary)' }} fill="currentColor" viewBox="0 0 20 20">
                  <path d="M2 5a2 2 0 012-2h7a2 2 0 012 2v4a2 2 0 01-2 2H9l-3 3v-3H4a2 2 0 01-2-2V5z" />
                  <path d="M15 7v2a4 4 0 01-4 4H9.828l-1.766 1.767c.28.149.599.233.938.233h2l3 3v-3h2a2 2 0 002-2V9a2 2 0 00-2-2h-1z" />
                </svg>
                <span className="font-semibold" style={{ color: 'var(--text-primary)' }}>Automated Podcast Insights</span>
              </div>
              <p style={{ color: 'var(--text-secondary)' }} className="text-sm">
                Powered by Claude AI • Generated weekly • Always up to date
              </p>
              <p style={{ color: 'var(--text-secondary)' }} className="text-xs mt-2 opacity-60">
                © 2025 Podcast Summaries Dashboard
              </p>
            </div>
          </div>
        </footer>
      </body>
    </html>
  )
}
