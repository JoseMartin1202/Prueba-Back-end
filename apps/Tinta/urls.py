from django.urls import path
from apps.Tinta.api import tinta_api_view,tinta_detail_api_view

urlpatterns = [
    path('tintas/', tinta_api_view, name='tintas_api'),
    path('tintas/<int:pk>', tinta_detail_api_view, name='tinta_detail_api_view'),
]