from django.urls import path
from . import views

app_name = "recrutador"
urlpatterns = [
    path("", views.index, name="index"), #REDIRECT PERFIL RECRUTADOR
    path("<int:recrutador_id>/", views.index, name="recrutador_detalhe"), #PERFIL RECRUTADOR
    path("new/", views.index, name="recrutador_new"), #NOVO RECRUTADOR
    path("empresa/new/", views.index, name="empresa_new"), #NOVA EMPRESA
    path("empresa/<int:empresa_id>/", views.index, name="empresa_detalhe"), #PERFIL EMPRESA
    path("processo/new/", views.index, name="processo_new"), #NOVO PROCESSO
    path("processo/<int:processo_id>/", views.index, name="processo_detalhe"), #PERFIL PROCESSO
]