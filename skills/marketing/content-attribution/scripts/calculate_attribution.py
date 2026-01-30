#!/usr/bin/env python3
"""
Content Attribution Calculator

Calculates first-touch, last-touch, and multi-touch attribution for content marketing.

Usage:
    python calculate_attribution.py --input crm-export.csv --model multi-touch --output report.csv
"""

import pandas as pd
import argparse
from datetime import datetime, timedelta
from typing import Dict, List, Tuple

class AttributionCalculator:
    """Calculate content attribution using different models"""
    
    def __init__(self, model='multi-touch', weights=None):
        self.model = model
        self.weights = weights or {'first': 20, 'middle': 30, 'last': 50}
        
    def calculate(self, df: pd.DataFrame) -> pd.DataFrame:
        """Calculate attribution based on model"""
        
        # Group by contact to get journeys
        journeys = df.groupby('contact_id')
        
        attribution_data = []
        
        for contact_id, journey in journeys:
            # Sort by timestamp
            journey = journey.sort_values('timestamp')
            
            # Get conversions (deals)
            conversions = journey[journey['deal_value'] > 0]
            
            if len(conversions) == 0:
                continue
                
            # For each conversion, attribute credit
            for _, conversion in conversions.iterrows():
                # Get touches before this conversion
                touches = journey[journey['timestamp'] <= conversion['timestamp']]
                
                if len(touches) == 0:
                    continue
                    
                deal_value = conversion['deal_value']
                
                # Calculate attribution
                if self.model == 'first-touch':
                    credits = self._first_touch(touches, deal_value)
                elif self.model == 'last-touch':
                    credits = self._last_touch(touches, deal_value)
                else:  # multi-touch
                    credits = self._multi_touch(touches, deal_value)
                
                attribution_data.extend(credits)
        
        # Aggregate by content
        if not attribution_data:
            return pd.DataFrame()
            
        result_df = pd.DataFrame(attribution_data)
        summary = result_df.groupby(['content_id', 'content_title', 'content_type']).agg({
            'revenue': 'sum',
            'deal_count': 'sum'
        }).reset_index()
        
        summary = summary.sort_values('revenue', ascending=False)
        summary['avg_deal_value'] = summary['revenue'] / summary['deal_count']
        
        return summary
    
    def _first_touch(self, touches: pd.DataFrame, deal_value: float) -> List[Dict]:
        """First-touch attribution: 100% to first touch"""
        first_touch = touches.iloc[0]
        return [{
            'content_id': first_touch['content_id'],
            'content_title': first_touch['content_title'],
            'content_type': first_touch['content_type'],
            'revenue': deal_value,
            'deal_count': 1
        }]
    
    def _last_touch(self, touches: pd.DataFrame, deal_value: float) -> List[Dict]:
        """Last-touch attribution: 100% to last touch"""
        last_touch = touches.iloc[-1]
        return [{
            'content_id': last_touch['content_id'],
            'content_title': last_touch['content_title'],
            'content_type': last_touch['content_type'],
            'revenue': deal_value,
            'deal_count': 1
        }]
    
    def _multi_touch(self, touches: pd.DataFrame, deal_value: float) -> List[Dict]:
        """Multi-touch attribution: Weighted across all touches"""
        credits = []
        num_touches = len(touches)
        
        if num_touches == 1:
            # Only one touch gets 100%
            return self._first_touch(touches, deal_value)
        
        first_weight = self.weights['first'] / 100
        last_weight = self.weights['last'] / 100
        middle_weight = self.weights['middle'] / 100
        
        for idx, (_, touch) in enumerate(touches.iterrows()):
            if idx == 0:
                # First touch
                credit = deal_value * first_weight
            elif idx == num_touches - 1:
                # Last touch
                credit = deal_value * last_weight
            else:
                # Middle touches split the middle weight
                num_middle = num_touches - 2
                credit = deal_value * (middle_weight / num_middle)
            
            credits.append({
                'content_id': touch['content_id'],
                'content_title': touch['content_title'],
                'content_type': touch['content_type'],
                'revenue': credit,
                'deal_count': 1
            })
        
        return credits


def main():
    parser = argparse.ArgumentParser(description='Calculate content attribution')
    parser.add_argument('--input', required=True, help='Input CSV file')
    parser.add_argument('--model', choices=['first-touch', 'last-touch', 'multi-touch'], 
                        default='multi-touch', help='Attribution model')
    parser.add_argument('--output', default='attribution-report.csv', help='Output file')
    parser.add_argument('--weights', help='Custom weights (format: 20,30,50)')
    
    args = parser.parse_args()
    
    # Load data
    print(f"Loading data from {args.input}...")
    df = pd.read_csv(args.input)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    print(f"Loaded {len(df)} rows")
    print(f"Unique contacts: {df['contact_id'].nunique()}")
    print(f"Unique content: {df['content_id'].nunique()}")
    
    # Parse weights if provided
    weights = None
    if args.weights:
        first, middle, last = map(int, args.weights.split(','))
        weights = {'first': first, 'middle': middle, 'last': last}
    
    # Calculate attribution
    print(f"\nCalculating {args.model} attribution...")
    calculator = AttributionCalculator(model=args.model, weights=weights)
    result = calculator.calculate(df)
    
    if result.empty:
        print("No conversions found in data")
        return
    
    # Save results
    result.to_csv(args.output, index=False)
    print(f"\nResults saved to {args.output}")
    
    # Print summary
    print(f"\n{'='*60}")
    print("ATTRIBUTION SUMMARY")
    print(f"{'='*60}\n")
    
    total_revenue = result['revenue'].sum()
    total_deals = result['deal_count'].sum()
    
    print(f"Total Revenue Attributed: ${total_revenue:,.2f}")
    print(f"Total Deals: {total_deals:.0f}")
    print(f"Average Deal Value: ${total_revenue/total_deals:,.2f}")
    
    print(f"\nTop 10 Content by Revenue:\n")
    print(result.head(10).to_string(index=False))
    
    print(f"\n{'='*60}")


if __name__ == "__main__":
    main()
