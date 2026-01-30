# Competitive Intelligence Add-on

Adds:
- Competitive content gap analysis
- Competitor keyword tracking
- Performance benchmarking
- Opportunity scoring + recommendations

Run scripts/ with exported competitor data.

## How to Run (Cookbook)

1) Prepare data (samples in assets/templates/)
- our_topics.csv, comp_topics.csv, our_perf.csv, comp_perf.csv

2) Run analysis
```
python scripts/analyze_gaps.py assets/templates/our_topics.csv assets/templates/comp_topics.csv
python scripts/track_competitors.py assets/templates/comp_perf.csv assets/templates/comp_benchmarks.csv
python scripts/benchmark_content.py assets/templates/our_perf.csv assets/templates/comp_benchmarks.csv
python scripts/recommend_strategy.py
```
Outputs (now saved under assets/templates/):
- gaps.csv
- comp_benchmarks.csv
- benchmark_report.csv
- strategy_recommendations.md

3) Act
- Cover top gap topics
- Improve underperforming topics vs. competitors
- Update quarterly content strategy

