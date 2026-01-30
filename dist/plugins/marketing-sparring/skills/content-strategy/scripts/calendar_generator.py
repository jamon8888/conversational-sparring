import sys
import csv
import calendar
from datetime import datetime

def generate_calendar(year, month, output_file):
    """
    Generates a CSV content calendar for the specified month and year.
    """
    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]
    
    headers = ["Date", "Day", "Content Pillar", "Topic/Title", "Format", "Status", "Owner"]
    
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        
        for week in cal:
            for day in week:
                if day == 0:
                    continue
                
                date_obj = datetime(year, month, day)
                day_name = date_obj.strftime("%A")
                date_str = date_obj.strftime("%Y-%m-%d")
                
                # Simple logic: Weekdays only? Or all days? Let's do all days.
                writer.writerow([date_str, day_name, "", "", "", "Planned", ""])
                
    print(f"✅ Content calendar for {month_name} {year} generated: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python calendar_generator.py [Year] [Month]")
        print("Example: python calendar_generator.py 2025 11")
        sys.exit(1)
        
    try:
        year = int(sys.argv[1])
        month = int(sys.argv[2])
        output = f"content_calendar_{year}_{month}.csv"
        generate_calendar(year, month, output)
    except ValueError:
        print("Error: Year and Month must be integers.")
