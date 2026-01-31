# Complete Guide

> For execution instructions, see [SKILL.md](../SKILL.md)


# Content Pipeline Orchestration

## Overview
A repeatable factory for content operations. Feed anchor assets, generate multi-format outputs, schedule, distribute, and measure.

## When to Use
- You need at-scale content operations for a month/quarter
- You must standardize workflows across teams

## Trigger Phrases
- "content factory" "orchestrate content pipeline" "monthly plan"

## What it Contains
- Pipeline stages and SLAs
- Automation triggers
- Calendar scheduling
- Distribution and analytics

## Canonical Pipeline
1) Ideation: content_ideation.py → prioritized list
2) Creation: seo-workflow-orchestration / seo-geo-blog-writing
3) Repurpose: content-creation-at-scale → multi-format
4) Schedule: content_calendar.py → CSV/JSON
5) Distribute: content-distributor.py (conceptual)
6) Measure: unified-analytics → reporting templates

## Related Recipes
- recipes/content-factory-30-days.md
- recipes/content-calendar-execution.md

## References
- Skills: content-creation-at-scale, seo-workflow-orchestration, unified-analytics, content-distribution
- Frameworks: Content-Funnel.md, Pillar-Cluster.md
