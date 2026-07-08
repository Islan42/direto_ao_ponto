from django.db import models
from vagas.models import Candidato, Funcao
# Create your models here.

class Empresa(models.Model):
    razao_social = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18)
    email = models.CharField(max_length=200)
    cep = models.CharField(max_length=9)
    cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=2)
    telefone = models.CharField(max_length=15)
    criado_em = models.DateTimeField()

class Recrutador(models.Model):
    id_empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    ativo = models.BooleanField()
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    criado_em = models.DateTimeField()

class ProcessoSeletivo(models.Model):
    id_recrutador = models.ForeignKey(Recrutador, on_delete=models.PROTECT)
    processo_pai = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    ativo = models.BooleanField()
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    cep = models.CharField(max_length=9)
    cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=2)
    remuneracao = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    criado_em = models.DateTimeField()

class ProcessoTemFuncao(models.Model):
    id_funcao = models.ForeignKey(Funcao, on_delete=models.PROTECT)
    id_processo = models.ForeignKey(ProcessoSeletivo, on_delete=models.CASCADE)

class CandidatoInscritoProcesso(models.Model):
    id_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    id_processo = models.ForeignKey(ProcessoSeletivo, on_delete=models.CASCADE)
    criado_em = models.DateTimeField()