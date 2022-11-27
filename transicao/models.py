from django.db import models

import uuid


class Types(models.TextChoices):
    DEBITO = "Débito"
    BOLETO = "Boleto"
    FIANCIAMENTO = "Financiamento"
    CREDITO = "Crédito"
    REC_EMPRESTIMO = "Recebimento Empréstimo"
    VENDAS = "Vendas"
    REC_TED = "Recebimento TED"
    REC_DOC = "Recebimento DOC"
    ALUGUEL = "Aluguel"
    ...


class Transicao(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    tipo = models.CharField(max_length=25, choices=Types.choices)
    data = models.DateField()
    valor = models.IntegerField()
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=13)
    hora = models.TimeField()
    dono = models.CharField(max_length=15)
    loja = models.CharField(max_length=20)
    ...
