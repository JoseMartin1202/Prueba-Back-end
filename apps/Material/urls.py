from django.urls import path
from apps.Material.api import \
    material_api_view, \
    material_detail_api_view, \
    materiales_string_api_view

urlpatterns = [
    path('materiales/', material_api_view, name='material_api_view'),
    path('materialesString/', materiales_string_api_view, name='materiales_string_api_view'),
    path('materiales/<int:pk>', material_detail_api_view, name='material_detail_api_view'),
]