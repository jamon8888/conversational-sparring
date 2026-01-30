---
name: agile-product-owner
description: Use when breaking down epics into user stories, planning sprints, or managing a backlog. Trigger when user stories are "too big", sprint planning feels disorganized, or needing to generate INVEST-compliant acceptance criteria for developer tasks.
license: MIT
---

# Agile Product Owner

Complete toolkit for Product Owners to excel at backlog management and sprint execution.

## Core Capabilities

- INVEST-compliant user story generation
- Automatic acceptance criteria creation
- Sprint capacity planning
- Backlog prioritization
- Velocity tracking and metrics

## Key Scripts

### user_story_generator.py

Generates well-formed user stories with acceptance criteria from epics.

**Usage**:

- Generate stories: `python scripts/user_story_generator.py`
- Plan sprint: `python scripts/user_story_generator.py sprint [capacity]`

**Features**:

- Breaks epics into stories
- INVEST criteria validation
- Automatic point estimation
- Priority assignment
- Sprint planning with capacity
