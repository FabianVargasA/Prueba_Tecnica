from rest_framework.serializers import ModelSerializer
from eventos.models import Evento

class EventoSerializers(ModelSerializer):
    class Meta:
        model =Evento
        fields = ['id','Nombre']