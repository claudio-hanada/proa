import requests
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import FormView, TemplateView
from core.forms import EnderecoForm

class SearchView(FormView):
    template_name = 'pages/zip_search.html'
    form_class = EnderecoForm 

class ResultView(TemplateView):
    template_name = 'pages/result.html'

    def post(self, request, *args, **kwargs):
        if request.POST.get('cep'):
            data = {
                'cep': request.POST.get('cep')
            }
            response = requests.post('http://127.0.0.1:8000/api/v1/endereco/', data=data)
            
        else:
            data = {
                'logradouro': request.POST.get('logradouro'),
                'uf': request.POST.get('uf'),
                'localidade': request.POST.get('localidade'),
            }
            response = requests.post('http://127.0.0.1:8000/api/v1/endereco/', data=data)
        
        return render(request, self.template_name, {'data':response.json()})