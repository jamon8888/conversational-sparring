---
name: app-store-optimization
description: Use when optimizing mobile app performance on Apple App Store or Google Play, including keyword research, metadata optimization, and competitor analysis.
license: MIT
---

# App Store Optimization (ASO)

## Overview

Comprehensive framework for improving app visibility and conversion rates on major mobile platforms through data-driven metadata and asset optimization.

## Core Capabilities

### 1. Research & Analysis

- **Keyword Research**: Analyze volume and competition. See [aso-best-practices.md](references/aso-best-practices.md).
- **Competitor Audits**: Identifying gaps in category-leading listings.
- **Sentiment Analysis**: Extracting pain points from user reviews.

### 2. Metadata Optimization

Standardize titles, descriptions, and keyword fields across platforms.

- **Platform Specs**: See [platform-specs.md](references/platform-specs.md) for character limits and logic differences between Apple and Google.
- **Automation**: Use `scripts/metadata_optimizer.py` for validation.

### 3. Performance Tracking

- **ASO Score**: Calculate health across metadata, ratings, and rankings.
- **A/B Testing**: Design and validate listing experiments.

---

## Strategy & Best Practices

- **Keywords**: Balance high-volume and long-tail terms.
- **Conversion**: Front-load benefits in titles and screenshots.
- **Reviews**: Implement strategic response and rating prompt cycles.
- **Full Library**: See [aso-best-practices.md](references/aso-best-practices.md) for detailed tactical guidelines.

---

## Automation Scripts

| Tool                    | Purpose                                                    |
| ----------------------- | ---------------------------------------------------------- |
| `keyword_analyzer.py`   | Research and difficulty scoring.                           |
| `metadata_optimizer.py` | Platform-specific limit validation.                        |
| `aso_scorer.py`         | 0-100 health assessment.                                   |
| `review_analyzer.py`    | Sentiment and issue extraction.                            |
| **Reference**           | See [script-reference.md](references/script-reference.md). |

## Boundaries & Constraints

- Focused on organic growth; does not cover paid Search Ads.
- Subject to proprietary store algorithms and periodic indexing delays.
- See [limitations.md](references/limitations.md) for full scope boundaries.
