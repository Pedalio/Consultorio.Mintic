from django.db import models

# Create your models here.
class ciudades(models.Model):
    nombre=models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.nombre

