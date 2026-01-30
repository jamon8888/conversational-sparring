---
name: xlsx
description: Use when creating or analyzing spreadsheets (xlsx/csv), implementing financial models with dynamic formulas, and ensuring zero formula errors (#REF!,
license: MIT
---

# XLSX processing & Financial Modeling

## Overview

High-precision spreadsheet manipulation, data analysis, and financial model construction using Python and automated verification scripts.

## Core Standards

### 1. Financial Modeling Integrity

- **Logic**: Use Excel formulas for all totals, ratios, and growth rates. Static values calculated in Python are forbidden.
- **Formatting**: Color coding (Blue for inputs, Black for formulas) and standard number formats (Parentheses for negatives, multiples as 0.0x).
- **Reference**: See [formatting-standards.md](references/formatting-standards.md) for full style and documentation rules.

### 2. Software & Automation

Automated editing and recalculation.

- **Tools**: `pandas` for bulk data operations; `openpyxl` for formatting and formula injection.
- **Recalculation**: **MANDATORY** use of `scripts/recalc.py` to evaluate formulas and scan for errors.
- **Code Reference**: See [python-processing.md](references/python-processing.md) and [verification-recalc.md](references/verification-recalc.md).

---

## Operating Guidelines

- **Template Discipline**: Match existing workbook conventions (formats, styles) unless specifically asked for an overhaul.
- **Verification**: Check column mapping (1-indexed in Excel) and handle `NaN` values to prevent formula crashes.
- **Error Types**: Success is defined as zero `#REF!`, `#DIV/0!`, or `#VALUE!` errors in the final output.

## Recommended Tool Selection

| Task                      | Primary Tool                                                  |
| ------------------------- | ------------------------------------------------------------- |
| High-volume data analysis | `pandas`                                                      |
| Preserving cell styles    | `openpyxl`                                                    |
| Formula verification      | `recalc.py` (LibreOffice)                                     |
| Hardcode tracing          | [formatting-standards.md](references/formatting-standards.md) |
