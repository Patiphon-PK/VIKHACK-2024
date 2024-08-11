import json
from datetime import datetime
import pytz
from ics import Calendar, Event

def json_to_ics(json_data):
    data = json.loads(json_data)
    calendar = Calendar()
    timezone = pytz.timezone('Australia/Sydney')

    for event_data in data.get('events', []):
        event = Event()
        event.name = event_data.get('name', 'No Title')
        event_time_str = event_data.get('time', '1970-01-01T00:00:00')
        event_time = datetime.fromisoformat(event_time_str)
        event_time = timezone.localize(event_time)
        event.begin = event_time
        event.location = event_data.get('location', 'No Location')
        calendar.events.add(event)
    
    return str(calendar)
