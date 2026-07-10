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
    context = {
        "processo" : processo,
    }
    return render(request, "recrutador/perfil_processo.html", context)

def new_recrutador(request):
    pass

def new_empresa(request):
    pass

def new_processo(request):
    pass