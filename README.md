# Podcast Automation System

> Intelligent podcast note extraction and AI-powered summarization using Claude Sonnet 4.5

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

An advanced automation system that extracts podcast episodes from Notion, converts them to markdown, and generates comprehensive AI-powered summaries using Claude's latest Sonnet 4.5 model with intelligent content compression.

### Key Features

- 🎯 **Intelligent Two-Stage Summarization**: Compresses content by 15-60% while preserving insights
- 🤖 **Claude Sonnet 4.5 Integration**: 200K context window, 16K output tokens
- 📊 **Cost Efficient**: 60-70% cost reduction vs. naive approach (~$0.30-0.60 per episode)
- 🔄 **Automatic Processing**: Fetches episodes from last 7 days automatically
- 🛡️ **Production Ready**: Environment-based config, comprehensive error handling
- 📝 **Rich Output**: Executive summaries, detailed analysis, key insights, citations
- 🌐 **Live Dashboard**: Static Next.js site with weekly summaries (auto-deploys to Vercel)

## Quick Start

### Prerequisites

- Python 3.11+
- [Notion Integration](https://www.notion.so/my-integrations) with database access
- [Anthropic API Key](https://console.anthropic.com/)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/podcast-automation.git
cd podcast-automation
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment variables**
```bash
cp .env.example .env
# Edit .env with your credentials
```

Required environment variables:
```bash
NOTION_TOKEN=your_notion_integration_token
NOTION_DATABASE_ID=your_database_id
ANTHROPIC_API_KEY=your_anthropic_api_key
```

Optional configuration:
```bash
OUTPUT_FOLDER=./output/podcast_notes  # Where markdown files are saved
OBSIDIAN_FOLDER=./output/summaries    # Where AI summaries are saved
```

4. **Run the automation**
```bash
python main.py
```

## How It Works

### Two-Stage Intelligent Summarization

**Stage 1: Intelligent Parsing** (`intelligent_parser.py`)
- Extracts structured data from Notion markdown
- Identifies key topics, timestamps, and dialogue
- Compresses content from ~16-96K → ~13-40K tokens (15-60% reduction)
- Preserves essential information while removing redundancy

**Stage 2: AI Summarization** (`batch_summary_generator.py`)
- Uses Claude Sonnet 4.5 for comprehensive analysis
- Generates 3000+ word executive summaries
- Includes: Executive Summary, Detailed Analysis, Key Insights, Definitions, Citations
- Processing time: ~2-3 minutes per episode

### Architecture

```
podcast-automation/
├── main.py                     # Main entry point
├── config.py                   # Environment-based configuration
├── notion_client_handler.py    # Notion API interface
├── markdown_converter.py       # Notion → Markdown conversion
├── intelligent_parser.py       # Content compression & extraction
├── batch_summary_generator.py  # AI summarization engine
├── requirements.txt            # Python dependencies
├── .env.example               # Configuration template
├── .gitignore                 # Security & cleanup
├── dashboard/                  # Next.js dashboard
│   ├── app/                   # Next.js App Router pages
│   ├── components/            # React components
│   ├── lib/                   # Data fetching utilities
│   └── public/summaries/      # Generated summaries (by GitHub Actions)
├── scripts/
│   └── generate_metadata.py  # Creates metadata.json for dashboard
├── .github/workflows/
│   └── podcast-automation.yml # Cloud automation + dashboard deployment
└── docs/
    ├── PROJECT_NOTES.md       # Detailed project documentation
    ├── ARCHITECTURE.md        # System design details
    ├── GITHUB_ACTIONS_SETUP.md # Cloud automation setup
    └── DASHBOARD_SETUP.md     # Dashboard deployment guide
```

## Usage

### Basic Usage

Process episodes from the last 7 days:
```bash
python main.py
```

### Manual Summary Generation

Generate summaries for existing markdown files:
```bash
python batch_summary_generator.py
```

### Configuration Options

All configuration via environment variables (see `.env.example`):

| Variable | Description | Default |
|----------|-------------|---------|
| `NOTION_TOKEN` | Notion integration token | Required |
| `NOTION_DATABASE_ID` | Database ID to query | Required |
| `ANTHROPIC_API_KEY` | Claude API key | Required |
| `OUTPUT_FOLDER` | Markdown output directory | `./output/podcast_notes` |
| `OBSIDIAN_FOLDER` | Summary output directory | `./output/summaries` |
| `CLAUDE_MODEL` | Claude model to use | `claude-sonnet-4-5-20250929` |
| `CLAUDE_MAX_TOKENS` | Max output tokens | `16384` |
| `BATCH_EPISODES` | Process in batch (experimental) | `false` |

## Output

### Episode Files (Markdown)
- **Location**: `OUTPUT_FOLDER`
- **Format**: `YYYY-MM-DDTHH:MM:SS.000+00:00_Episode-Title.md`
- **Content**: Complete transcript with metadata

### AI Summaries
- **Location**: `OBSIDIAN_FOLDER`
- **Format**: `Podcast_Name_Summary.md`
- **Sections**:
  - Executive Summary
  - Table of Contents
  - Detailed Analysis
  - Key Insights and Implications
  - Data and Figures
  - Definitions and Terminology
  - Methodology (if applicable)
  - References and Citations

## Performance

### Cost Efficiency
- **Before optimization**: ~$1.50-2.00 per episode
- **After optimization**: ~$0.30-0.60 per episode
- **Savings**: 60-70% reduction

### Processing Speed
- **Content extraction**: ~30-60 seconds
- **AI summarization**: ~2-3 minutes
- **Total per episode**: ~2.5-4 minutes

### Token Compression
| Episode Type | Original Tokens | Compressed Tokens | Reduction |
|--------------|----------------|-------------------|-----------|
| Short (30 min) | ~16K | ~13K | 17% |
| Medium (60 min) | ~38K | ~28K | 25% |
| Long (2+ hrs) | ~57K | ~23K | 59% |

## Notion Database Setup

Your Notion database should have these properties:

- **Episode** (Title) - Main episode title
- **Episode publish date** (Date) - Publication date
- **Show** (Rich text) - Podcast show name
- **Content** (Page body) - Full episode notes

Grant your integration access to the database.

## Troubleshooting

### "Configuration errors"
- Verify `.env` file exists and contains all required variables
- Check that environment variables are properly set

### "No episodes found"
- Check date range in logs (last 7 days)
- Verify Notion database has recent episodes
- Confirm integration has database access

### "Claude API error"
- Verify `ANTHROPIC_API_KEY` is correct
- Check API quota/limits at console.anthropic.com
- Review logs for specific error messages

### "Summary already exists, skipping"
- This is normal behavior (prevents duplicates)
- Delete existing summary file to regenerate

## Deployment Options

### Option 1: GitHub Actions + Vercel Dashboard ⭐ Recommended

**Complete cloud solution** - Automation runs weekly, summaries appear on live dashboard!

**Setup Overview**:
1. **Automation**: GitHub Actions runs every Sunday
   - Processes new episodes
   - Generates AI summaries
   - Commits to repository
   - See [docs/GITHUB_ACTIONS_SETUP.md](docs/GITHUB_ACTIONS_SETUP.md)

2. **Dashboard**: Vercel hosts the live site
   - Static Next.js dashboard
   - Shows all weekly summaries
   - Auto-deploys on git push
   - See [docs/DASHBOARD_SETUP.md](docs/DASHBOARD_SETUP.md)

**Benefits**:
- ✅ Fully automated in cloud
- ✅ Free for public repos
- ✅ Live public dashboard
- ✅ No local machine needed
- ✅ Growing archive over time

**Quick Dashboard Setup**:
```bash
# 1. Go to vercel.com/new
# 2. Import GitHub repo: rishdas2007/Notion-Summarizer
# 3. Configure:
#    - Root Directory: dashboard
#    - Framework: Next.js
# 4. Deploy!
```

Dashboard will be live at: `https://your-project.vercel.app`

### Option 2: Local Cron Job

Run automatically on your computer:

```bash
# Edit crontab
crontab -e

# Add this line for every Sunday at 9 AM
0 9 * * 0 cd "/path/to/podcast-automation" && python3 main.py
```

**Benefits**:
- ✅ Direct Obsidian vault integration
- ✅ No cloud dependency
- ✅ Full local control

### Option 3: Manual Execution

Run whenever you want:

```bash
cd "/path/to/podcast-automation"
python3 main.py
```

## Development

### Project Structure

- `config.py` - Central configuration management
- `notion_client_handler.py` - Notion API interactions
- `markdown_converter.py` - Content conversion logic
- `intelligent_parser.py` - Content compression algorithm
- `batch_summary_generator.py` - AI summarization engine
- `main.py` - Orchestration and workflow
- `.github/workflows/` - GitHub Actions automation

### Adding New Features

1. Update `config.py` for any new settings
2. Add new modules in root directory
3. Update `requirements.txt` if needed
4. Document changes in `docs/PROJECT_NOTES.md`

## Security

- ✅ No secrets in source code
- ✅ Environment variable based configuration
- ✅ `.gitignore` prevents accidental commits
- ✅ Portable across systems
- ✅ Production-ready

## License

MIT License - see LICENSE file for details

## Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Acknowledgments

- [Notion API](https://developers.notion.com/)
- [Anthropic Claude](https://www.anthropic.com/)
- [Python Notion Client](https://github.com/ramnes/notion-sdk-py)

## Support

For issues or questions:
- Check `docs/PROJECT_NOTES.md` for detailed documentation
- Review closed issues on GitHub
- Open a new issue with reproduction steps

---

Built with ❤️ using Claude Sonnet 4.5
