from django.db import models

# Create your models here.


class Contacto(models.Model):
    asunto = models.CharField(max_length=100)
    nombre_Apellido = models.CharField(
        max_length=100, blank=True, verbose_name=u"Nombre y Apellido")
    correo = models.EmailField(verbose_name=u"Correo Electrónico")
    mensaje = models.TextField()

    def __str__(self):
        return self.asunto
