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
    processofuncoes = processo.processotemfuncao_set.all()
    funcoes = [rel.funcao for rel in processofuncoes]

    context = {
        "processo" : processo,
        "funcoes" : funcoes,
    }
    return render(request, "vagas/perfil_processo.html", context)

def new_candidato(request):
    return HttpResponse("CADASTRANDO NOVO USUÁRIO")

def perfil_candidato(request, candidato_id):
    candidato = get_object_or_404(Candidato, pk = candidato_id)

    telefonescandidatos = candidato.telefonecandidato_set.all()
    telefones = [rel.telefone for rel in telefonescandidatos]

    funcoescandidatos = candidato.candidatotemfuncao_set.all()
    funcoes = [rel.funcao for rel in funcoescandidatos]

    candidato_processo = candidato.candidatoinscritoprocesso_set.all()
    #processos = [rel.processo for rel in candidato_processo if rel.processo.ativo] NESSE CASO, DEVE MOSTRAR TAMBÉM OS INATIVOS POR QUESTÃO DE HISTÓRICO
    processos = [rel.processo for rel in candidato_processo]
        

    context = {
        "candidato" : candidato,
        "telefones" : telefones,
        "funcoes" : funcoes,
        "processos" : processos,
    }
    return render(request, "vagas/perfil_candidato.html", context)
    

def perfil_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, pk = empresa_id)
    recrutadores = empresa.recrutador_set.all()
    processos = [processo for rec in recrutadores for processo in rec.processoseletivo_set.all() if processo.ativo]

    context = {
        "empresa" : empresa,
        "processos" : processos,
    }
    return render(request, "vagas/perfil_empresa.html", context)
