from django.urls import path, include
from login.views import LoginView

API_V1 = 'api/v1/'

urlpatterns = [
    path(API_V1, include('users.urls')),
]

urlpatterns += [
    path(API_V1 + 'auth/login', LoginView.as_view()),
]
