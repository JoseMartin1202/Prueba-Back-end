from django.db import models

# Create your models here.

class Suaje(models.Model):
    idSuaje = models.AutoField(primary_key=True,auto_created=True)
    numero = models.IntegerField(unique=True, null=False, blank=False)
    alto=models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    ancho=models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    numeroCortes=models.IntegerField(null=False, blank=False)
    precio=models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False,default=80)
    cantidad=models.IntegerField(null=False, blank=False,default=1000)
    
    def __str__(self):
        return f'{self.numero} {self.ancho}cm x {self.alto}cm {self.numeroCortes} cortes ${self.precio} '
    


