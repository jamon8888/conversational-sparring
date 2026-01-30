# Complete Guide

> For execution instructions, see [SKILL.md](../SKILL.md)


# SEO Workflow Orchestration

## Overview
An opinionated workflow to produce SEO-optimized content that performs in both traditional search and LLM answer engines. Orchestrates keyword research, outlining, drafting, validation, internal linking, image generation, publish checks, and analytics.

## When to Use
- You need a repeatable SEO pipeline for blogs, guides, or landing pages
- You want GEO/AEO-optimized content (Q&A, citations, schema, entities)
- You want automation: research, validation, linking, images, structure checks

## Trigger Phrases
- "build SEO workflow" "end-to-end SEO" "GEO AEO content"
- "keyword to publish pipeline" "pillar to cluster plan"

## What it Contains
- Keyword and entity planning
- GEO/AEO patterns (Q&A, citations, FAQ schema, entity glossary)
- Draft validation (50+ SEO criteria)
- Internal link suggestions and AI images
- Structure validation and measurement

## Canonical Workflow (Automation-Ready)
1) Research
- Use seo-geo-blog-writing/scripts/keyword_research.py for keyword set
- Create entity glossary (people, brands, concepts) and add to draft
2) Outline and Draft
- Pillar-Cluster + Content-Funnel frameworks
- Add Q&A section (2–5) and FAQ schema recommendation
- Require citations with URL + publication date
3) Optimize
- iterative_validation.py (50+ checks) → fix issues
- internal_linking.py → suggestions; auto_internal_linking.py if high confidence
- image_generation.py → hero + section visuals w/ alt text
4) Structure & Publish Checks
- validate_structure.py (headers, metadata, alt text)
5) Measure
- Use unified-analytics report templates (Content Performance + Attribution)

## Assets & References
- Frameworks: Pillar-Cluster.md, Content-Funnel.md
- Skills: seo-geo-blog-writing, content-creation-at-scale, unified-analytics

## Related Recipes
- recipes/generate-seo-blog.md
- recipes/build-keyword-strategy.md
- recipes/audit-site.md

## Tips
- Always add author credentials and last updated date
- Use entity glossary consistently in headers and body
- Include a summary box and a TL;DR for GEO friendliness
