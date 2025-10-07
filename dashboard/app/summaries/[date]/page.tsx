import { getWeekSummary, getSummaryWeeks, formatDate } from '@/lib/summaries'
import MarkdownRenderer from '@/components/MarkdownRenderer'
import { notFound } from 'next/navigation'

interface WeekPageProps {
  params: {
    date: string
  }
}

// Don't generate pages for params not returned by generateStaticParams
export const dynamicParams = false

// Generate static params for all weeks
export async function generateStaticParams() {
  try {
    const weeks = await getSummaryWeeks()
    if (weeks.length === 0) {
      console.log('No summaries found yet')
      return []
    }
    return weeks.map(week => ({
      date: week.date,
    }))
  } catch (error) {
    // Return empty array if no summaries exist yet
    console.log('Error reading summaries:', error)
    return []
  }
}

export default async function WeekPage({ params }: WeekPageProps) {
  const weekData = await getWeekSummary(params.date)

  if (!weekData) {
    notFound()
  }

  return (
    <div style={{ background: 'var(--background)' }} className="py-8 sm:py-12 min-h-screen">
      <div className="container-custom max-w-5xl">
        {/* Header */}
        <div className="mb-8">
          <a
            href="/summaries"
            className="inline-flex items-center mb-4 font-medium hover:opacity-80 transition-opacity"
            style={{ color: 'var(--primary)' }}
          >
            <svg
              className="w-5 h-5 mr-2"
              fill="none"
              stroke="currentColor"
              strokeWidth={2}
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                d="M10 19l-7-7m0 0l7-7m-7 7h18"
              />
            </svg>
            Back to Archive
          </a>

          <h1 className="text-3xl sm:text-4xl font-bold mb-3" style={{ color: 'var(--text-primary)' }}>
            Week of {formatDate(weekData.date)}
          </h1>
          <p className="text-base sm:text-lg" style={{ color: 'var(--text-secondary)' }}>
            {weekData.episodeCount} {weekData.episodeCount === 1 ? 'episode' : 'episodes'} summarized
          </p>
        </div>

        {/* Episodes */}
        <div className="space-y-8 sm:space-y-12">
          {weekData.episodes.map((episode, index) => (
            <article
              key={index}
              className="card p-6 sm:p-8"
            >
              <div className="mb-6">
                <div className="flex items-center space-x-2 text-sm mb-3" style={{ color: 'var(--text-secondary)' }}>
                  <svg
                    className="w-4 h-4"
                    fill="currentColor"
                    viewBox="0 0 20 20"
                  >
                    <path
                      fillRule="evenodd"
                      d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z"
                      clipRule="evenodd"
                    />
                  </svg>
                  <span className="font-medium">Episode {index + 1} of {weekData.episodeCount}</span>
                </div>
                <h2 className="text-2xl sm:text-3xl font-bold leading-tight" style={{ color: 'var(--text-primary)' }}>
                  {episode.title}
                </h2>
              </div>

              <div className="markdown-content">
                <MarkdownRenderer content={episode.content || 'Content not available'} />
              </div>
            </article>
          ))}
        </div>

        {/* Navigation */}
        <div className="mt-12 pt-8" style={{ borderTop: '1px solid var(--border)' }}>
          <div className="flex flex-col sm:flex-row gap-4 justify-between">
            <a
              href="/summaries"
              className="btn inline-flex items-center justify-center"
              style={{
                background: 'transparent',
                border: '2px solid var(--border)',
                color: 'var(--text-primary)'
              }}
            >
              <svg
                className="w-5 h-5 mr-2"
                fill="none"
                stroke="currentColor"
                strokeWidth={2}
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  d="M4 6h16M4 12h16M4 18h16"
                />
              </svg>
              View All Weeks
            </a>
            <a
              href="/"
              className="btn btn-primary inline-flex items-center justify-center"
            >
              <svg
                className="w-5 h-5 mr-2"
                fill="none"
                stroke="currentColor"
                strokeWidth={2}
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
                />
              </svg>
              Home
            </a>
          </div>
        </div>
      </div>
    </div>
  )
}
