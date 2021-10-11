from django.urls import path, re_path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    #------Usuario-------
    path('', views.inicio, name='login'),
    path('index/', views.index, name='index'),
    path('caso1/', views.caso1, name="caso1"),
    path('seleccion/', views.seleccion, name='seleccion'),
    path('video/', views.video, name='video'),
    path('foto/', views.foto, name='foto'),
    path('cuestionario/', views.cuestionario, name='cuestionario'),
    path('final/', views.final, name='final'),


]
