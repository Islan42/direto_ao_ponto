from django.contrib import admin
from .models import Empresa, Recrutador, ProcessoSeletivo, ProcessoTemFuncao, CandidatoInscritoProcesso
# Register your models here.

admin.site.register(Empresa)
admin.site.register(Recrutador)
admin.site.register(ProcessoSeletivo)
admin.site.register(ProcessoTemFuncao)
admin.site.register(CandidatoInscritoProcesso)