from django.db import models
from django.contrib.auth.models import User

class Tarea(models.Model):

    TIPO_TAREA = (
        ('DIA', 'Corto plazo (día)'),
        ('ANIO', 'Largo plazo (año)'),
    )

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    completo = models.BooleanField(default=False)

    tipo = models.CharField(
        max_length=4,
        choices=TIPO_TAREA,
        default='DIA'
    )

    fecha_limite = models.DateField(
        null=True,
        blank=True
    )

    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
