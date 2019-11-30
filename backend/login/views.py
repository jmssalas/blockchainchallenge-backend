from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework.response import Response
from rest_framework import status, permissions

from users.models import User
from users.serializers import UserSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER


class LoginView(ObtainJSONWebToken):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        response = super(LoginView, self).post(request, *args, **kwargs)
        res = response.data
        token = res.get('token')

        if token:
            user = jwt_decode_handler(token)
            user = User.objects.get(username=user.get('username'))
            serializer = UserSerializer(user)
            return Response({'success': True,
                             'message': 'Amb èxit logged dins',
                             'data': {'token': token, 'user': serializer.data}},
                             status=status.HTTP_200_OK)
        else:
            return Response({'success': False,
                             'message': 'Perdent o credencials incorrectes',
                             'data': None},
                             status=status.HTTP_401_UNAUTHORIZED)
