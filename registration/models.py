from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    GOALS = (
        ('P', 'Физическая активность'),
         ('WL', 'Снижение веса'),
         ('MG', 'Набор мышечной массы',),
    )

    GYM_NAME = (
        ('NB', 'Новая Боровая "Vibe"'),
        ('NEM', 'Немига "GymBox"')
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField('Имя', max_length=50, null=True, blank=False)
    last_name = models.CharField('Фамилия', max_length=50, null=True, blank=True)
    phone_number = models.CharField('Номер телефона',max_length=50, null=True, blank=True)
    birthday_date = models.DateField('Дата рождения', blank=False, null=True)
    instagram = models.CharField('Ник в Instagram', max_length=50, null=True, blank=True)
    telegram = models.CharField('Ник в Telegram', max_length=50, null=True, blank=False)
    email = models.EmailField('Email', max_length=50, null=True, blank=False)
    start_date = models.DateField(auto_now=True, blank=False)
    goal = models.CharField('Цель', max_length=50, choices=GOALS, blank=False, default='Физическая активность', null=True)
    gym_name = models.CharField('Зал', choices=GYM_NAME, blank=False, max_length=50, default='Новая Боровая "Vibe', null=True)


    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'username': self.user.username})


class UserProfile(models.Model):
    GOALS = (
        ('P', 'Физическая активность'),
         ('WL', 'Снижение веса'),
         ('MG', 'Набор мышечной массы',),
    )

    GYM_NAME = (
        ('NB', 'Новая Боровая "Vibe"'),
        ('NEM', 'Немига "GymBox"')
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField('Имя', max_length=50, null=True, blank=False)
    last_name = models.CharField('Фамилия', max_length=50, null=True, blank=True)
    phone_number = models.CharField('Номер телефона',max_length=50, null=True, blank=True)
    birthday_date = models.DateField('Дата рождения', blank=False, null=True)
    instagram = models.CharField('Ник в Instagram', max_length=50, null=True, blank=True)
    telegram = models.CharField('Ник в Telegram', max_length=50, null=True, blank=False)
    email = models.EmailField('Email', max_length=50, null=True, blank=False)
    start_date = models.DateField(auto_now=True, blank=False)
    goal = models.CharField('Цель', max_length=50, choices=GOALS, blank=False, default='Физическая активность', null=True)
    gym_name = models.CharField('Зал', choices=GYM_NAME, blank=False, max_length=50, default='Новая Боровая "Vibe', null=True)


    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'username': self.user.username})
