from django.urls import path
from apps.TipoImpresion.api import tipoImpresion_api_view, \
    tipoImpresion_detail_api_view, \
    tipoImpresion_fi_api_view, \
    tipoImpresion_fi_detail_api_view

urlpatterns = [
    path('tipoImpresiones/', tipoImpresion_api_view, name='tipoImpresiones_api'),
    path('tipoImpresiones/<int:pk>', tipoImpresion_detail_api_view, name='tipoImpresion_detail_api_view'),

    path('tipoImpresiones_fi/', tipoImpresion_fi_api_view, name='tipoImpresiones_fi_api_view'),
    path('tipoImpresiones_fi/<int:pk>', tipoImpresion_fi_detail_api_view, name='tipoImpresion_fi_detail_api_view'),
]