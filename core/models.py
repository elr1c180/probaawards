from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Закреплено за пользователем')
    password = models.CharField('Пароль', max_length=250)
    name = models.CharField('ФИО', max_length=3500)
    email = models.CharField('E-mail', max_length=3500)
    phone = models.CharField('Телефон', max_length=3500)
    company = models.CharField('Название компании', max_length=3500)

    def __str__(self):
        return f"{self.name}-{self.company}"
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Work(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='Владелец')
    project_name = models.CharField(max_length=3500)
    brand_name = models.CharField(max_length=3500)
    agency_name = models.CharField(max_length=3500)
    nom = models.CharField(max_length=3500)
    period = models.CharField(max_length=3500)
    short_info = models.CharField(max_length=3500)
    position = models.CharField(max_length=3500)
    point = models.CharField(max_length=3500)
    strategy = models.CharField(max_length=3500)
    idea = models.CharField(max_length=3500)
    channel1 = models.CharField(max_length=3500)
    channel2 = models.CharField(max_length=3500)
    channel3 = models.CharField(max_length=3500)
    budget = models.CharField(max_length=3500)
    desc  = models.CharField(max_length=3500)
    result = models.CharField(max_length=3500)
    file = models.FileField(upload_to='media/', blank=True, null=True)
    url = models.CharField(max_length=3500, null=True, blank=True)

class ResetPassword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    id_off = models.CharField(verbose_name='', max_length=99999)

    def __str__(self) -> str:
        return self.id_off
# class Draft(models.Model):
#     user = models.ForeignKey()
