from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):
    GOALS = (
        ('P', 'Физическая активность'),
         ('WL', 'Снижение веса'),
         ('MG', 'Набор мышечной массы',),
    )

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone_number = models.CharField('Номер телефона',max_length=50, null=True, blank=True)
    birthday_date = models.DateField(blank=False)
    instagram = models.CharField('Ник в Instagram', max_length=50, null=True, blank=True)
    telegram = models.CharField('Ник в Telegram', max_length=50, null=True, blank=False)
    email = models.EmailField('Email', max_length=50, null=True, blank=False)
    start_date = models.DateField(auto_now=True, blank=False)
    goal = models.CharField(max_length=2, choices=GOALS, blank=False, default='Физическая активность')

    def __str__(self):
        return str(self.user)



