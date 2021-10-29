from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect,Http404,JsonResponse
from django.shortcuts import render, redirect
from .models import (Administrador,
                             Cargo,
                             Casos,
                    EvaluacionCaso,
                          Evaluado,
                         Evaluador,
                         Resultado)
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError, models
from django.urls import reverse
from django.contrib import messages
from django.db import connection
from .forms import SubirvideoForm

# Create your views here.
def inicio(request):
    if request.method == "POST":
        try:
         detalleUsuario=Evaluado.objects.get(email_empresa=request.POST['correo'], contraseña=request.POST['password'])
         print("usuario=", detalleUsuario)
         request.session['email']=detalleUsuario.email_empresa
         return render(request, 'home/index.html')
        except Evaluado.DoesNotExist as e:
            messages.success(request,'Nombre de usuario o contraseña no es correcto..!')
    return render(request, 'home/inicio.html')

def loginA(request):
    if request.method == "POST":
        try:
         detalleAdmin=Administrador.objects.get(email_empresa=request.POST['correoA'], contraseña=request.POST['passwordA'])
         print("usuario=", detalleAdmin)
         request.session['email']=detalleAdmin.email_empresa
         return render(request, 'home/vistaA.html')
        except Administrador.DoesNotExist as e:
            messages.success(request,'Nombre de usuario o contraseña no es correcto..!')
    return render(request, 'home/inicioA.html')

def loginE(request):
    if request.method == "POST":
        try:
         detalleEvaluador=Evaluador.objects.get(email_empresa=request.POST['correoE'], contraseña=request.POST['passwordE'])
         print("usuario=", detalleEvaluador)
         request.session['email']=detalleEvaluador.email_empresa
         return render(request, 'home/vistaE.html')
        except Evaluador.DoesNotExist as e:
            messages.success(request,'Nombre de usuario o contraseña no es correcto..!')
    return render(request, 'home/inicioE.html')    

def subirvideo(request):
    if request.method == 'POST':
        form = SubirvideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = "Video uploaded succesfully!"
    else:
        form = SubirvideoForm()

    return render('home/caso1.html', locals(), context_instance=render(request))

def seleccion(request):
    return render(request,'home/seleccion.html')

def vistaA(request):
    return render(request,'home/vistaA.html')

def index(request):
    return render(request,'home/index.html')

def caso1(request):
    return render(request, 'home/caso1.html')

def caso2(request):
    return render(request, "home/caso2.html")

def perfil(request):
    return render(request, "home/perfil.html")

def vistaE(request):
    return render (request, "home/vistaE.html")

def video(request):
    return render(request,'home/video.html')

def foto(request):
    return render(request,'home/foto.html')

def cuestionario(request):
    return render(request,'home/cuestionario.html')

def final(request):
    return render(request, 'home/final.html')

def listadopruf(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor

    cursor.callproc("CASOS_UPDATE", [out_cur])
