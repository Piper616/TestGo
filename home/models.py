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
    rut_administrador = models.CharField(unique=True, max_length=13)
    nombres = models.CharField(max_length=50)
    apellido_p = models.CharField(max_length=50)
    apellido_m = models.CharField(max_length=50)
    num_cel = models.BigIntegerField(unique=True)
    email_personal = models.CharField(unique=True, max_length=100)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    fec_nac = models.CharField(max_length=20, blank=True, null=True)
    email_empresa = models.CharField(max_length=50)
    contrase±a = models.CharField(unique=True, max_length=500)

    class Meta:
        managed = False
        db_table = 'administrador'


class AudAdmin(models.Model):
    id = models.BigIntegerField(primary_key=True)
    accion = models.CharField(max_length=200, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aud_admin'


class AudCargo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    accion = models.CharField(max_length=200, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aud_cargo'


class AudCasos(models.Model):
    id = models.BigIntegerField(primary_key=True)
    accion = models.CharField(max_length=200, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aud_casos'


class AudEvaluado(models.Model):
    id = models.BigIntegerField(primary_key=True)
    accion = models.CharField(max_length=200, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aud_evaluado'


class AudEvaluador(models.Model):
    id = models.BigIntegerField(primary_key=True)
    accion = models.CharField(max_length=200, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aud_evaluador'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cargo(models.Model):
    id_cargo = models.BigIntegerField(primary_key=True)
    detalle_cargo = models.CharField(unique=True, max_length=1000)

    class Meta:
        managed = False
        db_table = 'cargo'


class Casos(models.Model):
    id_caso = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion_caso = models.CharField(max_length=500)
    pdf = models.BinaryField(blank=True, null=True)
    foto = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'casos'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
