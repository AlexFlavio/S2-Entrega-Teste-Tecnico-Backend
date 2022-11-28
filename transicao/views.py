from rest_framework.views import APIView, Request, Response, status
from .models import Transicao
from .serializers import (
    TransicaoSerialzer,
    UploadTransicaoSerializer,
    ListTransicaoSerializer,
)
from utils.modeling import ModelingTransicao
from django.shortcuts import get_list_or_404


class CreateTransicaoView(APIView):
    queryset = Transicao
    serializer_class = UploadTransicaoSerializer

    def post(self, request: Request) -> Response:
        file = request.FILES["file"].read().decode().split("\n")
        retorno = []
        for text in file:
            obj = ModelingTransicao(text)
            serializer = TransicaoSerialzer(data=obj.formatado)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            retorno.append(serializer.data)
        return Response(retorno, status=status.HTTP_201_CREATED)
        ...

    ...


class ListTransicaoView(APIView):

    # queryset = Transicao
    serializer_class = ListTransicaoSerializer

    def get(self, request: Request, nome_loja: str) -> Response:
        transacoes = get_list_or_404(Transicao, loja__icontains=nome_loja)
        if not transacoes:
            return Response()
        serializer = TransicaoSerialzer(transacoes, many=True)
        total = sum([transacao["valor"] for transacao in serializer.data])
        retorno = {"total": total, "transacoes": serializer.data}
        return Response(retorno, status=status.HTTP_200_OK)
        ...

    ...
