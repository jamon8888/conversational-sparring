import sys

def calculate_revenue_metrics(mrr, churn_rate, new_customers, avg_deal_size):
    """
    Calculate key revenue metrics and growth indicators.
    
    Args:
        mrr: Monthly Recurring Revenue
        churn_rate: Monthly churn rate (as decimal, e.g., 0.05 for 5%)
        new_customers: New customers added this month
        avg_deal_size: Average deal size
    
    Returns:
        dict: Revenue metrics and projections
    """
    # Calculate ARR
    arr = mrr * 12
    
    # Calculate Net Revenue Retention (NRR)
    # Simplified: assumes expansion revenue offsets some churn
    expansion_rate = 0.02  # Assume 2% expansion
    nrr = (1 - churn_rate + expansion_rate) * 100
    
    # Calculate Customer Lifetime Value (LTV)
    # LTV = ARPU / Churn Rate
    ltv = avg_deal_size / churn_rate if churn_rate > 0 else avg_deal_size * 36
    
    # Calculate growth metrics
    new_mrr = new_customers * avg_deal_size
    churned_mrr = mrr * churn_rate
    net_new_mrr = new_mrr - churned_mrr
    growth_rate = (net_new_mrr / mrr * 100) if mrr > 0 else 0
    
    # Project next 12 months
    projections = []
    current_mrr = mrr
    for month in range(1, 13):
        current_mrr = current_mrr * (1 + growth_rate / 100)
        projections.append({
            'month': month,
            'mrr': current_mrr,
            'arr': current_mrr * 12
        })
    
    return {
        'current': {
            'mrr': mrr,
            'arr': arr,
            'churn_rate': churn_rate * 100,
            'nrr': nrr,
            'ltv': ltv,
            'new_mrr': new_mrr,
            'churned_mrr': churned_mrr,
            'net_new_mrr': net_new_mrr,
            'growth_rate': growth_rate
        },
        'projections': projections
    }

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python revenue_metrics.py [mrr] [churn_rate] [new_customers] [avg_deal_size]")
        sys.exit(1)
    
    mrr = float(sys.argv[1])
    churn_rate = float(sys.argv[2])
    new_customers = int(sys.argv[3])
    avg_deal_size = float(sys.argv[4])
    
    results = calculate_revenue_metrics(mrr, churn_rate, new_customers, avg_deal_size)
    
    print("--- Revenue Metrics Analysis ---")
    print(f"\nCurrent Metrics:")
    print(f"  MRR: ${results['current']['mrr']:,.2f}")
    print(f"  ARR: ${results['current']['arr']:,.2f}")
    print(f"  Churn Rate: {results['current']['churn_rate']:.1f}%")
    print(f"  Net Revenue Retention: {results['current']['nrr']:.1f}%")
    print(f"  Customer LTV: ${results['current']['ltv']:,.2f}")
    
    print(f"\nGrowth Metrics:")
    print(f"  New MRR: ${results['current']['new_mrr']:,.2f}")
    print(f"  Churned MRR: ${results['current']['churned_mrr']:,.2f}")
    print(f"  Net New MRR: ${results['current']['net_new_mrr']:,.2f}")
    print(f"  Monthly Growth Rate: {results['current']['growth_rate']:.1f}%")
    
    print(f"\n12-Month Projection:")
    for proj in results['projections'][::3]:  # Show every 3 months
        print(f"  Month {proj['month']}: MRR ${proj['mrr']:,.2f} | ARR ${proj['arr']:,.2f}")
