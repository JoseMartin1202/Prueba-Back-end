from django.db import models
from apps.Prensa.models import Prensa
from apps.TipoImpresion.models import TipoImpresion

class PrecioPrensa(models.Model):
    idPrecioPrensa = models.AutoField(auto_created=True, primary_key=True)
    prensa = models.ForeignKey(Prensa, on_delete=models.PROTECT)
    tipoImpresion = models.ForeignKey(TipoImpresion, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.prensa.nombre} - {self.tipoImpresion.nombre} - {self.cantidad} - ${self.precio}'