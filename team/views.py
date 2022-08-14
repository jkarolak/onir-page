from django.shortcuts import render, redirect
from django.http import HttpResponse, request, response,HttpResponseRedirect
from .models import MatchPlayer, Match, Player
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Count

# Create your views here.
@login_required
def my_matches(request):
        get_active_player = Player.objects.get(user=request.user)
        print(get_active_player)
        return render(request, 'my_matches.html', {'MatchPlayer':MatchPlayer.objects.all().filter(player=get_active_player)})

@login_required
def frequency(request):
   date_to_return = []
   for match in Match.objects.order_by("date"):
      yes_count = 0
      no_count = 0
      no_decision_count = 0
      for row in MatchPlayer.objects.all().filter(match=match).values('availability').annotate(total=Count('availability')):
         if row['availability']=='yes':
            yes_count = row['total']
         elif row['availability']=='no':
            no_count = row['total']
         elif row['availability']=='no_decision':
            no_decision_count = row['total']

      print(yes_count,no_count,no_decision_count)
      date_to_return.append({'date':match.date,
       'enemy_team':match.enemy_team,
       'is_end':match.is_end,
       'yes_count':yes_count,
       'no_count':no_count,
       'no_decision_count':no_decision_count,
       })
   
   return render(request, 'frequency.html', {'data':date_to_return})

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
