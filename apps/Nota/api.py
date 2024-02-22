from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, JSONParser
from apps.Nota.models import Nota
from apps.Nota.serializers import NotaSerializer

@api_view(['GET','POST'])
@parser_classes([MultiPartParser , JSONParser])
def nota_api_view(request):
    if(request.method == 'GET'):
        notas = Nota.objects.all()
        notas_serializer = NotaSerializer(notas, many=True)
        return Response(notas_serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        nota_serializer = NotaSerializer(data=request.data)
        if nota_serializer.is_valid():
            nota_serializer.save()
            return Response( {'message':'¡Nota creada correctamente!'}, status=status.HTTP_201_CREATED )
        return Response( nota_serializer.errors, status=status.HTTP_400_BAD_REQUEST )

@api_view(['GET','PUT','DELETE'])
@parser_classes([MultiPartParser, JSONParser])
def nota_detail_api_view(request, pk=None ):
    
    nota = Nota.objects.filter( idNota = pk ).first()
    
    if nota:

        if request.method == 'GET':
            nota_serializer =  NotaSerializer(nota)
            return Response( nota_serializer.data, status=status.HTTP_200_OK )
        if request.method == 'PUT':
            nota_serializer = NotaSerializer(nota, data = request.data)
            if nota_serializer.is_valid():
                nota_serializer.save()
                return Response( {'message':'¡Nota actualizada correctamente!'}, status=status.HTTP_200_OK)
            return Response(nota_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            try:
                nota.delete()
                return Response(
                    {'message':'¡Nota eliminada correctamente!'}, 
                    status=status.HTTP_200_OK
                )
            except Exception as e:
                return Response(
                    {'message':'¡No es posible eliminar una nota en uso!'}, 
                    status=status.HTTP_409_CONFLICT
                )
    
    return Response(
        {'message':'No se encontró la nota'}, 
        status=status.HTTP_400_BAD_REQUEST
    )