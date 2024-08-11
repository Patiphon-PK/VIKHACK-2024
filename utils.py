import json
from datetime import datetime

def convert_to_ics_datetime(date_str, time_str):
    months = {
        'January': '01', 'February': '02', 'March': '03',
        'April': '04', 'May': '05', 'June': '06',
        'July': '07', 'August': '08', 'September': '09',
        'October': '10', 'November': '11', 'December': '12'
    }
    
    date_parts = date_str.split(' ')
    month = months[date_parts[1]]
    day = date_parts[0].replace('th', '').replace('st', '').replace('nd', '').replace('rd', '')
    year = datetime.now().year

    time_parts = time_str.split('-')
    start_time = time_parts[0].strip()
    end_time = time_parts[1].strip()

    start_dt = f"{year}{month}{day}T{start_time.replace(':', '')}00Z"
    end_dt = f"{year}{month}{day}T{end_time.replace(':', '')}00Z"

    return start_dt, end_dt

def json_to_ics(json_string, ics_filename='events.ics'):
    data = json.loads(json_string)

    ics_content = "BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//My Calendar//EN\n"

    for event in data['events']:
        name = event['name']
        location = event['location']
        date_time = event['time'].split(',')
        date_str = date_time[0].strip()
        time_str = date_time[1].strip()

        start_dt, end_dt = convert_to_ics_datetime(date_str, time_str)

        ics_content += f"BEGIN:VEVENT\nSUMMARY:{name}\nLOCATION:{location}\n"
        ics_content += f"DTSTART:{start_dt}\nDTEND:{end_dt}\n"
        ics_content += "END:VEVENT\n"

    ics_content += "END:VCALENDAR"

    # with open(ics_filename, 'w') as file:
    #     file.write(ics_content)
    return ics_content

