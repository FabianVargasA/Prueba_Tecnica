from django.db import models

evento_estado=[
    (1,'Pendiente por revisar'),
    (2,'Revisado')
]
# Create your models here.
class Evento(models.Model):
    Nombre=models.CharField(max_length=255)
    Tipo=models.CharField(max_length=255)
    Descripcion=models.TextField()
    Fecha=models.DateField()
    Estado=models.IntegerField(
        null=False, blank=False,
        choices=evento_estado,
        default=1
    )
   
    