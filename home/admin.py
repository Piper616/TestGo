from django.contrib import admin

from home.views import video
from .models import *
# Register your models here.

admin.site.register(Administrador)
admin.site.register(Cargo)
admin.site.register(Casos)
admin.site.register(EvaluacionCaso)
admin.site.register(Evaluado)
admin.site.register(Evaluador)
admin.site.register(Video)