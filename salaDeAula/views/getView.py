from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import SalaDeAula, Horario
from ..serializers import SalaDeAulaSerializer, HorarioSerializer

class ListaSalasDeAula(APIView):
    def get(self, request):
        salas = SalaDeAula.objects.all()
        serializer = SalaDeAulaSerializer(salas, many=True)
        return Response(serializer.data)

class DetalhesSalaDeAula(APIView):
    def get(self, request, id):
        try:
            sala = SalaDeAula.objects.get(id=id)
        except SalaDeAula.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SalaDeAulaSerializer(sala)
        return Response(serializer.data)

class ListaHorariosDisponiveis(APIView):
    def get(self, request, id):
        try:
            sala = SalaDeAula.objects.get(id=id)
        except SalaDeAula.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        horarios = Horario.objects.filter(sala=sala)
        serializer = HorarioSerializer(horarios, many=True)
        return Response(serializer.data)
