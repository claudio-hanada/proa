from rest_framework import serializers
from api.models import Endereco

class EnderecoSerializer(serializers.ModelSerializer):
    cep = serializers.CharField(max_length=9, required=False)
    logradouro = serializers.CharField(max_length=50, required=False)
    plain_logradouro = serializers.CharField(max_length=50, required=False)
    complemento = serializers.CharField(max_length=50, required=False)
    bairro = serializers.CharField(max_length=50, required=False)
    localidade = serializers.CharField(max_length=50, required=False)
    uf = serializers.CharField(max_length=2, required=False)
    ddd = serializers.CharField(max_length=3, required=False)
    gia = serializers.CharField(max_length=10, required=False)
    siafi = serializers.CharField(max_length=10, required=False)
    ibge = serializers.CharField(max_length=10, required=False)
    class Meta:
        model = Endereco
        fields = ('__all__')

    def create(self, validated_data):
        return Endereco.create(validated_data)