from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

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