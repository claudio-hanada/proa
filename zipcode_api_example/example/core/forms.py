from django import forms

class EnderecoForm(forms.Form):
    CHOICES =  (('AC', 'Acre'),
                ('AL', 'Alagoas'),
                ('AP', 'Amapá'),
                ('AM', 'Amazonas'),
                ('BA', 'Bahia'),
                ('CE', 'Ceará'),
                ('DF', 'Distrito Federal'),
                ('ES', 'Espírito Santo'),
                ('GO', 'Goiás'),
                ('MA', 'Maranhão'),
                ('MT', 'Mato Grosso'),
                ('MS', 'Mato Grosso do Sul'),
                ('MG', 'Minas Gerais'),
                ('PR', 'Paraná'),
                ('PB', 'Paraíba'),
                ('PA', 'Pará'),
                ('PE', 'Pernambuco'),
                ('PI', 'Piauí'),
                ('RN', 'Rio Grande do Norte'),
                ('RS', 'Rio Grande do Sul'),
                ('RJ', 'Rio de Janeiro'),
                ('RO', 'Rondônia'),
                ('RR', 'Roraima'),
                ('SC', 'Santa Catarina'),  
                ('SE', 'Sergipe'),  
                ('SP', 'São Paulo'),  
                ('TO', 'Tocantins'),  
                )
    cep = forms.CharField(max_length=9, required=False)
    logradouro = forms.CharField(max_length=50, label="Endereço",required=False)
    localidade = forms.CharField(max_length=50, label="Cidade",required=False)
    uf = forms.ChoiceField(choices=CHOICES, required=False)

    class Meta:
        fields = ('cep', 'logradouro', 'uf')