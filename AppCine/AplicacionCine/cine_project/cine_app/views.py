from django.shortcuts import render
from .models import Pelicula

def home(request):
    return render(request, 'home.html')

def catalog(request):
    peliculas = Pelicula.objects.all()[:5]
    return render(request, 'catalog.html', {'peliculas': peliculas})

def contact(request):
    return render(request, 'contact.html')

