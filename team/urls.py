from django.urls import path
from team.views import my_matches

urlpatterns = [
    path('my_matches/', my_matches)
]

