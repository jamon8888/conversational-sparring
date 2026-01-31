#!/usr/bin/env python3
"""Simple predictive scoring for future post performance.
Inputs: CSV with columns [title, channel, words, past_views, past_clicks, past_shares, weekday, hour]
Output: Adds predicted_score [0-100].
"""
import pandas as pd
import sys

WEIGHTS = {
    'past_views': 0.35,
    'past_clicks': 0.35,
    'past_shares': 0.2,
    'timing': 0.1,
}

BEST_HOURS = { # simplistic prior per channel
    'linkedin': [9,10,11,13,17],
    'twitter': [9,12,15,18,21],
    'email': [9,10,11],
    'blog': [10,11,14],
}

BEST_WEEKDAYS = {'Mon','Tue','Wed','Thu'}

def timing_score(row):
    ch = str(row.get('channel','')).lower()
    hour = int(row.get('hour', 12))
    wd = str(row.get('weekday','Mon'))[:3]
    s = 0
    if ch in BEST_HOURS and hour in BEST_HOURS[ch]:
        s += 0.6
    if wd in BEST_WEEKDAYS:
        s += 0.4
    return s

if __name__ == '__main__':
    inp = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else 'predicted_scores.csv'
    df = pd.read_csv(inp)
    ts = df.apply(timing_score, axis=1)
    # normalize metrics
    for c in ['past_views','past_clicks','past_shares']:
        if c not in df: df[c]=0
        m = df[c].max() or 1
        df[c] = df[c]/m
    score = (df['past_views']*WEIGHTS['past_views']+
             df['past_clicks']*WEIGHTS['past_clicks']+
             df['past_shares']*WEIGHTS['past_shares']+
             ts*WEIGHTS['timing'])
    df['predicted_score'] = (score*100).round(1)
    df.to_csv(out, index=False)
    print(f'Saved {out}')
