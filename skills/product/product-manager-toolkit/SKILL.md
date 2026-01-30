---
name: product-manager-toolkit
description: Use when prioritizing features using RICE, analyzing customer interviews, or drafting PRDs to align stakeholders on a product roadmap and extract user pain points.
license: MIT
---

# Product Manager Toolkit

## Overview

Essential frameworks for product discovery, prioritization, and requirements definition.

## Core Workflows

### 1. Feature Prioritization (RICE)

Systematic scoring and portfolio analysis to identify high-impact features.

- **Automation**: Use `scripts/rice_prioritizer.py` for RICE scores and capacity planning.
- **Frameworks**: See [prioritization_frameworks.md](references/prioritization_frameworks.md) for RICE, MoSCoW, and Value vs. Effort logic.

### 2. Customer Discovery & Insights

Extracting actionable pain points from user research.

- **Automation**: Use `scripts/customer_interview_analyzer.py` for NLP-driven transcript analysis.
- **Frameworks**: See [discovery_frameworks.md](references/discovery_frameworks.md) for interview guides and Opportunity Solution Trees.

### 3. Requirements Definition (PRD)

Structuring solutions for engineering and design execution.

- **Templates**: See [prd_templates.md](references/prd_templates.md) for Standard, One-Page, and Agile Epic formats.

---

## Strategy & Best Practices

- **Metrics**: Track success via North Star and AARRR frameworks. See [product_metrics.md](references/product_metrics.md).
- **Avoid Pitfalls**: Stay problem-first and avoid the "Feature Factory" trap. See [pm_best_practices.md](references/pm_best_practices.md).

## Tools & Commands

| Task              | Command                                                        |
| ----------------- | -------------------------------------------------------------- |
| Score Features    | `python scripts/rice_prioritizer.py features.csv`              |
| Analyze Interview | `python scripts/customer_interview_analyzer.py transcript.txt` |
| JSON Output       | Add `json` or `--output json` to script arguments.             |
