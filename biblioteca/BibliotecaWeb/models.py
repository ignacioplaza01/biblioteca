from django.db import models

# Create your models here.

class Libros(models.Model):
    Titulo = models.CharField(max_length=20)
    Autor = models.CharField(max_length=20)
    Genero = models.CharField(max_length=30)
    Resumen = models.CharField(max_length=500)
    Calificacion = models.CharField(max_length=10)
    Img = models.ImageField(upload_to="img_libros/", null=False, blank=False)