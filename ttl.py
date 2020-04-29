import json
from datetime import datetime, timedelta

def deletion_time(days: int=0, hours: int=0, minutes: int=0):
    delete_at_time = datetime.now() \
        + timedelta(days=days, hours=hours, minutes=minutes)
    minute = delete_at_time.minute
    hour = delete_at_time.hour
    day = delete_at_time.day
    cron_exp = f"cron({minute} {hour} {day} * ? *)"
    return cron_exp

def handler(event, context):
    print('Received event: %s' % json.dumps(event))
    cron_exp = deletion_time(days=2, hours=0, minutes=0)

    fragment = event['fragment']
    transform = {
        'ScheduleExpression': cron_exp
    }
    fragment.update(transform)
    print('Updated fragment: %s' % json.dumps(fragment))
    return {
        'requestId': event['requestId'],
        'status': 'SUCCESS',
        'fragment': fragment,
    } 
