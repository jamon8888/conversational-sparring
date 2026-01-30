import sys
from datetime import datetime, timedelta

def generate_cadence(num_touches=7, duration_days=21):
    """
    Generate a multi-touch cadence schedule.
    
    Args:
        num_touches: Number of touchpoints (default 7)
        duration_days: Total duration in days (default 21)
    
    Returns:
        list: Cadence schedule with days and channels
    """
    # Standard cadence patterns
    if num_touches == 7:
        schedule = [
            {"day": 0, "channel": "Email", "type": "Initial outreach"},
            {"day": 2, "channel": "LinkedIn", "type": "Connection request"},
            {"day": 4, "channel": "Email", "type": "Value-add follow-up"},
            {"day": 7, "channel": "Phone", "type": "Call attempt"},
            {"day": 10, "channel": "Email", "type": "Different angle"},
            {"day": 14, "channel": "LinkedIn", "type": "Engage with content"},
            {"day": 21, "channel": "Email", "type": "Breakup email"}
        ]
    elif num_touches == 14:
        schedule = [
            {"day": 0, "channel": "Email", "type": "Initial outreach"},
            {"day": 1, "channel": "LinkedIn", "type": "View profile"},
            {"day": 2, "channel": "LinkedIn", "type": "Connection request"},
            {"day": 3, "channel": "Email", "type": "Follow-up"},
            {"day": 5, "channel": "Phone", "type": "Call attempt"},
            {"day": 6, "channel": "Email", "type": "Value-add"},
            {"day": 8, "channel": "LinkedIn", "type": "Comment on post"},
            {"day": 10, "channel": "Email", "type": "Case study"},
            {"day": 12, "channel": "Phone", "type": "Call attempt"},
            {"day": 14, "channel": "Email", "type": "Different angle"},
            {"day": 17, "channel": "LinkedIn", "type": "Share content"},
            {"day": 19, "channel": "Email", "type": "Last value-add"},
            {"day": 21, "channel": "Phone", "type": "Final call"},
            {"day": 28, "channel": "Email", "type": "Breakup email"}
        ]
    else:
        # Simple distribution
        schedule = []
        interval = duration_days // (num_touches - 1)
        for i in range(num_touches):
            day = i * interval
            channel = ["Email", "LinkedIn", "Phone"][i % 3]
            schedule.append({"day": day, "channel": channel, "type": f"Touch {i+1}"})
    
    return schedule

if __name__ == "__main__":
    touches = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    duration = int(sys.argv[2]) if len(sys.argv) > 2 else 21
    
    cadence = generate_cadence(touches, duration)
    
    print(f"--- {touches}-Touch Cadence over {duration} Days ---\n")
    
    start_date = datetime.now()
    for touch in cadence:
        date = start_date + timedelta(days=touch['day'])
        print(f"Day {touch['day']:2d} ({date.strftime('%a %b %d')}): {touch['channel']:10s} - {touch['type']}")
