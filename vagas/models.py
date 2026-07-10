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

    def __str__(self):
        return f"{self.nome}"
    
    def telefones(self):
        candidato_telefone = self.telefonecandidato_set.all()
        arr_telefones = [rel.telefone for rel in candidato_telefone]
        return arr_telefones

    def funcoes(self):
        candidato_funcao = self.candidatotemfuncao_set.all()
        arr_funcoes = [rel.funcao for rel in candidato_funcao]
        return arr_funcoes

    def processos(self):
        candidato_processo = self.candidatoinscritoprocesso_set.all()
        arr_processos = [rel.processo for rel in candidato_processo]
        return arr_processos


class Funcao(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class CandidatoTemFuncao(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.candidato.nome} - {self.funcao.nome}"

class TelefoneCandidato(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        
        return f"{self.telefone} - {self.candidato.nome}"

