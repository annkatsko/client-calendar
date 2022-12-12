from django.urls import path, include
from .views import show_homepage,view_and_edit_profile


urlpatterns = [
    path('', show_homepage, name='homepage'),
    path('profile/', view_and_edit_profile, name='create_user_profile'),
]