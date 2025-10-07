# Dashboard Quick Start Guide

## What You Have Now

A complete **static Next.js dashboard** that displays your weekly podcast summaries with automatic deployment to Vercel.

## 🎯 How It Works

### Weekly Automation Flow

```
Sunday 9 AM UTC
↓
GitHub Actions runs podcast automation
↓
Episodes fetched from Notion → Summaries generated with Claude
↓
Summaries organized into dashboard/public/summaries/YYYY-MM-DD/
↓
metadata.json created for the week
↓
Changes committed to GitHub
↓
Vercel detects commit → Rebuilds dashboard → Live in 2-3 minutes
```

### Result
- New summaries appear automatically every Sunday
- Old summaries preserved forever
- Growing archive over time
- Fast, SEO-friendly static pages

## 🚀 Deploy in 5 Minutes

### Step 1: Push to GitHub (if not done)

```bash
cd "/Users/rishabhdas/Code_Projects/Notion Automation/podcast-automation"
git add .
git commit -m "Add Next.js dashboard for podcast summaries"
git push
```

### Step 2: Deploy to Vercel

1. **Go to Vercel**: https://vercel.com/new
2. **Sign in with GitHub**
3. **Import Repository**: Select `rishdas2007/Notion-Summarizer`
4. **Configure**:
   - **Root Directory**: `dashboard`
   - **Framework Preset**: Next.js
   - **Build Command**: Leave default
   - **Output Directory**: Leave empty
5. **Click "Deploy"**

Wait 2-3 minutes → Dashboard is live! 🎉

### Step 3: Verify Everything Works

Visit your dashboard URL (e.g., `https://notion-summarizer.vercel.app`)

You should see:
- ✅ Homepage with "No summaries yet" (normal until first run)
- ✅ Navigation working (Home, Archive)
- ✅ Clean, responsive design

## 📋 Next Steps

### Option A: Wait for Sunday
- GitHub Actions runs automatically every Sunday at 9 AM UTC
- Summaries will appear automatically
- Dashboard updates automatically

### Option B: Test Now (Recommended)

**Create sample data to verify dashboard**:

```bash
# Create sample week folder
mkdir -p "dashboard/public/summaries/2025-01-07"

# Create sample markdown
cat > "dashboard/public/summaries/2025-01-07/sample-episode.md" << 'EOF'
# Sample Podcast Episode

## Executive Summary
This is a test episode to verify the dashboard is working correctly.

## Key Points
- Dashboard architecture is complete
- Static site generation works
- Markdown rendering is functional
- Weekly automation is configured

## Detailed Analysis
Lorem ipsum dolor sit amet, consectetur adipiscing elit. This is sample content to demonstrate how podcast summaries will appear on the dashboard.

## Key Insights
> "Static site generation provides optimal performance"

The dashboard uses Next.js 14 with App Router for fast, SEO-friendly pages.

EOF

# Generate metadata
python3 scripts/generate_metadata.py "dashboard/public/summaries/2025-01-07"

# Commit and push
git add dashboard/public/summaries/
git commit -m "Add sample data for dashboard testing"
git push
```

**Wait 2-3 minutes**, then refresh your dashboard URL. The sample episode should appear!

### Option C: Trigger GitHub Actions Manually

1. Go to: https://github.com/rishdas2007/Notion-Summarizer/actions
2. Click "Podcast Automation"
3. Click "Run workflow" → "Run workflow"
4. Wait 5-10 minutes for completion
5. Refresh dashboard - new summaries appear!

## 📊 Dashboard Features

### Homepage (`/`)
- Shows latest 6 weeks
- Card-based layout
- Episode count per week
- Quick navigation

### Archive (`/summaries`)
- All weeks chronologically
- Complete history
- Searchable/browsable

### Week View (`/summaries/YYYY-MM-DD`)
- All episodes for that week
- Full markdown content
- Beautiful formatting
- Navigation between weeks

## 🎨 Customization

### Change Site Title
Edit `dashboard/app/layout.tsx`:
```typescript
export const metadata: Metadata = {
  title: "My Podcast Summaries", // Change here
  description: "Your description", // Change here
}
```

### Change Colors
Edit `dashboard/app/globals.css` for color scheme

### Update Header
Edit `dashboard/app/layout.tsx` for navigation text

Commit and push changes → Vercel redeploys automatically

## 🐛 Troubleshooting

### "No summaries yet" persists
- GitHub Actions hasn't run yet (wait for Sunday or trigger manually)
- Or no episodes in Notion database for past 7 days

### Build fails on Vercel
- Check build logs in Vercel dashboard
- Verify root directory is set to `dashboard`
- Try deploying again

### Dashboard URL not working
- Wait 2-3 minutes after deployment
- Check Vercel dashboard for deployment status
- Look for any error messages

## 📚 Full Documentation

- **Dashboard Setup**: [docs/DASHBOARD_SETUP.md](docs/DASHBOARD_SETUP.md)
- **GitHub Actions**: [docs/GITHUB_ACTIONS_SETUP.md](docs/GITHUB_ACTIONS_SETUP.md)
- **Architecture**: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
- **Dashboard Code**: [dashboard/README.md](dashboard/README.md)

## ✅ Success Checklist

- [ ] Code pushed to GitHub
- [ ] Vercel project created
- [ ] Root directory set to `dashboard`
- [ ] First deployment successful
- [ ] Dashboard URL accessible
- [ ] Sample data tested (or waiting for Sunday)
- [ ] GitHub Actions configured
- [ ] Auto-deployment working

## 🎉 You're Done!

Your podcast automation system now has:
- ✅ Weekly automation via GitHub Actions
- ✅ AI-powered summaries with Claude Sonnet 4.5
- ✅ Live dashboard on Vercel
- ✅ Growing archive over time
- ✅ Fully automated, no maintenance needed

**Dashboard URL**: Replace with your actual URL
**GitHub Repo**: https://github.com/rishdas2007/Notion-Summarizer
**Schedule**: Every Sunday at 9 AM UTC

Enjoy your automated podcast summary dashboard! 🚀
