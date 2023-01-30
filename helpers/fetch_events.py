from googleapiclient.discovery import build

def fetch_events(credentials):
    service = build('calendar', 'v3', credentials=credentials)

    # Call the Calendar API
    events_result = service.events().list(calendarId='primary').execute()
    events = events_result.get('items', [])

    if not events:
        return []

    # Prepare events_dict
    events_dict = {}
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        events_dict[start] = event['summary']
    return events_dict