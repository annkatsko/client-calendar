from django.urls import path, include
from .views import view_homepage,view_and_edit_profile, view_coach_contacts_info, view_profile


urlpatterns = [
    path('', view_homepage, name='homepage'),
    path('edit_profile/', view_and_edit_profile, name='create_user_profile'),
    path('contacts/', view_coach_contacts_info, name='contacts'),
    path('profile/', view_profile, name='users_profile')
]