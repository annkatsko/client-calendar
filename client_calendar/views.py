from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
from .models import Session
from registration.models import Profile

def show_calendar(request):
    sessions = Session.objects.get(pk=request.user.id)
    return HttpResponse(content=(sessions.date, sessions.client_id))