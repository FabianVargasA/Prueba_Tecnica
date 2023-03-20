from rest_framework.routers import DefaultRouter
from eventos.api.views import EventoApiViewsSet

router_Evento = DefaultRouter()

router_Evento.register(prefix = 'evento',basename='evento',viewset=EventoApiViewsSet)