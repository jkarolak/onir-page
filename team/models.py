from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


AVAILABILITIES_STATUS = (
    ('no','Nieobecny'),
    ('yes','Obecny'),
    ('no_decision','Nieodpowiedział'),
    ) 

# Create your models here.
class Player(models.Model):
    user = models.OneToOneField(User, name="Użytkownik", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True, name="Imię")
    last_name = models.CharField(max_length=50, blank=True, name="Nazwisko")
    email = models.EmailField(max_length=100, blank=True, name="Email")
    phone_number = models.CharField(max_length=9, name="Numer telefonu", blank=True)


class Match(models.Model):
    date = models.DateTimeField(blank=True, name="Data i godzina meczu")
    enemy_team = models.CharField(blank=True, name="Drużyna przeciwna", max_length=40)
    home = models.BooleanField(default=True, name="Jako gospodarze")
    our_goals = models.PositiveIntegerField(blank=True, name="My")
    enemy_goals = models.PositiveIntegerField(blank=True, name="Przeciwnicy")
    is_end = models.BooleanField(default=False, name="Mecz zakończony")

class MatchPlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match,on_delete=models.CASCADE)
    availability = models.CharField(choices=AVAILABILITIES_STATUS, default='no_decision', max_length=20)

