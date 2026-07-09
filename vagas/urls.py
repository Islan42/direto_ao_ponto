from django.urls import path
from . import views

app_name = "vagas"
urlpatterns = [
    path("", views.index, name="index"), #TODAS AS VAGAS
    path("<int:processo_id>/", views.index, name="processo_detalhe"), #PERFIL PROCESSO
    path("candidato/new/", views.index, name="candidato_new"), #NOVO CANDIDATO
    path("candidato/<int:candidato_id>/", views.index, name="candidato_detalhe"), #PERFIL DO CONDIDATO
    path("empresa/<int:empresa_id>/", views.index, name="empresa_detalhe"), #PERFIL EMPRESA
]