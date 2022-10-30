from django.urls import path
from .views import get_session_info
urlpatterns = [
    path('sessions/', get_session_info, name='sessions_calendar' )
]