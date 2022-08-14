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
    user = models.OneToOneField(User, verbose_name="Użytkownik", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True, verbose_name="Imię")
    last_name = models.CharField(max_length=50, blank=True, verbose_name="Nazwisko")
    email = models.EmailField(max_length=100, blank=True, verbose_name="Email")
    phone_number = models.CharField(max_length=9, verbose_name="Numer telefonu", blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Match(models.Model):
    date = models.DateTimeField(blank=True, verbose_name="Data i godzina meczu", null=True)
    enemy_team = models.CharField(blank=True, verbose_name="Drużyna przeciwna", max_length=40, null=True)
    at_home = models.BooleanField(default=True, verbose_name="Jako gospodarze")
    our_goals = models.PositiveIntegerField(blank=True, verbose_name="Bramki nasze", null=True)
    enemy_goals = models.PositiveIntegerField(blank=True, verbose_name="Bramki przeciwników", null=True)
    is_end = models.BooleanField(default=False, verbose_name="Mecz zakończony")

    def __str__(self):
        return f'{self.date} {self.enemy_team}'


class MatchPlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match,on_delete=models.CASCADE)
    availability = models.CharField(choices=AVAILABILITIES_STATUS, default='no_decision', max_length=20)


    @staticmethod
    def refreshMatchPlayer():
        for match in Match.objects.all():
            for player in Player.objects.all():
                if MatchPlayer.objects.filter(player=player, match=match).count()==0:
                    MatchPlayer.objects.create(player=player, match=match)

