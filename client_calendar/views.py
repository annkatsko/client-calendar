from .google_calendar import GoogleCalendar
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
@login_required
def get_session_info(request):
    calendar = GoogleCalendar()
    info = calendar.get_events_list()[request.user.username]


    return render(request, 'client_calendar/sessions_info.html', context={'info': info})

