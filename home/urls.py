from django.urls import path, re_path

from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    
]