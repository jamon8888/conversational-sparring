#!/usr/bin/env python3
"""Topic opportunity discovery using simple frequency & performance weighting.
Input CSV: [topic, views, clicks, posts]
Output CSV: topic_opportunities.csv with opportunity_score.
"""
import pandas as pd
import sys

if __name__ == '__main__':
    inp = sys.argv[1]
    out = sys.argv[2] if len(sys.argv)>2 else 'topic_opportunities.csv'
    df = pd.read_csv(inp)
    for c in ['views','clicks','posts']:
        if c not in df: df[c]=0
    # normalize
    for c in ['views','clicks']:
        m = df[c].max() or 1
        df[c] = df[c]/m
    df['opportunity_score'] = (0.6*df['clicks'] + 0.4*df['views']) / (df['posts'].replace(0,1))
    df = df.sort_values('opportunity_score', ascending=False)
    df.to_csv(out, index=False)
    print(f'Saved {out}')
