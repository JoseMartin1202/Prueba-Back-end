from django.urls import path
from apps.TipoMaterial.api import tipomaterial_api_view, tipomaterial_detail_api_view

urlpatterns = [
    path('tiposMateriales/', tipomaterial_api_view, name='tipomaterial_api_view'),
    path('tiposMateriales/<int:pk>', tipomaterial_detail_api_view, name='tipomaterial_detail_api_view'),
]