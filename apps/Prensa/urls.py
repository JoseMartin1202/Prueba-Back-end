from django.urls import path
from apps.Prensa.api import prensa_api_view,\
    prensa_detail_api_view,\
    prensa_fi_api_view,\
    prensa_fi_detail_api_view

urlpatterns = [
    path('prensas/', prensa_api_view, name='prensas_api'),
    path('prensas/<int:pk>', prensa_detail_api_view, name='prensa_detail_api_view'),

    path('prensas_fi/', prensa_fi_api_view, name='prensas_fi_api'),
    path('prensas_fi/<int:pk>', prensa_fi_detail_api_view, name='prensa_fi_detail_api_view'),
]