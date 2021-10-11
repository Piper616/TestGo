from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect,Http404,JsonResponse
from django.shortcuts import render, redirect
from .models import (Administrador,
                         AuthGroup,
              AuthGroupPermissions,
                    AuthPermission,
                          AuthUser,
                    AuthUserGroups,
           AuthUserUserPermissions,
                             Cargo,
                             Casos,
                    DjangoAdminLog,
                 DjangoContentType,
                  DjangoMigrations,
                     DjangoSession,
                    EvaluacionCaso,
                          Evaluado,
                         Evaluador,
                           Persona,
                         Resultado)
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def inicio(request):
    if request.method == "POST":
        try:
         detalleUsuario=Evaluado.objects.get(email=request.POST['correo'], contraseña=request.POST['password'])
         print("usuario=", detalleUsuario)
         request.session['email']=detalleUsuario.email
         return render(request, 'home/index.html')
        except Evaluado.DoesNotExist as e:
            messages.success(request,'Nombre de usuario o contraseña no es correcto..!')
    return render(request, 'home/inicio.html')         


def seleccion(request):
    return render(request,'home/seleccion.html')

def index(request):
    return render(request,'home/index.html')

def caso1(request):
    return render(request, 'home/caso1.html')    

def video(request):
    return render(request,'home/video.html')

def foto(request):
    return render(request,'home/foto.html')

def cuestionario(request):
    return render(request,'home/cuestionario.html')

def final(request):
    return render(request, 'home/final.html')
