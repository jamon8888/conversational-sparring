# Complete Guide

> For execution instructions, see [SKILL.md](../SKILL.md)


# Content Creation at Scale: Multi-Format, Multi-Platform Automation

## Overview

A comprehensive content production system that enables teams to create, repurpose, and distribute content across all formats and platforms at scale. Transform one piece of content into 20+ variations, maintain brand consistency across channels, and orchestrate team workflows with automated quality checks.

**Key Capabilities**:
- ✅ Multi-format content creation (blog, social, email, video, audio, visual)
- ✅ Automated content repurposing (1 blog → 20+ pieces)
- ✅ Platform-specific optimization (Twitter, LinkedIn, YouTube, TikTok, etc.)
- ✅ Content calendar management and scheduling
- ✅ Team workflow orchestration with approvals
- ✅ Cross-platform distribution automation
- ✅ Brand voice consistency checking
- ✅ A/B testing and performance analytics
- ✅ Batch processing for content series
- ✅ Topic research and ideation at scale

---

## When to Use This Skill

### Primary Use Cases

1. **Multi-Channel Campaigns** - Launch coordinated campaigns across 10+ platforms
2. **Content Repurposing** - Turn existing content into multiple formats automatically
3. **Content Series Production** - Create 30-day content calendars with batch processing
4. **Team Content Operations** - Coordinate distributed teams with workflow automation
5. **Omnichannel Presence** - Maintain consistent brand presence everywhere
6. **Content Agencies** - Manage multiple clients at scale
7. **A/B Testing Campaigns** - Test and optimize content variations
8. **Social Media at Scale** - Daily posting across multiple accounts

### When to Choose This vs. Other Skills

**Use content-creation-at-scale when**:
- You need content across multiple formats (blog + social + email + video)
- You're managing 5+ platforms simultaneously
- You have a team collaborating on content
- You need content calendar and workflow management
- You want to repurpose content automatically
- You're producing 10+ pieces of content per week

**Use seo-geo-blog-writing when**:
- You only need blog posts
- SEO optimization is the primary goal
- You don't need multi-platform distribution

**Use content-repurposing when**:
- You already have finished content
- You only need format conversion (no creation)

**Use individual format skills when**:
- You're focused on a single format (video, podcast, etc.)
- You don't need cross-format automation

---

## Content Formats Supported

### 1. Long-Form Content
- **Blog Posts** - 1,500+ word articles
- **White Papers** - 10+ page research documents
- **eBooks** - Multi-chapter guides
- **Case Studies** - Customer success stories
- **Research Reports** - Data-driven insights

### 2. Short-Form Content
- **Twitter/X** - Threads and standalone posts (280 chars)
- **LinkedIn** - Professional posts (1,200-1,500 chars optimal)
- **Facebook** - Engagement posts
- **Instagram** - Captions (2,200 char max)
- **TikTok** - Short video descriptions

### 3. Email Content
- **Newsletters** - Weekly/monthly updates
- **Drip Sequences** - Automated email series
- **Promotional Emails** - Product launches, offers
- **Transactional Emails** - Receipts, confirmations

### 4. Video Content
- **YouTube Videos** - Long-form scripts (10+ min)
- **Short-Form Videos** - TikTok, Reels, Shorts (<60 sec)
- **Video Descriptions** - SEO-optimized descriptions
- **Video Chapters** - Timestamp markers

### 5. Audio Content
- **Podcast Scripts** - Episode outlines and scripts
- **Audio Ad Scripts** - 15/30/60 second spots
- **Voice-Over Scripts** - Narration text

### 6. Visual Content
- **Social Graphics** - Quote cards, statistics
- **Infographics** - Data visualizations
- **Presentation Slides** - Deck outlines
- **Thumbnails** - Video/blog thumbnails

### 7. Interactive Content
- **Polls** - Engagement questions
- **Quizzes** - Lead generation quizzes
- **Surveys** - Feedback forms

---

## Core Automation Scripts

### 1. content_formatter.py
**Convert content between formats**

Transform content from one format to another while maintaining core message and adapting to platform requirements.

**Usage**:
```bash
# Blog to Twitter thread
python content_formatter.py blog-post.md --output twitter-thread --max-tweets 10

# Blog to LinkedIn post
python content_formatter.py blog-post.md --output linkedin --optimize-engagement

# Long-form to short-form
python content_formatter.py whitepaper.md --output instagram-caption
```

**Features**:
- Character limit enforcement
- Platform-specific formatting
- Hashtag optimization
- CTA adaptation
- Tone adjustment

---

### 2. content_repurposer.py
**Automatically create multiple content pieces from one source**

Take one piece of content and generate 20+ variations across formats.

**Usage**:
```bash
# Repurpose to all formats
python content_repurposer.py blog-post.md --all-formats

# Specific formats only
python content_repurposer.py blog-post.md \
  --formats twitter,linkedin,email,video-script,infographic

# With images
python content_repurposer.py blog-post.md --all-formats --generate-images
```

**Output Example**:
```
From 1 blog post, generates:
- 5 Twitter threads
- 3 LinkedIn posts
- 1 Email newsletter
- 1 Video script
- 5 Instagram captions
- 1 Infographic outline
- 10 Quote cards
= 26 total pieces
```

---

### 3. platform_optimizer.py
**Optimize content for specific platforms**

Ensure content meets platform requirements and best practices.

**Usage**:
```bash
# Optimize for Twitter
python platform_optimizer.py draft.txt --platform twitter --add-hashtags

# Optimize for LinkedIn
python platform_optimizer.py draft.txt --platform linkedin --professional-tone

# Check all platforms
python platform_optimizer.py draft.txt --check-all-platforms
```

**Platform Specs**:
- Character limits
- Image dimensions
- Hashtag recommendations
- Best posting times
- Engagement tactics

---

### 4. content_calendar.py
**Manage content calendar and scheduling**

Create, schedule, and track content across platforms.

**Usage**:
```bash
# Create 30-day calendar
python content_calendar.py --create --days 30 --platforms twitter,linkedin

# Add content to calendar
python content_calendar.py --add post.md --date 2025-01-15 --platform twitter

# View schedule
python content_calendar.py --view --month 2025-01

# Export calendar
python content_calendar.py --export --format csv
```

**Features**:
- Multi-platform scheduling
- Content gap identification
- Frequency balancing
- Deadline tracking
- Calendar export (CSV, iCal)

---

### 5. tone_analyzer.py
**Ensure brand voice consistency**

Analyze tone and check brand voice alignment across all content.

**Usage**:
```bash
# Analyze tone
python tone_analyzer.py draft.md --brand-voice-file brand-voice.json

# Compare against brand voice
python tone_analyzer.py draft.md --compare

# Batch check
python tone_analyzer.py content/*.md --batch --report
```

**Tone Attributes**:
- Formal vs. Casual
- Professional vs. Friendly
- Serious vs. Humorous
- Technical vs. Simple
- Direct vs. Conversational

---

### 6. content_workflow.py
**Orchestrate team workflows**

Manage content creation workflows with status tracking and approvals.

**Usage**:
```bash
# Initialize workflow
python content_workflow.py --init blog-workflow

# Update status
python content_workflow.py --update post-123 --status review

# Assign task
python content_workflow.py --assign post-123 --to editor@company.com

# View pipeline
python content_workflow.py --view --status all
```

**Workflow Stages**:
1. Ideation
2. Research
3. Draft
4. Review
5. Edit
6. Approve
7. Schedule
8. Publish

---

### 7. content_distributor.py
**Publish to multiple platforms**

Automate publishing across social media, blogs, and email.

**Usage**:
```bash
# Publish now
python content_distributor.py post.md \
  --platforms twitter,linkedin,medium

# Schedule for later
python content_distributor.py post.md \
  --platforms twitter,linkedin \
  --schedule "2025-01-15 10:00"

# Batch publish
python content_distributor.py content/*.md --schedule-optimal
```

**Supported Platforms**:
- Twitter/X API
- LinkedIn API
- Medium API
- WordPress REST API
- Facebook Graph API
- Instagram Graph API

---

### 8. performance_analyzer.py
**Track content performance**

Aggregate metrics across platforms and generate insights.

**Usage**:
```bash
# Analyze single post
python performance_analyzer.py --post-id 12345 --platform twitter

# Compare platforms
python performance_analyzer.py --campaign Q1-2025 --compare

# Generate report
python performance_analyzer.py --date-range "2025-01-01,2025-01-31" --report
```

**Metrics Tracked**:
- Views/Impressions
- Engagement (likes, comments, shares)
- Click-through rate
- Conversions
- ROI

---

### 9. ab_test_generator.py
**Create content variations for testing**

Generate multiple variations to test and optimize.

**Usage**:
```bash
# Generate headline variations
python ab_test_generator.py post.md --vary headlines --count 5

# Generate CTA variations
python ab_test_generator.py post.md --vary ctas --count 3

# Full variations
python ab_test_generator.py post.md --vary all --count 5
```

**Variation Types**:
- Headlines
- CTAs (Call to Action)
- Opening hooks
- Content length
- Tone/voice
- Visual elements

---

### 10. content_ideation.py
**Generate content ideas at scale**

Research trending topics and generate prioritized content ideas.

**Usage**:
```bash
# Generate ideas
python content_ideation.py --topic "content marketing" --count 50

# Trending topics
python content_ideation.py --trending --industry marketing

# Gap analysis
python content_ideation.py --competitor-gaps competitors.json
```

**Sources**:
- Trending topics (Google Trends, Twitter Trends)
- Competitor content gaps
- Keyword research
- Audience questions
- Seasonal content

---

## Modified Scripts from SEO-GEO

### keyword_research.py (Unchanged)
**Still used for**: Topic research, keyword data
- Kept as-is from SEO-GEO skill
- Useful for all content formats

### image_generation.py (Unchanged)
**Still used for**: Visual content generation
- Generates images for blog, social, email
- Google Imagen + DALL-E integration

### competitor_analysis.py (Unchanged)
**Still used for**: Competitive intelligence
- Multi-format competitor tracking
- Content strategy insights

### iterative_validation.py → quality_checker.py
**Enhanced for**: Multi-format quality checks
- Format-specific validation
- Brand voice checking
- Platform requirement validation

### config_loader.py (Unchanged)
**Still used for**: Configuration management
- API credentials
- Platform settings
- Workflow configurations

---

## Complete Workflow Examples

### Workflow 1: Blog Post → Multi-Platform Campaign

**Step 1: Research & Ideation**
```bash
# Generate content ideas
python content_ideation.py --topic "email marketing" --count 10

# Research keywords
python keyword_research.py "email marketing best practices" --limit 20
```

**Step 2: Create Blog Post**
```bash
# Write blog post (with AI assistance or manually)
# Save as blog-post.md
```

**Step 3: Repurpose to All Formats**
```bash
# Auto-generate 20+ content pieces
python content_repurposer.py blog-post.md --all-formats --output ./campaign/

# Generates:
# - twitter-threads/ (5 threads)
# - linkedin-posts/ (3 posts)
# - email-newsletter.md
# - video-script.md
# - instagram-captions/ (5 captions)
# - infographic-outline.md
# - quote-cards/ (10 quotes)
```

**Step 4: Generate Visuals**
```bash
# Create images for each format
python image_generation.py campaign/* --batch --optimize-sizes
```

**Step 5: Quality Check**
```bash
# Validate all content
python quality_checker.py campaign/* --batch --brand-voice brand-voice.json
```

**Step 6: Schedule Campaign**
```bash
# Add to content calendar
python content_calendar.py --add-campaign campaign/ \
  --start-date 2025-01-15 \
  --duration 30-days \
  --platforms twitter,linkedin,instagram,medium
```

**Step 7: Publish**
```bash
# Auto-publish on schedule
python content_distributor.py --from-calendar --auto-publish
```

**Step 8: Track Performance**
```bash
# Monitor results
python performance_analyzer.py --campaign blog-post-campaign --real-time
```

---

### Workflow 2: 30-Day Content Series

**Goal**: Create 30 days of content across all platforms

```bash
# Step 1: Generate 30 topic ideas
python content_ideation.py --topic "marketing" --count 30 > topics.json

# Step 2: Create content calendar
python content_calendar.py --create --days 30 --topics topics.json

# Step 3: Batch create content (loop through topics)
for topic in $(cat topics.json | jq -r '.[]'); do
  # Create base content
  echo "Creating content for: $topic"
  
  # Repurpose to all formats
  python content_repurposer.py "content-$topic.md" --all-formats
  
  # Generate images
  python image_generation.py "content-$topic.md" --batch
  
  # Quality check
  python quality_checker.py "content-$topic.md"
done

# Step 4: Schedule entire month
python content_calendar.py --schedule-batch output/ --optimize-timing

# Step 5: Auto-publish
python content_distributor.py --from-calendar --month 2025-01
```

---

### Workflow 3: A/B Testing Campaign

**Goal**: Test content variations and scale winners

```bash
# Step 1: Create base content
# Write base-content.md

# Step 2: Generate variations
python ab_test_generator.py base-content.md \
  --vary headlines,ctas \
  --count 5 \
  --output variations/

# Step 3: Publish variations to split audience
python content_distributor.py variations/* \
  --platform twitter \
  --split-test \
  --audience-split 20

# Step 4: Monitor performance (wait 24-48 hours)
python performance_analyzer.py \
  --campaign ab-test-001 \
  --report-interval 6h

# Step 5: Identify winner
python performance_analyzer.py \
  --campaign ab-test-001 \
  --select-winner \
  --criteria engagement

# Step 6: Scale winning variation
python content_distributor.py winner.md \
  --platforms twitter,linkedin,facebook \
  --full-audience
```

---

## Templates & Assets

### Format Templates (`assets/templates/`)

**blog-post-template.md** - Long-form blog structure
**twitter-thread-template.md** - Thread format with hooks
**linkedin-post-template.md** - Professional post structure
**email-newsletter-template.md** - Newsletter format
**video-script-template.md** - Video script outline
**instagram-caption-template.md** - IG caption with hashtags
**presentation-outline-template.md** - Slide deck structure

### Platform Specifications (`assets/platform-specs.json`)

```json
{
  "twitter": {
    "max_chars": 280,
    "max_images": 4,
    "image_dimensions": "1200x675",
    "optimal_hashtags": 2,
    "best_times": ["8-10am", "12-1pm", "5-6pm"]
  },
  "linkedin": {
    "max_chars": 3000,
    "optimal_chars": "1200-1500",
    "max_images": 9,
    "image_dimensions": "1200x627",
    "best_times": ["7-8am", "12pm", "5-6pm"]
  },
  "instagram": {
    "max_caption_chars": 2200,
    "optimal_caption_chars": "138-150",
    "image_dimensions": "1080x1080",
    "optimal_hashtags": "5-10",
    "max_hashtags": 30
  }
}
```

### Content Calendar Template (`assets/content-calendar-template.csv`)

```csv
Date,Day,Platform,Format,Topic,Status,Assignee,URL,Notes
2025-01-15,Wed,Twitter,Thread,Email Marketing,Draft,@editor,,
2025-01-15,Wed,LinkedIn,Post,Email Marketing,Draft,@editor,,
2025-01-16,Thu,Blog,Article,Email Marketing,Review,@writer,,
```

### Workflow Templates (`assets/workflow-templates.json`)

```json
{
  "blog_workflow": {
    "stages": ["ideation", "research", "draft", "review", "edit", "approve", "publish"],
    "approvers": {"review": "editor", "approve": "content_lead"},
    "sla_hours": 48,
    "notifications": true
  },
  "social_workflow": {
    "stages": ["draft", "review", "schedule", "publish"],
    "approvers": {"review": "social_manager"},
    "sla_hours": 4,
    "notifications": true
  }
}
```

### Brand Voice Guidelines (`assets/brand-voice.json`)

```json
{
  "brand_voice": {
    "attributes": ["professional", "helpful", "concise", "data-driven"],
    "tone_score": {
      "formal": 7,
      "professional": 9,
      "friendly": 6,
      "technical": 5
    },
    "avoid": ["jargon", "passive voice", "buzzwords"],
    "preferred_words": ["actionable", "proven", "results"],
    "examples": [
      {
        "good": "Our data shows 40% improvement in engagement",
        "bad": "We're like, super good at engagement stuff"
      }
    ]
  }
}
```

---

## Performance Metrics

### Time Savings

| Task | Manual Time | Automated | Savings |
|------|-------------|-----------|---------|
| Blog → Social conversion | 45 min | 2 min | 96% |
| Content calendar (30 days) | 4 hours | 15 min | 94% |
| Platform optimization | 20 min/platform | 1 min | 95% |
| Image creation | 30 min | 3 min | 90% |
| Quality checking | 15 min | 2 min | 87% |
| Publishing (5 platforms) | 30 min | 1 min | 97% |
| **Total per campaign** | **8 hours** | **40 min** | **92%** |

### Output Multiplier

**From 1 blog post**:
- 5 Twitter threads
- 3 LinkedIn posts
- 1 Email newsletter
- 1 Video script
- 5 Instagram captions
- 10 Quote cards
- 1 Infographic outline
- 3 Facebook posts
- 1 Medium article
= **30 pieces of content**

**Time**: 40 minutes total (with automation)

---

## Configuration

### Setup

**1. Install Dependencies**
```bash
cd content-toolkit/skills/content-creation-at-scale/scripts
pip install -r requirements.txt
```

**2. Configure APIs**

Create `content-scale-config.json`:
```json
{
  "apis": {
    "twitter": {"api_key": "...", "api_secret": "..."},
    "linkedin": {"access_token": "..."},
    "openai": {"api_key": "..."}
  },
  "settings": {
    "default_platforms": ["twitter", "linkedin"],
    "quality_threshold": 80,
    "auto_publish": false
  }
}
```

**3. Set Up Brand Voice**

Edit `assets/brand-voice.json` with your brand guidelines.

**4. Initialize Workflows**

```bash
python content_workflow.py --init blog-workflow
python content_workflow.py --init social-workflow
```

---

## Use Cases by Role

### Content Marketing Manager
- Plan 90-day content calendars
- Coordinate team workflows
- Track content performance across channels
- Maintain brand consistency

### Social Media Manager
- Repurpose blog content for social
- Schedule posts across platforms
- A/B test social content
- Monitor engagement metrics

### Content Agency
- Manage multiple client calendars
- Batch produce content
- Maintain client brand voices
- Report on multi-client performance

### Solo Creator/Founder
- Maximize reach with limited time
- Maintain consistent posting
- Automate distribution
- Focus on content quality, not logistics

---

## Advanced Features

### Batch Processing

Process 30 blog posts at once:
```bash
for file in content/*.md; do
  python content_repurposer.py "$file" --all-formats
  python image_generation.py "$file" --batch
  python quality_checker.py "$file"
done

python content_calendar.py --schedule-batch output/ --optimize-timing
```

### CI/CD Integration

```yaml
name: Content Pipeline
on: [push]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Quality Check
        run: python quality_checker.py content/*.md --strict
      
      - name: Generate Variations
        run: python content_repurposer.py content/*.md --all-formats
      
      - name: Schedule
        run: python content_calendar.py --schedule-batch output/
```

### API Integrations

Connect to existing tools:
- **CMS**: WordPress, Contentful, Sanity
- **Social**: Hootsuite, Buffer, Sprout Social
- **Email**: Mailchimp, ConvertKit, ActiveCampaign
- **Analytics**: Google Analytics, Mixpanel

---

## Troubleshooting

### Common Issues

**1. Platform API Rate Limits**
- Use `--rate-limit` flag
- Schedule publishing over time
- Cache API responses

**2. Brand Voice Consistency**
- Train tone analyzer with more examples
- Review `brand-voice.json` regularly
- Manual review for critical content

**3. Image Generation Costs**
- Use image caching
- Generate images selectively
- Consider stock photos for some formats

**4. Content Quality Drops**
- Set higher quality thresholds
- Manual review for key pieces
- Iterate on prompts and templates

---

## Related Skills

### Within Content Toolkit
- **seo-geo-blog-writing** - Specialized blog creation
- **content-repurposing** - Simple format conversion
- **content-analytics** - Performance measurement
- **video-marketing** - Video-specific optimization
- **podcasting** - Audio content creation

### Cross-Toolkit References

**→ Marketing Toolkit**:
- `content-strategy` - Overall content planning
- `marketing-analytics` - Campaign performance
- `social-media-content` - Social-specific tactics

**→ Growth Toolkit**:
- `experiment-design` - A/B testing methodology
- `growth-analytics` - Funnel optimization

**→ Strategic Research Toolkit**:
- `market-research` - Topic validation
- `customer-discovery` - Audience insights

---

## Tips & Best Practices

### Content Creation
1. **Start with pillar content** - Create one strong piece, repurpose to 20+
2. **Maintain brand voice** - Use tone analyzer on every piece
3. **Quality over quantity** - Set high quality thresholds
4. **Test everything** - A/B test headlines, CTAs, formats
5. **Track what works** - Use performance analyzer to optimize

### Workflow Management
1. **Clear approval process** - Define who approves what
2. **Realistic SLAs** - Set achievable turnaround times
3. **Buffer time** - Don't schedule everything last-minute
4. **Review cadence** - Weekly pipeline reviews
5. **Team communication** - Use notifications sparingly

### Platform Optimization
1. **Know your platforms** - Different content performs differently
2. **Best posting times** - Follow platform-specific guidelines
3. **Hashtag strategy** - Research before adding
4. **Visual consistency** - Use brand colors and fonts
5. **Engagement tactics** - Include CTAs, questions, polls

---

## Cost Analysis

### API Costs (per 1000 pieces)

| Service | Usage | Unit Cost | Total |
|---------|-------|-----------|-------|
| Topic Research | 100 queries | $0.50 | $50 |
| Image Generation | 500 images | $0.02-0.08 | $10-40 |
| Platform APIs | 1000 posts | $0 | $0 (free tiers) |
| **Total** | | | **$60-90** |

### Time Value

At $50/hour team rate:
- Manual: 8 hours × $50 = $400 per campaign
- Automated: 40 min × $50/60 = $33 per campaign
- **Savings**: $367 per campaign

**ROI**: Break-even at 1 campaign

---

## Version History

- **v1.0** - November 2025: Initial release with 10 core scripts
- Multi-format support
- Platform optimization
- Team workflows
- Content repurposing

---

## License & Attribution

Based on GTM Agents Content Toolkit standards.
- **License**: MIT
- **Adapted From**: SEO-GEO Blog Writing skill

---

## Support & Documentation

### References
- `references/platform-guidelines.md` - Platform best practices
- `references/content-formats-guide.md` - Format templates
- `references/brand-voice-framework.md` - Voice consistency
- `references/content-workflows.md` - Workflow templates
- `references/repurposing-playbook.md` - Repurposing strategies
- `references/scale-optimization.md` - Scale best practices

### Script Help
```bash
python [script].py --help
```

---

**Next Steps**: Start with `content_ideation.py` to generate ideas, then follow Workflow 1 to create your first multi-platform campaign.
