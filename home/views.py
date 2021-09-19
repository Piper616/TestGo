from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,'home/inicio.html')