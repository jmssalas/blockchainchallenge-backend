from rest_framework import serializers
from users.models import User
from tracks.serializers import TrackSerializer


class UserHomeSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)
    userPoints = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['tracks', 'userPoints']

    def get_userPoints(self, instance):
        return sum([track.points for track in instance.tracks.all()])
