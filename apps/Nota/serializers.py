from rest_framework import serializers
 
from apps.Nota.models import Nota
 

class NotaSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Nota
        fields = '__all__'