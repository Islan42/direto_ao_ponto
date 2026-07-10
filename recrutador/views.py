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
    recrutador = get_object_or_404(Recrutador, pk=recrutador_id)
    context = {
        "recrutador" : recrutador,
    }
    return render(request, "recrutador/perfil_recrutador.html", context)

def perfil_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, pk=empresa_id)
    context = {
        "empresa" : empresa,
    }
    return render(request, "recrutador/perfil_empresa.html", context)

def perfil_processo(request, processo_id):
    processo = get_object_or_404(ProcessoSeletivo, pk=processo_id)
    context = {
        "processo" : processo,
    }
    return render(request, "recrutador/perfil_processo.html", context)

def new_recrutador(request):
    return render(request, "recrutador/new_recrutador.html")

def new_empresa(request):
    return render(request, "recrutador/new_empresa.html")

def new_processo(request):
    return render(request, "recrutador/new_processo.html")