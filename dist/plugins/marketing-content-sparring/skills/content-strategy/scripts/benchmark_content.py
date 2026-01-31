#!/usr/bin/env python3
"""Benchmark our content against competitor benchmarks.
Inputs: our_perf.csv [url, topic, views, shares, backlinks] and comp_benchmarks.csv
Output: benchmark_report.csv with relative % vs competitors.
"""
import pandas as pd
import sys

if __name__ == '__main__':
    ours = pd.read_csv(sys.argv[1])
    comps = pd.read_csv(sys.argv[2])
    # average per topic competitor metrics
    comp_avg = comps.groupby('topic').agg({'views':'mean','shares':'mean','backlinks':'mean'}).reset_index()
    merged = ours.merge(comp_avg, on='topic', suffixes=('', '_comp'))
    for m in ['views','shares','backlinks']:
        merged[f'{m}_vs_comp_%'] = ((merged[m] - merged[f'{m}_comp'])/(merged[f'{m}_comp'].replace(0,1))*100).round(1)
    merged.to_csv('benchmark_report.csv', index=False)
    print('Saved benchmark_report.csv')
