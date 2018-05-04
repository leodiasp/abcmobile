from django.conf.urls import url, include
from .views import *
from portal.views import *
from admin import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    url(r'^portal/', portal,    name='portal'),
    url(r'^login/',  do_login,  name='login'),
    url(r'^logout/', do_logout, name='logout'),

    url(r'^mobile/', mobile, name='mobile'),

    url(r'^responsavel_usuario/', responsavel_usuario, name="responsavel_usuario"),
    url(r'^usuario_new/', usuario_new, name="usuario_new"),
    url(r'^usuario_edit/(?P<pk>[0-9]+)', usuario_edit, name="usuario_edit"),

    url(r'^instituicao/', instituicao, name='instituicao'),
    url(r'^instituicao_new/', instituicao_new, name="instituicao_new"),
    url(r'^instituicao_edit/(?P<pk>[0-9]+)', instituicao_edit, name="instituicao_edit"),

    url(r'^periodoletivo/', periodoletivo, name='periodoletivo'),
    url(r'^periodoletivo_new/', periodoletivo_new, name="periodoletivo_new"),
    url(r'^periodoletivo_edit/(?P<pk>[0-9]+)', periodoletivo_edit, name="periodoletivo_edit"),

    # url(r'^turma/', turma, name='turma'),
    # url(r'^turma_new/', turma_new, name="turma_new"),
    # url(r'^turma_edit/(?P<pk>[0-9]+)', turma_edit, name="turma_edit"),
    # #
    # url(r'^disciplina/', disciplina, name='disciplina'),
    # url(r'^disciplina_new/', disciplina_new, name="disciplina_new"),
    # url(r'^disciplina_edit/(?P<pk>[0-9]+)', disciplina_edit, name="disciplina_edit"),
    #
    # url(r'^turmadisciplina/', turmadisciplina, name='turmadisciplina'),
    # url(r'^form_turmadisciplina/(?P<pk>[0-9]+)', form_turmadisciplina, name='form_turmadisciplina'),

    url(r'^aluno/', aluno, name='aluno'),
    url(r'^form_aluno/(?P<pk>[0-9]+)', form_aluno, name='form_aluno'),
    url(r'^graficos/(?P<pk>[0-9]+)', graficos, name='grafico'),

    #    url(r'^importar_csv/', importar_csv, name='importar_csv'),

    url(r'^professor/', professor, name='professor'),
    url(r'^form_professor/(?P<pk>[0-9]+)', form_professor, name='form_professor'),

    # url(r'^financeiro/(?P<pk>[0-9]+)', financeiro, name='financeiro'),

    url(r'^form_boletim/(?P<pk>[0-9]+)', form_boletim, name='form_boletim'),

    url(r'^responsavel/', responsavel, name='responsavel'),
    url(r'^form_responsavel/(?P<pk>[0-9]+)', form_responsavel, name='form_responsavel'),
    #url(r'^edit_responsavel/(?P<pk>[0-9]+)', edit_responsavel, name='edit_responsavel'),

    url(r'^perfil/', perfil, name='perfil'),
    url(r'^upload/', upload, name='upload'),
    url(r'^administracao/', administracao,   name='administracao'),

    #url(r'^importacao_csv/(?P<pk>[0-9]+)', importacao_csv, name='importacao_csv'),
    url(r'^importacao_excel/(?P<pk>[0-9]+)', importacao_excel, name='importacao_excel'),
    url(r'^upload_csv/', upload_csv, name='upload_csv'),

   # url(r'^importacao_excel/', importacao_excel, name='importacao_excel'),

    url(r'^mensagem/', mensagem, name='mensagem'),
    url(r'^mensagem_new/', mensagem_new, name='mensagem_new'),
    url(r'^mensagem_edit/(?P<pk>[0-9]+)', mensagem_edit, name='mensagem_edit'),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
