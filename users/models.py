from django.contrib.auth.models import AbstractUser
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class UserRoles:
    USER = 'member'
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    choices = ((USER, "Пользователь"),
               (ADMIN, "Админ"),
               (MODERATOR, "Модератор"))


class User(AbstractUser):
    role = models.CharField(choices=UserRoles.choices, default='member', max_length=12)
    location = models.ManyToManyField(Location)
    age = models.PositiveSmallIntegerField(null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"Пользователь {self.first_name} {self.last_name}"
