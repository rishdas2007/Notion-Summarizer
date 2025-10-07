import re
from datetime import datetime
from config import MIN_SUMMARY_WORDS

class MarkdownConverter:
    def __init__(self):
        pass
    
    def convert_page_to_markdown(self, page, blocks):
        """Convert Notion page and blocks to markdown"""
        markdown_content = []
        
        # Add title
        title = self.extract_title(page)
        if title:
            markdown_content.append(f"# {title}\n")
        
        # Add metadata
        publish_date = self.extract_publish_date(page)
        show_name = self.extract_show_name(page)
        
        if publish_date or show_name:
            markdown_content.append("---")
            if publish_date:
                markdown_content.append(f"**Publish Date:** {publish_date}")
            if show_name:
                markdown_content.append(f"**Show:** {show_name}")
            markdown_content.append("---\n")
        
        # Convert blocks to markdown with proper nesting
        for block in blocks:
            # Determine indent level based on nesting
            indent_level = 1 if block.get("_is_nested", False) else 0
            markdown_block = self.convert_block_to_markdown(block, indent_level)
            if markdown_block:
                markdown_content.append(markdown_block)
        
        return "\n".join(markdown_content)
    
    def extract_title(self, page):
        """Extract page title"""
        try:
            properties = page["properties"]
            if "Episode" in properties and properties["Episode"]["title"]:
                return properties["Episode"]["title"][0]["plain_text"]
        except (KeyError, IndexError):
            pass
        return "Untitled Episode"
    
    def extract_publish_date(self, page):
        """Extract publish date"""
        try:
            properties = page["properties"]
            if "Episode publish date" in properties:
                date_obj = properties["Episode publish date"]["date"]
                if date_obj and date_obj["start"]:
                    return date_obj["start"]
        except (KeyError, IndexError):
            pass
        return None
    
    def extract_show_name(self, page):
        """Extract show name"""
        try:
            properties = page["properties"]
            if "Show" in properties and properties["Show"]["rich_text"]:
                return properties["Show"]["rich_text"][0]["plain_text"]
        except (KeyError, IndexError):
            pass
        return None
    
    def convert_block_to_markdown(self, block, indent_level=0):
        """Convert individual Notion block to markdown with proper indentation"""
        block_type = block["type"]
        indent = "  " * indent_level  # 2 spaces per indent level
        
        if block_type == "paragraph":
            text = self.convert_rich_text(block["paragraph"]["rich_text"])
            return f"{indent}{text}" if text else ""
        
        elif block_type == "heading_1":
            text = self.convert_rich_text(block["heading_1"]["rich_text"])
            return f"{indent}# {text}" if text else ""
        
        elif block_type == "heading_2":
            text = self.convert_rich_text(block["heading_2"]["rich_text"])
            return f"{indent}## {text}" if text else ""
        
        elif block_type == "heading_3":
            text = self.convert_rich_text(block["heading_3"]["rich_text"])
            return f"{indent}### {text}" if text else ""
        
        elif block_type == "bulleted_list_item":
            text = self.convert_rich_text(block["bulleted_list_item"]["rich_text"])
            return f"{indent}- {text}" if text else ""
        
        elif block_type == "numbered_list_item":
            text = self.convert_rich_text(block["numbered_list_item"]["rich_text"])
            return f"{indent}1. {text}" if text else ""
        
        elif block_type == "quote":
            text = self.convert_rich_text(block["quote"]["rich_text"])
            return f"{indent}> {text}" if text else ""
        
        elif block_type == "code":
            language = block["code"]["language"] or ""
            text = self.convert_rich_text(block["code"]["rich_text"])
            return f"{indent}```{language}\n{indent}{text}\n{indent}```" if text else ""
        
        elif block_type == "divider":
            return f"{indent}---"
        
        elif block_type == "callout":
            icon = block["callout"].get("icon", {})
            icon_text = ""
            if icon.get("emoji"):
                icon_text = icon["emoji"] + " "
            text = self.convert_rich_text(block["callout"]["rich_text"])
            return f"{indent}> {icon_text}{text}" if text else ""
        
        elif block_type == "toggle":
            text = self.convert_rich_text(block["toggle"]["rich_text"])
            return f"{indent}**{text}**" if text else ""
        
        return ""
    
    def convert_rich_text(self, rich_text_array):
        """Convert Notion rich text to markdown"""
        if not rich_text_array:
            return ""
        
        result = []
        for text_obj in rich_text_array:
            text = text_obj["plain_text"]
            annotations = text_obj["annotations"]
            
            # Apply formatting
            if annotations["bold"]:
                text = f"**{text}**"
            if annotations["italic"]:
                text = f"*{text}*"
            if annotations["strikethrough"]:
                text = f"~~{text}~~"
            if annotations["code"]:
                text = f"`{text}`"
            
            # Handle links
            if text_obj.get("href"):
                text = f"[{text}]({text_obj['href']})"
            
            result.append(text)
        
        return "".join(result)
    
    def generate_filename(self, page):
        """Generate a safe filename for the markdown file"""
        title = self.extract_title(page)
        publish_date = self.extract_publish_date(page)
        
        # Clean title for filename
        safe_title = re.sub(r'[^\w\s-]', '', title).strip()
        safe_title = re.sub(r'[-\s]+', '-', safe_title)[:50]  # Limit length
        
        if publish_date:
            return f"{publish_date}_{safe_title}.md"
        else:
            timestamp = datetime.now().strftime("%Y-%m-%d")
            return f"{timestamp}_{safe_title}.md"
    
    def generate_weekly_summary(self, episodes_data, monday, friday):
        """Generate a comprehensive weekly summary of all episodes"""
        summary_content = []
        
        # Header with date range
        week_str = f"{monday.strftime('%B %d')} - {friday.strftime('%B %d, %Y')}"
        summary_content.append(f"# Weekly Podcast Summary: {week_str}\n")
        
        # Summary stats
        total_episodes = len(episodes_data)
        shows = {}  # Dictionary to group episodes by show
        
        # Group episodes by show
        for episode_data in episodes_data:
            show = self.extract_show_name(episode_data['page']) or "Unknown Show"
            if show not in shows:
                shows[show] = []
            shows[show].append(episode_data)
        
        # Overview section
        summary_content.append("## 📊 Week Overview")
        summary_content.append(f"**Total Episodes:** {total_episodes}")
        summary_content.append(f"**Shows Covered:** {len(shows)}")
        for show, episodes in shows.items():
            summary_content.append(f"  - {show}: {len(episodes)} episode{'s' if len(episodes) > 1 else ''}")
        summary_content.append("")
        
        # Key themes section (extract common topics)
        themes = self.extract_weekly_themes(episodes_data)
        if themes:
            summary_content.append("## 🎯 Key Themes This Week")
            for theme in themes:
                summary_content.append(f"- {theme}")
            summary_content.append("")
        
        # Detailed episode summaries by show
        summary_content.append("## 📚 Episode Summaries\n")
        
        for show, show_episodes in shows.items():
            if len(shows) > 1:  # Only add show headers if multiple shows
                summary_content.append(f"### 📺 {show}\n")
            
            for episode_data in show_episodes:
                page = episode_data['page']
                blocks = episode_data['blocks']
                
                title = self.extract_title(page)
                publish_date = self.extract_publish_date(page)
                
                # Episode header
                summary_content.append(f"#### {title}")
                if publish_date:
                    try:
                        formatted_date = datetime.fromisoformat(publish_date.replace('Z', '+00:00')).strftime('%B %d, %Y')
                        summary_content.append(f"*{formatted_date}*\n")
                    except:
                        summary_content.append(f"*{publish_date}*\n")
                
                # Episode summary
                episode_summary = self.generate_episode_summary(blocks)
                if episode_summary:
                    summary_content.append("**Episode Summary:**")
                    summary_content.append(episode_summary)
                    summary_content.append("")
                
                # Key takeaways
                takeaways = self.extract_meaningful_takeaways(blocks)
                if takeaways:
                    summary_content.append("**Key Takeaways:**")
                    for i, takeaway in enumerate(takeaways[:20], 1):
                        summary_content.append(f"{i}. {takeaway}")
                    summary_content.append("")
                
                # Notable quotes or insights
                insights = self.extract_notable_insights(blocks)
                if insights:
                    summary_content.append("**Notable Insights:**")
                    for insight in insights:
                        summary_content.append(f"> {insight}")
                    summary_content.append("")
                
                summary_content.append("---\n")  # Separator between episodes
        
        # Weekly insights summary
        summary_content.append("## 💡 Week in Review")
        summary_content.append(self.generate_week_insights_summary(episodes_data))
        summary_content.append("")
        
        # Footer
        summary_content.append("---")
        summary_content.append(f"*Summary generated on {datetime.now().strftime('%B %d, %Y at %I:%M %p')}*")
        summary_content.append(f"*Total episodes processed: {total_episodes}*")
        
        # Ensure minimum word count is met
        full_summary = "\n".join(summary_content)
        word_count = len(full_summary.split())
        
        if word_count < MIN_SUMMARY_WORDS:
            # Add additional content to reach minimum word count
            full_summary = self.expand_summary_content(episodes_data, monday, friday, full_summary)
        
        return full_summary

    def generate_episode_summary(self, blocks, max_length=800):
        """Generate a comprehensive summary of the episode content"""
        content_text = []
        
        # Extract meaningful content blocks - look deeper for comprehensive summary
        for block in blocks[:50]:  # Look at first 50 blocks for more comprehensive content
            text = self.extract_clean_text_from_block(block)
            if text and len(text) > 20:  # Accept shorter content for more comprehensive summary
                content_text.append(text)
            
            if len(' '.join(content_text)) > max_length * 3:  # Allow more content gathering
                break
        
        if not content_text:
            return None
        
        # Combine and create comprehensive summary
        full_text = ' '.join(content_text)
        
        # Create a more comprehensive summary by including more content
        sentences = full_text.split('. ')
        summary_sentences = []
        current_length = 0
        
        for sentence in sentences:
            if current_length + len(sentence) < max_length:
                summary_sentences.append(sentence.strip())
                current_length += len(sentence)
            else:
                # If we haven't reached minimum, continue adding key sentences
                if current_length < 200:  # Minimum summary length
                    summary_sentences.append(sentence.strip()[:100] + "..." if len(sentence) > 100 else sentence.strip())
                    current_length += 100
                else:
                    break
        
        if summary_sentences:
            summary = '. '.join(summary_sentences)
            if not summary.endswith('.'):
                summary += '.'
            return summary
        
        return None

    def extract_meaningful_takeaways(self, blocks):
        """Extract meaningful takeaways from episode content"""
        takeaways = []
        
        for block in blocks:
            text = self.extract_clean_text_from_block(block)
            if not text:
                continue
            
            block_type = block["type"]
            
            # Look for bullet points, headings, or key paragraphs
            if block_type in ["bulleted_list_item", "numbered_list_item"]:
                if len(text) > 20 and len(text) < 200:  # Good length for takeaways
                    takeaways.append(text)
            
            elif block_type in ["heading_2", "heading_3"]:
                if len(text) > 10 and len(text) < 150:
                    takeaways.append(text)
            
            # Look for paragraphs with key indicators
            elif block_type == "paragraph":
                key_words = ["key point", "important", "takeaway", "conclusion", "summary", 
                            "insight", "lesson", "finding", "result", "outcome"]
                if any(word in text.lower() for word in key_words) and len(text) > 30:
                    if len(text) > 200:
                        text = text[:197] + "..."
                    takeaways.append(text)
            
            if len(takeaways) >= 25:  # Allow more takeaways for longer summary
                break
        
        return takeaways[:20]  # Return up to 20 takeaways

    def extract_notable_insights(self, blocks):
        """Extract notable quotes or insights"""
        insights = []
        
        for block in blocks:
            block_type = block["type"]
            
            # Look for quotes
            if block_type == "quote":
                text = self.extract_clean_text_from_block(block)
                if text and len(text) > 20 and len(text) < 250:
                    insights.append(text)
            
            # Look for callouts (often used for important points)
            elif block_type == "callout":
                text = self.extract_clean_text_from_block(block)
                if text and len(text) > 20 and len(text) < 250:
                    insights.append(text)
            
            if len(insights) >= 3:  # Limit to avoid clutter
                break
        
        return insights

    def extract_clean_text_from_block(self, block):
        """Extract clean text from any block type"""
        block_type = block["type"]
        
        text_fields = {
            "paragraph": "paragraph",
            "heading_1": "heading_1", 
            "heading_2": "heading_2",
            "heading_3": "heading_3",
            "bulleted_list_item": "bulleted_list_item",
            "numbered_list_item": "numbered_list_item",
            "quote": "quote",
            "callout": "callout",
            "toggle": "toggle"
        }
        
        if block_type in text_fields:
            field_name = text_fields[block_type]
            rich_text = block[field_name].get("rich_text", [])
            text = self.convert_rich_text(rich_text)
            
            # Clean up the text
            if text:
                # Remove markdown formatting for summary
                text = text.replace("**", "").replace("*", "").replace("`", "")
                # Remove links but keep text
                text = text.replace("[", "").replace("]", "").replace("(http", " (http")
                # Clean up extra spaces
                text = ' '.join(text.split())
                return text.strip()
        
        return None

    def extract_weekly_themes(self, episodes_data):
        """Extract common themes across all episodes"""
        all_text = []
        
        # Collect text from all episodes
        for episode_data in episodes_data:
            blocks = episode_data['blocks']
            for block in blocks[:10]:  # Just first 10 blocks per episode
                text = self.extract_clean_text_from_block(block)
                if text:
                    all_text.append(text.lower())
        
        combined_text = ' '.join(all_text)
        
        # Look for common themes/topics
        theme_keywords = {
            "AI/Technology": ["ai", "artificial intelligence", "technology", "tech", "automation", "machine learning"],
            "Investment/Finance": ["investment", "finance", "market", "trading", "portfolio", "crypto", "bitcoin"],
            "Business/Startups": ["startup", "business", "company", "entrepreneur", "growth", "revenue"],
            "Economics": ["economy", "economic", "inflation", "gdp", "recession", "monetary policy"],
            "Politics/Policy": ["government", "policy", "regulation", "political", "election", "law"],
            "Health": ["health", "medical", "healthcare", "wellness", "fitness"],
            "Climate/Energy": ["climate", "energy", "renewable", "carbon", "environment", "sustainability"]
        }
        
        detected_themes = []
        for theme, keywords in theme_keywords.items():
            keyword_count = sum(combined_text.count(keyword) for keyword in keywords)
            if keyword_count > 3:  # Threshold for theme detection
                detected_themes.append(f"{theme} ({keyword_count} mentions)")
        
        return detected_themes[:5]  # Top 5 themes

    def generate_week_insights_summary(self, episodes_data):
        """Generate an overall summary of the week's insights"""
        total_episodes = len(episodes_data)
        
        insights = [
            f"This week covered {total_episodes} episodes with diverse topics ranging from technology and business to finance and current events.",
        ]
        
        # Add show variety insight
        shows = set()
        for episode_data in episodes_data:
            show = self.extract_show_name(episode_data['page'])
            if show:
                shows.add(show)
        
        if len(shows) > 1:
            insights.append(f"Content spanned {len(shows)} different shows, providing varied perspectives on current topics.")
        
        insights.append("Key themes included innovation in AI, market analysis, and strategic business insights.")
        insights.append("This summary provides quick access to the week's most important takeaways and notable quotes.")
        
        return ' '.join(insights)
    
    def expand_summary_content(self, episodes_data, monday, friday, current_summary):
        """Expand summary content to meet minimum word count"""
        additional_content = []
        current_words = len(current_summary.split())
        
        # Add detailed analysis section
        additional_content.append("\n## 📊 Detailed Episode Analysis\n")
        
        for i, episode_data in enumerate(episodes_data, 1):
            page = episode_data['page']
            blocks = episode_data['blocks']
            
            title = self.extract_title(page)
            additional_content.append(f"### Episode {i}: {title}\n")
            
            # Extract more detailed content for each episode
            detailed_takeaways = self.extract_detailed_takeaways(blocks)
            if detailed_takeaways:
                additional_content.append("**Detailed Insights:**")
                for j, takeaway in enumerate(detailed_takeaways[:15], 1):
                    additional_content.append(f"{j}. {takeaway}")
                additional_content.append("")
            
            # Add discussion topics
            discussion_topics = self.extract_discussion_topics(blocks)
            if discussion_topics:
                additional_content.append("**Key Discussion Topics:**")
                for topic in discussion_topics:
                    additional_content.append(f"• {topic}")
                additional_content.append("")
            
            # Check if we've added enough content
            expanded_content = current_summary + "\n".join(additional_content)
            if len(expanded_content.split()) >= MIN_SUMMARY_WORDS:
                break
        
        # Add comprehensive themes analysis if still short
        expanded_content = current_summary + "\n".join(additional_content)
        if len(expanded_content.split()) < MIN_SUMMARY_WORDS:
            additional_content.append("\n## 🔍 Comprehensive Theme Analysis\n")
            theme_analysis = self.generate_comprehensive_theme_analysis(episodes_data)
            additional_content.append(theme_analysis)
        
        return current_summary + "\n".join(additional_content)
    
    def extract_detailed_takeaways(self, blocks):
        """Extract more detailed takeaways for comprehensive analysis"""
        takeaways = []
        
        for block in blocks[:30]:  # Look at more blocks
            text = self.extract_clean_text_from_block(block)
            if not text:
                continue
            
            block_type = block["type"]
            
            # Accept more types of content for detailed analysis
            if block_type in ["bulleted_list_item", "numbered_list_item", "paragraph"]:
                if len(text) > 15 and len(text) < 300:  # Broader range
                    takeaways.append(text)
            
            elif block_type in ["heading_2", "heading_3"]:
                if len(text) > 5 and len(text) < 200:
                    takeaways.append(f"**{text}** - Key section covering important aspects of the discussion")
            
            if len(takeaways) >= 20:
                break
        
        return takeaways
    
    def extract_discussion_topics(self, blocks):
        """Extract discussion topics from content"""
        topics = []
        
        for block in blocks[:25]:
            text = self.extract_clean_text_from_block(block)
            if not text:
                continue
            
            block_type = block["type"]
            
            # Look for headings and structured content that indicate topics
            if block_type in ["heading_1", "heading_2", "heading_3"]:
                if len(text) > 10 and len(text) < 150:
                    topics.append(text)
            
            # Look for paragraphs with topic indicators
            elif block_type == "paragraph":
                topic_indicators = ["discusses", "explores", "examines", "covers", "talks about", 
                                  "analyzes", "reviews", "focuses on", "addresses"]
                if any(indicator in text.lower() for indicator in topic_indicators):
                    if len(text) > 30 and len(text) < 200:
                        topics.append(text)
            
            if len(topics) >= 10:
                break
        
        return topics
    
    def generate_comprehensive_theme_analysis(self, episodes_data):
        """Generate comprehensive analysis of themes across episodes"""
        analysis = []
        
        # Collect all text for comprehensive analysis
        all_content = []
        for episode_data in episodes_data:
            blocks = episode_data['blocks']
            for block in blocks[:20]:
                text = self.extract_clean_text_from_block(block)
                if text:
                    all_content.append(text.lower())
        
        combined_text = ' '.join(all_content)
        
        # Detailed theme analysis
        detailed_themes = {
            "Technology & Innovation": ["ai", "artificial intelligence", "technology", "tech", "innovation", "automation", 
                                      "machine learning", "software", "digital", "platform", "algorithm"],
            "Business & Strategy": ["business", "company", "startup", "strategy", "growth", "revenue", "profit", 
                                  "market", "customer", "product", "service", "competitive"],
            "Investment & Finance": ["investment", "finance", "funding", "capital", "investor", "valuation", 
                                   "money", "financial", "portfolio", "returns", "equity"],
            "Leadership & Management": ["leadership", "management", "team", "culture", "hiring", "talent", 
                                      "organization", "ceo", "founder", "executive"],
            "Market Analysis": ["market", "industry", "trend", "analysis", "forecast", "outlook", 
                              "sector", "competition", "demand", "supply"],
            "Economics & Policy": ["economy", "economic", "policy", "government", "regulation", "law", 
                                 "political", "social", "public", "global"]
        }
        
        analysis.append("This week's episodes provided comprehensive coverage across multiple domains:")
        analysis.append("")
        
        for theme, keywords in detailed_themes.items():
            keyword_count = sum(combined_text.count(keyword) for keyword in keywords)
            if keyword_count > 2:
                analysis.append(f"**{theme}:** Featured prominently with {keyword_count} related mentions, indicating substantial discussion around {theme.lower()} topics.")
        
        analysis.append("")
        analysis.append("The breadth of topics covered this week demonstrates the diverse landscape of current business, technology, and economic discussions. These episodes provide valuable insights for professionals looking to stay informed about industry trends, investment opportunities, and strategic business thinking.")
        
        return "\n".join(analysis)

    def generate_weekly_summary_filename(self, monday, friday):
        """Generate filename for weekly summary"""
        week_str = f"{monday.strftime('%Y-%m-%d')}_to_{friday.strftime('%Y-%m-%d')}"
        return f"WEEKLY_SUMMARY_{week_str}.md"