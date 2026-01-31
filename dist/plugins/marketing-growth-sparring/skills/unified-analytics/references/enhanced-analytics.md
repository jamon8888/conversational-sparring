# Enhanced Unified Analytics

This add-on introduces:
- Predictive performance scoring (simple model)
- Trend analysis (content and channel)
- Optimal posting time recommendations
- Topic opportunity discovery

See scripts/ for runnable utilities and assets/templates/ for dashboard templates.

## How to Run (Cookbook)

### 1) Predict Performance
```
python scripts/predict_performance.py assets/templates/sample_content_history.csv assets/templates/predicted_scores.csv
```
Input schema: title,channel,words,past_views,past_clicks,past_shares,weekday,hour
Output: assets/templates/predicted_scores.csv

### 2) Analyze Trends (MoM)
```
python scripts/analyze_trends.py assets/templates/sample_channel_timeseries.csv assets/templates/trend_summary.csv
```
Input schema: date,content_type,channel,views,clicks,shares

### 3) Optimize Timing
```
python scripts/optimize_timing.py assets/templates/sample_timing_dataset.csv assets/templates/timing_recommendations.csv
```
Input schema: channel,weekday,hour,posts,clicks

### 4) Discover Topic Opportunities
```
python scripts/discover_topics.py assets/templates/sample_topics.csv assets/templates/topic_opportunities.csv
```
Input schema: topic,views,clicks,posts

All outputs saved to assets/templates for quick inspection.

