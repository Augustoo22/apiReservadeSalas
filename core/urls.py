from django.urls import path
from salaDeAula.views.postview import CriarSalaDeAula
from salaDeAula.views.getView import ListaSalasDeAula, DetalhesSalaDeAula, ListaHorariosDisponiveis

urlpatterns = [
    path('api/salas/', ListaSalasDeAula.as_view(), name='lista-salas'),
    path('api/salas/<int:id>/', DetalhesSalaDeAula.as_view(), name='detalhes-sala'),
    path('api/salas/<int:id>/horarios/', ListaHorariosDisponiveis.as_view(), name='lista-horarios'),
    path('salas/criar/', CriarSalaDeAula.as_view(), name='criar_sala_de_aula'),
]
