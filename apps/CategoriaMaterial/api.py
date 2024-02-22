from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, JSONParser
from apps.CategoriaMaterial.serializers import CategoriaMaterialSerializer
from apps.CategoriaMaterial.models import CategoriaMaterial

@api_view(['GET','POST'])
@parser_classes([MultiPartParser , JSONParser])
def categoriaMaterial_api_view(request):
    # list
    if request.method == 'GET':
        c = CategoriaMaterial.objects.all()
        c_sz = CategoriaMaterialSerializer(c,many=True)
        return Response( c_sz.data, status=status.HTTP_200_OK )

    # Create
    elif request.method == 'POST':
        c_sz = CategoriaMaterialSerializer(data=request.data)
        if c_sz.is_valid():
            c_sz.save()
            all = CategoriaMaterialSerializer( CategoriaMaterial.objects.all(), many=True )
            return Response( {
                'message':'¡Categoria creada correctamente!',
                'newOptsList':all.data,
                'newOptId': c_sz.data.get('idCategoriaMaterial')
                }, status=status.HTTP_201_CREATED )
        return Response( c_sz.errors, status=status.HTTP_400_BAD_REQUEST )


@api_view(['GET','PUT','DELETE'])
@parser_classes([MultiPartParser, JSONParser])
def categoriaMaterial_detail_api_view(request, pk=None ):
    if request.method == 'GET':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
            material = CategoriaMaterial.objects.filter( idCategoriaMaterial = pk ).first()
            try:
                material.delete()
                categorias = CategoriaMaterial.objects.all()
                categorias_serializadas = CategoriaMaterialSerializer(categorias,many=True) 
                return Response({
                    'message':'¡Categoria eliminada correctamente!',
                    'newOptsList': categorias_serializadas.data
                    }, 
                    status=status.HTTP_200_OK
                )
            except Exception as e:
                print(e)
                return Response(
                    {'message':'¡No es posible eliminar una categoria en uso!'}, 
                    status=status.HTTP_409_CONFLICT
                )
    return Response(
        {'message':'No se encontró la categoria'}, 
        status=status.HTTP_400_BAD_REQUEST
    )
      