from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

API_V1 = 'api/v1/'

urlpatterns = [
    path(API_V1, include('users.urls')),
]

urlpatterns += [
    path(API_V1 + 'auth/login', obtain_jwt_token),
]
