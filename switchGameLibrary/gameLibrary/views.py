from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render
from .models import Game

# Create your views here.
def landing_page_view(request):
    games = Game.objects.all().order_by('release_date')

    return render(request, "gameLibrary/home.html", {"games": games})

def about_view(request):
    return render(request, "gameLibrary/about.html")

def detail_view(request, slug):
    try:
        game = Game.objects.get(slug=slug)
    except:
        raise Http404(f"{slug} was not found in the game list")

    return render(request, "gameLibrary/detail.html", {"game": game})