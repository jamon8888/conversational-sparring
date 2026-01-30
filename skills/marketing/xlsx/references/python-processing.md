# Python XLSX Processing Reference

## 1. pandas (Data Analysis)

Best for bulk operations, statistics, and clean data export.

```python
import pandas as pd
df = pd.read_excel('file.xlsx')
# Statistics
print(df.describe())
# Vectorized operations (fast)
df['Total'] = df['A'] + df['B']
df.to_excel('output.xlsx', index=False)
```

## 2. openpyxl (Formatting & Formulas)

Best for preserving structure, adding dynamic formulas, and styling.

### Formula Injection

**CRITICAL**: Use Excel formulas instead of hardcoding Python-calculated values.

```python
# GOOD: Dynamic
sheet['B10'] = '=SUM(B2:B9)'
# BAD: Static
total = df['Sales'].sum()
sheet['B10'] = total # Hardcodes value
```

### Styling

```python
from openpyxl.styles import Font, Alignment
sheet['A1'].font = Font(bold=True)
sheet['A1'].alignment = Alignment(horizontal='center')
```

### Sheet Management

```python
wb = load_workbook('existing.xlsx')
new_sheet = wb.create_sheet('Summary')
wb.save('modified.xlsx')
```
