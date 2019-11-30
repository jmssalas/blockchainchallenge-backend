from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tracks import views

urlpatterns = (
    path('tracks', views.CreateTrack.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
