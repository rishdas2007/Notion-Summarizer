import type { Metadata } from "next"
import "./globals.css"

export const metadata: Metadata = {
  title: "Podcast Summaries Dashboard",
  description: "Weekly podcast episode summaries and highlights",
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="en">
      <body>
        <header className="bg-gray-900 text-white py-6 shadow-lg">
          <div className="container mx-auto px-4">
            <h1 className="text-2xl font-bold">
              <a href="/" className="hover:text-gray-300">
                Podcast Summaries
              </a>
            </h1>
            <nav className="mt-2">
              <a href="/" className="text-gray-300 hover:text-white mr-4">
                Home
              </a>
              <a href="/summaries" className="text-gray-300 hover:text-white">
                Archive
              </a>
            </nav>
          </div>
        </header>
        <main className="min-h-screen">
          {children}
        </main>
        <footer className="bg-gray-100 py-8 mt-16">
          <div className="container mx-auto px-4 text-center text-gray-600">
            <p>Automated podcast summaries generated weekly using Claude AI</p>
          </div>
        </footer>
      </body>
    </html>
  )
}
