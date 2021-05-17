from django.db import models

# Create your models here.

class Tarea(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    dia = models.CharField(max_length=20)