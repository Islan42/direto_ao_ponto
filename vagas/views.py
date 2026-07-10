from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import Candidato
from recrutador.models import ProcessoSeletivo, Empresa

def index(request):
    vagas = get_list_or_404(ProcessoSeletivo, ativo = True) #ORDER BY
    context = {
        "vagas" : vagas,
        }
    return render(request, "vagas/index.html", context)

def perfil_processo(request, processo_id):
    processo = get_object_or_404(ProcessoSeletivo, pk = processo_id)
    context = {
        "processo" : processo,
    }
    return render(request, "vagas/perfil_processo.html", context)

def new_candidato(request):
    return HttpResponse("CADASTRANDO NOVO USUÁRIO")

def perfil_candidato(request, candidato_id):
    candidato = get_object_or_404(Candidato, pk = candidato_id)    
    context = {
        "candidato" : candidato,
    }
    return render(request, "vagas/perfil_candidato.html", context)
    

def perfil_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, pk = empresa_id)
    context = {
        "empresa" : empresa,
    }
    return render(request, "vagas/perfil_empresa.html", context)
