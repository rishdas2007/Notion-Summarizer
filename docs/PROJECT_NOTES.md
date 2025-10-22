# Podcast Notes Automation - Project Notes

## Project Overview

An advanced intelligent automation system that extracts podcast notes from a Notion database, converts them to markdown files, and automatically generates comprehensive AI-powered summaries using Claude API.

## System Capabilities

### Content Extraction
- Complete content extraction with pagination support (100+ blocks per page)
- Nested block handling (indented bullets, toggle content)
- Rich text formatting preservation (bold, italic, links, code)
- All major Notion block types supported

### Intelligence & Analysis (Claude Sonnet 4.5)
- **Intelligent Two-Stage Summarization**: Condenses content by ~15-60% while preserving key insights
- **Comprehensive Analysis**: 3000+ word detailed summaries
- **Pattern Recognition**: Identifies themes, cause-effect relationships
- **Technical Context**: Explains complex concepts and industry terminology
- **Actionable Intelligence**: Specific recommendations and research directions

### Automation & Reliability
- Automatic date logic (last 7 days)
- Robust error handling
- Comprehensive logging
- Duplicate detection (skips existing files)
- Fallback systems if Claude API unavailable

## Architecture

### Two-Stage Intelligent Summarization

**Stage 1: Intelligent Parsing**
- Extracts structured data (metadata, topics, transcripts)
- Identifies key discussion segments
- Compresses content by 15-60% while preserving insights
- Target: ~40K tokens from original ~16-96K tokens

**Stage 2: AI Summarization**
- Uses Claude Sonnet 4.5 (200K context, 16K output)
- Generates comprehensive executive summaries
- Detailed analysis with key insights
- Definitions, methodology, and citations

### Cost Efficiency
- **Before optimization**: ~$1.50-2.00 per episode
- **After optimization**: ~$0.30-0.60 per episode
- **Savings**: 60-70% reduction in API costs

## Configuration

All sensitive configuration is managed via environment variables:

```bash
# Required
NOTION_TOKEN=<your_notion_integration_token>
NOTION_DATABASE_ID=<your_database_id>
ANTHROPIC_API_KEY=<your_anthropic_api_key>

# Optional (with defaults)
OUTPUT_FOLDER=./output/podcast_notes
OBSIDIAN_FOLDER=./output/summaries
CLAUDE_MODEL=claude-sonnet-4-5-20250929
CLAUDE_MAX_TOKENS=16384
BATCH_EPISODES=false
```

See `.env.example` for a complete template.

## Notion Database Schema

Required properties:
- **Episode** (Title) - Main episode title
- **Episode publish date** (Date) - Publication timestamp
- **Show** (Rich text) - Podcast show name
- **Content** - Full episode notes in page body

## Output Files

### Episode Files (Markdown)
- **Location**: `OUTPUT_FOLDER`
- **Format**: `YYYY-MM-DDTHH:MM:SS.000+00:00_Episode-Title.md`
- **Content**: Complete episode transcript with metadata

### Summary Files
- **Location**: `OBSIDIAN_FOLDER` (or your preferred output)
- **Format**: `Podcast_Name_Summary.md`
- **Content**: Comprehensive AI-generated analysis with:
  - Executive Summary
  - Table of Contents
  - Detailed Analysis
  - Key Insights and Implications
  - Data and Figures
  - Definitions and Terminology
  - Methodology
  - References and Citations

## Technical Implementation

### Intelligent Parser (`intelligent_parser.py`)
- Parses Notion markdown structure
- Extracts metadata, topics, and transcripts
- Compresses content intelligently
- Preserves key dialogue and insights

### Notion Client (`notion_client_handler.py`)
- Handles API pagination (100+ blocks per page)
- Recursively fetches nested content
- Preserves block relationships

### Markdown Converter (`markdown_converter.py`)
- Converts all Notion block types to markdown
- Preserves rich text formatting
- Handles nested structures with proper indentation

### Summarizer (`batch_summary_generator.py`)
- Manages Claude API integration
- Implements two-stage summarization
- Handles retries and error recovery
- Processes episodes individually or in batch

## Performance Metrics

### Test Results (Week of Sept 30 - Oct 6, 2025)
- **Episodes Processed**: 6
- **Token Reduction**: 15-60% (avg 29%)
- **Processing Time**: ~2-3 min per episode
- **API Cost**: ~$0.30-0.60 per episode
- **Success Rate**: 100%

### Example Compressions
| Episode | Original Tokens | Condensed Tokens | Reduction |
|---------|----------------|------------------|-----------|
| Free Speech | 16,622 | 13,762 | 17.2% |
| Corporate Dev | 38,161 | 28,539 | 25.2% |
| Marc/John/Charlie | 57,333 | 23,632 | 58.8% |

## Security & Privacy

- ✅ No hardcoded secrets
- ✅ Environment variable based configuration
- ✅ `.gitignore` excludes logs, cache, and secrets
- ✅ Portable across systems
- ✅ Production-ready architecture

## Development History

### October 2025 - Sonnet 4.5 Optimization
- Upgraded to Claude Sonnet 4.5 (200K context)
- Implemented intelligent two-stage summarization
- Increased output tokens to 16,384
- Achieved 60-70% cost reduction
- Removed deprecated batch processing code

### September 2025 - Individual Processing
- Fixed date logic (last 7 days instead of work week)
- Individual episode processing
- Summary v7 prompt integration
- Obsidian vault integration
- Smart duplicate detection

### August 2025 - Initial Release
- Basic Notion extraction
- Markdown conversion
- Claude API integration
- Pagination support
