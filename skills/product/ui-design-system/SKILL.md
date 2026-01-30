---
name: ui-design-system
description: Use when generating design tokens (colors, typography, spacing), documenting reusable UI components, or calculating responsive layouts. Trigger when visual consistency is lacking across products, needing a 4px/8px grid system, or facilitating a design-to-development handoff.
license: MIT
---

# UI Design System

Professional toolkit for creating and maintaining scalable design systems.

## Core Capabilities

- Design token generation (colors, typography, spacing)
- Component system architecture
- Responsive design calculations
- Accessibility compliance
- Developer handoff documentation

## Key Scripts

### design_token_generator.py

Generates complete design system tokens from brand colors.

**Usage**: `python scripts/design_token_generator.py [brand_color] [style] [format]`

- Styles: modern, classic, playful
- Formats: json, css, scss

**Features**:

- Complete color palette generation
- Modular typography scale
- 8pt spacing grid system
- Shadow and animation tokens
- Responsive breakpoints
- Multiple export formats
