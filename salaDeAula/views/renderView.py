from django.shortcuts import render
from ..models import SalaDeAula

def listar_salas(request):
    salas = SalaDeAula.objects.all()
    return render(request, 'listar_salas.html', {'salas': salas})
