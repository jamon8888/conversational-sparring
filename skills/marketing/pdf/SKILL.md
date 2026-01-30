---
name: pdf
description: Use when you need to extract text/tables, fill forms, or create/merge/split PDFs programmatically using Python (pypdf, pdfplumber) or CLI tools (qpdf).
license: MIT
---

# PDF Processing

## Overview

Programmatic manipulation and data extraction from PDF documents using Python libraries and high-performance CLI tools.

## Core Capabilities

### 1. Python Processing

Automated manipulation of PDF structure and content.

- **Structural**: Merge, split, rotate, and password-protect pages.
- **Extraction**: Extract text with layout preservation and hierarchical table extraction.
- **Reference**: See [python-processing.md](references/python-processing.md) for `pypdf`, `pdfplumber`, and `pytesseract` snippets.

### 2. Creation & Templating

- **Generation**: Create dynamic PDFs from scratch using `reportlab`.
- **Forms**: Populate and flatten interactive PDF forms. See [forms.md](forms.md).

### 3. CLI Tools

Fast, low-overhead operations for bulk processing or containerized environments.

- **Tools**: `qpdf` for structural changes, `poppler-utils` for text/image extraction.
- **Reference**: See [cli-tools.md](references/cli-tools.md).

---

## Strategy & Best Practices

- **OCR**: For scanned documents, convert to high-DPI images before passing to Tesseract.
- **Security**: Always decrypt before structural modification; re-encrypt per policy.
- **Hybrid Approach**: Use CLI tools for structural transformation and Python for deep content analysis.

## Tools Summary

| Action       | Recommended Tool  |
| ------------ | ----------------- |
| Merge/Split  | `pypdf` or `qpdf` |
| Table Data   | `pdfplumber`      |
| Scanned Text | `pytesseract`     |
| New PDF      | `reportlab`       |
