from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from apps.TipoMaterial.models import TipoMaterial
from apps.TipoMaterial.serializers import TipoMaterialSerializer
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

@api_view(['GET','POST'])
@parser_classes([MultiPartParser , JSONParser])
def tipomaterial_api_view(request):
    # list
    if request.method == 'GET':
        tipoMaterial = TipoMaterial.objects.all()
        tipoMaterial_serializado = TipoMaterialSerializer(tipoMaterial,many=True)
        return Response( tipoMaterial_serializado.data, status=status.HTTP_200_OK )

    # Create
    elif request.method == 'POST':
        tipoMaterial_serializado = TipoMaterialSerializer(data=request.data)
        if tipoMaterial_serializado.is_valid():
            tipoMaterial_serializado.save()
            all = TipoMaterialSerializer( TipoMaterial.objects.all(), many=True )
            return Response( {
                'message':'¡Tipo de material creado correctamente!',
                'newOptsList':all.data,
                'newOptId': tipoMaterial_serializado.data.get('idTipoMaterial')
                }, status=status.HTTP_201_CREATED )
        return Response( tipoMaterial_serializado.errors, status=status.HTTP_400_BAD_REQUEST )

@api_view(['GET','PUT','DELETE'])
@parser_classes([MultiPartParser, JSONParser])
def tipomaterial_detail_api_view(request, pk=None ):
    # Queryset
    tipoMaterial = TipoMaterial.objects.filter( idTipoMaterial = pk ).first()
    
    # Validacion
    if tipoMaterial:
        # Retrieve
        if request.method == 'GET':
            tipoMaterial_serializado =  TipoMaterialSerializer(tipoMaterial)
            return Response( tipoMaterial_serializado.data, status=status.HTTP_200_OK )
        
        # Update
        elif request.method == 'PUT':
            tipoMaterial_serializado = TipoMaterialSerializer(tipoMaterial, data = request.data)
            if tipoMaterial_serializado.is_valid():
                tipoMaterial_serializado.save()
                return Response( {'message':'¡Tipo de Material actualizado correctamente!'}, status=status.HTTP_200_OK)
            return Response(tipoMaterial_serializado.errors, status = status.HTTP_400_BAD_REQUEST)
        
        # Delete
        elif request.method == 'DELETE':
            material = TipoMaterial.objects.filter( idTipoMaterial = pk ).first()
            try:
                material.delete()
                # return the new TipoMaterial records
                tipoMaterial = TipoMaterial.objects.all()
                tipoMaterial_serializado = TipoMaterialSerializer(tipoMaterial,many=True) 
                return Response({
                    'message':'¡Tipo de material eliminado correctamente!',
                    'newOptsList': tipoMaterial_serializado.data
                    }, 
                    status=status.HTTP_200_OK
                )
            except Exception as e:
                print(e)
                return Response(
                    {'message':'¡No es posible eliminar un tipo de material en uso!'}, 
                    status=status.HTTP_409_CONFLICT
                )

    return Response(
        {'message':'No se encontró el tipo de material'}, 
        status=status.HTTP_400_BAD_REQUEST
    )
        