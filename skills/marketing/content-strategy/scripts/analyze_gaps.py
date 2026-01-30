#!/usr/bin/env python3
"""Gap analysis comparing our topics vs competitor topics.
Inputs: our_topics.csv [topic, posts] and comp_topics.csv [competitor, topic, posts]
Output: gaps.csv listing topics competitors cover that we do not (ranked by competitor coverage).
"""
import pandas as pd
import sys

if __name__ == '__main__':
    ours = pd.read_csv(sys.argv[1])
    comps = pd.read_csv(sys.argv[2])
    our_set = set(ours['topic'].str.lower())
    comp_counts = (comps.groupby('topic')['posts'].sum()
                        .sort_values(ascending=False).reset_index())
    comp_counts['covered_by_us'] = comp_counts['topic'].str.lower().isin(our_set)
    gaps = comp_counts[~comp_counts['covered_by_us']]
    gaps.to_csv('gaps.csv', index=False)
    print('Saved gaps.csv')
