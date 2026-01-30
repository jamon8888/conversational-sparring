# Multi-Campaign Coordination

Adds portfolio-level orchestration:
- Portfolio dashboard (active campaigns, phases, owners, status)
- Resource allocation and load across campaigns
- Schedule conflict detection (by channel/team)
- Cross-campaign analytics

Use the templates and scripts in assets/ and scripts/.

## How to Run (Cookbook)

1) Prepare portfolio
- Edit assets/templates/portfolio-dashboard.csv (campaigns, dates, channels, hours)

2) Detect conflicts
```
python scripts/conflict_detection.py assets/templates/portfolio-dashboard.csv
```
Outputs:
- assets/templates/conflicts_owner.csv (owners > 32h/week)
- assets/templates/conflicts_channel.csv (channels with > 2 overlapping campaigns)

3) Review & rebalance
- Reduce hours for over-allocated owners
- Stagger channels with collisions

