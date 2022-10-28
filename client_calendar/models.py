from django.db import models
from registration.models import Profile
# Create your models here.

class Session(models.Model):
    GYM_NAME = (
        ('NB', 'Новая Боровая "Vibe"'),
        ('NEM', 'Немига "GymBox"')
    )

    date = models.DateField('Дата тренировки', blank=False)
    created_date = models.DateField(auto_now=True, blank=False)
    session_time = models.TimeField('Время тренировки', blank=True, null=True)
    gym_name = models.CharField('Зал', choices=GYM_NAME, blank=False, max_length=50, default='Новая Боровая "Vibe')
    client = models.ForeignKey(Profile, on_delete=models.PROTECT, verbose_name='client_id')