from .google_calendar import GoogleCalendar
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
@login_required
def get_session_info(request):
    calendar = GoogleCalendar()
    date = calendar.get_events_list()[request.user.username].get('date')
    time = calendar.get_events_list()[request.user.username].get('time')
    return render(request, 'client_calendar/sessions_info.html', context= {'date': date,
                                                                           'time':time})


    # return HttpResponse(content=f'Date - {date}'
    #                             f'Time - {time}')