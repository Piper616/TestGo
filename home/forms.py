from django import forms
from .models import (Administrador,
                             Cargo,
                             Casos,
                    EvaluacionCaso,
                          Evaluado,
                         Evaluador,
                         Resultado)

class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ['id_admin','rut_administrador','nombres','apellido_p','apellido_m','num_cel','email_personal','direccion','fec_nac','email_empresa','contraseña','cargo_id_cargo']

class CargosForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['id_cargo','detalle_cargo']

class CasosForm(forms.ModelForm):
    class Meta:
        model = Casos
        fields = ['id_caso','nombre','descripcion_caso']

class evaluacion_casoForm(forms.ModelForm):
    class Meta:
        model = EvaluacionCaso
        fields = ['id_evcaso','casos_id_caso','administrador_id_admin','evaluado_id_evaluado','fecha_asignacion','fecha_realizacion']

class evaluadoForm(forms.ModelForm):
    class Meta:
        model = Evaluado
        fields = ['id_evaluado','rut_evaluado','nombres','apellido_p','apellido_m','num_cel','email_personal','direccion','fec_nac','empresa','email_empresa','contraseña','cargo_id_cargo']

class evaluadorForm(forms.ModelForm):
    class Meta:
        model = Evaluador
        fields = ['id_evaluador','rut_evaluador','nombres','apellido_p','apellido_m','num_cel','email_personal','direccion','fec_nac','administrador_id_admin','email_empresa','contraseña','cargo_id_cargo']

class ResultadoForm(forms.ModelForm):
    class Meta:
        model = Resultado
        fields = ['id_resultado','descripcion','evaluador_id_evaluador','evaluacion_caso_id_evcaso','fecha_revision']
