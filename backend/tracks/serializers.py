from rest_framework import serializers
from tracks.models import Track, TrackStates


class TrackStateSerializer(serializers.ModelSerializer):
    track = serializers.ReadOnlyField(source='track.ticketCode')

    class Meta:
        model = TrackStates
        fields = ['id', 'state', 'timestamp', 'track']


class TrackSerializer(serializers.ModelSerializer):
    states = serializers.PrimaryKeyRelatedField(many=True, queryset=TrackStates.objects.all())

    class Meta:
        model = Track
        fields = ['id', 'ticketCode', 'states']


class CreateTrackSerializer(serializers.Serializer):
    ticketCode = serializers.CharField(max_length=1000)
