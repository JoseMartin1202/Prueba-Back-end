from rest_framework import serializers
 
from apps.Tinta.models import Tinta
 

class TintaSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tinta
        fields = '__all__'