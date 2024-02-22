from django.urls import path
from apps.Terminado.api import terminado_api_view,terminado_detail_api_view

urlpatterns = [
    path('terminados/', terminado_api_view, name='terminados_api'),
    path('terminados/<int:pk>', terminado_detail_api_view, name='terminado_detail_api_view'),
]