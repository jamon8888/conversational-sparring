#!/usr/bin/env python3
"""Detect simple trends by content_type and channel over time.
Input CSV: [date, content_type, channel, views, clicks, shares]
Outputs: trend_summary.csv with MoM deltas.
"""
import pandas as pd
import sys

if __name__ == '__main__':
    inp = sys.argv[1]
    out = sys.argv[2] if len(sys.argv)>2 else 'trend_summary.csv'
    df = pd.read_csv(inp, parse_dates=['date'])
    df['ym'] = df['date'].dt.to_period('M')
    agg = df.groupby(['ym','content_type','channel']).agg({'views':'sum','clicks':'sum','shares':'sum'}).reset_index()
    agg = agg.sort_values('ym')
    # compute month-over-month deltas per group
    agg['views_mom'] = agg.groupby(['content_type','channel'])['views'].pct_change().round(3)
    agg['clicks_mom'] = agg.groupby(['content_type','channel'])['clicks'].pct_change().round(3)
    agg['shares_mom'] = agg.groupby(['content_type','channel'])['shares'].pct_change().round(3)
    agg.to_csv(out, index=False)
    print(f'Saved {out}')
