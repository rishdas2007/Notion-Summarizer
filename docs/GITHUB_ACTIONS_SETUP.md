# GitHub Actions Setup Guide

This guide will help you set up automated podcast processing that runs weekly in GitHub Actions (cloud automation).

## Overview

GitHub Actions will:
- ✅ Run automatically every Sunday at 9 AM UTC
- ✅ Process last 7 days of podcast episodes
- ✅ Generate AI summaries using Claude
- ✅ Store results as downloadable artifacts
- ✅ Can be triggered manually anytime

## Step-by-Step Setup

### 1. Push Your Code to GitHub

If you haven't already:

```bash
cd "/Users/rishabhdas/Code_Projects/Notion Automation/podcast-automation"
git init
git add .
git commit -m "Initial commit with GitHub Actions"
git remote add origin https://github.com/rishdas2007/Notion-Summarizer.git
git branch -M main
git push -u origin main
```

### 2. Add Secrets to GitHub

⚠️ **CRITICAL**: Never commit your API keys! Add them as GitHub Secrets instead.

1. **Go to your repository**: https://github.com/rishdas2007/Notion-Summarizer

2. **Navigate to Settings**:
   - Click **Settings** tab
   - Click **Secrets and variables** → **Actions**
   - Click **New repository secret**

3. **Add these three secrets** (get values from your `.env` file):

   **Secret 1: NOTION_TOKEN**
   - Name: `NOTION_TOKEN`
   - Value: Your Notion integration token (starts with `ntn_`)
   - Click **Add secret**

   **Secret 2: NOTION_DATABASE_ID**
   - Name: `NOTION_DATABASE_ID`
   - Value: Your Notion database ID (32-character hex string)
   - Click **Add secret**

   **Secret 3: ANTHROPIC_API_KEY**
   - Name: `ANTHROPIC_API_KEY`
   - Value: Your Claude API key (starts with `sk-ant-`)
   - Click **Add secret**

### 3. Verify Secrets Are Added

After adding all three secrets, you should see:
```
✓ NOTION_TOKEN
✓ NOTION_DATABASE_ID
✓ ANTHROPIC_API_KEY
```

### 4. Enable GitHub Actions

1. Go to **Actions** tab in your repository
2. Click **I understand my workflows, go ahead and enable them**
3. You should see the workflow: **Podcast Automation**

## Usage

### Automatic Execution

The workflow runs automatically:
- **Schedule**: Every Sunday at 9:00 AM UTC
- **What it does**: Processes episodes from the last 7 days
- **Duration**: ~5-15 minutes depending on episode count

### Manual Execution

You can trigger it anytime:

1. Go to **Actions** tab
2. Click **Podcast Automation** workflow
3. Click **Run workflow** button (top right)
4. Click green **Run workflow** button
5. Wait for it to complete (~5-15 min)

### Viewing Results

After workflow completes:

1. **View Summary**:
   - Click on the workflow run
   - See episode counts and summary in the summary section

2. **Download Files**:
   - Scroll to **Artifacts** section at bottom
   - Click **podcast-summaries-X** to download
   - Extract the ZIP file
   - Find your summaries in `output/summaries/`

## Workflow Details

### What Gets Processed

```yaml
Input:  Notion episodes from last 7 days
Output: Markdown files + AI summaries
```

### File Structure in Artifacts

```
podcast-summaries-X.zip
├── output/
│   ├── podcast_notes/          # Raw markdown transcripts
│   │   └── *.md
│   └── summaries/              # AI-generated summaries
│       └── *_Summary.md
└── *.log                       # Processing logs
```

### Workflow Configuration

The workflow is defined in `.github/workflows/podcast-automation.yml`:

- **Runs on**: Ubuntu (latest)
- **Python version**: 3.11
- **Timeout**: 60 minutes (default)
- **Artifact retention**: 30 days
- **Cost**: **FREE** (GitHub Actions is free for public repos, 2000 min/month for private)

## Customization

### Change Schedule

Edit `.github/workflows/podcast-automation.yml`:

```yaml
schedule:
  - cron: '0 9 * * 0'  # Every Sunday at 9 AM UTC
```

Cron format: `minute hour day month weekday`

Examples:
- Every day at 9 AM: `'0 9 * * *'`
- Every Monday at 6 AM: `'0 6 * * 1'`
- Twice a week (Mon, Thu at 10 AM): `'0 10 * * 1,4'`

Use [crontab.guru](https://crontab.guru/) to generate cron expressions.

### Change Timezone

GitHub Actions runs in UTC. To adjust for your timezone:

- **PST (UTC-8)**: Use `17` for 9 AM PST (9 + 8 = 17)
- **EST (UTC-5)**: Use `14` for 9 AM EST (9 + 5 = 14)
- **IST (UTC+5:30)**: Use `3` for 9 AM IST (9 - 5.5 ≈ 3:30)

Example for 9 AM EST:
```yaml
schedule:
  - cron: '0 14 * * 0'  # 9 AM EST = 2 PM UTC
```

### Increase Lookback Period

To process more than 7 days, update `config.py`:

```python
def get_week_date_range():
    """Get the last X days"""
    today = datetime.now().date()
    start_date = today - timedelta(days=13)  # 14 days (2 weeks)
    end_date = today
    return start_date, end_date
```

## Monitoring

### View Workflow Status

1. Go to **Actions** tab
2. See all workflow runs with status:
   - ✅ Green = Success
   - ❌ Red = Failed
   - 🟡 Yellow = In progress

### Email Notifications

GitHub sends email notifications for:
- Failed workflow runs
- First successful run after a failure

Configure in: Settings → Notifications → Actions

### Check Logs

Click on any workflow run to see:
- Setup steps
- Episode processing logs
- Summary generation logs
- Error messages (if any)

## Troubleshooting

### "Error: Configuration errors"

**Problem**: Missing secrets

**Solution**:
1. Go to Settings → Secrets and variables → Actions
2. Verify all three secrets are added
3. Re-run the workflow

### "No episodes found"

**Problem**: Date range has no episodes

**Solution**:
- This is normal if no episodes were published in last 7 days
- Check your Notion database for recent episodes
- Manually trigger workflow to test

### "Claude API error"

**Problem**: API key invalid or quota exceeded

**Solution**:
1. Verify `ANTHROPIC_API_KEY` secret is correct
2. Check your Anthropic console for quota: https://console.anthropic.com/
3. Ensure you have API credits

### "Workflow not running automatically"

**Problem**: Schedule not triggering

**Solution**:
- GitHub Actions has a ~15 minute delay for scheduled workflows
- Scheduled workflows only run if there was a commit in the last 60 days
- Use manual trigger to test

## Cost Analysis

### GitHub Actions (Free Tier)

**Public repositories**: ✅ Unlimited free minutes
**Private repositories**: 2,000 minutes/month free

**Your usage**: ~5-15 min/week = ~60-80 min/month

✅ **Well within free tier!**

### Claude API

- **Per episode**: ~$0.30-0.60
- **Weekly (6 episodes)**: ~$1.80-3.60
- **Monthly**: ~$7-15

Total cost: **~$7-15/month** (just Claude API, GitHub is free)

## Benefits of GitHub Actions

✅ **Cloud-based**: No local machine needed
✅ **Automated**: Runs on schedule
✅ **Reliable**: GitHub infrastructure
✅ **Free**: For public repos
✅ **Accessible**: Results downloadable anywhere
✅ **Versioned**: All runs logged and traceable

## Limitations

⚠️ **No direct Obsidian sync**: Files are artifacts, not in your vault

**Workaround options**:
1. Download artifacts and move to Obsidian manually
2. Keep running locally with cron job for direct vault integration
3. Use GitHub API to automatically download artifacts (advanced)

## Hybrid Approach (Recommended)

Use both:
- **GitHub Actions**: Backup/cloud processing
- **Local cron**: Direct Obsidian integration

This gives you redundancy and flexibility! 🚀

## Next Steps

1. ✅ Add secrets to GitHub
2. ✅ Push code with workflow file
3. ✅ Manually trigger workflow to test
4. ✅ Verify artifacts download correctly
5. ✅ Wait for automatic Sunday run

## Support

If you encounter issues:
1. Check workflow logs in Actions tab
2. Review this documentation
3. Check GitHub Actions documentation: https://docs.github.com/en/actions
4. Review Anthropic API status: https://status.anthropic.com/

---

🎉 **You're all set!** Your podcast automation will now run automatically in the cloud every week!
