#!/usr/bin/env python3
"""
Generate metadata.json for a week's podcast summaries.

This script scans a directory for markdown files and creates a metadata.json
file containing information about all the episodes in that week.

Usage:
    python3 generate_metadata.py <target_directory>

Example:
    python3 generate_metadata.py dashboard/public/summaries/2025-01-07
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime
import re


def extract_title_from_markdown(filepath):
    """Extract title from markdown filename - the filename IS the title"""
    # Remove " Summary" suffix if present
    title = filepath.stem
    if title.endswith(' Summary'):
        title = title[:-8]  # Remove " Summary"

    # Replace underscores and multiple spaces with single spaces
    title = title.replace('_', ' ')
    title = re.sub(r'\s+', ' ', title).strip()

    return title


def generate_metadata(target_dir):
    """Generate metadata.json for a week's summaries"""
    target_path = Path(target_dir)

    if not target_path.exists():
        print(f"Error: Directory {target_dir} does not exist")
        sys.exit(1)

    # Find all markdown files
    markdown_files = list(target_path.glob("*.md"))

    if not markdown_files:
        print(f"Warning: No markdown files found in {target_dir}")
        episodes = []
    else:
        episodes = []
        for md_file in sorted(markdown_files):
            title = extract_title_from_markdown(md_file)
            episodes.append({
                'filename': md_file.name,
                'title': title
            })
            print(f"Found episode: {title} ({md_file.name})")

    # Create metadata
    metadata = {
        'episodeCount': len(episodes),
        'episodes': episodes,
        'generatedAt': datetime.now().isoformat()
    }

    # Write metadata.json
    metadata_path = target_path / 'metadata.json'
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Generated {metadata_path}")
    print(f"   Episodes: {len(episodes)}")
    print(f"   Timestamp: {metadata['generatedAt']}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 generate_metadata.py <target_directory>")
        print("Example: python3 generate_metadata.py dashboard/public/summaries/2025-01-07")
        sys.exit(1)

    generate_metadata(sys.argv[1])
