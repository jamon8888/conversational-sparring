#!/usr/bin/env python3
"""Detect schedule/resource conflicts across multiple campaigns.
Input: portfolio-dashboard.csv
Outputs: conflicts.csv with detected conflicts by week/channel/owner.
"""
import pandas as pd
import sys

if __name__ == '__main__':
    inp = sys.argv[1] if len(sys.argv)>1 else 'portfolio-dashboard.csv'
    out = sys.argv[2] if len(sys.argv)>2 else 'conflicts.csv'
    df = pd.read_csv(inp, parse_dates=['start_date','end_date'])
    # explode per week
    rows = []
    for _,r in df.iterrows():
        rng = pd.date_range(r['start_date'], r['end_date'], freq='W-MON')
        channels = [c.strip() for c in str(r['channels']).split(';')]
        for d in rng:
            for ch in channels:
                rows.append({'week': d, 'owner': r['owner'], 'channel': ch, 'hours': r['weekly_hours'], 'campaign': r['campaign_name']})
    wk = pd.DataFrame(rows)
    # detect over-allocation (>32 hours/week per owner) and per-channel collisions
    owner_over = (wk.groupby(['week','owner'])['hours'].sum().reset_index())
    owner_over = owner_over[owner_over['hours']>32]
    chan_coll = (wk.groupby(['week','channel']).size().reset_index(name='count'))
    chan_coll = chan_coll[chan_coll['count']>2]
    # write combined
    owner_over['type'] = 'owner_overalloc'
    chan_coll['type'] = 'channel_collision'
    owner_over.to_csv('conflicts_owner.csv', index=False)
    chan_coll.to_csv('conflicts_channel.csv', index=False)
    print('Saved conflicts_owner.csv and conflicts_channel.csv')
