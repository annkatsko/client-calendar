from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
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


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request,
                      'registration/edit_profile.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})