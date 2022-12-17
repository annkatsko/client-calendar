from django.urls import path, include
from .views import view_homepage, view_coach_contacts_info, view_profile, edit


urlpatterns = [
    path('', view_homepage, name='homepage'),
    path('edit_profile/', edit, name='create_user_profile'),
    path('contacts/', view_coach_contacts_info, name='contacts'),
    path('profile/', view_profile, name='users_profile')
]