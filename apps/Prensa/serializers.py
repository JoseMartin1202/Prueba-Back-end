from rest_framework import serializers
 
from apps.Prensa.models import Prensa
 

class PrensaSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Prensa
        fields = '__all__'