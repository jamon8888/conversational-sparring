import sys
import json
from datetime import datetime, timedelta

def calculate_attribution(touchpoints, revenue, model='linear'):
    """
    Calculate marketing attribution based on different models.
    
    Args:
        touchpoints: List of dicts with 'channel', 'date', 'cost'
        revenue: Total revenue from the deal
        model: Attribution model ('linear', 'first_touch', 'last_touch', 'time_decay', 'u_shaped')
    
    Returns:
        dict: Attribution results by channel
    """
    if not touchpoints:
        return {}
    
    attribution = {}
    
    if model == 'linear':
        # Equal credit to all touchpoints
        credit_per_touch = revenue / len(touchpoints)
        for tp in touchpoints:
            channel = tp['channel']
            attribution[channel] = attribution.get(channel, 0) + credit_per_touch
    
    elif model == 'first_touch':
        # 100% credit to first touchpoint
        first_channel = touchpoints[0]['channel']
        attribution[first_channel] = revenue
    
    elif model == 'last_touch':
        # 100% credit to last touchpoint
        last_channel = touchpoints[-1]['channel']
        attribution[last_channel] = revenue
    
    elif model == 'time_decay':
        # More credit to recent touchpoints
        total_weight = sum(2 ** i for i in range(len(touchpoints)))
        for i, tp in enumerate(touchpoints):
            weight = 2 ** i
            credit = (weight / total_weight) * revenue
            channel = tp['channel']
            attribution[channel] = attribution.get(channel, 0) + credit
    
    elif model == 'u_shaped':
        # 40% first, 40% last, 20% distributed to middle
        if len(touchpoints) == 1:
            attribution[touchpoints[0]['channel']] = revenue
        elif len(touchpoints) == 2:
            attribution[touchpoints[0]['channel']] = revenue * 0.5
            attribution[touchpoints[-1]['channel']] = revenue * 0.5
        else:
            # First touch: 40%
            attribution[touchpoints[0]['channel']] = revenue * 0.4
            # Last touch: 40%
            last_channel = touchpoints[-1]['channel']
            attribution[last_channel] = attribution.get(last_channel, 0) + revenue * 0.4
            # Middle touches: 20% distributed
            middle_credit = (revenue * 0.2) / (len(touchpoints) - 2)
            for tp in touchpoints[1:-1]:
                channel = tp['channel']
                attribution[channel] = attribution.get(channel, 0) + middle_credit
    
    # Calculate ROI for each channel
    results = {}
    for channel, attributed_revenue in attribution.items():
        channel_cost = sum(tp['cost'] for tp in touchpoints if tp['channel'] == channel)
        roi = ((attributed_revenue - channel_cost) / channel_cost * 100) if channel_cost > 0 else 0
        results[channel] = {
            'attributed_revenue': attributed_revenue,
            'cost': channel_cost,
            'roi': roi
        }
    
    return results

if __name__ == "__main__":
    # Example usage
    touchpoints = [
        {'channel': 'Google Ads', 'date': '2024-01-01', 'cost': 500},
        {'channel': 'LinkedIn', 'date': '2024-01-05', 'cost': 300},
        {'channel': 'Email', 'date': '2024-01-10', 'cost': 50},
        {'channel': 'Demo', 'date': '2024-01-15', 'cost': 0}
    ]
    
    revenue = 10000
    model = sys.argv[1] if len(sys.argv) > 1 else 'linear'
    
    results = calculate_attribution(touchpoints, revenue, model)
    
    print(f"--- Attribution Analysis ({model.upper()} model) ---")
    print(f"Total Revenue: ${revenue:,.2f}\n")
    
    for channel, data in sorted(results.items(), key=lambda x: x[1]['attributed_revenue'], reverse=True):
        print(f"{channel}:")
        print(f"  Attributed Revenue: ${data['attributed_revenue']:,.2f}")
        print(f"  Cost: ${data['cost']:,.2f}")
        print(f"  ROI: {data['roi']:.1f}%")
        print()
