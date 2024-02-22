from rest_framework import serializers
 
from apps.Terminado.models import Terminado
 

class TerminadoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Terminado
        fields = '__all__'