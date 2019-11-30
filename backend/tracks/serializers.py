from rest_framework import serializers
from tracks.models import Track, TrackState


class TrackStateSerializer(serializers.ModelSerializer):
    track = serializers.ReadOnlyField(source='track.ticketCode')

    class Meta:
        model = TrackState
        fields = ['id', 'state', 'timestamp', 'track']


class TrackSerializer(serializers.ModelSerializer):
    states = serializers.PrimaryKeyRelatedField(many=True, queryset=TrackState.objects.all())

    class Meta:
        model = Track
        fields = ['id', 'ticketCode', 'states']
