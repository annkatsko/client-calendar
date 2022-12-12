from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserRegistrationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput, min_length=4, )
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput, min_length=4)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        help_texts = {'first_name': 'Введите полное имя.',
                      'username': 'Используйте только буквы, цифры и символы @/./+/-/_.'}


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']



class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['gym_name', 'phone_number', 'birthday_date', 'instagram', 'telegram', 'goal']








