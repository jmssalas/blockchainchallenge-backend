from rest_framework import serializers
from tracks.models import Track, TrackStates


class TrackStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackStates
        fields = ['id', 'state', 'timestamp']


class TrackSerializer(serializers.ModelSerializer):
    states = TrackStateSerializer(many=True, read_only=True)

    class Meta:
        model = Track
        fields = ['id', 'ticketCode', 'trashType', 'states']


class CreateTrackSerializer(serializers.Serializer):
    ticketCode = serializers.CharField(max_length=1000)
