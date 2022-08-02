from django.shortcuts import render
from django.http import HttpResponse, request, response
from .models import MatchPlayer

# Create your views here.
def my_matches(request):

    return render(request, 'my_matches.html', {'MatchPlayer':MatchPlayer.objects.all()})
