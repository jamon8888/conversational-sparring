---
name: pptx
description: Use when creating, editing, or analyzing PowerPoint (.pptx) presentations, including layout manipulation, text extraction, and design customization.
license: Proprietary
---

# PPTX Presentation Management

## Overview

Presentation creation, editing, and analysis using OOXML manipulation, HTML rendering, and template-based workflows.

## Reading and Analyzing

### Text Extraction

Convert documents to markdown for rapid reading:

```bash
python -m markitdown path-to-file.pptx
```

### Raw XML Access

Required for comments, speaker notes, and complex layouts.

- **Unpack**: `python ooxml/scripts/unpack.py <office_file> <output_dir>`
- **Key Files**: `ppt/presentation.xml`, `ppt/slides/`, `ppt/theme/`.

---

## Creating New Presentations (from Scratch)

Use the **html2pptx** workflow to convert HTML/CSS slides to PowerPoint.

### 1. Design Strategy

**CRITICAL**: Analyze subject matter and branding before coding.

- **Visual Design**: See [visual-design.md](references/visual-design.md) for color palettes, typography, and layout innovation patterns.

### 2. Workflow

1. **READ**: [`html2pptx.md`](html2pptx.md) completely before starting.
2. **HTML Generation**: Create distinct HTML files for each slide (720pt × 405pt).
3. **Conversion**: Run [`html2pptx.js`](scripts/html2pptx.js) to generate the .pptx.
4. **Validation**: Generate thumbnails and check for text overlap/cutoff.

---

## Template-Based Creation

Duplicate and re-arrange existing template slides to preserve brand integrity.

### Workflow

1. **Inventory**: Create a visual inventory to identify layout patterns.
2. **Selection**: Match content to appropriate template layout counts.
3. **Execution**: Detailed procedures for re-ordering and content replacement are in [template-workflows.md](references/template-workflows.md).

---

## Editing Existing Presentations

Work directly with the Office Open XML (OOXML) structure.

### Workflow

1. **READ**: [`ooxml.md`](ooxml.md) (~500 lines) for structural guidance.
2. **Edit**: Unpack → Edit XML → Validate → Pack.
3. **Validation**: Always run `python ooxml/scripts/validate.py` after edits.

---

## Visual Verification

Generate thumbnail grids to spot layout issues:

```bash
python scripts/thumbnail.py output.pptx [prefix]
```

Check for: **Text cutoff**, **Overlap**, and **Positioning** issues.
