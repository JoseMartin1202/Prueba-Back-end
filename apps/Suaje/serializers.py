from rest_framework import serializers
from apps.Suaje.models import Suaje

class SuajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suaje
        fields = '__all__'