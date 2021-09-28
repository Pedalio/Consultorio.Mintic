from django.db import models

# Create your models here.
class Ciudades(models.Model):
    nombre=models.CharField(max_length=50)
    #codigo=models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.nombre

