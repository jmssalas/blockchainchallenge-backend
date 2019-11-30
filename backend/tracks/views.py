from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from tracks.models import Track, TrackStates
from tracks.serializers import CreateTrackSerializer

import tracks.validate_codes as validate_codes
import tracks.states as states


class CreateTrack(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        user = request.user
        serializer = CreateTrackSerializer(data=request.data)
        if serializer.is_valid():
            ticket_code = serializer.data['ticketCode']
            if validate_codes.validate(ticket_code):
                track = Track(ticketCode=ticket_code, trashType=validate_codes.trash_type(ticket_code), user=user)
                track.save()
                track_state = TrackStates(track=track, state=states.TRACK_STATE_ID[states.SCANNED])
                track_state.save()
                return Response({'success': True,
                             'message': 'Trash scanned',
                             'data': None})
            return Response({'success': False,
                             'message': 'Codi invàlid',
                             'data': None}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'success': False,
                             'message': 'Request errors',
                             'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
