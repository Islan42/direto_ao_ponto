from django.db import models

# Create your models here.

class Candidato(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    cep = models.CharField(max_length=9)
    cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=2)
    resumo_profissional = models.TextField()
    criado_em = models.DateTimeField()

class Funcao(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)

class CandidatoTemFuncao(models.Model):
    id_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    id_funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE)

class TelefoneCandidato(models.Model):
    id_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15)

