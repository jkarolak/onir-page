from atexit import register
from django.contrib import admin
from .models import Player,Match,MatchPlayer
# Register your models here.
@admin.register(Player)
class TeamAdmin(admin.ModelAdmin):
    pass

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    pass

@admin.register(MatchPlayer)
class MatchPlayerAdmin(admin.ModelAdmin):
    pass


