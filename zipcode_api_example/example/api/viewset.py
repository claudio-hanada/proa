import requests
from unidecode import unidecode
from rest_framework import viewsets
from rest_framework.response import Response
from api.serializer import EnderecoSerializer
from api.models import Endereco


class EnderecoViewSet(viewsets.ModelViewSet):
    queryset=Endereco.objects.all()
    serializer_class = EnderecoSerializer

    def get_queryset(self):
        return Endereco.objects.all()

    def create(self, request):
        if 'cep' in request.data:
            endereco = Endereco.objects.filter(cep=request.data['cep'])
            
            if not endereco:
                data = requests.get(f'http://viacep.com.br/ws/{request.data["cep"]}/json/')
                endereco = Endereco.create(data.json())
                serializer = EnderecoSerializer(endereco, many=False)
                return Response([serializer.data])
            
            serializer = EnderecoSerializer(endereco, many=True)
        else:
            localidade = request.data["localidade"]
            logradouro = request.data["logradouro"]
            uf = request.data["uf"]
            endereco = Endereco.objects.filter(plain_logradouro=unidecode(logradouro), uf=uf)
            
            if not endereco:
                
                lista_endereco = list()
                data = requests.get(f'http://viacep.com.br/ws/{uf}/{localidade}/{logradouro}/json/')
                for result in data.json():
                    lista_endereco.append(Endereco.create(result))
                serializer = EnderecoSerializer(lista_endereco, many=True)
                return Response(serializer.data)
            
            serializer = EnderecoSerializer(endereco, many=True)
            
        return Response(serializer.data)