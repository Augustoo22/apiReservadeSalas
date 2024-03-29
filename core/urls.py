from django.urls import path
from salaDeAula.views.postView import CriarSala, ReservarSala
from salaDeAula.views.getView import ListarSalas, DetalhesSala, ListarHorarios
from salaDeAula.views.putView import AtualizarSala
from salaDeAula.views.deleteView import ExcluirSala, CancelarReserva

urlpatterns = [
    path('salas/', ListarSalas.as_view()),
    path('salas/<int:id>/', DetalhesSala.as_view()),
    path('salas/criar/', CriarSala.as_view()),
    path('salas/<int:id>/atualizar/', AtualizarSala.as_view()),
    path('salas/<int:id>/excluir/', ExcluirSala.as_view()),
    path('salas/<int:id>/horarios/', ListarHorarios.as_view()),
    path('salas/<int:id>/reservar/', ReservarSala.as_view()),
    path('reservas/<int:id>/cancelar/', CancelarReserva.as_view()),
]
