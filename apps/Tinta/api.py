from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, JSONParser
from apps.Tinta.models import Tinta
from apps.Tinta.serializers import TintaSerializer

@api_view(['GET','POST'])
@parser_classes([MultiPartParser , JSONParser])
def tinta_api_view(request):
    if request.method == 'POST':
        tnta_serializado = TintaSerializer(data=request.data)
        if tnta_serializado.is_valid():
            tnta_serializado.save()
            all = TintaSerializer( Tinta.objects.all(), many=True )
            return Response({
                'message':'¡Tinta creada correctamente!',
                'newOptsList':all.data,
                'newOptId': tnta_serializado.data.get('idTinta')}, 
                status=status.HTTP_201_CREATED 
            )
    if(request.method == 'GET'):
        tntas = Tinta.objects.all()
        tntas_serializado = TintaSerializer(tntas,many=True)
        return Response( tntas_serializado.data, status=status.HTTP_200_OK )
        

@api_view(['GET','PUT','DELETE'])
@parser_classes([MultiPartParser, JSONParser])
def tinta_detail_api_view(request, pk=None ):
    if request.method == 'GET':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        tnta = Tinta.objects.filter( idTinta = pk ).first()
        try:
            tnta.delete()
            # return the new Tinta records
            tntas = Tinta.objects.all()
            tntas_serializado = TintaSerializer(tntas,many=True) 
            return Response({
                'message':'¡Tinta eliminada correctamente!',
                'newOptsList':tntas_serializado.data}, 
                status=status.HTTP_200_OK 
            )
        except:
            return Response({
                'message':'¡No es posible eliminar una tinta en uso!'}, 
                status=status.HTTP_409_CONFLICT 
            )