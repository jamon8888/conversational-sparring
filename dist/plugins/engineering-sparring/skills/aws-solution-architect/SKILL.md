---
name: aws-solution-architect
description: Use when designing serverless cloud infrastructure on AWS, optimizing cloud costs, or implementing infrastructure-as-code (IaC) to resolve scalability bottlenecks or architectural uncertainty.
license: MIT
---

# AWS Solution Architect for Startups

## Overview

Strategic architecture design for cloud-native startups, focusing on serverless, scalability, security, and cost-efficiency.

## Architecture Design

### Core Patterns

Standardized architectures for various startup needs:

- **Patterns Catalog**: See [architecture_patterns.md](references/architecture_patterns.md) for serverless, event-driven, and three-tier stacks.
- **Service Guide**: Use the [service_selection.md](references/service_selection.md) to choose the right compute, database, and messaging tools.

### Evolution Strategy

Architecture should grow with the company:

- **Lifecycle Phases**: See [startup_lifecycle.md](references/startup_lifecycle.md) for MVP to Series A+ scaling strategies and common pitfalls.

---

## Best Practices (Well-Architected)

Maintain high standards across secondary pillars:

- **Optimization & Safety**: See [well_architected.md](references/well_architected.md) for cost-saving tactics, security hardening, and reliability principles.

---

## Infrastructure as Code (IaC) & Scripts

| Tool                       | Purpose                                      |
| -------------------------- | -------------------------------------------- |
| `architecture_designer.py` | Service and pattern recommendations.         |
| `serverless_stack.py`      | Automates Lambda/APIG/DynamoDB creation.     |
| `cost_optimizer.py`        | Bill analysis and reduction recommendations. |
| `iac_generator.py`         | Outputs CloudFormation, CDK, or Terraform.   |
| `security_auditor.py`      | Compliance and best practice validation.     |

## Input Requirements

To design an architecture, provide:

1. **Application Type**: SaaS, API, Mobile, etc.
2. **Traffic Scales**: Expected users/day, requests/sec.
3. **Data profile**: Storage volume, type (Relational/NoSQL).
4. **Constraints**: Budget limits, compliance (GDPR/HIPAA), team skill level.
