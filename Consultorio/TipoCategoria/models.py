from django.db import models

# Create your models here.
class TipoCategoria(models.Model):
    tipoCategoria=models.CharField(max_length=20)
    valorCategoria=models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.tipoCategoria + " - " + str(self.valorCategoria)
