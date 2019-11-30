from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from home import views

urlpatterns = (
    path('home', views.GetUserHome.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
