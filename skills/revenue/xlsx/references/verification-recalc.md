# XLSX Formula Verification & Recalculation

## 1. Recalculation (recalc.py)

Openpyxl preserves formulas as strings but doesn't calculate results. **MANDATORY** use of `recalc.py` to evaluate values.

```bash
python recalc.py output.xlsx [timeout_seconds]
```

- **Execution**: Automates LibreOffice headlessly to refresh all sheets.
- **Validation**: Scans for `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`.
- **Handoff**: Success results in JSON status or `errors_found` with cell locations.

## 2. Formula Quality Checklist

- [ ] **Sample Test**: Verify 3 random cell references before broad application.
- [ ] **Row/Col Mapping**: Confirm index offsets (Excel is 1-indexed, DataFrame is 0-indexed).
- [ ] **Error Handling**: Check for nulls/NaNs to prevent formula crashes.
- [ ] **Sheet Links**: Ensure `SheetName!A1` format is correct for links.

## 3. Interpreting Results

- **Success**: Code proceeds to save/deliver.
- **Fail**: Audit the `error_summary` in JSON to pinpoint the invalid reference or syntax.
