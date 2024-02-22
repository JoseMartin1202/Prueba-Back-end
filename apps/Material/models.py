from django.db import models
from apps.TipoMaterial.models import TipoMaterial
from apps.CategoriaMaterial.models import CategoriaMaterial

# Create your models here.
class Material(models.Model):
    
    idMaterial = models.AutoField(primary_key=True,auto_created=True)
    categoria = models.ForeignKey(CategoriaMaterial, on_delete=models.PROTECT, null=False, blank=False)
    tipoMaterial = models.ForeignKey(TipoMaterial, on_delete=models.PROTECT, null=False, blank=False)
    alto = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    ancho = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    gramaje = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    grosor=models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    stock = models.IntegerField(null=False, blank=False)
    otros = models.CharField(max_length=100, null=True, blank=True)
    alturaGuillotina = models.IntegerField(null=False, blank=False, default=100)
    
    def __str__(self):
        # Format gramaje, grosor, and color to handle None values with tabulation
        gramaje_str = f'{self.gramaje}gr' if self.gramaje is not None else ''
        grosor_str = self.grosor if self.grosor else ''
        color_str = self.color if self.color else ''

        # Using f-string with consistent spacing or tabulation
        return f'{self.categoria.nombre}\t{self.tipoMaterial.nombre}\t{self.alto}cm x {self.ancho}cm\t{gramaje_str}\t{grosor_str}\t{color_str}\t${self.precio}' 
