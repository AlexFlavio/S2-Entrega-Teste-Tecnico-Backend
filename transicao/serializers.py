from rest_framework import serializers

from .models import Transicao


class TransicaoSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Transicao
        fields = "__all__"

    ...


class UploadTransicaoSerializer(serializers.Serializer):
    file = serializers.FileField(write_only=True)
    id = serializers.CharField(read_only=True)
    tipo = serializers.CharField(max_length=25,read_only=True)
    data = serializers.DateField(read_only=True)
    valor = serializers.FloatField(read_only=True)
    cpf = serializers.CharField(max_length=11,read_only=True)
    cartao = serializers.CharField(max_length=13,read_only=True)
    hora = serializers.TimeField(read_only=True)
    dono = serializers.CharField(max_length=15,read_only=True)
    loja = serializers.CharField(max_length=20,read_only=True)

    # class Meta:
    #     model = Transicao
    #     fields = ["file"]

    ...


class ListTransicaoSerializer(serializers.Serializer):
    total = serializers.FloatField()
    transacoes = TransicaoSerialzer()
    ...
