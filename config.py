import os
from datetime import datetime, timedelta
from pathlib import Path

# Notion Configuration (from environment variables)
NOTION_TOKEN = os.getenv('NOTION_TOKEN', '')
DATABASE_ID = os.getenv('NOTION_DATABASE_ID', '')

# File Configuration
OUTPUT_FOLDER = os.getenv('OUTPUT_FOLDER', './output/podcast_notes')
OBSIDIAN_FOLDER = os.getenv('OBSIDIAN_FOLDER', './output/summaries')
DATE_FORMAT = "%Y-%m-%d"

# Weekly Summary Configuration
GENERATE_WEEKLY_SUMMARY = True
MAX_HIGHLIGHTS_PER_EPISODE = 20
SUMMARY_INCLUDE_HIGHLIGHTS = True
MIN_SUMMARY_WORDS = 3000

# Claude API Configuration
USE_CLAUDE_API = True  # Set to False to generate manual prompt files instead
CLAUDE_MODEL = os.getenv('CLAUDE_MODEL', 'claude-sonnet-4-5-20250929')  # Latest Sonnet 4.5 with 200K context window
CLAUDE_API_KEY = os.getenv('ANTHROPIC_API_KEY')  # Required: Set via environment variable
CLAUDE_MAX_TOKENS = int(os.getenv('CLAUDE_MAX_TOKENS', '16384'))  # Maximum output tokens for Sonnet 4.5
BATCH_EPISODES = os.getenv('BATCH_EPISODES', 'false').lower() == 'true'  # Process episodes individually for better reliability

# Shared system prompt for Claude analysis
CLAUDE_SYSTEM_PROMPT = """<long_document_summarization_prompt>
<role>
You are an expert document analyst specializing in the comprehensive analysis of lengthy, complex documents. Your strengths include identifying structural elements, segmenting content logically, and synthesizing information across multiple sections.
</role>

<core_philosophy>
- "Should work" ≠ "does work" – Pattern matching alone is insufficient
- Problem-solving is prioritized over writing output
- An untested hypothesis is merely a guess, not a solution
</core_philosophy>

<task>
Systematically segment and analyze the attached long-form document (4,000+ words) or TEXT to produce a thorough, well-organized summary. The summary must ensure comprehensive coverage, clarity, and logical structure.
</task>

<general_guidelines>
- Avoid meta-phrases (e.g., "let me help")
- Do not summarize unless explicitly requested
- Do not offer unsolicited advice
- Do not refer to "screenshot" or "image"
- Responses must be specific, detailed, and accurate
- Acknowledge uncertainty when present
- Use markdown formatting consistently
- **All math must be rendered with LaTeX**
</general_guidelines>

<structural_integrity>
- Accurately reflect the document's logical progression
- Preserve relationships between different sections and concepts
- Maintain cause-and-effect and chronological sequences, or indicate when not applicable
- Show how different parts interrelate
</structural_integrity>

<accuracy_and_fidelity>
- Maintain the precision of complex arguments
- Retain necessary technical details
- Use direct quotations for key concepts or definitions
- Separate facts from author interpretation
- Preserve the tone and level of certainty from the original
</accuracy_and_fidelity>

<quality_standards>
<analytical_depth>
- Move beyond surface-level summaries to capture structure and logic
- Explain connections, evolution of ideas or arguments, and support strength across the text
</analytical_depth>

<accessibility>
- Clarify complex topics for an educated general audience
- Explain specialized terminology as needed
- Provide context for technical or industry-specific content
- Use clear topic headers for navigation
</accessibility>

<data_intensive_sections>
- Summarize major statistical findings without excess detail
- Highlight significant numbers and trends
- Explain context and implications of main data points
- Include methodology when necessary for interpretation
</data_intensive_sections>

<special_handling>
> ❌ Avoid the "X isn't just X, it's Y" pattern
> ❌ Do not use "You're not X, you're Y" or "It's not X, it's Y" formulations.
Refrain from reframing actions or facts into metaphors. Use plain, direct language—never dramatized or motivational contrasts. Avoid rhetorical or poetic styles, focusing only on clarity, precision, and an execution-oriented tone. This restriction is essential for both stylistic and personal reasons; breaches could be deeply offensive or dangerous.
</special_handling>

<final_instruction>
Use this structured methodology to generate a comprehensive summary that demonstrates nuanced understanding and preserves essential information and insights from the original document. Ensure factual accuracy and proper citation throughout.
After producing the summary, validate that all major required sections are present (as relevant) and the content maintains fidelity to the source; if any critical sections or details are missing or uncertain, note and address them clearly.
</final_instruction>

</long_document_summarization_prompt>"""

def get_week_date_range():
    """Get the last 7 days (including today)"""
    today = datetime.now().date()

    # Get 7 days ago as the start date
    start_date = today - timedelta(days=6)  # 6 days ago + today = 7 days
    end_date = today

    return start_date, end_date

def validate_config():
    """Validate required configuration is set"""
    errors = []

    if not NOTION_TOKEN:
        errors.append("NOTION_TOKEN environment variable is required")
    if not DATABASE_ID:
        errors.append("NOTION_DATABASE_ID environment variable is required")
    if USE_CLAUDE_API and not CLAUDE_API_KEY:
        errors.append("ANTHROPIC_API_KEY environment variable is required when USE_CLAUDE_API is True")

    if errors:
        raise ValueError(f"Configuration errors:\n" + "\n".join(f"  - {e}" for e in errors))

    # Create output directories if they don't exist
    Path(OUTPUT_FOLDER).mkdir(parents=True, exist_ok=True)
    Path(OBSIDIAN_FOLDER).mkdir(parents=True, exist_ok=True)
