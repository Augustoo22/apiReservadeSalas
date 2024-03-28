from django.urls import path
from salaDeAula.views.postview import CriarSalaDeAula

urlpatterns = [
    path('salas/criar/', CriarSalaDeAula.as_view(), name='criar_sala_de_aula'),
]
