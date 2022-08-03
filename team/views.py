from django.shortcuts import render, redirect
from django.http import HttpResponse, request, response,HttpResponseRedirect
from .models import MatchPlayer, Match, Player
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def my_matches(request):
        get_active_player = Player.objects.get(user=request.user)
        return render(request, 'my_matches.html', {'MatchPlayer':MatchPlayer.objects.all().filter(player=get_active_player)})

def present_button(request, pk):
   matchPlayer = MatchPlayer.objects.get(id=pk)
   matchPlayer.availability='yes'
   matchPlayer.save()
   return redirect('../../my_matches/')

def absent_button(request, pk):
   matchPlayer = MatchPlayer.objects.get(id=pk)
   matchPlayer.availability='no'
   matchPlayer.save()
   return redirect('../../my_matches/')

def refreshMatchPlayer(request):
    MatchPlayer.refreshMatchPlayer()
    return redirect('../my_matches/')
