from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tracks import views

urlpatterns = (
    path('tracks/scanned', views.CreateTrack.as_view()),
    path('tracks/container', views.ContainerTrack.as_view()),

    path('tracks/<int:id>', views.TrackDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
