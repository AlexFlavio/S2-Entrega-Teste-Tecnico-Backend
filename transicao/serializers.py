from rest_framework import serializers

from .models import Transicao



class TransicaoSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Transicao
        fields = "__all__"
    ...

class UploadTransicaoSerializer(serializers.Serializer):
    file = serializers.FileField()
    ...