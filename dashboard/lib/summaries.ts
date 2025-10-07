import fs from 'fs/promises'
import path from 'path'

export interface Episode {
  filename: string
  title: string
  content?: string
}

export interface SummaryWeek {
  date: string
  episodeCount: number
  episodes: Episode[]
  generatedAt: string
  path: string
}

/**
 * Get all summary weeks, sorted by date (newest first)
 */
export async function getSummaryWeeks(): Promise<SummaryWeek[]> {
  const summariesDir = path.join(process.cwd(), 'public', 'summaries')

  try {
    // Check if summaries directory exists
    await fs.access(summariesDir)

    const weeks = await fs.readdir(summariesDir)

    const weekData = await Promise.all(
      weeks
        .filter(week => week.match(/^\d{4}-\d{2}-\d{2}$/)) // Only YYYY-MM-DD folders
        .map(async (weekDate) => {
          try {
            const metadataPath = path.join(summariesDir, weekDate, 'metadata.json')
            const metadata = JSON.parse(await fs.readFile(metadataPath, 'utf-8'))

            return {
              date: weekDate,
              episodeCount: metadata.episodeCount || 0,
              episodes: metadata.episodes || [],
              generatedAt: metadata.generatedAt || weekDate,
              path: `/summaries/${weekDate}`,
            } as SummaryWeek
          } catch (error) {
            console.error(`Error reading metadata for ${weekDate}:`, error)
            return null
          }
        })
    )

    // Filter out null entries and sort by date (newest first)
    return weekData
      .filter((week): week is SummaryWeek => week !== null)
      .sort((a, b) => b.date.localeCompare(a.date))
  } catch (error) {
    console.error('Error reading summaries directory:', error)
    return []
  }
}

/**
 * Get a specific week's summary data
 */
export async function getWeekSummary(weekDate: string): Promise<SummaryWeek | null> {
  const summariesDir = path.join(process.cwd(), 'public', 'summaries', weekDate)

  try {
    const metadataPath = path.join(summariesDir, 'metadata.json')
    const metadata = JSON.parse(await fs.readFile(metadataPath, 'utf-8'))

    // Read content for each episode
    const episodesWithContent = await Promise.all(
      metadata.episodes.map(async (episode: Episode) => {
        try {
          const contentPath = path.join(summariesDir, episode.filename)
          const content = await fs.readFile(contentPath, 'utf-8')
          return { ...episode, content }
        } catch (error) {
          console.error(`Error reading ${episode.filename}:`, error)
          return { ...episode, content: 'Content not available' }
        }
      })
    )

    return {
      date: weekDate,
      episodeCount: metadata.episodeCount || 0,
      episodes: episodesWithContent,
      generatedAt: metadata.generatedAt || weekDate,
      path: `/summaries/${weekDate}`,
    }
  } catch (error) {
    console.error(`Error reading week summary for ${weekDate}:`, error)
    return null
  }
}

/**
 * Format date for display
 */
export function formatDate(dateString: string): string {
  try {
    const date = new Date(dateString)
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
    })
  } catch (error) {
    return dateString
  }
}
