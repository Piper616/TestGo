from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Administrador, Cargo, Casos, DjangoContentType, DjangoMigrations, EvaluacionCaso, Evaluado, Evaluador, Persona, Resultado  
import random
from random import randint

# Create your views here.
def inicio(request):
    return render(request,'home/inicio.html')

def seleccion(request):
    return render(request,'home/seleccion.html')

def video(request):
    return render(request,'home/video.html') 

def foto(request):
    return render(request,'home/foto.html')

def cuestionario(request):
    return render(request,'home/cuestionario.html')    

def final(request):
    return render(request, 'home/final.html')     

def fotoaleatoria(request):
    fotoa = ['/static/home/img/foto1.jpg', '/static/home/img/foto2.jpg']
    random.sample(fotoa, 1)
    return render(request, 'home/foto.html')