from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
    code = models.CharField(max_length=1000, blank=True, default='')

    def __init__(self):
        User._meta.get_field('email')._unique = True

    def __str__(self):
        return self.username
