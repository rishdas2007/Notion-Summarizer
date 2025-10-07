# Podcast Summaries

This directory contains weekly podcast episode summaries organized by date.

## Directory Structure

Each week gets its own folder in the format `YYYY-MM-DD`:

```
summaries/
├── 2025-01-07/
│   ├── metadata.json
│   ├── Episode_1_Summary.md
│   └── Episode_2_Summary.md
├── 2025-01-14/
│   ├── metadata.json
│   └── Episode_3_Summary.md
└── ...
```

## Metadata Format

Each week folder contains a `metadata.json` file:

```json
{
  "episodeCount": 2,
  "episodes": [
    {
      "filename": "Episode_1_Summary.md",
      "title": "Episode Title Here"
    }
  ],
  "generatedAt": "2025-01-07T09:15:30.123456"
}
```

## How Summaries Are Added

Summaries are automatically added by GitHub Actions:

1. **Every Sunday at 9 AM UTC**: GitHub Actions workflow runs
2. **Process Episodes**: Python automation fetches and summarizes episodes
3. **Organize Files**: Summaries copied to `dashboard/public/summaries/YYYY-MM-DD/`
4. **Generate Metadata**: `scripts/generate_metadata.py` creates metadata.json
5. **Commit**: Changes committed to repository
6. **Deploy**: Vercel detects commit and rebuilds dashboard

## Manual Addition

To add summaries manually:

```bash
# Create week folder
WEEK_DATE=$(date +%Y-%m-%d)
mkdir -p "dashboard/public/summaries/$WEEK_DATE"

# Copy markdown files
cp output/summaries/*.md "dashboard/public/summaries/$WEEK_DATE/"

# Generate metadata
python3 scripts/generate_metadata.py "dashboard/public/summaries/$WEEK_DATE"

# Commit and push
git add dashboard/public/summaries/
git commit -m "Add summaries for week of $WEEK_DATE"
git push
```

## Note

This directory is initially empty. It will be populated by GitHub Actions after the first automation run.
