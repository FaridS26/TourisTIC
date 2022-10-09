from django.db import models
from django.forms import NullBooleanSelect
# Create your models here.


class Contacto(models.Model):
    asunto = models.CharField(max_length=100)
    nombre_Apellido = models.CharField(
        max_length=100, blank=True, verbose_name=u"Nombre y Apellido")
    correo = models.EmailField(verbose_name=u"Correo Electrónico")
    mensaje = models.TextField()

    def __str__(self):
        return self.asunto


REGIONES = [
    ('amazonica', 'Amazoníca'),
    ('andina', 'Andina'),
    ('caribe', 'Caribe'),
    ('orinoquia', 'Orinoquía'),
    ('pacifica', 'Pacífica'),
]


class sitioTuristico(models.Model):
    nombre = models.CharField(max_length=200, verbose_name=u"nombre")
    region = models.CharField(max_length=9, choices=REGIONES)
    imagen = models.TextField(default="url-imagen")
    description = models.TextField(default="descripcion sitio")
    video = models.TextField(default="url-video")
    ubicacion = models.TextField(default="url-ubicacion")
    precio = models.TextField(default="precio")
    sitioFavorito = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre+", región "+self.region


class Region(models.Model):
    region = models.CharField(max_length=9, choices=REGIONES)
    imagen = models.TextField(default="url_imagen")

    def __str__(self):
        return self.region


class misRutas(models.Model):
    username = models.CharField(max_length=100, default="Usuario")
    nombre = models.CharField(
        max_length=200, verbose_name=u"nombre", default="Nombre")
    ubicacion = models.TextField(default="url-ubicacion")
    precio = models.TextField(default="precio")

    def __str__(self):
        return self.username+", "+self.nombre
