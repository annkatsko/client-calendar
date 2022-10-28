from django.urls import path
from .views import show_calendar

urlpatterns = [
    path('main/', show_calendar, name='main_calendar'),
]