from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import Http404

from tracks.models import Track, TrackStates
from tracks.serializers import TicketCodeSerializer, TrackDetailSerializer

import tracks.validate_codes as validate_codes
import tracks.states as states


class CreateTrack(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        user = request.user
        serializer = TicketCodeSerializer(data=request.data)
        if serializer.is_valid():
            ticket_code = serializer.data['ticketCode']
            if validate_codes.validate(ticket_code):
                try:
                    Track.objects.get(ticketCode=ticket_code)
                    return Response({'success': False,
                                     'message': 'Codi ja utilitzat',
                                     'data': None}, status=status.HTTP_409_CONFLICT)
                except Track.DoesNotExist:
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


class TrackDetail(APIView):
    def get_object(self, id):
        try:
            return Track.objects.get(id=id)
        except Track.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        track = self.get_object(id)
        serializer = TrackDetailSerializer(track)
        return Response(serializer.data)


class ContainerTrack(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        serializer = TicketCodeSerializer(data=request.data)
        if serializer.is_valid():
            ticket_code = serializer.data['ticketCode']
            try:
                track = Track.objects.get(ticketCode=ticket_code)
                track_state = TrackStates(track=track, state=states.TRACK_STATE_ID[states.IN_CONTAINER])
                track_state.save()
                return Response({'success': True,
                                 'message': 'Track updated',
                                 'data': None})
            except Track.DoesNotExist:
                return Response({'success': False,
                                 'message': 'Codi invàlid',
                                 'data': None}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'success': False,
                         'message': 'Request errors',
                         'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
