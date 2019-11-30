from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = (
    path('users', views.UserCreate.as_view()),
    path('users/code', views.UpdateUserCode.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
