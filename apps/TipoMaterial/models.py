from django.db import models

# Create your models here.
class TipoMaterial(models.Model):
    idTipoMaterial = models.AutoField(primary_key=True,auto_created=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
 
    def __str__(self):
        return f'{self.nombre}'
