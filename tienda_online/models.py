from django.db import models
from django.utils import timezone


class Categorias(models.Model):
    nombre = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.nombre


class Productos(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.CharField(max_length=1000)
    precio = models.IntegerField()
    image = models.ImageField(default='vacio.png')
    timestamp = models.DateTimeField(default=timezone.now)
    categoria = models.ForeignKey(
        Categorias, on_delete=models.CASCADE, related_name='productos', null=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'El producto es {self.titulo}'
