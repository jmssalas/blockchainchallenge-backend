from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from home.serializers import UserHomeSerializer


class GetUserHome(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        serializer = UserHomeSerializer(user)
        return Response({'success': True,
                         'message': "Home d'usuari",
                         'data': {'home': serializer.data}},
                        status=status.HTTP_200_OK)
