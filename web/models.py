from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    # Imagen
    # Color
    # Genero
    tallas = models.CharField(max_length=12)
    

    def __str__(self):
        return self.nombre