from django.shortcuts import render, redirect
from django.http import HttpResponse, request, response,HttpResponseRedirect
from .models import MatchPlayer, Match, Player,TrainingDate,TrainingDatePlayer
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Count

# Create your views here.



@login_required
def my_matches(request):
        get_active_player = Player.objects.get(user=request.user)
        return render(request, 'my_matches.html', {
         'MatchPlayer':MatchPlayer.objects.all().filter(player=get_active_player, match__is_end=False).order_by('match__date'),
         'MatchPlayerEnded':MatchPlayer.objects.all().filter(player=get_active_player, match__is_end=True).order_by('match__date')})

@login_required
def frequency(request):
   date_to_return = []
   for match in Match.objects.filter(is_end=False).order_by("-is_end", "date"):
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

      date_to_return.append({'date':match.date,
       'enemy_team':match.enemy_team,
       'is_end':match.is_end,
       'yes_count':yes_count,
       'no_count':no_count,
       'no_decision_count':no_decision_count,
       })
   
   return render(request, 'frequency.html', {'data':date_to_return})

@login_required
def training_vote(request):
   get_active_player = Player.objects.get(user=request.user)
   date_to_return = []
   training_days_names = []
   return render(request, 'training_vote.html', {
      'days_list':[str(i) for i in range(1,8)],
      'hour_list':[str(i) for i in range(9,22)],
      'accept_days':get_active_player.training_vote.split(" ")
      }
      )

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

def saveTrainingDaysButton(request,values):
   get_active_player = Player.objects.get(user=request.user)
   get_active_player.training_vote = values
   get_active_player.save()
   return redirect('../../')