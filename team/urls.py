from django.urls import path
from team.views import my_matches, login, frequency
from . import views


urlpatterns = [
    path('my_matches/', my_matches),
    path('', my_matches),
    path('present_button/<int:pk>/', views.present_button, name="present_button"),
    path('absent_button/<int:pk>/', views.absent_button, name="absent_button"),
    path('refresh_match_player_button/', views.refreshMatchPlayer, name="refresh_match_player_button"),
    path('frequency/', views.frequency, name="frequency"),


]

