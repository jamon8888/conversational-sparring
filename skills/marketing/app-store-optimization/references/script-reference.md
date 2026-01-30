# ASO Script Reference

## 1. keyword_analyzer.py

Analyze keyword volume, competition, and relevance.

- **Functions**: `analyze_keyword()`, `find_long_tail()`, `calculate_difficulty()`.
- **Usage**: `python scripts/keyword_analyzer.py --keywords "task manager,todo"`

## 2. metadata_optimizer.py

Validate and optimize metadata against platform limits.

- **Functions**: `optimize_title()`, `validate_character_limits()`.
- **Usage**: `python scripts/metadata_optimizer.py --platform apple --title "New Title"`

## 3. competitor_analyzer.py

Analyze top competitors' ASO strategies and asset usage.

- **Functions**: `get_top_competitors()`, `identify_gaps()`.

## 4. aso_scorer.py

Calculate overall 0-100 ASO health score.

- **Dimensions**: Metadata quality, Ratings, Keyword rankings, Conversion.

## 5. ab_test_planner.py

Calculate sample sizes and statistical significance for metadata experiments.

## 6. review_analyzer.py

Perform sentiment analysis and extract common themes/issues from reviews.

- **Functions**: `analyze_sentiment()`, `extract_common_themes()`.
