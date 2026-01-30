import sys

def calculate_metrics(spend, revenue, customers):
    """
    Calculates key marketing metrics.
    """
    spend = float(spend)
    revenue = float(revenue)
    customers = int(customers)
    
    roi = ((revenue - spend) / spend) * 100 if spend > 0 else 0
    cac = spend / customers if customers > 0 else 0
    # Simple LTV assumption (revenue per customer) - usually LTV is over time
    ltv = revenue / customers if customers > 0 else 0
    
    return {
        "ROI": roi,
        "CAC": cac,
        "LTV": ltv,
        "LTV:CAC": ltv / cac if cac > 0 else 0
    }

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python roi_calculator.py [Spend] [Revenue] [Customers]")
        sys.exit(1)
        
    spend = sys.argv[1]
    revenue = sys.argv[2]
    customers = sys.argv[3]
    
    metrics = calculate_metrics(spend, revenue, customers)
    
    print("--- Marketing Metrics ---")
    print(f"Spend: ${float(spend):,.2f}")
    print(f"Revenue: ${float(revenue):,.2f}")
    print(f"Customers: {customers}")
    print("-" * 20)
    print(f"ROI: {metrics['ROI']:.2f}%")
    print(f"CAC: ${metrics['CAC']:.2f}")
    print(f"Avg Value (LTV proxy): ${metrics['LTV']:.2f}")
    print(f"LTV:CAC Ratio: {metrics['LTV:CAC']:.2f}")
