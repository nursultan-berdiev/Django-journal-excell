from django.db import models
from django.contrib.auth.models import User


def name_user(str):
    need_officer = Officer.objects.filter(name=str)[0]
    our_user = need_officer.user
    return our_user


class Office(models.Model):
    office_id = models.IntegerField(null=False, blank=False, primary_key=True, unique=True,
                                    verbose_name='Идентификатор офиса')
    office_name = models.CharField(max_length=255, verbose_name='Наименование офиса')

    def __str__(self):
        return '{} - {}'.format(self.office_id, self.office_name)


class Officer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='ФИО Сотрудника')
    office = models.ForeignKey(Office, on_delete=models.CASCADE, verbose_name='Офис')

    def __str__(self):
        return self.name
