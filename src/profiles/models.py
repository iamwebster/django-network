from django.db import models
from django.contrib.auth.models import AbstractUser


class UserNet(AbstractUser):
    '''Custom user model'''
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    middle_name = models.CharField(max_length=50)
    first_login = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(max_length=14)
    avatar = models.ImageField(upload_to='user/avatar', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    github = models.CharField(max_length=500, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    