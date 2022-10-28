from django.contrib import admin
from django.urls import path
from .views import WelcomeView, UserRegistrationCreateView, ProfileCreatePageView
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('create_profile_page/<int:pk>/', ProfileCreatePageView.as_view(), name='create_user_profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', WelcomeView.as_view(), name='welcome'),
    path('registration/', UserRegistrationCreateView.as_view(), name='registration'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]