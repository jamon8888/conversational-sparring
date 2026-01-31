#!/usr/bin/env python3
"""Aggregate competitor content performance.
Input: comp_perf.csv [competitor, url, topic, views, shares, backlinks]
Output: comp_benchmarks.csv with per-competitor/per-topic aggregates.
"""
import pandas as pd
import sys

if __name__ == '__main__':
    inp = sys.argv[1]
    out = sys.argv[2] if len(sys.argv)>2 else 'comp_benchmarks.csv'
    df = pd.read_csv(inp)
    agg = df.groupby(['competitor','topic']).agg({'views':'sum','shares':'sum','backlinks':'sum','url':'count'}).rename(columns={'url':'posts'}).reset_index()
    agg.to_csv(out, index=False)
    print(f'Saved {out}')
