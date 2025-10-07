import { getSummaryWeeks } from '@/lib/summaries'
import SummaryCard from '@/components/SummaryCard'

export default async function Home() {
  const weeks = await getSummaryWeeks()
  const latestWeeks = weeks.slice(0, 6)

  return (
    <div style={{ background: 'var(--background)' }} className="py-12">
      <div className="container-custom">
        {/* Hero Section */}
        <div className="text-center mb-12">
          <h1 className="text-4xl sm:text-5xl font-bold mb-4" style={{ color: 'var(--text-primary)' }}>
            Latest Podcast Summaries
          </h1>
          <p className="text-lg sm:text-xl max-w-2xl mx-auto" style={{ color: 'var(--text-secondary)' }}>
            Stay informed with AI-powered summaries of your favorite podcast episodes
          </p>
        </div>

        {latestWeeks.length === 0 ? (
          /* Empty State */
          <div className="empty-state">
            <div className="max-w-md mx-auto">
              <div className="card p-8 sm:p-12">
                <div className="empty-state-icon mx-auto mb-6">
                  <svg
                    fill="none"
                    stroke="currentColor"
                    strokeWidth={1.5}
                    viewBox="0 0 24 24"
                    style={{ color: 'var(--secondary)' }}
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      d="M19.114 5.636a9 9 0 010 12.728M16.463 8.288a5.25 5.25 0 010 7.424M6.75 8.25l4.72-4.72a.75.75 0 011.28.53v15.88a.75.75 0 01-1.28.53l-4.72-4.72H4.51c-.88 0-1.704-.507-1.938-1.354A9.01 9.01 0 012.25 12c0-.83.112-1.633.322-2.396C2.806 8.756 3.63 8.25 4.51 8.25H6.75z"
                    />
                  </svg>
                </div>
                <h3 className="text-2xl font-bold mb-3" style={{ color: 'var(--text-primary)' }}>
                  No Summaries Yet
                </h3>
                <p className="text-base mb-6" style={{ color: 'var(--text-secondary)' }}>
                  New summaries are automatically generated every Sunday at 9 AM UTC
                </p>
                <div className="flex flex-col sm:flex-row gap-3 justify-center">
                  <a
                    href="/summaries"
                    className="btn btn-primary"
                  >
                    View Archive
                  </a>
                  <a
                    href="https://github.com/rishdas2007/Notion-Summarizer"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="btn"
                    style={{
                      background: 'transparent',
                      border: '2px solid var(--border)',
                      color: 'var(--text-primary)'
                    }}
                  >
                    <svg className="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M10 0C4.477 0 0 4.484 0 10.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0110 4.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.203 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.942.359.31.678.921.678 1.856 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0020 10.017C20 4.484 15.522 0 10 0z" clipRule="evenodd" />
                    </svg>
                    View Code
                  </a>
                </div>
              </div>
            </div>
          </div>
        ) : (
          <>
            {/* Summary Grid - Latest 6 */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-16">
              {latestWeeks.map(week => (
                <SummaryCard key={week.date} week={week} />
              ))}
            </div>

            {/* Table of Contents - All Summaries */}
            <div className="card p-6 sm:p-8 mb-12">
              <div className="flex items-center justify-between mb-6">
                <h2 className="text-2xl sm:text-3xl font-bold" style={{ color: 'var(--text-primary)' }}>
                  All Summaries
                </h2>
                <span className="px-3 py-1 rounded-full text-sm font-semibold" style={{
                  background: 'var(--primary)',
                  color: 'white'
                }}>
                  {weeks.length} {weeks.length === 1 ? 'Week' : 'Weeks'}
                </span>
              </div>

              <div className="space-y-3">
                {weeks.map((week, index) => (
                  <a
                    key={week.date}
                    href={week.path}
                    className="block p-4 rounded-lg transition-all hover:shadow-md"
                    style={{
                      background: index % 2 === 0 ? 'var(--background)' : 'transparent',
                      border: '1px solid var(--border)'
                    }}
                  >
                    <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2">
                      <div className="flex-1">
                        <div className="flex items-center gap-3 mb-1">
                          <span className="font-semibold text-lg" style={{ color: 'var(--text-primary)' }}>
                            Week of {new Date(week.date).toLocaleDateString('en-US', {
                              month: 'long',
                              day: 'numeric',
                              year: 'numeric'
                            })}
                          </span>
                          <span className="px-2 py-0.5 rounded text-xs font-medium" style={{
                            background: 'var(--accent)',
                            color: 'white'
                          }}>
                            {week.episodeCount} {week.episodeCount === 1 ? 'episode' : 'episodes'}
                          </span>
                        </div>
                        <p className="text-sm" style={{ color: 'var(--text-secondary)' }}>
                          {week.episodes.slice(0, 2).map(ep => ep.title).join(' • ')}
                          {week.episodes.length > 2 && ` • +${week.episodes.length - 2} more`}
                        </p>
                      </div>
                      <div className="flex items-center gap-2 text-sm" style={{ color: 'var(--text-secondary)' }}>
                        <svg className="w-4 h-4" fill="none" stroke="currentColor" strokeWidth={2} viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                        </svg>
                        <span className="hidden sm:inline">{week.date}</span>
                        <svg className="w-5 h-5 ml-2" style={{ color: 'var(--primary)' }} fill="none" stroke="currentColor" strokeWidth={2} viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" d="M9 5l7 7-7 7" />
                        </svg>
                      </div>
                    </div>
                  </a>
                ))}
              </div>
            </div>
          </>
        )}
      </div>
    </div>
  )
}
