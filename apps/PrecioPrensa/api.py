from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, JSONParser
from apps.PrecioPrensa.models import PrecioPrensa
from apps.PrecioPrensa.serializers import PrecioPrensaSerializer
from apps.TipoImpresion.models import TipoImpresion
from apps.TipoImpresion.serializers import TipoImpresionSerializer
from apps.Prensa.models import Prensa
from apps.Prensa.serializers import PrensaSerializer

@api_view(['GET','POST'])
@parser_classes([MultiPartParser , JSONParser])
def precioPrensa_api_view(request):
    if request.method == 'POST':
        pass
    if(request.method == 'GET'):
        precios = PrecioPrensa.objects.all()
        precios_serializado = PrecioPrensaSerializer(precios,many=True)
        return Response( precios_serializado.data, status=status.HTTP_200_OK )

@api_view(['GET','PUT','DELETE'])
@parser_classes([MultiPartParser, JSONParser])
def precioPrensa_detail_api_view(request, pk=None ):
    if request.method == 'GET':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        prcio_prsa = PrecioPrensa.objects.filter( idPrecioPrensa = pk ).first()
        prcio_prsa.delete()
        return Response({'message':'Precio eliminado correctamente!'},status=status.HTTP_200_OK)

@api_view(['GET'])
@parser_classes([MultiPartParser, JSONParser])
def preciosPrensa_tipoImpresion_api_view(request, pk=None ):
    # Obtenemos los precios de un tipo de impresion
    if request.method == 'GET':
        precios = PrecioPrensa.objects.filter( tipoImpresion = pk )
        precios_serializado = PrecioPrensaSerializer(precios,many=True)

        tpo_imp = TipoImpresion.objects.filter( idTipoImpresion = pk ).first()
        tpo_imp_serializado = TipoImpresionSerializer(tpo_imp)
        return Response( {
            'tipoImpresion':tpo_imp_serializado.data.get('nombre'), 
            'precios':precios_serializado.data}, 
            status=status.HTTP_200_OK )
    
@api_view(['GET'])
@parser_classes([MultiPartParser, JSONParser])
def preciosPrensa_prensa_api_view(request, pk=None ):
    # Obtenemos los precios de una prensa
    if request.method == 'GET':
        precios = PrecioPrensa.objects.filter( prensa = pk )
        precios_serializado = PrecioPrensaSerializer(precios,many=True)

        prensa = Prensa.objects.filter( idPrensa = pk ).first()
        prensa_serializado = PrensaSerializer(prensa)
        return Response( {
            'prensa':prensa_serializado.data.get('nombre'),
            'precios':precios_serializado.data
        }, status=status.HTTP_200_OK )