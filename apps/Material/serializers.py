from rest_framework import serializers
from apps.Material.models import Material

class MaterialSerializerString(serializers.ModelSerializer):
    material = serializers.SerializerMethodField()

    class Meta:
        model = Material
        fields = ['idMaterial', 'material']

    def get_material(self, obj):
        return str(obj)

class MaterialSerializerCrear( serializers.ModelSerializer ):
    class Meta:
        model = Material
        fields = '__all__'

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'
        depth = 1   # This will include the related model's fields