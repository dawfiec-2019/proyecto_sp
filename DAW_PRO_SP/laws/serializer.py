from .models import *
from rest_framework import serializers



class AsambleistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asambleista
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class Leyserializer(serializers.ModelSerializer):
    class Meta:
        model = Ley
        fields = '__all__'


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'

class ComentarioLeySerializer(serializers.ModelSerializer):
    class Meta:
        model = ComentarioLey
        fields = '__all__'

class VotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voto
        fields = '__all__'
