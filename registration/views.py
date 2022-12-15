from django.shortcuts import render
from .forms import UserRegistrationForm
from .models import Profile
from django.contrib import messages


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