from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets

from apps.Users.models import User
from apps.Users.serializer import (
    UserSerializer, UserListSerializer, UpdateUserSerializer,
    PasswordSerializer,CustomUserSerializer
)

class UserViewSet(viewsets.GenericViewSet):
    model = User
    serializer_class = UserSerializer
    list_serializer_class = CustomUserSerializer
    queryset = None

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects.all()
        return self.queryset

    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        user = self.get_object(pk)
        password_serializer = PasswordSerializer(data=request.data)
        if password_serializer.is_valid():
            user.set_password(password_serializer.validated_data['password'])
            user.save()
            return Response({
                'message': '¡Contraseña actualizada correctamente!'
            })
        return Response({
            'message': 'Hay errores en la información enviada',
            'errors': password_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        users = self.get_queryset()
        users_serializer = self.list_serializer_class(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message': '¡Usuario registrado correctamente!'
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'Hay errores en el registro',
            'errors': user_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)



    def retrieve(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = self.list_serializer_class(user)
        return Response(user_serializer.data)
    
    '''def destroy(self, request, pk=None):
        try:
            user = self.get_object(pk)
            user.delete()
            return Response({
                "message": "¡Usuario eliminado correctamente!",       
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "message": "Error al eliminar el usuario.",
                "error": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)'''
    
    @action(detail=False, methods=['delete'])
    def delete_user_apiView( self, request ):
        print(request.data)
        ids = request.data
        for obj in ids:
            User.objects.filter( id = obj.get('id') ).delete()
        return Response( {
            "message":"¡Eliminación correcta de usuarios!",       
        }, status=status.HTTP_200_OK )


    def update(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = UpdateUserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'usuario': user_serializer.data,
                'message': '¡Usuario actualizado correctamente!'
            }, status=status.HTTP_200_OK)
        return Response({ 
            'message': 'Hay errores en la actualización',
            'errors': user_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
