from django.urls import path
from apps.CategoriaMaterial.api import categoriaMaterial_api_view,categoriaMaterial_detail_api_view

urlpatterns = [
    path('categoriasMateriales/', categoriaMaterial_api_view, name='categoriasMateriales_api'),
    path('categoriasMateriales/<int:pk>', categoriaMaterial_detail_api_view, name='categoriasMateriael_detail_api_view'),
]