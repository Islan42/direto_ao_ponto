from django.urls import path
from . import views

app_name = "vagas"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:processo_id>/", views.perfil_processo, name="perfil_processo"),
    path("candidato/new/", views.new_candidato, name="candidato_new"),
    path("candidato/<int:candidato_id>/", views.perfil_candidato, name="perfil_candidato"),
    path("empresa/<int:empresa_id>/", views.perfil_empresa, name="perfil_empresa"),
]