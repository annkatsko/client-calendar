from django.shortcuts import get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import Profile

class ClientLoginView(LoginView):
    next_page = '/homepage'



class ProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context



class ProfileCreatePageView(CreateView):
    model = Profile

    template_name = 'registration/create_profile.html'
    fields = ['phone_number', 'birthday_date', 'instagram', 'telegram',
              'email', 'goal']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = 'homepage/'


class ClientLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'
