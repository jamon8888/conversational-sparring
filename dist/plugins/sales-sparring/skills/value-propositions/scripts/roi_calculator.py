import sys

def calculate_roi(current_cost, current_result, proposed_cost, proposed_result, timeframe_months=12):
    """
    Calculate ROI for a business case/proposal.
    
    Args:
        current_cost: Current annual cost
        current_result: Current annual result/revenue
        proposed_cost: Proposed solution cost
        proposed_result: Projected result with solution
        timeframe_months: Timeframe for ROI calculation
    
    Returns:
        dict: ROI metrics
    """
    # Calculate improvements
    cost_savings = current_cost - proposed_cost
    revenue_increase = proposed_result - current_result
    total_benefit = cost_savings + revenue_increase
    
    # ROI calculation
    roi_percentage = (total_benefit / proposed_cost) * 100 if proposed_cost > 0 else 0
    
    # Payback period (months)
    monthly_benefit = total_benefit / 12
    payback_months = proposed_cost / monthly_benefit if monthly_benefit > 0 else 999
    
    # Annualized values
    annual_benefit = total_benefit
    annual_roi = roi_percentage
    
    return {
        "investment": proposed_cost,
        "annual_benefit": annual_benefit,
        "roi_percentage": roi_percentage,
        "payback_months": payback_months,
        "cost_savings": cost_savings,
        "revenue_increase": revenue_increase,
        "total_benefit": total_benefit
    }

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python roi_calculator.py [current_cost] [current_result] [proposed_cost] [proposed_result]")
        sys.exit(1)
    
    current_cost = float(sys.argv[1])
    current_result = float(sys.argv[2])
    proposed_cost = float(sys.argv[3])
    proposed_result = float(sys.argv[4])
    
    result = calculate_roi(current_cost, current_result, proposed_cost, proposed_result)
    
    print("--- ROI Analysis ---")
    print(f"Investment: ${result['investment']:,.2f}")
    print(f"Annual Benefit: ${result['annual_benefit']:,.2f}")
    print(f"ROI: {result['roi_percentage']:.1f}%")
    print(f"Payback Period: {result['payback_months']:.1f} months")
    print(f"\nBreakdown:")
    print(f"  Cost Savings: ${result['cost_savings']:,.2f}")
    print(f"  Revenue Increase: ${result['revenue_increase']:,.2f}")
