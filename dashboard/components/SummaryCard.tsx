import { SummaryWeek, formatDate } from '@/lib/summaries'

interface SummaryCardProps {
  week: SummaryWeek
}

export default function SummaryCard({ week }: SummaryCardProps) {
  return (
    <a
      href={week.path}
      className="block p-6 bg-white rounded-lg border border-gray-200 shadow-md hover:shadow-lg hover:border-blue-500 transition-all duration-200"
    >
      <div className="mb-3">
        <h2 className="text-xl font-bold text-gray-900 mb-1">
          Week of {formatDate(week.date)}
        </h2>
        <p className="text-sm text-gray-500">
          {week.date}
        </p>
      </div>

      <div className="flex items-center justify-between">
        <div className="flex items-center space-x-2">
          <svg
            className="w-5 h-5 text-blue-600"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z"
            />
          </svg>
          <span className="text-gray-700 font-medium">
            {week.episodeCount} {week.episodeCount === 1 ? 'episode' : 'episodes'}
          </span>
        </div>

        <span className="text-blue-600 font-medium">
          View →
        </span>
      </div>

      {week.episodes.length > 0 && (
        <div className="mt-4 pt-4 border-t border-gray-200">
          <p className="text-sm text-gray-600 font-medium mb-2">Episodes:</p>
          <ul className="text-sm text-gray-600 space-y-1">
            {week.episodes.slice(0, 3).map((episode, index) => (
              <li key={index} className="truncate">
                • {episode.title}
              </li>
            ))}
            {week.episodes.length > 3 && (
              <li className="text-gray-500 italic">
                +{week.episodes.length - 3} more
              </li>
            )}
          </ul>
        </div>
      )}
    </a>
  )
}
