from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import SalaDeAula, Reserva
from ..serializers import SalaDeAulaSerializer, ReservaSerializer

class ExcluirSala(APIView):
    def delete(self, request, id):
        try:
            sala = SalaDeAula.objects.get(id=id)
        except SalaDeAula.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        sala.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CancelarReserva(APIView):
    def delete(self, request, id):
        try:
            reserva = Reserva.objects.get(id=id)
        except Reserva.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        reserva.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
