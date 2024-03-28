from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from salaDeAula.models import SalaDeAula
from salaDeAula.serializers import SalaDeAulaSerializer

class CriarSalaDeAula(APIView):
    def post(self, request):
        serializer = SalaDeAulaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
