from django.db import models

class Terminado(models.Model):
    idTerminado = models.AutoField(auto_created=True, primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    cantidad = models.IntegerField(blank=False, null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    tipoTrabajo = models.CharField(
        max_length=20,
        choices=[
            ('Etiquetas', 'Etiquetas'),
            ('Notas', 'Notas')
        ],
        default='Etiquetas'
    )

    def __str__(self):
        return f'{self.nombre} - {self.tipoTrabajo}'