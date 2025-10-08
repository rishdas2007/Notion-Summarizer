import type { Metadata } from "next"
import "./globals.css"

export const metadata: Metadata = {
  title: "Rishabh's Podcast Summaries | AI-Powered Weekly Insights",
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
              <div className="flex flex-col">
                <a href="/" className="flex items-center space-x-2 hover:opacity-80 transition-opacity mb-2">
                  <svg className="w-8 h-8" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M18 3a1 1 0 00-1.196-.98l-10 2A1 1 0 006 5v9.114A4.369 4.369 0 005 14c-1.657 0-3 .895-3 2s1.343 2 3 2 3-.895 3-2V7.82l8-1.6v5.894A4.37 4.37 0 0015 12c-1.657 0-3 .895-3 2s1.343 2 3 2 3-.895 3-2V3z" />
                  </svg>
                  <span className="text-xl font-bold hidden sm:inline">Rishabh's Podcast Summaries</span>
                  <span className="text-xl font-bold sm:hidden">Rishabh's Summaries</span>
                </a>
                <div className="flex items-center space-x-3 ml-10 text-sm">
                  <a
                    href="https://rishabhdas.substack.com/"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="hover:opacity-80 transition-opacity flex items-center space-x-1"
                  >
                    <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                      <path d="M22.539 8.242H1.46V5.406h21.08v2.836zM1.46 10.812V24L12 18.11 22.54 24V10.812H1.46zM22.54 0H1.46v2.836h21.08V0z"/>
                    </svg>
                    <span className="hidden sm:inline">Substack</span>
                  </a>
                  <a
                    href="https://das-crypto-newsletter.beehiiv.com/"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="hover:opacity-80 transition-opacity flex items-center space-x-1"
                  >
                    <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                      <path d="M12 2L2 7v10c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-10-5zm0 18c-3.31 0-6-2.69-6-6s2.69-6 6-6 6 2.69 6 6-2.69 6-6 6z"/>
                    </svg>
                    <span className="hidden sm:inline">Crypto Blog</span>
                  </a>
                  <a
                    href="https://www.linkedin.com/in/rishabh-das/"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="hover:opacity-80 transition-opacity flex items-center space-x-1"
                  >
                    <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                      <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
                    </svg>
                    <span className="hidden sm:inline">LinkedIn</span>
                  </a>
                </div>
              </div>
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
