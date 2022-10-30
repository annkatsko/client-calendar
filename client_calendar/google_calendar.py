from __future__ import print_function
import datetime
import googleapiclient
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']

calendarId = '4ef49f9c5a93b050a65df71b6445840cc97ce43859d93e6eaceeb9aa8c27fa12@group.calendar.google.com'
SERVICE_ACCOUNT_FILE = 'coach-helper-366918-d7b6d7a657a1.json'


class GoogleCalendar(object):
    def __init__(self):
        credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        self.service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

    # создание словаря с информацией о событии
    # def create_event_dict(self):
    #     event = {
    #         'summary': 'test event',
    #         'description': 'some info',
    #         'start': {
    #             'dateTime': '2020-08-03T03:00:00+03:00',
    #         },
    #         'end': {
    #             'dateTime': '2020-08-03T05:30:00+03:00',
    #         }
    #     }
    #     return event

    # создание события в календаре
    # def create_event(self, event):
    #     e = self.service.events().insert(calendarId=calendarId,
    #                                      body=event).execute()
    #     print('Event created: %s' % (e.get('id')))

    # вывод списка из десяти предстоящих событий
    def get_events_list(self):
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        in_week = (datetime.datetime.utcnow() + datetime.timedelta(days=6)).isoformat() + 'Z'
        print('Getting the upcoming 10 events')
        events_result = self.service.events().list(calendarId=calendarId,
                                                   timeMin=now, singleEvents=True,
                                                   timeMax=in_week,
                                                   orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            desc = event.get('summary')
            print(start, desc)


calendar = GoogleCalendar()
print("+ - create event\n? - print event list\n")
c = input()

if c == '+':
    event = calendar.create_event_dict()
    calendar.create_event(event)
elif c == '?':
    calendar.get_events_list()
else:
    pass