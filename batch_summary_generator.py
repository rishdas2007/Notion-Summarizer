#!/usr/bin/env python3

import os
import glob
import logging
from pathlib import Path
from datetime import datetime, timedelta
from config import OUTPUT_FOLDER, OBSIDIAN_FOLDER, CLAUDE_API_KEY, CLAUDE_MODEL, USE_CLAUDE_API, CLAUDE_MAX_TOKENS, CLAUDE_SYSTEM_PROMPT, BATCH_EPISODES
from intelligent_parser import IntelligentPodcastParser
import re

class BatchSummaryGenerator:
    def __init__(self):
        self.script_dir = Path(__file__).parent
        self.claude_client = None
        self.parser = IntelligentPodcastParser()

        # Initialize Claude API client if configured
        if USE_CLAUDE_API:
            try:
                import anthropic
                api_key = CLAUDE_API_KEY or os.getenv('ANTHROPIC_API_KEY')
                if api_key:
                    self.claude_client = anthropic.Anthropic(api_key=api_key)
                    logging.info("✅ Claude API client initialized")
                else:
                    logging.warning("⚠️ Claude API key not found. Set ANTHROPIC_API_KEY environment variable.")
            except ImportError:
                logging.error("❌ Anthropic library not installed. Run: pip install anthropic")

    def get_recent_episode_files(self, days_back=7):
        """Get episode files from the most recent week (last 7 days)"""
        today = datetime.now().date()
        start_date = today - timedelta(days=days_back-1)  # 6 days ago + today = 7 days
        
        # Pattern to match episode files with dates
        pattern = os.path.join(OUTPUT_FOLDER, "*.md")
        all_files = glob.glob(pattern)
        
        recent_files = []
        for filepath in all_files:
            filename = os.path.basename(filepath)
            
            # Skip summary files and analysis prompts
            if any(keyword in filename.upper() for keyword in ['CLAUDE_', 'WEEKLY_SUMMARY', 'ANALYSIS_PROMPT']):
                continue
            
            # Extract date from filename (format: YYYY-MM-DDTHH:MM:SS.000+00:00_...)
            date_match = re.match(r'(\d{4}-\d{2}-\d{2})T', filename)
            if date_match:
                file_date_str = date_match.group(1)
                try:
                    file_date = datetime.strptime(file_date_str, '%Y-%m-%d').date()
                    if file_date >= start_date and file_date <= today:
                        recent_files.append(filepath)
                except ValueError:
                    continue
        
        recent_files.sort()  # Sort by filename (which includes date)
        logging.info(f"Found {len(recent_files)} recent episode files from {start_date} to {today}")
        return recent_files

    def create_summary_v7_prompt(self):
        """Create the Summary v7 prompt template using shared config"""
        return f"""{CLAUDE_SYSTEM_PROMPT}

TEXT:

{{content}}

## Output Format

- If the input document or text is missing, malformed, or below 4,000 words, reply with a single markdown code block containing:
  ```markdown
  ## Error: Document Not Suitable for Summarization
  The input document is either missing, unparseable, or does not meet the minimum length requirement of 4,000 words.
  ```

- For valid input, produce a single markdown-formatted string for the summary file. The summary must include these required top-level sections (omit those not applicable, but always include at least Sections 1–4):

  1. `# Title` (from the document)
  2. `## Table of Contents` (logical sections as links)
  3. `## Executive Summary` (main argument, objectives, key points)
  4. `## Detailed Analysis` (systematic breakdown by section or theme)
  5. `## Key Insights and Implications` (noteworthy and non-obvious conclusions)
  6. `## Data and Figures` (major statistics, using LaTeX where needed)
  7. `## Definitions and Terminology` (explanations for technical terms)
  8. `## Methodology` (explanation of data collection or process, if relevant)
  9. `## References and Citations` (source quotes or page/section references where possible)

- Omit sections only if not relevant but retain the original order. Headings should use clear markdown and anchoring.
- Note uncertainty or gaps at the appropriate points in the summary.
- If the document is non-chronological, explain its organizational logic (e.g., thematic or conceptual structure) in `## Detailed Analysis`.
- Always output a single markdown-formatted string as the summary. Do not attach files or include download links; render the summary for inline viewing only."""

    def extract_podcast_title(self, filepath):
        """Extract podcast title from the episode file content"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Look for the first # heading which should be the title
            lines = content.split('\n')
            for line in lines:
                if line.startswith('# ') and len(line.strip()) > 2:
                    title = line[2:].strip()
                    # Clean title for filename
                    clean_title = re.sub(r'[^\w\s-]', '', title).replace(' ', '_')
                    return clean_title[:100]  # Limit length
            
            # Fallback: use filename without date
            filename = os.path.basename(filepath)
            # Remove date prefix and extension
            clean_name = re.sub(r'^\d{4}-\d{2}-\d{2}T[\d:.+]+_', '', filename)
            clean_name = clean_name.replace('.md', '')
            return clean_name
            
        except Exception as e:
            logging.error(f"Error extracting title from {filepath}: {e}")
            return "Unknown_Podcast"

    def generate_episode_summary(self, episode_file):
        """Generate summary for a single episode using intelligent parsing and condensed prompt"""
        if not self.claude_client:
            logging.error("❌ Claude client not available")
            return None

        try:
            with open(episode_file, 'r', encoding='utf-8') as f:
                raw_content = f.read()
        except Exception as e:
            logging.error(f"Error reading file {episode_file}: {e}")
            return None

        # Parse and condense the content intelligently
        try:
            logging.info(f"🔍 Parsing episode content...")
            parsed_data = self.parser.parse_episode(raw_content)
            condensed_content = self.parser.create_condensed_content(parsed_data, target_tokens=40000)

            # Get participants
            participants = self.parser.extract_participants(raw_content)

            original_tokens = len(raw_content) // 4
            condensed_tokens = len(condensed_content) // 4
            reduction = ((original_tokens - condensed_tokens) / original_tokens) * 100

            logging.info(f"📊 Original: ~{original_tokens} tokens")
            logging.info(f"📊 Condensed: ~{condensed_tokens} tokens ({reduction:.1f}% reduction)")
            logging.info(f"👥 Participants: {', '.join(participants[:5])}")  # Show first 5

        except Exception as e:
            logging.error(f"Error parsing content: {e}")
            logging.info(f"⚠️ Falling back to raw content")
            condensed_content = raw_content
            participants = []

        # Create the prompt with Summary v7 template
        prompt_template = self.create_summary_v7_prompt()
        full_prompt = prompt_template.format(content=condensed_content)
        
        try:
            episode_name = os.path.basename(episode_file)
            logging.info(f"🤖 Generating summary for: {episode_name}")
            
            response = self.claude_client.messages.create(
                model=CLAUDE_MODEL,
                max_tokens=CLAUDE_MAX_TOKENS,
                temperature=0.1,
                messages=[
                    {
                        "role": "user",
                        "content": full_prompt
                    }
                ]
            )
            
            return response.content[0].text
            
        except Exception as e:
            logging.error(f"❌ Error generating summary for {os.path.basename(episode_file)}: {e}")
            return None

    def generate_batch_summary(self, episode_files, batch_size=10):
        """Generate summary for multiple episodes in a single API call"""
        if not self.claude_client:
            logging.error("❌ Claude client not available")
            return None

        # Combine content from multiple episodes
        combined_content = []
        combined_content.append(f"# Weekly Podcast Analysis ({len(episode_files)} Episodes)\n")

        for i, filepath in enumerate(episode_files, 1):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                filename = os.path.basename(filepath)
                combined_content.append(f"\n\n---\n\n## Episode {i}: {filename}\n\n{content}")

            except Exception as e:
                logging.error(f"Error reading file {filepath}: {e}")
                continue

        combined_text = "\n".join(combined_content)
        estimated_tokens = len(combined_text) // 4
        logging.info(f"📊 Batch content size: ~{estimated_tokens} tokens for {len(episode_files)} episodes")

        # Create batch analysis prompt
        prompt = f"""{CLAUDE_SYSTEM_PROMPT}

TEXT:

{combined_text}

## Output Format

Produce a comprehensive weekly summary that synthesizes ALL episodes above. The summary should:

1. `# Weekly Podcast Intelligence Report` (with date range)
2. `## Table of Contents` (logical sections as links)
3. `## Executive Summary` (overarching themes and key insights from the week)
4. `## Episode-by-Episode Analysis` (brief analysis of each episode with key points)
5. `## Cross-Episode Themes & Patterns` (synthesize common threads across multiple episodes)
6. `## Key Insights and Implications` (noteworthy conclusions from the week's content)
7. `## Technical Deep Dives` (detailed analysis of important technical topics mentioned)
8. `## Definitions and Terminology` (explanations for technical terms across all episodes)
9. `## Strategic Takeaways` (actionable insights for different stakeholder groups)
10. `## Follow-Up Research` (questions and topics worth investigating further)

Focus on cross-episode synthesis and pattern recognition. Identify themes that span multiple episodes and provide strategic context."""

        try:
            logging.info(f"🤖 Generating batch summary for {len(episode_files)} episodes...")
            logging.info(f"⏱️ This may take 2-3 minutes for large batches...")

            response = self.claude_client.messages.create(
                model=CLAUDE_MODEL,
                max_tokens=CLAUDE_MAX_TOKENS,
                temperature=0.1,
                timeout=300.0,  # 5 minute timeout
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            logging.info(f"✅ API call completed successfully")
            return response.content[0].text

        except Exception as e:
            logging.error(f"❌ Error generating batch summary: {e}")
            import traceback
            logging.error(traceback.format_exc())
            return None

    def process_episodes_individually(self):
        """Process recent episodes individually and generate summaries"""
        # Use configured Obsidian folder
        obsidian_folder = OBSIDIAN_FOLDER

        # Ensure obsidian folder exists
        os.makedirs(obsidian_folder, exist_ok=True)

        # Get recent episode files
        recent_files = self.get_recent_episode_files()

        if not recent_files:
            logging.info("No recent episode files found to process")
            return []

        # If batch mode is enabled and we have multiple episodes, use batch processing
        if BATCH_EPISODES and len(recent_files) > 1:
            logging.info(f"🚀 Batch mode enabled: Processing {len(recent_files)} episodes together")

            # Generate one comprehensive weekly summary
            today = datetime.now().date()
            start_date = today - timedelta(days=6)
            batch_summary = self.generate_batch_summary(recent_files)

            if batch_summary:
                summary_filename = f"WEEKLY_SUMMARY_{start_date.strftime('%Y-%m-%d')}_to_{today.strftime('%Y-%m-%d')}.md"
                summary_filepath = os.path.join(obsidian_folder, summary_filename)

                # Check if summary already exists
                if os.path.exists(summary_filepath):
                    logging.info(f"⏭️ Weekly summary already exists: {summary_filename}")
                    return [summary_filepath]

                # Save weekly summary
                with open(summary_filepath, 'w', encoding='utf-8') as f:
                    f.write(batch_summary)

                logging.info(f"✅ Weekly batch summary saved: {summary_filename}")
                return [summary_filepath]
            else:
                logging.error("❌ Failed to generate weekly batch summary")
                return []

        # Otherwise, process episodes individually (original behavior)
        logging.info("Processing episodes individually...")
        generated_summaries = []

        for i, episode_file in enumerate(recent_files, 1):
            logging.info(f"Processing episode {i}/{len(recent_files)}")

            # Generate summary for this episode
            summary = self.generate_episode_summary(episode_file)

            if summary:
                # Extract podcast title for filename
                podcast_title = self.extract_podcast_title(episode_file)
                summary_filename = f"{podcast_title} Summary.md"
                summary_filepath = os.path.join(obsidian_folder, summary_filename)

                # Check if summary already exists
                if os.path.exists(summary_filepath):
                    logging.info(f"⏭️ Summary already exists, skipping: {summary_filename}")
                    generated_summaries.append(summary_filepath)  # Still count as processed
                    continue

                # Save episode summary
                with open(summary_filepath, 'w', encoding='utf-8') as f:
                    f.write(summary)

                logging.info(f"✅ Episode summary saved: {summary_filename}")
                generated_summaries.append(summary_filepath)
            else:
                logging.error(f"❌ Failed to generate summary for {os.path.basename(episode_file)}")

        return generated_summaries

def main():
    """Main function to run individual episode summary generation"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('individual_summary_generation.log'),
            logging.StreamHandler()
        ]
    )
    
    logging.info("🚀 Starting individual episode summary generation for recent episodes...")
    
    generator = BatchSummaryGenerator()
    summaries = generator.process_episodes_individually()
    
    if summaries:
        logging.info(f"✅ Completed! Generated {len(summaries)} individual episode summaries:")
        for summary in summaries:
            logging.info(f"   - {os.path.basename(summary)}")
    else:
        logging.info("No summaries were generated")

if __name__ == "__main__":
    main()