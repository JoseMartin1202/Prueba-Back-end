
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from django.urls import path,re_path
from django.views.static import serve

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.Users.views import Login,Logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', Logout.as_view(), name = 'logout'),
    path('login/',Login.as_view(), name = 'login'),
    path('users/',include('apps.Users.routers')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/',include('apps.Users.routers')),
    path('api/',include('apps.Suaje.urls')),
    path('api/',include('apps.Material.urls')),
    path('api/',include('apps.TipoMaterial.urls')),
    path('api/',include('apps.CategoriaMaterial.urls')),
    path('api/',include('apps.TipoImpresion.urls')),
    path('api/',include('apps.Tinta.urls')),
    path('api/',include('apps.Prensa.urls')),
    path('api/',include('apps.PrecioPrensa.urls')),
    path('api/',include('apps.Nota.urls')),
    path('api/',include('apps.Terminado.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
