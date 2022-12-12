from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', include('registration.urls')),
    path('', include('home_page.urls')),
    path('calendar/', include('client_calendar.urls')),
]
