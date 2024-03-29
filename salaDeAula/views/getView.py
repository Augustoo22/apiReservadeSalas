from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import SalaDeAula, Horario
from ..serializers import SalaDeAulaSerializer, HorarioSerializer

class ListarSalas(APIView):
    def get(self, request):
        salas = SalaDeAula.objects.all()
        serializer = SalaDeAulaSerializer(salas, many=True)
        return Response(serializer.data)

class DetalhesSala(APIView):
    def get(self, request, id):
        try:
            sala = SalaDeAula.objects.get(id=id)
            serializer = SalaDeAulaSerializer(sala)
            return Response(serializer.data)
        except SalaDeAula.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ListarHorarios(APIView):
    def get(self, request, id):
        try:
            horarios = Horario.objects.filter(sala_id=id)
            serializer = HorarioSerializer(horarios, many=True)
            return Response(serializer.data)
        except SalaDeAula.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
