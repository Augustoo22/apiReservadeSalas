from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import SalaDeAula
from ..serializers import SalaDeAulaSerializer

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

        # Aqui você precisará implementar a lógica para listar os horários disponíveis
        # Vou supor que você tenha um campo 'horario' no modelo SalaDeAula
        horarios_disponiveis = sala.horario.split(',') if sala.horario else []

        return Response({"horarios_disponiveis": horarios_disponiveis})
