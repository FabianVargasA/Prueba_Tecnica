from rest_framework.viewsets import ModelViewSet
from eventos.api.serializers import EventoSerializers
from eventos.models import Evento
class EventoApiViewsSet(ModelViewSet):
    serializer_class = EventoSerializers
    queryset = Evento.objects.all()
