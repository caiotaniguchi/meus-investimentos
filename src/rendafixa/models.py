from django.db import models


class RendaFixa(models.Model):
    def __init__(self, data_inicio, data_fim, valor_aporte):
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.valor_aporte = valor_aporte

    def calcular_valor_atual(self):
        pass
