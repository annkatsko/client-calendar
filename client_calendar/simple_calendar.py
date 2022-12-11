from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa.recurrence import Recurrence, DAILY, SU, SA

from beautiful_date import Jan, Apr


calendar = GoogleCalendar('1187484l@gmail.com',
                          credentials_path='../credentials.json')

for event in calendar:
    print(event)