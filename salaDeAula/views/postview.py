from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import SalaDeAula, Reserva
from ..serializers import SalaDeAulaSerializer, ReservaSerializer

class CriarSala(APIView):
    def post(self, request):
        serializer = SalaDeAulaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReservarSala(APIView):
    def post(self, request, id):
        try:
            sala = SalaDeAula.objects.get(id=id)
        except SalaDeAula.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ReservaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(sala=sala)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
