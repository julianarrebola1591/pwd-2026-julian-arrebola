from django.db import models

# Create your models here.

class Carrera(models.Model):
    nombre = models.CharField(max_length=128)

class Profesor(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    mostrar = models.CharField(max_length=256)

class Materia(models.Model):
    nombre = models.CharField(max_length=128)
    cant_alumnos = models.IntegerField()
    id_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

class Aula(models.Model):
    descripcion = models.CharField(max_length=128)
    ubicacion = models.CharField(max_length=128)
    cant_proyector = models.IntegerField(default=0)
    aforo = models.IntegerField(default=0)
    es_climatizada = models.BooleanField(default=False)

class Reserva_aula(models.Model):
    id_aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    fh_desde = models.DateTimeField()
    fh_hasta = models.DateTimeField()
    observacion = models.CharField(max_length=256, blank=True)

class Horario_materia(models.Model):
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    id_reserva = models.ForeignKey(Reserva_aula, on_delete=models.CASCADE)
    fh_desde = models.DateTimeField()
    fh_hasta = models.DateTimeField()