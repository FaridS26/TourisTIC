from django.urls import path
from .views import VRegistro, cerrar_sesion, logear
from Crud import views


urlpatterns = [
    path('region-<str:region>', views.sitioRegion, name="region"),
    path('contacto', views.Contacto, name="Contacto"),
    path('region-<str:region>/<str:nombre>',
         views.SitioTuristico, name="sitioTuristico"),
    path('', views.Inicio, name="Inicio"),
    path('mi-perfil/<str:username>', views.MiPerfil, name="miPerfil"),
    path('crear-cuenta', VRegistro.as_view(), name="crear_cuenta"),
    path('cerrar-sesion', cerrar_sesion, name="cerrar_sesion"),
    path('iniciar-sesion', logear, name="iniciar_sesion"),
    #path('mis-rutas', anadirRuta, name="mis_rutas")
]
