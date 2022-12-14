import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPES = ['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/calendar.readonly']

calendarId = '4ef49f9c5a93b050a65df71b6445840cc97ce43859d93e6eaceeb9aa8c27fa12@group.calendar.google.com'
SERVICE_ACCOUNT_FILE = 'credentials.json'




def get_events(user_name):
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # # If there are no (valid) credentials available, let the user log in.
    # if not creds or not creds.valid:
    #     if creds and creds.expired and creds.refresh_token:
    #         creds.refresh(Request())
    #     else:
    #         flow = InstalledAppFlow.from_client_secrets_file(
    #             'credentials.json', SCOPES)
    #         creds = flow.run_local_server(port=0)
    #     # Save the credentials for the next run
    #     with open('token.json', 'w') as token:
    #         token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])
        user_events = []

        if not events:
            return None

        for event in events:
            if event['summary'] == user_name:
                start = event['start'].get('dateTime', event['start'].get('date'))
                readable_start = datetime.datetime.strptime(start[:19], '%Y-%m-%dT%H:%M:%S')

                user_events.append(f'{readable_start}')  #event['htmlLink'] - link to event
        return user_events

    except HttpError:
        raise HttpError


if __name__ == '__main__':
    get_events('Анна Катько')



