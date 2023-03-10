from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from registration.forms import UserEditForm, ProfileEditForm
from django.contrib import messages


def view_homepage(request):
    return render(request, 'home_page/homepage.html')

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Профиль обновлен.')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'registration/edit_profile.html',
                       {'user_form': user_form,
                       'profile_form': profile_form})


def view_coach_contacts_info(request):
    return render(request, 'home_page/contacts.html')


@login_required
def view_profile(request):
    return render(request, 'home_page/portfolio_detail.html')