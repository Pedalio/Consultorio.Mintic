from django.db import models

# Create your models here.
class tipoCita(models.Model):
    tipo=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.tipo
