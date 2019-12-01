from rest_framework import serializers
from tracks.models import Track, TrackStates


class TrackStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackStates
        fields = ['id', 'state', 'timestamp']


class TrackSerializer(serializers.ModelSerializer):
    currentState = serializers.SerializerMethodField()

    class Meta:
        model = Track
        fields = ['id', 'trashType', 'currentState', 'points']


    def get_currentState(self, instance):
        state = instance.states.last()
        return TrackStateSerializer(state).data


class TrackDetailSerializer(serializers.ModelSerializer):
    states = TrackStateSerializer(many=True, read_only=True)

    class Meta:
        model = Track
        fields = ['id', 'trashType', 'states']


class TicketCodeSerializer(serializers.Serializer):
    ticketCode = serializers.CharField(max_length=1000)
