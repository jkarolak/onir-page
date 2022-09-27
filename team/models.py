from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import (post_save, m2m_changed)
from django.dispatch import receiver
#from smsapi.client import SmsApiPlClient
from django.conf import settings


AVAILABILITIES_STATUS = (
    ('no','Nieobecny'),
    ('yes','Obecny'),
    ('no_decision','Nieodpowiedział'),
    ) 

PLACES = (
    ('huba', 'Pod Hubą'),
    ('sulechowska', 'Sulechowska')
)

# Create your models here.
class Player(models.Model):
    user = models.OneToOneField(User, verbose_name="Użytkownik", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True, verbose_name="Imię")
    last_name = models.CharField(max_length=50, blank=True, verbose_name="Nazwisko")
    email = models.EmailField(max_length=100, blank=True, verbose_name="Email")
    phone_number = models.CharField(max_length=9, verbose_name="Numer telefonu", blank=True)
    number = models.PositiveIntegerField(verbose_name="Numer koszulki", unique=True, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Match(models.Model):
    date = models.DateTimeField(blank=True, verbose_name="Data i godzina meczu", null=True)
    enemy_team = models.CharField(blank=True, verbose_name="Drużyna przeciwna", max_length=40, null=True)
    at_home = models.BooleanField(default=True, verbose_name="Jako gospodarze")
    our_goals = models.PositiveIntegerField(blank=True, verbose_name="Bramki nasze", null=True)
    enemy_goals = models.PositiveIntegerField(blank=True, verbose_name="Bramki przeciwników", null=True)
    is_end = models.BooleanField(default=False, verbose_name="Mecz zakończony")
    place = models.CharField(choices=PLACES, default='huba', null=True, blank=True, max_length=30)

    def __str__(self):
        return f'{self.date} {self.enemy_team}'


class MatchPlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match,on_delete=models.CASCADE)
    availability = models.CharField(choices=AVAILABILITIES_STATUS, default='no_decision', max_length=20)
    last_modification_date = models.DateTimeField(auto_now=True, null=True, verbose_name="Data ostatniej modyfikacji", editable=False)


    @staticmethod
    def refreshMatchPlayer():
        for match in Match.objects.all():
            for player in Player.objects.all():
                if MatchPlayer.objects.filter(player=player, match=match).count()==0:
                    MatchPlayer.objects.create(player=player, match=match)

def sentSmsAPI(to, message):
    pass
    """
    token = settings.SMS_API_TOKEN

    client = SmsApiPlClient(access_token=token)
    send_results = client.sms.send(to=to, message=message,  from_="ONIR TEAM", encoding="utf-8", skip_foreign=1,normalize=1)

    for result in send_results:
        print(result.id, result.points, result.error)
    """

class Sms(models.Model):
    players = models.ManyToManyField(Player, verbose_name="Adresaci")
    content = models.CharField(max_length=160)
    phone_numbers = models.TextField(null=True, verbose_name="Numery adresatów")
    request = models.TextField(null=True, verbose_name="request")
    response = models.TextField(null=True, verbose_name="response")
    sent = models.BooleanField(default=False)

"""
@receiver(m2m_changed,sender=Sms.players.through)
def sentSms(sender, instance,action, **kwargs):
    if not instance.sent and action=="post_add":
        phone_numbers = []
        for player in instance.players.all():
            if player.phone_number:
                phone_numbers.append(player.phone_number)
        if phone_numbers:
            to = ",".join(phone_numbers)
            message = instance.content
            sentSmsAPI(to, message)

            
        #instance.sent = True
"""       #instance.save()

@receiver(post_save,sender=Match)
def refresh_match_player_list(*args,**kwargs):
    MatchPlayer.refreshMatchPlayer()

@receiver(post_save,sender=Player)
def refresh_match_player_list(*args,**kwargs):
    MatchPlayer.refreshMatchPlayer()