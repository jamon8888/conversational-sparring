#!/usr/bin/env python3
"""Recommend strategy actions from gaps + benchmarks.
Inputs: gaps.csv, benchmark_report.csv
Output: strategy_recommendations.md
"""
import pandas as pd
import os

if __name__ == '__main__':
    gaps = pd.read_csv('gaps.csv') if os.path.exists('gaps.csv') else None
    bench = pd.read_csv('benchmark_report.csv') if os.path.exists('benchmark_report.csv') else None
    lines = ['# Strategy Recommendations','']
    if gaps is not None and not gaps.empty:
        top = gaps.head(10)
        lines += ['## Gap Topics to Cover Next','']
        for _,r in top.iterrows():
            lines.append(f"- {r['topic']} (competitor posts: {int(r['posts'])})")
        lines.append('')
    if bench is not None and not bench.empty:
        lines += ['## Underperforming Topics (Improve)','']
        bad = bench.sort_values('views_vs_comp_%').head(10)
        for _,r in bad.iterrows():
            lines.append(f"- {r['topic']}: views {r['views_vs_comp_%']}% vs competitors")
        lines.append('')
    if len(lines)==2:
        lines.append('No data available yet. Run analysis scripts first.')
    open('strategy_recommendations.md','w',encoding='utf-8').write('\n'.join(lines))
    print('Saved strategy_recommendations.md')
