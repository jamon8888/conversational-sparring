# Complete Guide

> For execution instructions, see [SKILL.md](../SKILL.md)


# Email Campaign Automation

## Overview
Create newsletters and drip sequences from anchor content, generate variations for testing, ensure tone consistency, schedule across a content calendar, and measure outcomes.

## When to Use
- You need fast campaign/sequence generation from existing content
- You want A/B tests for subjects, CTAs, offers
- You want tone consistency and scheduling

## Trigger Phrases
- "build email sequence" "newsletter from blog" "email automation"

## What it Contains
- Sequence templates and testing plan
- Brand voice checks
- Calendar scheduling
- Measurement handoff

## Workflow
1) Generate base emails from anchor content: content_formatter.py / content_repurposer.py
2) A/B test: ab_test_generator.py (subjects, CTAs)
3) Tone & voice: tone_analyzer.py (brand-voice.json)
4) Schedule: content_calendar.py (CSV/JSON export)
5) Measure: unified-analytics (email dashboard blocks)

## Related Recipes
- recipes/design-email-campaign.md
- recipes/build-email-automation.md
- recipes/optimize-deliverability.md

## References
- Skills: content-creation-at-scale, unified-analytics, lead-magnets
- Frameworks: AIDA.md, Hook-Story-Offer.md
