from django.db import models

class Sala(models.Model):
    nome = models.CharField(max_length=100)
    capacidade = models.IntegerField()

    def __str__(self):
        return self.nome

class Reserva(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    data = models.DateField()
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()

    def __str__(self):
        return f"Reserva para {self.sala} em {self.data} - {self.horario_inicio} às {self.horario_fim}"
