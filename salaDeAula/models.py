from django.db import models

class SalaDeAula(models.Model):
    nome = models.CharField(max_length=100)
    capacidade = models.PositiveIntegerField()
    localizacao = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    horario = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nome)

