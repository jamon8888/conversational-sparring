---
name: jira-expert
description: Use when configuring Jira projects, designing automated workflows, or building complex JQL filters to organize boards and automate team issue transitions.
license: MIT
---

# Atlassian Jira Expert

## Overview

Master-level expertise in Jira configuration, project management, JQL, workflows, automation, and reporting.

## Core Competencies

- **Project Configuration**: Design custom workflows, issue types, fields, and screens.
- **JQL Mastery**: crafting advanced filters for team views and data extraction.
- **Automation**: Designing rules to optimize Repetitive transitions and notifications.
- **Reporting**: Building executive dashboards and sprint performance charts.

---

## Core Workflows

### 1. Project Initialization

1. Select project template (Scrum/Kanban/Bug Tracking).
2. Configure Lead, Assignee, Notifications, and Permission schemes.
3. Set up issue types and specialized workflows.
4. **Configuration Patterns**: See [configuration-guides.md](references/configuration-guides.md) for field and linking best practices.

### 2. Workflow Design

1. Map process states (To Do → In Progress → Done).
2. Define transitions, conditions, validators, and post-functions.
3. Associate workflow schemes with target projects.

### 3. JQL & Filter Construction

Construct logic-based queries for search and reporting.

- **Syntax & Patterns**: See [jql-reporting-reference.md](references/jql-reporting-reference.md) for operators, functions, and standard reporting templates.
- **Examples**: Extensive query patterns are documented in [jql-examples.md](references/jql-examples.md).

### 4. Dashboards & Automation

1. Add gadgets (Filter Results, Burndown, Velocity, Pie Charts) to shared dashboards.
2. Define triggers (Issue Created/Field Changed) and actions for automation rules.

- **Automation Patterns**: See [automation-examples.md](references/automation-examples.md).

---

## Stakeholder & Handoff Protocols

### Decision Framework

- **Escalate to Admin**: For license/billing, org-wide security, or new project permission schemes.
- **Collaborate with Scrum Master**: For board filtering, backlog views, and burndown configuration.
- **Collaborate with Senior PM**: For portfolio-level reporting and cross-project dependencies.

### Best Practices

- **Data Quality**: Enforce required fields and use consistent naming conventions.
- **Performance**: Optimize JQL and limit dashboard gadget counts to ensure fast response.
- **Governance**: Document workflow rationale and audit permissions regularly.

---

## Atlassian MCP Integration

**Actions**: Create/configure projects, execute JQL extraction, update fields, and manage boards/filters programmatically.
**Synergy**: Pull metrics for Senior PM, board configuration for Scrum Master, and support documentation for Confluence Expert.
