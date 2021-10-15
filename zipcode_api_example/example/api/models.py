from django.db import models
from unidecode import unidecode

class Endereco(models.Model):
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=50)
    plain_logradouro = models.CharField(max_length=50, null=True, blank=True)
    complemento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    localidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    ddd = models.CharField(max_length=3)
    gia = models.CharField(max_length=10)
    siafi = models.CharField(max_length=10)
    ibge = models.CharField(max_length=10)

    @staticmethod
    def create(data):
        endereco = Endereco(**data)
        endereco.plain_logradouro = unidecode(data['logradouro'])
        endereco.save()
        return endereco
