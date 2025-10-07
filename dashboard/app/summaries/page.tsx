import { getSummaryWeeks } from '@/lib/summaries'
import SummaryCard from '@/components/SummaryCard'

export default async function SummariesArchive() {
  const weeks = await getSummaryWeeks()

  return (
    <div className="container mx-auto px-4 py-12">
      <div className="max-w-6xl mx-auto">
        <div className="mb-12">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">
            All Summaries
          </h1>
          <p className="text-lg text-gray-600">
            Complete archive of all podcast summaries, organized by week
          </p>
        </div>

        {weeks.length === 0 ? (
          <div className="text-center py-16">
            <svg
              className="mx-auto h-12 w-12 text-gray-400 mb-4"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
              />
            </svg>
            <h3 className="text-lg font-medium text-gray-900 mb-2">
              No summaries yet
            </h3>
            <p className="text-gray-600">
              Check back after the weekly automation runs on Sunday
            </p>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {weeks.map(week => (
              <SummaryCard key={week.date} week={week} />
            ))}
          </div>
        )}

        <div className="mt-12 text-center">
          <p className="text-gray-600">
            Total weeks: <span className="font-semibold">{weeks.length}</span>
          </p>
        </div>
      </div>
    </div>
  )
}
