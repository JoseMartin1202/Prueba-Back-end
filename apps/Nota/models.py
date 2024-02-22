from django.db import models

class Nota(models.Model):
    idNota = models.AutoField(auto_created=True, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    alto=models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    ancho=models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    
    def __str__(self):
        return f'{self.nombre} - {self.alto}x{self.ancho}'