from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Recrutador, Empresa, ProcessoSeletivo

# Create your views here.
def index(request):
    processos = get_list_or_404(ProcessoSeletivo, ativo=True)
    context = {
        "processos" : processos,
    }
    return render(request, "recrutador/index.html", context)

def perfil_recrutador(request, recrutador_id):
    pass

def perfil_empresa(request, empresa_id):
    pass

def perfil_processo(request, processo_id):
    processo = get_object_or_404(ProcessoSeletivo, pk=processo_id)
    empresa = processo.recrutador.empresa
    
    processo_funcoes = processo.processotemfuncao_set.all()
    funcoes = [rel.funcao for rel in processo_funcoes]

    candidatos_processo = processo.candidatoinscritoprocesso_set.all()
    candidatos = [rel.candidato for rel in candidatos_processo]

    context = {
        "processo" : processo,
        "empresa" : empresa,
        "funcoes" : funcoes,
        "candidatos" : candidatos,
    }

    return render(request, "recrutador/perfil_processo.html", context)

def new_recrutador(request):
    pass

def new_empresa(request):
    pass

def new_processo(request):
    pass