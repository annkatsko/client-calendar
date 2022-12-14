from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import datetime
from .google_calendar import get_events



def get_session_info(request):
    if request.user.is_authenticated:
        if request.user.first_name and request.user.last_name:
            name = f'{request.user.first_name} {request.user.last_name}'
            info = get_events(name)
            return render(request, 'client_calendar/sessions_info.html', context={'info': info})
    return render(request, 'client_calendar/sessions_info.html')

