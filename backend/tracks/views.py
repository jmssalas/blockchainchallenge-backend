from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import Http404

from tracks.models import Track, TrackStates
from tracks.serializers import TicketCodeSerializer, TrackDetailSerializer

import tracks.validate_codes as validate_codes
import tracks.states as states
import eth.utils as eth

import hashlib

from backend.settings import RECYCLED_POINTS


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

                    hash = hash_track(track.id, track_state.state, track_state.timestamp)
                    print(eth.sendTrack(hash))

                    return Response({'success': True,
                                     'message': 'Track escanejat',
                                     'data': None})
            return Response({'success': False,
                             'message': 'Codi invàlid',
                             'data': None}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'success': False,
                         'message': 'Request errors',
                         'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class TrackDetail(APIView):
    def get_object(self, request, id):
        try:
            return Track.objects.get(id=id, user=request.user)
        except Track.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        track = self.get_object(request, id)
        serializer = TrackDetailSerializer(track)
        return Response(serializer.data)


def path_to_state(path):
    return states.TRACK_STATE_ID[path.upper()]


def hash_track(trackId, state, timestamp):
    concat = "{}_{}_{}".format(trackId, state, timestamp).encode('utf-8')
    return '0x' + hashlib.md5(concat).hexdigest()


class UpdateTrackState(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, path, format=None):
        serializer = TicketCodeSerializer(data=request.data)
        if serializer.is_valid():
            ticket_code = serializer.data['ticketCode']
            try:
                track = Track.objects.get(ticketCode=ticket_code)
                state = path_to_state(path)
                track_state = TrackStates(track=track, state=state)
                track_state.save()

                hash = hash_track(track.id, track_state.state, track_state.timestamp)
                print(eth.sendTrack(hash))

                if track_state.state == states.TRACK_STATE_ID[states.RECYCLED]:
                    track.points = RECYCLED_POINTS
                    track.save()
                    print(eth.sendPoints(track.user.address, track.points))

                return Response({'success': True,
                                 'message': 'Track actualitzat',
                                 'data': None})
            except Track.DoesNotExist:
                return Response({'success': False,
                                 'message': 'Codi invàlid',
                                 'data': None}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'success': False,
                         'message': 'Request errors',
                         'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
