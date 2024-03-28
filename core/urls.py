from django.urls import path
from salaDeAula.views.getView import ListaSalasDeAula, DetalhesSalaDeAula, ListaHorariosDisponiveis

urlpatterns = [
    path('api/salas/', ListaSalasDeAula.as_view(), name='lista-salas'),
    path('api/salas/<int:id>/', DetalhesSalaDeAula.as_view(), name='detalhes-sala'),
    path('api/salas/<int:id>/horarios/', ListaHorariosDisponiveis.as_view(), name='lista-horarios'),
]
