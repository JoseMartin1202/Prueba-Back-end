from django.urls import path
from apps.Suaje.api import suaje_api_view, suaje_detail_api_view

urlpatterns = [
    path('suajes/', suaje_api_view, name='suaje_api_view'),
    path('suajes/<int:pk>', suaje_detail_api_view, name='suaje_detail_api_view'),
]