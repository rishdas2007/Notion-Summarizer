import { getWeekSummary, getSummaryWeeks, formatDate } from '@/lib/summaries'
import MarkdownRenderer from '@/components/MarkdownRenderer'
import { notFound } from 'next/navigation'

interface WeekPageProps {
  params: {
    date: string
  }
}

// Generate static params for all weeks
export async function generateStaticParams() {
  try {
    const weeks = await getSummaryWeeks()
    return weeks.map(week => ({
      date: week.date,
    }))
  } catch (error) {
    // Return empty array if no summaries exist yet
    console.log('No summaries found, returning empty params')
    return []
  }
}

// Don't generate pages for params not returned by generateStaticParams
export const dynamicParams = false

export default async function WeekPage({ params }: WeekPageProps) {
  const weekData = await getWeekSummary(params.date)

  if (!weekData) {
    notFound()
  }

  return (
    <div className="container mx-auto px-4 py-12">
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="mb-8">
          <a
            href="/summaries"
            className="inline-flex items-center text-blue-600 hover:text-blue-700 mb-4"
          >
            <svg
              className="w-5 h-5 mr-2"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M10 19l-7-7m0 0l7-7m-7 7h18"
              />
            </svg>
            Back to Archive
          </a>

          <h1 className="text-4xl font-bold text-gray-900 mb-2">
            Week of {formatDate(weekData.date)}
          </h1>
          <p className="text-gray-600">
            {weekData.episodeCount} {weekData.episodeCount === 1 ? 'episode' : 'episodes'} summarized
          </p>
        </div>

        {/* Episodes */}
        <div className="space-y-12">
          {weekData.episodes.map((episode, index) => (
            <article
              key={index}
              className="bg-white rounded-lg shadow-md p-8 border border-gray-200"
            >
              <div className="mb-6">
                <div className="flex items-center space-x-2 text-sm text-gray-500 mb-2">
                  <svg
                    className="w-4 h-4"
                    fill="currentColor"
                    viewBox="0 0 20 20"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      fillRule="evenodd"
                      d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z"
                      clipRule="evenodd"
                    />
                  </svg>
                  <span>Episode {index + 1} of {weekData.episodeCount}</span>
                </div>
                <h2 className="text-2xl font-bold text-gray-900">
                  {episode.title}
                </h2>
              </div>

              <div className="prose prose-slate max-w-none">
                <MarkdownRenderer content={episode.content || 'Content not available'} />
              </div>
            </article>
          ))}
        </div>

        {/* Navigation */}
        <div className="mt-12 pt-8 border-t border-gray-200">
          <div className="flex justify-between items-center">
            <a
              href="/summaries"
              className="inline-flex items-center px-4 py-2 border border-gray-300 rounded-md text-gray-700 hover:bg-gray-50 transition-colors"
            >
              <svg
                className="w-5 h-5 mr-2"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M4 6h16M4 12h16M4 18h16"
                />
              </svg>
              View All Weeks
            </a>
            <a
              href="/"
              className="inline-flex items-center px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-colors"
            >
              Home
              <svg
                className="w-5 h-5 ml-2"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
                />
              </svg>
            </a>
          </div>
        </div>
      </div>
    </div>
  )
}
