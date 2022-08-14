from atexit import register
from django.contrib import admin
from .models import Player,Match,MatchPlayer
# Register your models here.
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name','last_name','email','phone_number')

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('date', 'enemy_team','at_home','our_goals','enemy_goals','is_end')

@admin.register(MatchPlayer)
class MatchPlayerAdmin(admin.ModelAdmin):
    list_display = ('player','match','availability', 'last_modification_date')
    list_filter = ('availability',)

