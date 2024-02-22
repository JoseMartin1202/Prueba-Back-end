from django.urls import path
from apps.Nota.api import nota_api_view,nota_detail_api_view

urlpatterns = [
    path('notas/', nota_api_view, name='notas_api'),
    path('notas/<int:pk>', nota_detail_api_view, name='nota_detail_api_view'),
]