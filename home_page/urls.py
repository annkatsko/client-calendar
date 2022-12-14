from django.urls import path, include
from .views import view_homepage,view_and_edit_profile, view_coach_contacts_info


urlpatterns = [
    path('', view_homepage, name='homepage'),
    path('profile/', view_and_edit_profile, name='create_user_profile'),
    path('contacts/', view_coach_contacts_info, name='contacts')
]