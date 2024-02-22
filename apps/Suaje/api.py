from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from apps.Suaje.models import Suaje
from apps.Suaje.serializers import SuajeSerializer
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

@api_view(['GET','POST'])
@parser_classes([MultiPartParser , JSONParser])
def suaje_api_view(request):
    # list
    if request.method == 'GET':
        suaje = Suaje.objects.all()
        suaje_serializer = SuajeSerializer(suaje,many=True)
        return Response( suaje_serializer.data, status=status.HTTP_200_OK )

    # Create
    elif request.method == 'POST':
        suaje_serializer = SuajeSerializer(data=request.data)
        if suaje_serializer.is_valid():
            suaje_serializer.save()
            return Response( {'message':'¡Suaje creado correctamente!'}, status=status.HTTP_201_CREATED )
        return Response( suaje_serializer.errors, status=status.HTTP_400_BAD_REQUEST )

@api_view(['GET','PUT','DELETE'])
@parser_classes([MultiPartParser, JSONParser])
def suaje_detail_api_view(request, pk=None ):
    # Queryset
    suaje = Suaje.objects.filter( idSuaje = pk ).first()
    
    # Validacion
    if suaje:
        # Retrieve
        if request.method == 'GET':
            suaje_serializer =  SuajeSerializer(suaje)
            return Response( suaje_serializer.data, status=status.HTTP_200_OK )
        
        # Update
        elif request.method == 'PUT':
            suaje_serializer = SuajeSerializer(suaje, data = request.data)
            if suaje_serializer.is_valid():
                suaje_serializer.save()
                return Response( {'message':'¡Suaje actualizado correctamente!'}, status=status.HTTP_200_OK)
            return Response(suaje_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        # Delete
        elif request.method == 'DELETE':
            suaje = Suaje.objects.filter( idSuaje = pk ).first()
            try:
                suaje.delete()
                return Response(
                    {'message':'¡Suaje eliminado correctamente!'}, 
                    status=status.HTTP_200_OK
                )
            except Exception as e:
                return Response(
                    {'message':'¡No es posible eliminar un suaje en uso!'}, 
                    status=status.HTTP_409_CONFLICT
                )

    return Response(
        {'message':'No se encontró el suaje'}, 
        status=status.HTTP_400_BAD_REQUEST
    )
        