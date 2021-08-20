from django.shortcuts import render
from Task2App.models import Movie,Song

# Create your views here.

def Index(request):
    return render(request, 'index.html')

def Movies(request):
    return render(request, 'movies.html')

def Songs(request):
    return render(request, 'songs.html')