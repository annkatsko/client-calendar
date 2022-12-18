from .views import register_user
from django.contrib.auth.views import LoginView, LogoutView
from .views import edit, password_reset_request
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('create_profile_page/', edit, name='create_user_profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', register_user, name='registration'),
    path("reset_password/", password_reset_request, name="password_reset"),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/my_password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="registration/my_password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset_password/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/my_password_reset_complete.html'), name='password_reset_complete'),
]