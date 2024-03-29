from django.urls import path
from salaDeAula.views.postView import CriarSalaDeAula
from salaDeAula.views.getView import ListaSalasDeAula, DetalhesSalaDeAula, ListaHorariosDisponiveis
from salaDeAula.views.renderView import listar_salas

urlpatterns = [
    path('salas/', ListaSalasDeAula.as_view(), name='lista-salas'),
    path('salas/<int:id>/', DetalhesSalaDeAula.as_view(), name='detalhes-sala'),
    path('salas/<int:id>/horarios/', ListaHorariosDisponiveis.as_view(), name='lista-horarios'),
    path('salas/criar/', CriarSalaDeAula.as_view(), name='criar_sala_de_aula'),
    path('salas/', listar_salas, name='listar_salas'),
]
