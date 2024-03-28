from rest_framework import generics
from ..models import SalaDeAula, Horario
from ..serializers import SalaDeAulaSerializer, HorarioSerializer

class ListaSalasDeAula(generics.ListAPIView):
    queryset = SalaDeAula.objects.all()
    serializer_class = SalaDeAulaSerializer

class DetalhesSalaDeAula(generics.RetrieveAPIView):
    queryset = SalaDeAula.objects.all()
    serializer_class = SalaDeAulaSerializer
    lookup_field = 'id'

class ListaHorariosDisponiveis(generics.ListAPIView):
    serializer_class = HorarioSerializer

    def get_queryset(self):
        sala_id = self.kwargs['id']
        return Horario.objects.filter(sala_id=sala_id)
