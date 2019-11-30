from rest_framework import serializers
from users.models import User
from tracks.serializers import TrackSerializer


class UserHomeSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'tracks']
