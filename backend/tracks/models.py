from django.db import models
from users.models import User


REGISTER = 'SCANNED'
IN_CONTAINER = 'IN_CONTAINER'
COLLECTED = 'COLLECTED'
RECICLED = 'RECICLED'
TRACK_STATE_ID = {REGISTER: 1, IN_CONTAINER: 2, COLLECTED: 3, RECICLED: 4}


class Track(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    ticketCode = models.CharField(max_length=1000)

    user = models.ForeignKey(User, related_name='tracks', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class TrackStates(models.Model):
    state = models.IntegerField()
    timestamp = models.DateField(auto_now_add=True)

    track = models.ForeignKey(Track, related_name='states', on_delete=models.CASCADE)

    class Meta:
        ordering = ['timestamp']
