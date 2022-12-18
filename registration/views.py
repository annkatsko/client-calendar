from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib import messages

from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Восстановление пароля"
                    email_template_name = "registration/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'coach-helper',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                        'username': user.username
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'coach_helper@gmail.com', [user.email], fail_silently=False)
                    except BadHeaderError:

                        return HttpResponse('Invalid header found.')

                    messages.success(request, 'Сообщение для восстановления пароля было отпрвлено к Вам на почту.')
                    return redirect("login")
            messages.error(request, 'Проверьте правильность введенного Email.')
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="registration/my_password_reset.html",
                  context={"password_reset_form": password_reset_form})


def register_user(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            profile.first_name = user_form.cleaned_data['first_name']
            profile.last_name = user_form.cleaned_data['last_name']
            profile.email = user_form.cleaned_data['email']
            messages.success(request, 'Вы успешно зарегистрировались!')

    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register_user.html', {'form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        messages.success(request, 'Профиль обновлен!')
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Профиль обновлен!')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request,
                      'registration/edit_profile.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})




