from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.
def landing_page_view(request):
    return render(request, "gameLibrary/home.html")

def about_view(request):
    return render(request, "gameLibrary/about.html")