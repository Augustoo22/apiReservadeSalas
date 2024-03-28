from rest_framework import serializers
from .models import SalaDeAula

class SalaDeAulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaDeAula
        fields = ['nome', 'capacidade', 'localizacao', 'descricao', 'horario']
