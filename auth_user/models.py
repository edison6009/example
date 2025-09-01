from django.db import models
from django.contrib.auth.models import AbstractUser
from abcstract.models import TimestampedMixin, SoftDeleteMixin

#Clase 2 modulo 6 jueves 26-6-25
class User(AbstractUser, TimestampedMixin, SoftDeleteMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)


    class Meta:
        db_table = "users"
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f"{self.username} ({self.email})"

