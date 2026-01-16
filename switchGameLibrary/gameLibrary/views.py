from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.
def landing_page_view(request):
    return HttpResponse("<h1>Switch Game Library</h1><p>test</p>")