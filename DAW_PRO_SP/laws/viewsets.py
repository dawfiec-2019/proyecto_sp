from rest_framework import viewsets

from .models import *
from .serializer import *

class AsableistaViewSet(viewsets.ModelViewSet):
    queryset = Asableista.objects.all()
    serializer_class = AsambleistaSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class LeyViewSet(viewsets.ModelViewSet):
    queryset = Ley.objects.all()
    serializer_class = Leyserializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class ComentarioLeyViewSet(viewsets.ModelViewSet):
    queryset = ComentarioLey.objects.all()
    serializer_class = ComentarioLeySerializer

class VotoViewSet(viewsets.ModelViewSet):
    queryset = Voto.objects.all()
    serializer_class = VotoSerializer


