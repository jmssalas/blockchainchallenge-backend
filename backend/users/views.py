from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.models import User
from users.serializers import UserSerializer, UserCodeSerializer

import users.validate_codes as validate_codes


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UpdateUserCode(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, format=None):
        user = request.user
        serializer = UserCodeSerializer(data=request.data)
        if serializer.is_valid():
            if validate_codes.validate(serializer.data['code']):
                user.code = serializer.data['code']
                user.save()
                return Response()
            return Response({'error': 'Codi invàlid'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
