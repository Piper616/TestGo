from django.contrib import admin
from .models import (Administrador,
                             Cargo,
                             Casos,
                    EvaluacionCaso,
                          Evaluado,
                         Evaluador)
# Register your models here.

admin.site.register(Administrador)
admin.site.register(Cargo)
admin.site.register(Casos)
admin.site.register(EvaluacionCaso)
admin.site.register(Evaluado)
admin.site.register(Evaluador)