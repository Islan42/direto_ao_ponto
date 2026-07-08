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

    def __str__(self):
        return f"{self.razao_social} - {self.cnpj}"

class Recrutador(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    ativo = models.BooleanField()
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    criado_em = models.DateTimeField()

    def __str__(self):
        return f"{self.nome} - {self.empresa.razao_social}"

class ProcessoSeletivo(models.Model):
    recrutador = models.ForeignKey(Recrutador, on_delete=models.PROTECT)
    processo_pai = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    ativo = models.BooleanField()
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    cep = models.CharField(max_length=9)
    cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=2)
    remuneracao = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    criado_em = models.DateTimeField()

    def __str__(self):
        return f"{self.titulo} - {self.recrutador}"

class ProcessoTemFuncao(models.Model):
    funcao = models.ForeignKey(Funcao, on_delete=models.PROTECT)
    processo = models.ForeignKey(ProcessoSeletivo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.processo.titulo} - {self.funcao.nome}"

class CandidatoInscritoProcesso(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    processo = models.ForeignKey(ProcessoSeletivo, on_delete=models.CASCADE)
    criado_em = models.DateTimeField()

    def __str__(self):
        return f"{self.candidato.nome} - {self.processo.titulo}"
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['candidato', 'processo'],
                name="unique_candidato_processo"
            )
        ]