# PowerPoint Template Workflows

## Workflow 1: Creating from Template

When using an existing template, follow this systematic process to preserve design integrity.

### 1. Extract and Analyze

- **Extract Text**: `python -m markitdown template.pptx > template-content.md`
- **Create Thumbnails**: `python scripts/thumbnail.py template.pptx`
- **Inventory Analysis**: Identify layouts (Title, Content, Quote, etc.) and save to `template-inventory.md`.

### 2. Map Content to Layouts

- Match layout structure to content pieces.
- Verify each placeholder will be filled.
- Create `outline.md` with mapping (e.g., `template_mapping = [0, 34, 34, 50, 54]`).

### 3. Rearrange and Prepare

- **Duplicate/Reorder**: `python scripts/rearrange.py template.pptx working.pptx 0,34,34,50,52`
- **Extract Inventory**: `python scripts/inventory.py working.pptx text-inventory.json`

## Workflow 2: Content Replacement

### Replacement Procedure

1. **Analyze Inventory**: Study `text-inventory.json` for shape names, placeholder types, and original formatting.
2. **Generate Replacements**: Create `replacement-text.json`.
   - **CRITICAL**: Use "paragraphs" field with formatting properties (bold, bullet, etc.).
   - **AUTOMATIC CLEARING**: Shapes not in JSON will be cleared.
3. **Apply**: `python scripts/replace.py working.pptx replacement-text.json output.pptx`

### JSON Formatting Standards

```json
"paragraphs": [
  {
    "text": "Header Text",
    "bold": true,
    "alignment": "CENTER"
  },
  {
    "text": "Bullet Point",
    "bullet": true,
    "level": 0
  }
]
```

## Tools Reference

### Thumbnail Creation

`python scripts/thumbnail.py template.pptx [output_prefix] --cols 4`

### Visual Analysis (Image Conversion)

1. **PDF**: `soffice --headless --convert-to pdf template.pptx`
2. **JPEG**: `pdftoppm -jpeg -r 150 template.pdf slide`
