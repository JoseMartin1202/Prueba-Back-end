from rest_framework import serializers
 
from apps.PrecioPrensa.models import PrecioPrensa
from apps.Tinta.serializers import TintaSerializer
from apps.Prensa.serializers import PrensaSerializer
from apps.TipoImpresion.serializers import TipoImpresionSerializer

class PrecioPrensaSerializer(serializers.ModelSerializer):
    prensa = PrensaSerializer()
    tipoImpresion = TipoImpresionSerializer()
    class Meta:
        model = PrecioPrensa
        fields = '__all__'