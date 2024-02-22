from rest_framework import serializers
 
from apps.TipoImpresion.models import TipoImpresion
 

class TipoImpresionSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = TipoImpresion
        fields = '__all__'
