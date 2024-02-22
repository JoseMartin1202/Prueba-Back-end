from rest_framework import serializers
 
from apps.CategoriaMaterial.models import CategoriaMaterial
 

class CategoriaMaterialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = CategoriaMaterial
        fields = '__all__'