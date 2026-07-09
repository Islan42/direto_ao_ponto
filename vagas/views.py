from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import Candidato
from recrutador.models import ProcessoSeletivo, Empresa

def index(request):
    vagas = get_list_or_404(ProcessoSeletivo, ativo = True)
    lista_vagas = [vaga.__str__() for vaga in vagas]
    return HttpResponse(f"{lista_vagas}")

def perfil_processo(request, processo_id):
    processo = get_object_or_404(ProcessoSeletivo, pk = processo_id)
    return HttpResponse(f"{processo.titulo}\nRemuneração: R${processo.remuneracao}\n{processo.cidade}")

def new_candidato(request):
    return HttpResponse("CADASTRANDO NOVO USUÁRIO")

def perfil_candidato(request, candidato_id):
    candidato = get_object_or_404(Candidato, pk = candidato_id)
    return HttpResponse(f"{candidato.nome} - {candidato.email} - {candidato.cidade} - {candidato.resumo_profissional}")

def perfil_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, pk = empresa_id)
    return HttpResponse(f"{empresa.razao_social} ({empresa.cnpj}) - {empresa.cidade}/{empresa.estado}")
