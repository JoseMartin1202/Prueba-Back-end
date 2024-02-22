from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from apps.Material.models import Material
from apps.Material.serializers import \
    MaterialSerializer, \
    MaterialSerializerCrear, \
    MaterialSerializerString

from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

@api_view(['GET','POST'])
@parser_classes([MultiPartParser , JSONParser])
def material_api_view(request):
    # list
    if request.method == 'GET':
        material = Material.objects.all()
        material_serializer = MaterialSerializer(material,many=True)
        return Response( material_serializer.data, status=status.HTTP_200_OK )

    # Create
    elif request.method == 'POST':
        material_serializer = MaterialSerializerCrear(data=request.data)
        if material_serializer.is_valid():
            material_serializer.save()
            return Response( {'message':'¡Material creado correctamente!'}, status=status.HTTP_201_CREATED )
    
        return Response( material_serializer.errors, status=status.HTTP_400_BAD_REQUEST )

@api_view(['GET'])
@parser_classes([MultiPartParser , JSONParser])
def materiales_string_api_view(request):
    # list
    if request.method == 'GET':
        material = Material.objects.all()
        material_serializer = MaterialSerializer(material,many=True)
        return Response( material_serializer.data, status=status.HTTP_200_OK )

@api_view(['GET','PUT','DELETE'])
@parser_classes([MultiPartParser, JSONParser])
def material_detail_api_view(request, pk=None ):
    # Queryset
    material = Material.objects.filter( idMaterial = pk ).first()
    
    # Validacion
    if material:
        # Retrieve
        if request.method == 'GET':
            material_serializer =  MaterialSerializer(material)
            return Response( material_serializer.data, status=status.HTTP_200_OK )
        
        # Update
        elif request.method == 'PUT':
            material_serializer = MaterialSerializer(material, data = request.data)
            if material_serializer.is_valid():
                material_serializer.save()
                return Response( {'message':'¡Material actualizado correctamente!'}, status=status.HTTP_200_OK)
            return Response(material_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        # Delete
        elif request.method == 'DELETE':
            material = Material.objects.filter( idMaterial = pk ).first()
            try:
                material.delete()
                return Response(
                    {'message':'¡Material eliminado correctamente!'}, 
                    status=status.HTTP_200_OK
                )
            except Exception as e:
                return Response(
                    {'message':'¡No es posible eliminar un Material en uso!'}, 
                    status=status.HTTP_409_CONFLICT
                )

    return Response(
        {'message':'No se encontró el Material'}, 
        status=status.HTTP_400_BAD_REQUEST
    )
        