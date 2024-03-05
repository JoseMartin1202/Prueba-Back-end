from django.urls import path
from apps.Tarea.api import tarea_api_view,tarea_detail_api_view

urlpatterns = [
    path('tareas/', tarea_api_view, name='tareas_api'),
    path('tareas/<int:pk>', tarea_detail_api_view, name='tarea_detail_api_view'),
]