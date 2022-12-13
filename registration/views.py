from django.shortcuts import render
from .forms import UserRegistrationForm
from .models import Profile
from django.contrib import messages


# class ProfileCreatePageView(LoginRequiredMixin, UpdateView):
#     model = Profile
#     template_name = 'registration/create_profile.html'
#     fields = ['first_name', 'last_name', 'gym_name', 'phone_number', 'birthday_date', 'instagram', 'telegram',
#               'email', 'goal']
#     success_url = '/welcome/'
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#
#         if '@' in form.cleaned_data['instagram']:
#             form.add_error('instagram', 'Введите ник без символа "@"')
#             return self.form_invalid(form)
#
#         elif form.cleaned_data['first_name'].isalpha() is False:
#             form.add_error('first_name', 'Ваше должно содержать только буквы')
#             return self.form_invalid(form)
#
#         elif form.cleaned_data['last_name'].isalpha() is False:
#             form.add_error('last_name', 'Ваша фамилия далжна содержать только буквы')
#             return self.form_invalid(form)
#
#         elif form.cleaned_data['phone_number'].isnumeric() is False:
#             form.add_error('phone_number', 'Номер телефона должен содержать только цифры')
#             return self.form_invalid(form)
#
#         elif '@' in form.cleaned_data['telegram']:
#             form.add_error('telegram', 'Введите ник без символа "@"')
#             return self.form_invalid(form)
#
#         return super(ProfileCreatePageView, self).form_valid(form)


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
            messages.success(request, 'Вы успешно зарегистрировались!')

    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register_user.html', {'form': user_form})