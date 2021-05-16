from django.db import models
from rest_framework import serializers
from django_project.utils.validators import validate_size, validate_extension


class Client(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Фамилия')
    address = models.TextField(null=True, blank=True, verbose_name='Адрес')
    city = models.CharField(max_length=100, null=True, blank=True, verbose_name='Город')
    country = models.CharField(max_length=100, null=True, blank=True, verbose_name='Страна')
    photo = models.ImageField(upload_to='pictures',
                              validators=[validate_size, validate_extension],
                              null=True, blank=True)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.first_name


class Artist(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Фамилия')
    email = models.CharField(max_length=255, null=True, blank=True, verbose_name='Email')
    photo = models.ImageField(upload_to='author_photos',
                              validators=[validate_size, validate_extension],
                              null=True, blank=True)

    class Meta:
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'





