from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, JSONParser
from apps.Prensa.models import Prensa
from apps.Prensa.serializers import PrensaSerializer
from apps.TipoImpresion.models import TipoImpresion
from apps.PrecioPrensa.models import PrecioPrensa
from django.db import transaction

@api_view(['GET','POST'])
@parser_classes([MultiPartParser , JSONParser])
def prensa_api_view(request):
    
    if request.method == 'GET':
        prensas = Prensa.objects.all()
        prensas_serializado = PrensaSerializer(prensas,many=True)
        return Response( prensas_serializado.data, status=status.HTTP_200_OK )
    
    if request.method == 'POST':
        try:
            with transaction.atomic():
                prensa = Prensa.objects.create(
                    nombre = request.data.get('prensa')
                )
                precios = [
                    PrecioPrensa(
                        prensa = prensa,
                        tipoImpresion = TipoImpresion.objects.filter( idTipoImpresion = precio.get('tipoImpresion') ).first(),
                        cantidad = precio.get('cantidad'),
                        precio = precio.get('precio')
                    )
                    for precio in request.data.get('precios')
                ]

                PrecioPrensa.objects.bulk_create(precios)
                return Response({'message':'Precios creados correctamente!'},status=status.HTTP_201_CREATED)
            
        except Exception as e:
            print(e)
            return Response({'message':'No es posible crear los precios!'},status=status.HTTP_409_CONFLICT)

@api_view(['GET','PUT','DELETE'])
@parser_classes([MultiPartParser, JSONParser])
def prensa_detail_api_view(request, pk=None ):
    if request.method == 'PUT':
        
        prensa = Prensa.objects.filter( idPrensa = pk ).first()
        cambios = request.data.get('cambiosPrecios')
        nuevos = request.data.get('nuevosPrecios')

        try:
            with transaction.atomic():
                prensa.nombre = request.data.get('prensa')
                prensa.save()

                for cambio in cambios:
                    precio = PrecioPrensa.objects.filter( idPrecioPrensa = cambio.get('idPrecioPrensa') ).first()
                    precio.tipoImpresion = TipoImpresion.objects.filter( idTipoImpresion = cambio.get('tipoImpresion') ).first()
                    precio.cantidad = cambio.get('cantidad')
                    precio.precio = cambio.get('precio')
                    precio.save()
                for nuevo in nuevos:
                    precio = PrecioPrensa(
                        prensa = prensa,
                        tipoImpresion = TipoImpresion.objects.filter( idTipoImpresion = nuevo.get('tipoImpresion') ).first(),
                        cantidad = nuevo.get('cantidad'),
                        precio = nuevo.get('precio')
                    )
                    precio.save()
                
                return Response({'message':'Precios actualizados correctamente!'},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'message':'No es posible actualizar los precios!'},status=status.HTTP_409_CONFLICT)

@api_view(['GET','POST'])
@parser_classes([MultiPartParser , JSONParser])
def prensa_fi_api_view(request):
    if request.method == 'POST':
        prensa_serializado = PrensaSerializer(data=request.data)
        if prensa_serializado.is_valid():
            prensa_serializado.save()
            all = PrensaSerializer( Prensa.objects.all(), many=True )
            return Response({
                'message':'¡Prensa creada correctamente!',
                'newOptsList':all.data,
                'newOptId': prensa_serializado.data.get('idPrensa')}, 
                status=status.HTTP_201_CREATED 
            )        
    if(request.method == 'GET'):
        prensas = Prensa.objects.all()
        prensas_serializado = PrensaSerializer(prensas,many=True)
        return Response( prensas_serializado.data, status=status.HTTP_200_OK )

@api_view(['GET','PUT','DELETE'])
@parser_classes([MultiPartParser, JSONParser])
def prensa_fi_detail_api_view(request, pk=None ):
    if request.method == 'GET':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        prensa = Prensa.objects.filter( idPrensa = pk ).first()
        try:
            prensa.delete()
            # return the new Prensa records
            prensas = Prensa.objects.all()
            prensas_serializado = PrensaSerializer(prensas,many=True) 
            return Response({
                'message':'¡Prensa eliminada correctamente!',
                'newOptsList':prensas_serializado.data}, 
                status=status.HTTP_200_OK 
            )
        except:
            return Response({
                'message':'¡No es posible eliminar una prensa en uso!'}, 
                status=status.HTTP_409_CONFLICT 
            )
        
