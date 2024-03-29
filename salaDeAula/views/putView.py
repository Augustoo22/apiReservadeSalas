from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import SalaDeAula
from ..serializers import SalaDeAulaSerializer

class AtualizarSala(APIView):
    def put(self, request, id):
        try:
            sala = SalaDeAula.objects.get(id=id)
        except SalaDeAula.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = SalaDeAulaSerializer(sala, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
