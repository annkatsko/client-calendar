
from django.urls import path, include
from .views import show_homepage
urlpatterns = [
    path('', show_homepage, name='homepage'),
]