# Excel Formatting & Financial Modeling Standards

## 1. Color Coding Standards

_Unless overridden by existing templates:_

- **Blue (0,0,255)**: Hardcoded inputs and scenario variables.
- **Black (0,0,0)**: All formulas and calculations.
- **Green (0,128,0)**: Internal links (same workbook).
- **Red (255,0,0)**: External links (different files).
- **Yellow Background (255,255,0)**: Key assumptions or cells needing update.

## 2. Number Formatting Rules

- **Years**: Text format (e.g., `2024`).
- **Currency**: `$#,##0` with units in headers. Zeros as `-`.
- **Percentages**: One decimal (e.g., `15.0%`).
- **Multiples**: `0.0x` (e.g., `8.5x`).
- **Negatives**: Parentheses `(123)`.

## 3. Assumptions & Documentation

- **Assumptions**: Place in separate cells; refer to them by cell reference (`=B5*(1+$B$6)`) never hardcodes.
- **Hardcode Sources**: Must be commented or in adjacent cells.
  - _Format_: "Source: [System], [Date], [Reference], [URL]"
  - _Example_: "Source: Company 10-K, FY2024, Page 45"
