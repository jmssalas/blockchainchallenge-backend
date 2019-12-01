from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from tracks import views

urlpatterns = (
    path('tracks/scanned', views.CreateTrack.as_view()),
    re_path(r'tracks/(?P<path>(container|collected|recycled))$', views.UpdateTrackState.as_view()),

    path('tracks/<int:id>', views.TrackDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
