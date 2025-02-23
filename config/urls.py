"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from users.api.views import UserProfileExampleViewSet
from petshop.api.views import AdministradorViewSet, ClienteViewSet, DadosMedicosViewSet, UsuarioViewSet, ProdutoViewSet, PetViewSet, AgendamentoViewSet, VeterinarioViewSet

router = SimpleRouter()


router.register('usuarios', UsuarioViewSet, basename='usuarios')
router.register('administradores', AdministradorViewSet, basename='administradores')
router.register('clientes', ClienteViewSet, basename='clientes')
router.register('veterinarios', VeterinarioViewSet, basename='veterinarios')
router.register('produtos', ProdutoViewSet, basename='produtos')
router.register('dados-medicos', DadosMedicosViewSet, basename='dados-medicos')
router.register('pets', PetViewSet, basename='pets')
router.register('agendamentos', AgendamentoViewSet, basename='agendamentos')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token-auth/", views.obtain_auth_token),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]+router.urls
