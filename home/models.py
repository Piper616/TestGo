# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrador(models.Model):
    id_admin = models.BigIntegerField(primary_key=True)
    rut_administrador = models.CharField(max_length=13)
    nombres = models.CharField(max_length=50)
    apellido_p = models.CharField(max_length=50)
    apellido_m = models.CharField(max_length=50)
    num_cel = models.BigIntegerField()
    email_personal = models.CharField(max_length=25)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    fec_nac = models.CharField(max_length=20, blank=True, null=True)
    email_empresa = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    cargo_id_cargo = models.ForeignKey('Cargo', models.DO_NOTHING, db_column='cargo_id_cargo')

    class Meta:
        managed = False
        db_table = 'administrador'


class Cargo(models.Model):
    id_cargo = models.BigIntegerField(primary_key=True)
    detalle_cargo = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'cargo'


class Casos(models.Model):
    id_caso = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion_caso = models.CharField(max_length=500)
    foto = models.BinaryField(blank=True, null=True)
    video = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'casos'


class EvaluacionCaso(models.Model):
    id_evcaso = models.BigIntegerField(primary_key=True)
    casos_id_caso = models.ForeignKey(Casos, models.DO_NOTHING, db_column='casos_id_caso')
    administrador_id_admin = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='administrador_id_admin')
    evaluado_id_evaluado = models.ForeignKey('Evaluado', models.DO_NOTHING, db_column='evaluado_id_evaluado')
    fecha_asignacion = models.DateField()
    fecha_realizacion = models.DateField()
    video_respuesta = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluacion_caso'


class Evaluado(models.Model):
    id_evaluado = models.BigIntegerField(primary_key=True)
    rut_evaluado = models.CharField(max_length=13)
    nombres = models.CharField(max_length=50)
    apellido_p = models.CharField(max_length=50)
    apellido_m = models.CharField(max_length=50)
    num_cel = models.BigIntegerField()
    email_personal = models.CharField(max_length=25)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    fec_nac = models.CharField(max_length=20, blank=True, null=True)
    empresa = models.CharField(max_length=50)
    email_empresa = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    cargo_id_cargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='cargo_id_cargo')

    class Meta:
        managed = False
        db_table = 'evaluado'


class Evaluador(models.Model):
    id_evaluador = models.BigIntegerField(primary_key=True)
    rut_evaluador = models.CharField(max_length=13)
    nombres = models.CharField(max_length=50)
    apellido_p = models.CharField(max_length=50)
    apellido_m = models.CharField(max_length=50)
    num_cel = models.BigIntegerField()
    email_personal = models.CharField(max_length=25)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    fec_nac = models.CharField(max_length=20, blank=True, null=True)
    administrador_id_admin = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='administrador_id_admin')
    email_empresa = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    cargo_id_cargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='cargo_id_cargo')

    class Meta:
        managed = False
        db_table = 'evaluador'


class Resultado(models.Model):
    id_resultado = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=500)
    evaluador_id_evaluador = models.ForeignKey(Evaluador, models.DO_NOTHING, db_column='evaluador_id_evaluador')
    evaluacion_caso_id_evcaso = models.ForeignKey(EvaluacionCaso, models.DO_NOTHING, db_column='evaluacion_caso_id_evcaso')
    fecha_revision = models.DateField()

    class Meta:
        managed = False
        db_table = 'resultado'