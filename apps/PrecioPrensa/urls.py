from django.urls import path
from apps.PrecioPrensa.api import precioPrensa_api_view, \
    precioPrensa_detail_api_view, \
    preciosPrensa_tipoImpresion_api_view, \
    preciosPrensa_prensa_api_view

urlpatterns = [
    path('precioPrensas/', precioPrensa_api_view, name='precioPrensas_api'),
    path('precioPrensas/<int:pk>', precioPrensa_detail_api_view, name='precioPrensa_detail_api_view'),
    path('precios_tipo_impresion/<int:pk>', preciosPrensa_tipoImpresion_api_view, name='precios_tipo_impresion_detail_api_view'),
    
    path('precios_prensa/<int:pk>', preciosPrensa_prensa_api_view, name='precios_prensa_detail_api_view'),
]