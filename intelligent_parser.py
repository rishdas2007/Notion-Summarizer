#!/usr/bin/env python3

import re
import logging

class IntelligentPodcastParser:
    """
    Intelligently parse podcast markdown to extract structured information
    and compress content while preserving key insights.
    """

    def __init__(self):
        pass

    def parse_episode(self, markdown_content):
        """
        Parse a podcast episode markdown file and extract structured data.
        Returns a condensed version optimized for summarization (~40K tokens from ~96K).
        """
        result = {
            'metadata': {},
            'description': '',
            'topics': [],
            'full_transcript_segments': []
        }

        lines = markdown_content.split('\n')

        # Extract title (first # heading)
        for line in lines[:20]:  # Check first 20 lines
            if line.startswith('# ') and len(line.strip()) > 2:
                result['metadata']['title'] = line[2:].strip()
                break

        # Extract metadata section (between --- markers)
        in_metadata = False
        metadata_lines = []
        for line in lines[:50]:  # Check first 50 lines
            if line.strip() == '---':
                if in_metadata:
                    break
                in_metadata = True
                continue
            if in_metadata and line.strip():
                metadata_lines.append(line.strip())

        # Parse metadata
        for line in metadata_lines:
            if line.startswith('**Publish Date:**'):
                result['metadata']['publish_date'] = line.replace('**Publish Date:**', '').strip()
            elif line.startswith('**Show:**'):
                result['metadata']['show'] = line.replace('**Show:**', '').strip()

        # Extract episode description (after metadata, before "Your snips")
        description_started = False
        for i, line in enumerate(lines):
            if '**Episode show notes**' in line or 'show notes' in line.lower():
                description_started = True
                continue
            if description_started and ('## Your snips' in line or '## Snips' in line):
                break
            if description_started and line.strip() and not line.strip().startswith('#'):
                result['description'] += line.strip() + ' '

        result['description'] = result['description'].strip()[:2000]  # Limit description

        # Extract topics from snips (these are already well-structured!)
        current_topic = None
        in_transcript = False

        for i, line in enumerate(lines):
            # Detect snip headers with timestamps
            snip_match = re.match(r'###\s*\[\[(\d{2}:\d{2})\]\].*', line)
            if snip_match:
                if current_topic:
                    result['topics'].append(current_topic)

                current_topic = {
                    'timestamp': snip_match.group(1),
                    'title': '',
                    'description': '',
                    'transcript': ''
                }

                # Get title from next line or same line
                title_text = line.replace(snip_match.group(0), '').strip()
                if title_text:
                    current_topic['title'] = title_text
                elif i + 1 < len(lines):
                    # Check next few lines for title
                    for j in range(i+1, min(i+5, len(lines))):
                        if lines[j].strip() and not lines[j].strip().startswith('['):
                            current_topic['title'] = lines[j].strip()
                            break

                in_transcript = False
                continue

            # Extract description (bold text after snip header)
            if current_topic and line.strip().startswith('**') and not in_transcript:
                desc_text = line.strip().replace('**', '').strip()
                if desc_text and not desc_text.startswith('ð'):
                    current_topic['description'] += desc_text + ' '

            # Detect transcript section
            if '**ð Transcript**' in line or 'Transcript' in line:
                in_transcript = True
                continue

            # Extract speaker dialogue from transcript
            if current_topic and in_transcript:
                # Match speaker patterns like **Speaker Name**
                speaker_match = re.match(r'\*\*([^*]+)\*\*', line)
                if speaker_match:
                    speaker = speaker_match.group(1)
                    dialogue = line.replace(f'**{speaker}**', '').strip()
                    if dialogue:
                        current_topic['transcript'] += f"{speaker}: {dialogue}\n"
                elif line.strip() and not line.startswith('###'):
                    # Continuation of previous dialogue
                    current_topic['transcript'] += line.strip() + ' '

        # Add last topic
        if current_topic:
            result['topics'].append(current_topic)

        return result

    def create_condensed_content(self, parsed_data, target_tokens=40000):
        """
        Create condensed version of content optimized for summarization.
        Target ~40K tokens (160K characters, assuming 4 chars per token).
        """
        condensed = []

        # Add metadata
        condensed.append(f"# {parsed_data['metadata'].get('title', 'Unknown Episode')}")
        condensed.append(f"**Published:** {parsed_data['metadata'].get('publish_date', 'Unknown')}")
        condensed.append(f"**Show:** {parsed_data['metadata'].get('show', 'Unknown')}")
        condensed.append("")

        # Add episode description
        if parsed_data['description']:
            condensed.append("## Episode Overview")
            condensed.append(parsed_data['description'][:3000])  # First 3000 chars
            condensed.append("")

        # Add topics with smart compression
        condensed.append("## Key Discussion Topics")
        condensed.append("")

        target_chars = 160000  # ~40K tokens
        current_chars = len('\n'.join(condensed))
        chars_per_topic = (target_chars - current_chars) // max(len(parsed_data['topics']), 1)

        for i, topic in enumerate(parsed_data['topics'], 1):
            topic_section = []
            topic_section.append(f"### {i}. {topic['title']} [{topic['timestamp']}]")
            topic_section.append("")

            if topic['description']:
                topic_section.append(f"**Summary:** {topic['description'].strip()}")
                topic_section.append("")

            if topic['transcript']:
                # Include compressed transcript
                transcript_budget = int(chars_per_topic * 0.7)  # 70% for transcript
                transcript = topic['transcript'][:transcript_budget]

                # Try to end at a sentence
                last_period = transcript.rfind('.')
                if last_period > len(transcript) * 0.8:  # If we're close to the end
                    transcript = transcript[:last_period + 1]

                topic_section.append("**Key Dialogue:**")
                topic_section.append(transcript.strip())
                topic_section.append("")

            condensed.extend(topic_section)

        return '\n'.join(condensed)

    def extract_participants(self, markdown_content):
        """Extract participant names from the transcript."""
        participants = set()

        # Find all speaker patterns
        speaker_pattern = re.compile(r'\*\*([A-Z][a-zA-Z\s]+?)\*\*(?=\n|:)')
        matches = speaker_pattern.findall(markdown_content)

        for match in matches:
            name = match.strip()
            # Filter out common false positives
            if name and len(name) < 50 and not any(x in name.lower() for x in ['transcript', 'summary', 'snip', 'play']):
                participants.add(name)

        return sorted(list(participants))
