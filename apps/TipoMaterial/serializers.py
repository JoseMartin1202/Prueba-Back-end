from rest_framework import serializers
from apps.TipoMaterial.models import TipoMaterial

class TipoMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMaterial
        fields = '__all__'