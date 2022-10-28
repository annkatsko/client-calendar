from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from .forms import RegisterForm

from .models import Profile


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


class UserRegistrationCreateView(CreateView):
    template_name = 'registration/register_user.html'
    form_class = RegisterForm
    success_url = '/welcome/login/'

