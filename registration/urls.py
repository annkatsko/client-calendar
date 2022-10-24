from django.contrib import admin
from django.urls import path
from .views import LoginView, ProfilePageView, ProfileCreatePageView, ClientLoginView, ClientLogoutView

urlpatterns = [
    path('login/', ClientLoginView.as_view(), name='login'),
    path('profile/<int:pk>/', ProfilePageView.as_view(), name='profile'),
    path('create_profile_page/', ProfileCreatePageView.as_view(), name='create_user_profile'),
    path('logout/', ClientLogoutView.as_view(), name='logout'),
]