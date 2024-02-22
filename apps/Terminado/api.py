from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, JSONParser
from apps.Terminado.models import Terminado
from apps.Terminado.serializers import TerminadoSerializer

@api_view(['GET','POST'])
@parser_classes([MultiPartParser , JSONParser])
def terminado_api_view(request):
    if(request.method == 'GET'):
        terminados = Terminado.objects.all()
        terminados_serializer = TerminadoSerializer(terminados, many=True)
        return Response(terminados_serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        terminado_serializer = TerminadoSerializer(data=request.data)
        if terminado_serializer.is_valid():
            terminado_serializer.save()
            return Response( {'message':'¡Terminado creado correctamente!'}, status=status.HTTP_201_CREATED )
        return Response( terminado_serializer.errors, status=status.HTTP_400_BAD_REQUEST )

@api_view(['GET','PUT','DELETE'])
@parser_classes([MultiPartParser, JSONParser])
def terminado_detail_api_view(request, pk=None ):
    
    terminado = Terminado.objects.filter( idTerminado = pk ).first()
    
    if request.method == 'GET':
        terminado_serializer =  TerminadoSerializer(terminado)
        return Response( terminado_serializer.data, status=status.HTTP_200_OK )
    if request.method == 'PUT':
        terminado_serializer = TerminadoSerializer(terminado, data = request.data)
        if terminado_serializer.is_valid():
            terminado_serializer.save()
            return Response( {'message':'¡Terminado actualizado correctamente!'}, status=status.HTTP_200_OK)
        return Response(terminado_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        try:
            terminado.delete()
            return Response(
                {'message':'¡Terminado eliminado correctamente!'}, 
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {'message':'¡No es posible eliminar un terminado en uso!'}, 
                status=status.HTTP_409_CONFLICT
            )