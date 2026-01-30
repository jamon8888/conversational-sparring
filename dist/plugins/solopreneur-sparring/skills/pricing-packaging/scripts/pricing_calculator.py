import sys

def calculate_pricing_metrics(base_price, cogs, target_margin=0.4):
    """
    Calculate pricing metrics and recommendations.
    
    Args:
        base_price: Current or proposed price
        cogs: Cost of goods sold
        target_margin: Target gross margin (default 40%)
    
    Returns:
        dict: Pricing analysis
    """
    # Calculate current metrics
    gross_profit = base_price - cogs
    gross_margin = (gross_profit / base_price) if base_price > 0 else 0
    markup = (gross_profit / cogs) if cogs > 0 else 0
    
    # Calculate target price for desired margin
    target_price = cogs / (1 - target_margin)
    
    # Calculate price elasticity scenarios
    scenarios = {}
    for change_pct in [-20, -10, 0, 10, 20]:
        new_price = base_price * (1 + change_pct / 100)
        new_profit = new_price - cogs
        new_margin = (new_profit / new_price) if new_price > 0 else 0
        
        # Assume volume changes inversely (simplified elasticity)
        volume_change = -change_pct * 0.8  # 0.8 elasticity coefficient
        
        scenarios[f"{change_pct:+d}%"] = {
            'price': new_price,
            'margin': new_margin * 100,
            'volume_change': volume_change,
            'profit_per_unit': new_profit
        }
    
    return {
        'current': {
            'price': base_price,
            'cogs': cogs,
            'gross_profit': gross_profit,
            'gross_margin': gross_margin * 100,
            'markup': markup * 100
        },
        'target': {
            'price': target_price,
            'margin': target_margin * 100,
            'price_increase_needed': ((target_price - base_price) / base_price * 100) if base_price > 0 else 0
        },
        'scenarios': scenarios
    }

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python pricing_calculator.py [base_price] [cogs] [target_margin]")
        sys.exit(1)
    
    base_price = float(sys.argv[1])
    cogs = float(sys.argv[2])
    target_margin = float(sys.argv[3]) if len(sys.argv) > 3 else 0.4
    
    results = calculate_pricing_metrics(base_price, cogs, target_margin)
    
    print("--- Pricing Analysis ---")
    print(f"\nCurrent Metrics:")
    print(f"  Price: ${results['current']['price']:,.2f}")
    print(f"  COGS: ${results['current']['cogs']:,.2f}")
    print(f"  Gross Profit: ${results['current']['gross_profit']:,.2f}")
    print(f"  Gross Margin: {results['current']['gross_margin']:.1f}%")
    print(f"  Markup: {results['current']['markup']:.1f}%")
    
    print(f"\nTarget ({target_margin*100:.0f}% margin):")
    print(f"  Recommended Price: ${results['target']['price']:,.2f}")
    print(f"  Price Increase Needed: {results['target']['price_increase_needed']:.1f}%")
    
    print(f"\nPrice Elasticity Scenarios:")
    for scenario, data in results['scenarios'].items():
        print(f"  {scenario} price change:")
        print(f"    New Price: ${data['price']:,.2f}")
        print(f"    Margin: {data['margin']:.1f}%")
        print(f"    Est. Volume Change: {data['volume_change']:+.1f}%")
