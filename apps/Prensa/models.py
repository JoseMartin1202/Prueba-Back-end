from django.db import models

class Prensa(models.Model):
    idPrensa = models.AutoField(auto_created=True, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    
    def __str__(self):
        return self.nombre