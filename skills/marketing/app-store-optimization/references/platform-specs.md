# App Store Platform Specifications

## Apple App Store

- **Title**: 30 characters maximum.
- **Subtitle**: 30 characters maximum.
- **Promotional Text**: 170 characters (editable without app update).
- **Description**: 4,000 characters maximum.
- **Keyword Field**: 100 characters (comma-separated, no spaces between items).
- **What's New**: 4,000 characters.

## Google Play Store

- **Title**: 50 characters maximum.
- **Short Description**: 80 characters maximum.
- **Full Description**: 4,000 characters maximum.
- **Keyword Logic**: No separate field; keywords must be naturally integrated into the title and description for indexing.

## Character Count Validation

Always validate against these limits before proposing metadata changes. Use `scripts/metadata_optimizer.py` to automate validation.
