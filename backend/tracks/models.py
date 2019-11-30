from django.db import models
from users.models import User


class Track(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    ticketCode = models.CharField(max_length=1000)
    trashType = models.IntegerField()
    points = models.IntegerField(default=0)

    user = models.ForeignKey(User, related_name='tracks', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created']


class TrackStates(models.Model):
    state = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    track = models.ForeignKey(Track, related_name='states', on_delete=models.CASCADE)

    class Meta:
        ordering = ['timestamp']
