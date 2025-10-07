# Dashboard Setup Guide

This guide will help you set up and deploy the podcast summaries dashboard to Vercel.

## Overview

The dashboard is a modern, mobile-optimized static Next.js 14 site that displays your weekly podcast summaries. It features a professional gradient design, responsive layout, and automatically updates when GitHub Actions commits new summaries every Sunday.

### Features

- 📱 **Mobile Optimized**: CSS variables ensure perfect readability on all devices
- 🎨 **Modern Design**: Professional gradient header, card-based layout, smooth hover effects
- 📑 **Table of Contents**: Homepage displays all weeks for easy navigation
- ⚡ **Static Site Generation**: Lightning-fast page loads with pre-rendered HTML
- 🔄 **Auto-Deploy**: Vercel rebuilds automatically on git push (2-3 minutes)
- 📊 **Weekly Archive**: Organized by ISO date format (YYYY-MM-DD)

## Prerequisites

- GitHub repository with podcast automation set up
- Vercel account (free tier works)
- GitHub Actions successfully running

## Step 1: Verify Dashboard Files

Ensure these files exist in your repository:

```
dashboard/
├── app/
├── components/
├── lib/
├── public/summaries/  (will be populated by GitHub Actions)
├── package.json
├── next.config.js
└── tsconfig.json
```

## Step 2: Deploy to Vercel

### Option A: Deploy via Vercel Dashboard (Recommended)

1. **Go to Vercel**
   - Visit https://vercel.com/new
   - Sign in with GitHub

2. **Import Repository**
   - Click "Add New..." → "Project"
   - Select "Import Git Repository"
   - Find and select: `rishdas2007/Notion-Summarizer`
   - Click "Import"

3. **Configure Project**
   ```
   Framework Preset: Next.js
   Root Directory: dashboard
   Build Command: npm run build (leave default)
   Output Directory: (leave empty)
   Install Command: npm install (leave default)
   ```

4. **Deploy**
   - Click "Deploy"
   - Wait 2-3 minutes for initial build
   - Your dashboard will be live at: `https://your-project.vercel.app`

### Option B: Deploy via Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Navigate to dashboard
cd dashboard

# Deploy
vercel

# Follow prompts:
# Set up and deploy? Y
# Which scope? [your account]
# Link to existing project? N
# Project name? podcast-summaries-dashboard
# Directory? ./
# Override settings? N

# Deploy to production
vercel --prod
```

## Step 3: Configure Auto-Deployment

Vercel automatically deploys on git push. To verify:

1. **Go to Vercel Dashboard**
   - Select your project
   - Click "Settings" → "Git"

2. **Verify Settings**
   ```
   ✓ Production Branch: main
   ✓ Deploy Hooks: Enabled
   ✓ Auto Deploy: Enabled
   ```

3. **Test Auto-Deploy**
   - Make a small change to dashboard/README.md
   - Commit and push
   - Watch Vercel dashboard for new deployment

## Step 4: Test the Workflow

### Create Sample Data (Optional)

To test before the first automation run:

```bash
# Create sample week
mkdir -p dashboard/public/summaries/2025-01-07

# Add sample markdown
cat > dashboard/public/summaries/2025-01-07/sample-episode.md << 'EOF'
# Sample Podcast Episode

## Summary
This is a test episode to verify the dashboard is working.

## Key Points
- Dashboard is configured
- Static site generation works
- Markdown rendering is functional

## Highlights
> "This is a sample quote from the episode"

EOF

# Generate metadata
python3 scripts/generate_metadata.py dashboard/public/summaries/2025-01-07

# Commit and push
git add dashboard/public/summaries/
git commit -m "Add sample data for dashboard testing"
git push
```

Watch Vercel redeploy and verify the sample appears at your dashboard URL.

### Run GitHub Actions Manually

1. Go to GitHub repository
2. Click "Actions" tab
3. Select "Podcast Automation" workflow
4. Click "Run workflow" → "Run workflow"
5. Wait for completion
6. Check Vercel for automatic redeployment

## Step 5: Verify Everything Works

1. **Check Homepage**
   - Visit `https://your-project.vercel.app`
   - Should see latest weeks or "No summaries yet"

2. **Check Archive**
   - Visit `https://your-project.vercel.app/summaries`
   - Should see all weeks

3. **Check Individual Week**
   - Click on a week card
   - Should see episode summaries with markdown formatting

4. **Check Auto-Update Flow**
   - Wait for Sunday automation (or trigger manually)
   - Verify new summaries appear automatically

## Customization

### Update Site Title and Branding

Edit `dashboard/app/layout.tsx`:

```typescript
export const metadata: Metadata = {
  title: "My Podcast Summaries", // Change this
  description: "Your custom description", // Change this
}
```

### Update Colors

Edit `dashboard/app/globals.css` to customize the color scheme.

### Update Header

Edit `dashboard/app/layout.tsx` to customize navigation and header text.

## Troubleshooting

### Dashboard Shows "No summaries yet"

**Cause**: No summary folders in `dashboard/public/summaries/`

**Solution**:
1. Run GitHub Actions manually
2. Or add sample data as shown above
3. Verify `metadata.json` exists in each week folder

### Build Fails on Vercel

**Common Issues**:

1. **TypeScript Module Resolution Errors**
   ```bash
   # Ensure tsconfig.json has:
   {
     "compilerOptions": {
       "baseUrl": ".",
       "moduleResolution": "node"
     }
   }
   ```

2. **Missing Dependencies**
   ```bash
   # Check package.json includes:
   - @tailwindcss/typography
   - react-markdown
   - remark-gfm

   # Test locally:
   cd dashboard
   npm install
   npm run build
   ```

3. **Path Issues**
   - Ensure root directory is set to `dashboard` in Vercel settings
   - Verify `.gitignore` has `/lib/` (not `lib/`) to allow `dashboard/lib/`

4. **Dynamic Route Issues**
   - Ensure `dashboard/app/summaries/[date]/page.tsx` exists (not `_date_disabled`)
   - Verify `generateStaticParams()` function is present

### Summaries Not Updating

**Check**:
1. GitHub Actions completed successfully
2. Summaries committed to `dashboard/public/summaries/`
3. Vercel detected the commit (check Deployments tab)
4. No build errors in Vercel logs
5. Cache cleared (may take 2-3 minutes)

### Mobile Text Barely Visible

**Fixed in latest version!** ✅

The issue was caused by hardcoded Tailwind colors. Now uses CSS variables:

```typescript
// Before (problematic):
<h1 className="text-gray-900">

// After (correct):
<h1 style={{ color: 'var(--text-primary)' }}>
```

**If still experiencing issues**:
1. Ensure you're on latest commit
2. Clear browser cache
3. Check Vercel deployment completed successfully
4. Verify `dashboard/app/globals.css` has CSS variables defined

### Episode Titles Showing as "Major Sub-Tasks for Summarization"

**Fixed in latest version!** ✅

The issue was in `scripts/generate_metadata.py`. Now extracts titles from filenames:

```python
# Before (problematic):
# Used first H1 from markdown content

# After (correct):
title = filepath.stem  # Use filename as title
```

**If still experiencing issues**:
1. Delete `metadata.json` files
2. Re-run `python3 scripts/generate_metadata.py <week_folder>`
3. Or trigger GitHub Actions to regenerate

### 404 Error on Summary Pages

**Cause**: Dynamic route folder disabled or missing

**Solution**:
1. Verify `dashboard/app/summaries/[date]/page.tsx` exists
2. Ensure folder is named `[date]` not `_date_disabled`
3. Check `generateStaticParams()` function exists in page.tsx

### Styling Looks Wrong

**Solutions**:
1. Clear Next.js cache: `rm -rf dashboard/.next`
2. Rebuild: `cd dashboard && npm run build`
3. Check browser console for errors
4. Verify Tailwind CSS is processing correctly
5. Ensure `@tailwindcss/typography` plugin is installed

## Monitoring

### GitHub Actions
- **Schedule**: Every Sunday at 9 AM UTC
- **Status**: Check Actions tab in GitHub
- **Logs**: Click on workflow run for detailed logs

### Vercel Deployments
- **Dashboard**: https://vercel.com/dashboard
- **Builds**: View all deployments and their status
- **Analytics**: Monitor page views and performance

## Cost

- **Vercel Free Tier**: 100GB bandwidth/month, unlimited deployments
- **GitHub Actions**: 2,000 minutes/month (free for public repos)
- **Anthropic API**: Pay per token (~$0.30-0.60 per episode)

## Next Steps

1. ✅ Set up custom domain (optional)
2. ✅ Add analytics (Vercel Analytics)
3. ✅ Set up monitoring/alerts
4. ✅ Customize branding and colors
5. ✅ Share your dashboard URL

## Support

If you encounter issues:
1. Check GitHub Actions logs
2. Check Vercel deployment logs
3. Review this guide
4. Check Next.js documentation
5. Review Vercel documentation

## Useful Links

- **Your Dashboard**: https://your-project.vercel.app
- **Vercel Dashboard**: https://vercel.com/dashboard
- **GitHub Repo**: https://github.com/rishdas2007/Notion-Summarizer
- **Next.js Docs**: https://nextjs.org/docs
- **Vercel Docs**: https://vercel.com/docs
