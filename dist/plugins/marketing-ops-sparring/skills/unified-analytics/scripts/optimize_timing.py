#!/usr/bin/env python3
"""Recommend optimal posting windows by channel based on historical engagement.
Input CSV: [channel, weekday, hour, posts, clicks]
Output CSV: timing_recommendations.csv with top windows.
"""
import pandas as pd
import sys

if __name__ == '__main__':
    inp = sys.argv[1]
    out = sys.argv[2] if len(sys.argv)>2 else 'timing_recommendations.csv'
    df = pd.read_csv(inp)
    df['ctr'] = (df['clicks']/(df['posts'].replace(0,1))).round(4)
    rec = (df.groupby(['channel','weekday','hour'])['ctr']
             .mean().reset_index()
             .sort_values(['channel','ctr'], ascending=[True,False]))
    top = rec.groupby('channel').head(10)
    top.to_csv(out, index=False)
    print(f'Saved {out}')
