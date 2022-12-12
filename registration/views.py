from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, UpdateView
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                      'registration/create_profile.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})

class ProfileCreatePageView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'registration/create_profile.html'
    fields = ['first_name', 'last_name', 'gym_name', 'phone_number', 'birthday_date', 'instagram', 'telegram',
              'email', 'goal']
    success_url = '/welcome/'

    def form_valid(self, form):
        form.instance.user = self.request.user

        if '@' in form.cleaned_data['instagram']:
            form.add_error('instagram', 'Введите ник без символа "@"')
            return self.form_invalid(form)

        elif form.cleaned_data['first_name'].isalpha() is False:
            form.add_error('first_name', 'Ваше должно содержать только буквы')
            return self.form_invalid(form)

        elif form.cleaned_data['last_name'].isalpha() is False:
            form.add_error('last_name', 'Ваша фамилия далжна содержать только буквы')
            return self.form_invalid(form)

        elif form.cleaned_data['phone_number'].isnumeric() is False:
            form.add_error('phone_number', 'Номер телефона должен содержать только цифры')
            return self.form_invalid(form)

        elif '@' in form.cleaned_data['telegram']:
            form.add_error('telegram', 'Введите ник без символа "@"')
            return self.form_invalid(form)

        return super(ProfileCreatePageView, self).form_valid(form)




class WelcomeView(TemplateView):
    template_name = 'registration/welcome.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('welcome'))
        else:
            return HttpResponseRedirect(reverse('login'))



def register_user(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            profile.first_name = user_form.cleaned_data['first_name'].capitalize()
            profile.last_name = user_form.cleaned_data['last_name'].capitalize()
            profile.email = user_form.cleaned_data['email']
            return HttpResponseRedirect(reverse('login'))
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register_user.html', {'form': user_form})