#!/usr/bin/env python3
"""
Content Formatter - Convert content between formats

Transforms content from one format to another while maintaining core
message and adapting to platform requirements.

Usage:
    python content_formatter.py blog.md --output twitter-thread
    python content_formatter.py blog.md --output linkedin --max-length 1500
    python content_formatter.py blog.md --output email-newsletter
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass

@dataclass
class PlatformSpec:
    """Platform specifications and constraints"""
    name: str
    max_chars: int
    optimal_chars: Optional[int] = None
    supports_markdown: bool = True
    supports_images: bool = True
    max_hashtags: Optional[int] = None
    
PLATFORMS = {
    "twitter": PlatformSpec("Twitter", 280, None, False, True, 2),
    "twitter-thread": PlatformSpec("Twitter Thread", 280, 250, False, True, 2),
    "linkedin": PlatformSpec("LinkedIn", 3000, 1500, True, True, 3),
    "instagram": PlatformSpec("Instagram", 2200, 150, False, True, 30),
    "facebook": PlatformSpec("Facebook", 63206, 500, False, True, 3),
    "email": PlatformSpec("Email Newsletter", 100000, 2000, True, True, 0),
    "youtube": PlatformSpec("YouTube Description", 5000, 200, False, True, 5),
}

class ContentFormatter:
    """Format content for different platforms"""
    
    def __init__(self, source_file: Path):
        self.source_file = source_file
        with open(source_file, 'r', encoding='utf-8') as f:
            self.content = f.read()
    
    def format_for_platform(self, platform: str, **kwargs) -> str:
        """Format content for specific platform"""
        if platform not in PLATFORMS:
            raise ValueError(f"Unknown platform: {platform}")
        
        spec = PLATFORMS[platform]
        
        if platform == "twitter-thread":
            return self._format_twitter_thread(**kwargs)
        elif platform == "twitter":
            return self._format_twitter(**kwargs)
        elif platform == "linkedin":
            return self._format_linkedin(**kwargs)
        elif platform == "instagram":
            return self._format_instagram(**kwargs)
        elif platform == "email":
            return self._format_email(**kwargs)
        elif platform == "youtube":
            return self._format_youtube(**kwargs)
        else:
            return self._format_generic(spec, **kwargs)
    
    def _extract_key_points(self, max_points: int = 10) -> List[str]:
        """Extract key points from content"""
        # Extract headers and first sentences
        lines = self.content.split('\n')
        key_points = []
        
        for line in lines:
            # Headers
            if line.startswith('#'):
                point = line.lstrip('#').strip()
                if point and len(point) > 10:
                    key_points.append(point)
            # Bullet points
            elif line.strip().startswith(('-', '*', '•')):
                point = line.strip().lstrip('-*•').strip()
                if point and len(point) > 10:
                    key_points.append(point)
        
        return key_points[:max_points]
    
    def _format_twitter_thread(self, max_tweets: int = 10) -> str:
        """Format as Twitter thread"""
        key_points = self._extract_key_points(max_tweets - 2)
        
        # Extract title
        title_match = re.search(r'^#\s+(.+)$', self.content, re.MULTILINE)
        title = title_match.group(1) if title_match else "Thread"
        
        tweets = []
        
        # Hook tweet
        tweets.append(f"🧵 {title}\n\nA thread 👇")
        
        # Content tweets
        for i, point in enumerate(key_points, 1):
            tweet = f"{i}/ {point}"
            if len(tweet) > 280:
                tweet = tweet[:277] + "..."
            tweets.append(tweet)
        
        # CTA tweet
        tweets.append(f"{len(key_points) + 1}/ Want to learn more?\n\n[Add your CTA here]")
        
        return "\n\n---TWEET---\n\n".join(tweets)
    
    def _format_twitter(self, **kwargs) -> str:
        """Format as single Twitter post"""
        key_points = self._extract_key_points(1)
        
        if key_points:
            tweet = key_points[0]
            if len(tweet) > 280:
                tweet = tweet[:277] + "..."
            return tweet
        
        # Fallback: use first paragraph
        paragraphs = [p.strip() for p in self.content.split('\n\n') if p.strip()]
        if paragraphs:
            tweet = paragraphs[0][:277] + "..."
            return tweet
        
        return "Content formatted for Twitter"
    
    def _format_linkedin(self, optimize_engagement: bool = False, **kwargs) -> str:
        """Format for LinkedIn"""
        # Extract title and key points
        title_match = re.search(r'^#\s+(.+)$', self.content, re.MULTILINE)
        title = title_match.group(1) if title_match else "Insight"
        
        key_points = self._extract_key_points(5)
        
        # Build LinkedIn post
        post = f"{title}\n\n"
        
        # Add hook (first paragraph or summary)
        paragraphs = [p.strip() for p in self.content.split('\n\n') if p.strip() and not p.startswith('#')]
        if paragraphs:
            hook = paragraphs[0][:200]
            post += f"{hook}...\n\n"
        
        # Add key points
        if key_points:
            post += "Key takeaways:\n\n"
            for point in key_points:
                post += f"→ {point}\n"
        
        post += "\n---\n\nWhat's your take on this?"
        
        # Optimize for engagement if requested
        if optimize_engagement:
            post += "\n\n💬 Comment below\n🔄 Repost to share\n👍 Like if helpful"
        
        # Ensure under 3000 chars
        if len(post) > 3000:
            post = post[:2997] + "..."
        
        return post
    
    def _format_instagram(self, add_hashtags: bool = True, **kwargs) -> str:
        """Format for Instagram caption"""
        # Short, engaging caption
        key_points = self._extract_key_points(3)
        
        caption = ""
        if key_points:
            caption = key_points[0]
            if len(caption) > 150:
                caption = caption[:147] + "..."
        
        caption += "\n\n💡 Key insights:\n"
        for i, point in enumerate(key_points[1:4], 1):
            short_point = point[:50] + "..." if len(point) > 50 else point
            caption += f"{i}. {short_point}\n"
        
        caption += "\n👉 Link in bio for full article"
        
        if add_hashtags:
            caption += "\n\n#contentmarketing #digitalmarketing #marketing"
        
        return caption
    
    def _format_email(self, **kwargs) -> str:
        """Format for email newsletter"""
        # Extract title
        title_match = re.search(r'^#\s+(.+)$', self.content, re.MULTILINE)
        title = title_match.group(1) if title_match else "Newsletter"
        
        # Build email
        email = f"Subject: {title}\n\n"
        email += "---EMAIL BODY---\n\n"
        email += f"Hi there,\n\n"
        
        # Add summary
        key_points = self._extract_key_points(5)
        email += f"Today I want to share insights about {title.lower()}.\n\n"
        
        # Add main content (abbreviated)
        email += "Here's what you'll learn:\n\n"
        for point in key_points:
            email += f"• {point}\n"
        
        email += "\n[Add full content or link to full article here]\n\n"
        email += "Best,\n[Your Name]"
        
        return email
    
    def _format_youtube(self, **kwargs) -> str:
        """Format for YouTube description"""
        # Extract title
        title_match = re.search(r'^#\s+(.+)$', self.content, re.MULTILINE)
        title = title_match.group(1) if title_match else "Video"
        
        key_points = self._extract_key_points(8)
        
        description = f"{title}\n\n"
        
        # Add chapters/timestamps
        description += "📖 Chapters:\n"
        for i, point in enumerate(key_points):
            time = f"0{i}:00" if i < 10 else f"{i}:00"
            description += f"{time} - {point}\n"
        
        description += "\n---\n\n"
        description += "Subscribe for more content!\n"
        description += "\n#youtube #tutorial #howto"
        
        return description
    
    def _format_generic(self, spec: PlatformSpec, **kwargs) -> str:
        """Generic formatting for unknown platforms"""
        key_points = self._extract_key_points(5)
        
        content = "\n".join(f"• {point}" for point in key_points)
        
        if spec.max_chars and len(content) > spec.max_chars:
            content = content[:spec.max_chars - 3] + "..."
        
        return content

def main():
    parser = argparse.ArgumentParser(description="Format content for different platforms")
    parser.add_argument("input_file", type=Path, help="Input markdown file")
    parser.add_argument("--output", "-o", required=True, 
                       choices=list(PLATFORMS.keys()),
                       help="Output platform format")
    parser.add_argument("--max-tweets", type=int, default=10,
                       help="Max tweets for thread (default: 10)")
    parser.add_argument("--optimize-engagement", action="store_true",
                       help="Add engagement CTAs (LinkedIn)")
    parser.add_argument("--add-hashtags", action="store_true",
                       help="Add hashtags (Instagram)")
    parser.add_argument("--output-file", "-f", type=Path,
                       help="Output file (default: stdout)")
    
    args = parser.parse_args()
    
    if not args.input_file.exists():
        print(f"Error: File not found: {args.input_file}", file=sys.stderr)
        sys.exit(1)
    
    try:
        formatter = ContentFormatter(args.input_file)
        result = formatter.format_for_platform(
            args.output,
            max_tweets=args.max_tweets,
            optimize_engagement=args.optimize_engagement,
            add_hashtags=args.add_hashtags
        )
        
        if args.output_file:
            with open(args.output_file, 'w', encoding='utf-8') as f:
                f.write(result)
            print(f"✅ Formatted content saved to: {args.output_file}")
        else:
            print(result)
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
