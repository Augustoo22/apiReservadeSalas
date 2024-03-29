from rest_framework import serializers
from .models import SalaDeAula, Horario, Reserva

class SalaDeAulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaDeAula
        fields = '__all__'

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
