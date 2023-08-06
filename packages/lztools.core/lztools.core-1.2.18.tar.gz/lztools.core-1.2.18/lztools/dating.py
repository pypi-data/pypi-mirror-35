from datetime import timedelta

def hours_minutes_seconds(time:timedelta):
    return time.seconds // 3600, (time.seconds // 60) % 60, time.seconds % 60