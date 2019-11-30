from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
    AbstractUser._meta.get_field('email')._unique = True
    code = models.CharField(max_length=1000, blank=True, default='')

    def __str__(self):
        return self.username
