from django import forms
from django.contrib.auth.models import User
from .models import Profile
import phonenumbers

class UserRegistrationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
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

    def clean(self):
        self.cleaned_data['first_name'] = self.cleaned_data['first_name'].capitalize()
        self.cleaned_data['last_name'] = self.cleaned_data['last_name'].capitalize()
        return self.cleaned_data



class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['gym_name', 'phone_number', 'birthday_date', 'instagram', 'telegram', 'goal']
        help_texts = {'birthday_date': 'Введите дату в формате день.месяц.год',
                      'instagram': 'Введите ник без символа "@" или ссылку на Ваш профиль.',
                      'telegram': 'Введите ник без символа "@" или ссылку на Ваш профиль.',
                      'phone_number': 'Введите номер телефона в формате +375...'
                      }

    def clean(self):
        cleaned_data = super().clean()
        user_instagram = cleaned_data['instagram']
        user_telegram = cleaned_data['telegram']
        string_user_phone = cleaned_data['phone_number']
        parsed_user_phone = phonenumbers.parse(string_user_phone, 'BY')
        if '@' in user_instagram or '@' in user_telegram:
            raise forms.ValidationError('Введите ник без "@"')
        if not phonenumbers.is_valid_number(parsed_user_phone):
            raise forms.ValidationError('Введите корректный номер телефона.')













