# Complete Guide

> For execution instructions, see [SKILL.md](../SKILL.md)


# Marketing Analytics Mastery

## Overview
Measure what matters. This skill helps you track, analyze, and optimize your marketing performance using key metrics like ROI, CAC, and LTV.

## When to Use This Skill
- Calculating campaign profitability
- Setting up marketing dashboards
- Reporting to stakeholders
- Budgeting for next quarter

## Key Metrics

### 1. Return on Investment (ROI)
Formula: `(Revenue - Cost) / Cost * 100`
Use this to determine the efficiency of your ad spend.

### 2. Customer Acquisition Cost (CAC)
Formula: `Total Sales & Marketing Cost / New Customers Acquired`
Use this to understand how much you pay for each new client.

### 3. Lifetime Value (LTV)
Formula: `Average Revenue Per User * Gross Margin * Retention Period`
Use this to determine how much you can afford to spend on acquisition (Target CAC < LTV/3).

## Dashboard Setup
Use the `kpi_dashboard_config.json` asset to structure your reporting dashboard. It covers Acquisition, Engagement, Conversion, and Retention metrics.

## Tools
Use the `roi_calculator.py` script to quickly crunch numbers.
Usage: `python scripts/roi_calculator.py [Spend] [Revenue] [Customers]`
