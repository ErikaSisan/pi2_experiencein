# experiencein/perfis/views.py 
from django.shortcuts import render
from perfis.models import Perfil

def index(request):
    return render(request, 'index.html')

# experiencein/perfis/views.py 

# código anterior omitido

def exibir(request, perfil_id):

    perfil = Perfil.objects.get(id=perfil_id)
    return render(request, 'perfil.html', { "perfil" : perfil})

# Create your views here.


