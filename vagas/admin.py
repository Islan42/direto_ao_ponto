from django.contrib import admin
from .models import Candidato, Funcao, CandidatoTemFuncao, TelefoneCandidato
# Register your models here.

admin.site.register(Candidato)
admin.site.register(Funcao)
admin.site.register(CandidatoTemFuncao)
admin.site.register(TelefoneCandidato)