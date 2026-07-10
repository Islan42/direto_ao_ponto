from django.urls import path
from . import views

app_name = "recrutador"
urlpatterns = [
    path("", views.index, name="index"), #REDIRECT PERFIL RECRUTADOR
    path("<int:recrutador_id>/", views.perfil_recrutador, name="perfil_recrutador"),
    path("new/", views.new_recrutador, name="new_recrutador"),
    path("empresa/<int:empresa_id>/", views.perfil_empresa, name="perfil_empresa"),
    path("empresa/new/", views.new_empresa, name="new_empresa"),
    path("processo/<int:processo_id>/", views.perfil_processo, name="perfil_processo"),
    path("processo/new/", views.new_processo, name="new_processo"),
]