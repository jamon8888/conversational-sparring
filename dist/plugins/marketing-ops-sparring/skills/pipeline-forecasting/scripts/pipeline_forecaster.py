import sys
import json
from datetime import datetime, timedelta

def forecast_pipeline(deals, method='weighted'):
    """
    Forecast revenue from pipeline using different methods.
    
    Args:
        deals: List of dicts with 'value', 'stage', 'close_date', 'probability'
        method: Forecasting method ('weighted', 'best_case', 'worst_case', 'commit')
    
    Returns:
        dict: Forecast results by time period
    """
    forecast = {
        'this_month': 0,
        'next_month': 0,
        'this_quarter': 0,
        'next_quarter': 0,
        'total_pipeline': 0
    }
    
    now = datetime.now()
    current_month_end = datetime(now.year, now.month + 1 if now.month < 12 else 1, 1) - timedelta(days=1)
    next_month_end = datetime(now.year, now.month + 2 if now.month < 11 else 1, 1) - timedelta(days=1)
    
    # Determine current quarter
    current_quarter = (now.month - 1) // 3 + 1
    quarter_start_month = (current_quarter - 1) * 3 + 1
    quarter_end_month = quarter_start_month + 2
    current_quarter_end = datetime(now.year, quarter_end_month + 1 if quarter_end_month < 12 else 1, 1) - timedelta(days=1)
    
    # Stage probability mapping (if not provided)
    default_probabilities = {
        'Prospecting': 0.1,
        'Qualification': 0.2,
        'Needs Analysis': 0.3,
        'Proposal': 0.5,
        'Negotiation': 0.7,
        'Closed Won': 1.0,
        'Closed Lost': 0.0
    }
    
    for deal in deals:
        value = deal.get('value', 0)
        stage = deal.get('stage', 'Unknown')
        probability = deal.get('probability', default_probabilities.get(stage, 0.5))
        close_date_str = deal.get('close_date', '')
        
        try:
            close_date = datetime.strptime(close_date_str, '%Y-%m-%d')
        except:
            continue
        
        # Calculate weighted value based on method
        if method == 'weighted':
            weighted_value = value * probability
        elif method == 'best_case':
            weighted_value = value if probability >= 0.5 else 0
        elif method == 'worst_case':
            weighted_value = value if probability >= 0.9 else 0
        elif method == 'commit':
            weighted_value = value if probability >= 0.7 else 0
        else:
            weighted_value = value * probability
        
        # Add to total pipeline
        forecast['total_pipeline'] += value
        
        # Categorize by time period
        if close_date <= current_month_end:
            forecast['this_month'] += weighted_value
        elif close_date <= next_month_end:
            forecast['next_month'] += weighted_value
        
        if close_date <= current_quarter_end:
            forecast['this_quarter'] += weighted_value
        else:
            forecast['next_quarter'] += weighted_value
    
    return forecast

if __name__ == "__main__":
    # Example usage
    sample_deals = [
        {'value': 50000, 'stage': 'Proposal', 'close_date': '2024-11-30', 'probability': 0.5},
        {'value': 100000, 'stage': 'Negotiation', 'close_date': '2024-12-15', 'probability': 0.7},
        {'value': 75000, 'stage': 'Qualification', 'close_date': '2024-12-31', 'probability': 0.2},
        {'value': 200000, 'stage': 'Proposal', 'close_date': '2025-01-15', 'probability': 0.5},
    ]
    
    method = sys.argv[1] if len(sys.argv) > 1 else 'weighted'
    
    results = forecast_pipeline(sample_deals, method)
    
    print(f"--- Pipeline Forecast ({method.upper()}) ---")
    print(f"Total Pipeline Value: ${results['total_pipeline']:,.2f}\n")
    print(f"This Month Forecast: ${results['this_month']:,.2f}")
    print(f"Next Month Forecast: ${results['next_month']:,.2f}")
    print(f"This Quarter Forecast: ${results['this_quarter']:,.2f}")
    print(f"Next Quarter Forecast: ${results['next_quarter']:,.2f}")
