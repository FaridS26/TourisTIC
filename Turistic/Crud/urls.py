from django.urls import path

from Crud import views

urlpatterns = [
    path('Login',views.Login, name="Login"),
    path('Register',views.Register, name="Register"),
    path('region-andina',views.Region_Andina, name="Region_andina"),
    path('contacto',views.Contacto, name="Contacto"),
    path('sitio1',views.Sitio1, name="Sitio1"),
    path('index',views.Index, name="Index"),
]