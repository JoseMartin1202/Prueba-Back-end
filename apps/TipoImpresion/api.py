from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, JSONParser
from apps.TipoImpresion.models import TipoImpresion
from apps.TipoImpresion.serializers import TipoImpresionSerializer
from apps.PrecioPrensa.models import PrecioPrensa
from apps.Tinta.models import Tinta
from apps.Prensa.models import Prensa
from django.db import transaction

@api_view(['GET','POST'])
@parser_classes([MultiPartParser , JSONParser])
def tipoImpresion_api_view(request):
    if request.method == 'POST':
        try:
            tpoImp = request.data.get('tipoImpresion')
            tipoImpresion = TipoImpresion.objects.create(
                nombre = tpoImp
            )
            
            precios = [
                PrecioPrensa(
                prensa = Prensa.objects.filter( idPrensa = precio.get('prensa') ).first(),
                precioColor = precio.get('precioColor'),
                cantidad = precio.get('cantidad'),
                precioCantidad = precio.get('precioCantidad'),
                tinta = Tinta.objects.filter( idTinta = precio.get('tinta') ).first(),
                tipoImpresion = tipoImpresion
                )
                for precio in request.data.get('precios')
            ]

            PrecioPrensa.objects.bulk_create(precios)
            return Response({'message':'Precios creados correctamente!'},status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({'message':'No es posible crear los precios!'},status=status.HTTP_409_CONFLICT)

    if(request.method == 'GET'):
        tpoImp = TipoImpresion.objects.all()
        tpoImp_serializado = TipoImpresionSerializer(tpoImp,many=True)
        return Response( tpoImp_serializado.data, status=status.HTTP_200_OK )

@transaction.atomic
@api_view(['GET','PUT','DELETE'])
@parser_classes([MultiPartParser, JSONParser])
def tipoImpresion_detail_api_view(request, pk=None ):
    if request.method == 'GET':
        pass
    if request.method == 'PUT':
        
        tpo_Imp = TipoImpresion.objects.filter( idTipoImpresion = pk ).first()
        nuevo_nombre = request.data.get('tipoImpresion')
        cambios = request.data.get('cambiosPrecios')
        nuevos = request.data.get('nuevosPrecios')

        try:
            with transaction.atomic():
                tpo_Imp.nombre = nuevo_nombre
                tpo_Imp.save()
                for cambio in cambios:
                    precio = PrecioPrensa.objects.filter( idPrecioPrensa = cambio.get('idPrecioPrensa') ).first()
                    precio.precioColor = cambio.get('precioColor')
                    precio.cantidad = cambio.get('cantidad')
                    precio.precioCantidad = cambio.get('precioCantidad')
                    precio.tinta = Tinta.objects.filter( idTinta = cambio.get('tinta') ).first()
                    precio.prensa = Prensa.objects.filter( idPrensa = cambio.get('prensa') ).first()
                    precio.save()
                for nuevo in nuevos:
                    precio = PrecioPrensa(
                        prensa = Prensa.objects.filter( idPrensa = nuevo.get('prensa') ).first(),
                        precioColor = nuevo.get('precioColor'),
                        cantidad = nuevo.get('cantidad'),
                        precioCantidad = nuevo.get('precioCantidad'),
                        tinta = Tinta.objects.filter( idTinta = nuevo.get('tinta') ).first(),
                        tipoImpresion = tpo_Imp
                    )
                    precio.save()
                return Response({'message':'Precios actualizados correctamente!'},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'message':'No es posible actualizar los precios!'},status=status.HTTP_409_CONFLICT)
        
    if request.method == 'DELETE':
        tpo_Imp = TipoImpresion.objects.filter( idTipoImpresion = pk ).first()
        try:
            tpo_Imp.delete()
            # return the new TipoImpresion records
            tpoImp = TipoImpresion.objects.all()
            tpoImp_serializado = TipoImpresionSerializer(tpoImp,many=True) 
            return Response({
                'message':'¡Tipo de impresion eliminado correctamente!',
                'newOptsList':tpoImp_serializado.data}, 
                status=status.HTTP_200_OK 
            )
        except:
            return Response({
                'message':'¡No es posible eliminar un tipo de impresion en uso!'}, 
                status=status.HTTP_409_CONFLICT 
            )
   

@api_view(['GET','POST'])
@parser_classes([MultiPartParser , JSONParser])
def tipoImpresion_fi_api_view(request):
    if request.method == 'POST':
        tpo_serializado = TipoImpresionSerializer(data=request.data)
        if tpo_serializado.is_valid():
            tpo_serializado.save()
            all = TipoImpresionSerializer( TipoImpresion.objects.all(), many=True )
            return Response({
                'message':'Tipo impresion creado correctamente!',
                'newOptsList':all.data,
                'newOptId': tpo_serializado.data.get('idTipoImpresion')}, 
                status=status.HTTP_201_CREATED 
            )        
    if(request.method == 'GET'):
        tpos = TipoImpresion.objects.all()
        tpo_serializado = TipoImpresionSerializer(tpos,many=True)
        return Response( tpo_serializado.data, status=status.HTTP_200_OK )

@api_view(['GET','PUT','DELETE'])
@parser_classes([MultiPartParser, JSONParser])
def tipoImpresion_fi_detail_api_view(request, pk=None ):
    if request.method == 'GET':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        tpo = TipoImpresion.objects.filter( idTipoImpresion = pk ).first()
        try:
            tpo.delete()
            # return the new TipoImpresion records
            tpos = TipoImpresion.objects.all()
            tpos_serializado = TipoImpresionSerializer(tpos,many=True) 
            return Response({
                'message':'¡tipo de impresion eliminado correctamente!',
                'newOptsList':tpos_serializado.data}, 
                status=status.HTTP_200_OK 
            )
        except:
            return Response({
                'message':'¡No es posible eliminar tipo de impresion en uso!'}, 
                status=status.HTTP_409_CONFLICT 
            )