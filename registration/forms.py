from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='Придумайте ник')
    password = forms.CharField(label='Придумайте пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', )

    def check_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return data['password2']

    def clean_username(self):
        data = self.cleaned_data['username']

        if data.isalpha() is False:
            raise ValidationError('Имя пользователя должно содержать только буквы')
        return data





