import os
import logging
from datetime import datetime
from notion_client_handler import NotionClient
from markdown_converter import MarkdownConverter
from config import OUTPUT_FOLDER, GENERATE_WEEKLY_SUMMARY, USE_CLAUDE_API

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('podcast_automation.log'),
        logging.StreamHandler()
    ]
)

def main():
    """Main function to process weekly podcast notes"""
    # Validate configuration first
    from config import validate_config
    try:
        validate_config()
    except ValueError as e:
        logging.error(f"Configuration error: {e}")
        return

    logging.info("Starting podcast notes extraction...")

    # Show date range being processed
    from config import get_week_date_range
    start_date, end_date = get_week_date_range()
    logging.info(f"Processing episodes from the last 7 days: {start_date} to {end_date}")
    
    # Initialize clients
    notion_client = NotionClient()
    converter = MarkdownConverter()
    
    # Ensure output directory exists
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    
    # Get episodes from the past week
    episodes = notion_client.get_weekly_episodes()
    logging.info(f"Found {len(episodes)} episodes from this week")
    
    if not episodes:
        logging.info("No episodes found for this week")
        return
    
    # Store episode data for summary generation
    episodes_data = []
    
    # Process each episode
    successful_exports = 0
    skipped_duplicates = 0
    for episode in episodes:
        try:
            page_id = episode["id"]
            logging.info(f"Processing episode: {page_id}")
            
            # Get full page content first to generate filename
            page, blocks = notion_client.get_page_content(page_id)
            
            if not page:
                logging.warning(f"Could not fetch content for {page_id}")
                continue
            
            # Generate filename to check if it already exists
            filename = converter.generate_filename(page)
            filepath = os.path.join(OUTPUT_FOLDER, filename)
            
            # Check if file already exists (duplicate detection)
            if os.path.exists(filepath):
                logging.info(f"⏭️ Skipping existing file: {filename}")
                # Still add to episodes_data for summary generation if needed
                episodes_data.append({
                    'page': page,
                    'blocks': blocks
                })
                skipped_duplicates += 1
                continue
            
            # Store for summary generation
            episodes_data.append({
                'page': page,
                'blocks': blocks
            })
            
            # Convert to markdown
            markdown_content = converter.convert_page_to_markdown(page, blocks)

            # Save individual episode
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(markdown_content)

            # Save metadata for MLA citation generation
            import json
            metadata_filepath = filepath.replace('.md', '_metadata.json')
            metadata = converter.extract_metadata_for_citation(page)
            with open(metadata_filepath, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2)

            logging.info(f"Successfully saved: {filename}")
            successful_exports += 1
            
        except Exception as e:
            logging.error(f"Error processing episode {page_id}: {e}")
            continue
    
    # Generate individual episode summaries if enabled
    summaries_generated = 0
    if successful_exports > 0 and GENERATE_WEEKLY_SUMMARY and USE_CLAUDE_API:
        try:
            logging.info("🚀 Starting individual episode summary generation...")
            from batch_summary_generator import BatchSummaryGenerator
            
            # Initialize the batch summary generator
            batch_generator = BatchSummaryGenerator()
            
            # Process episodes individually with Summary v7 prompt
            individual_summaries = batch_generator.process_episodes_individually()
            
            if individual_summaries:
                summaries_generated = len(individual_summaries)
                logging.info(f"✅ Generated {summaries_generated} individual episode summaries")
                for summary_path in individual_summaries:
                    logging.info(f"   - {os.path.basename(summary_path)}")
            else:
                logging.warning("❌ No individual summaries were generated")
            
        except Exception as e:
            logging.error(f"Error generating individual summaries: {e}")
    elif not USE_CLAUDE_API:
        logging.info("⏭️ Skipping individual summaries (Claude API disabled)")
    elif successful_exports == 0:
        logging.info("⏭️ Skipping individual summaries (no new episodes processed)")
    
    logging.info(f"Completed! Successfully exported {successful_exports} new episodes, skipped {skipped_duplicates} existing files, and generated {summaries_generated} individual episode summaries")

if __name__ == "__main__":
    main()