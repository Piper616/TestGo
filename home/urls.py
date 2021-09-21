from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('seleccion/', views.seleccion, name='seleccion'),
    
]