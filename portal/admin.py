# -*- coding: utf-8 -*-
from django.contrib import admin
#from portal.models import Pais, Estado,Cidade, Instituicao, TabelaImportacao,ImportacaoCSV, Aluno, Responsavel, Financeiro, Professor
from portal.models import *

# Register your models here.

class PaisAdmin(admin.ModelAdmin):

    model = Pais
    list_display = ['nome','abreviacao','stativo']
    list_filter = ['nome','abreviacao','stativo']
    search_fields = ['nome','abreviacao','stativo']
    save_on_top = True

admin.site.register(Pais);

admin.site.register(Estado);
admin.site.register(Cidade);

# class InstituicaoAdmin(admin.ModelAdmin):
#
#     model = Instituicao
#     list_display = ['razaosocial','nomefantasia','cgc','inscestadual','telefone','email','endereco','complemento',
#                     'bairro','cep','estado','cidade','contato','imagem','telefax','registro']
#     list_filter = ['razaosocial','nomefantasia','cgc','codigo','cidade','estado']
#     search_fields = ['razaosocial','nomefantasia','cgc','codigo','cidade','estado']
#     save_on_top = True
#
# admin.site.register(Instituicao,InstituicaoAdmin)

# class TabelaImportacaoAdmin(admin.ModelAdmin):
#
#     model = TabelaImportacao
#     list_display = ['nome','descricao']
#     list_filter  = ['nome']
#     search_fields = ['nome']
#     save_on_top = True
#
# admin.site.register(TabelaImportacao, TabelaImportacaoAdmin)

class AlunoAdmin(admin.ModelAdmin):

    model = Aluno
    list_display = ['nome','imagem']
    list_filter  = ['nome']
    search_fields = ['nome']
    save_on_top = True

admin.site.register(Aluno, AlunoAdmin);

class ProfessorAdmin(admin.ModelAdmin):

    model = Professor
    list_display = ['registro_professor','nome']
    list_filter  = ['registro_professor','nome']
    search_fields = ['registro_professor','nome']
    save_on_top = True

admin.site.register(Professor,ProfessorAdmin);

admin.site.register(Financeiro);
admin.site.register(Responsavel);


# class ImportacaoCSVAdmin(admin.ModelAdmin):
#
#     model = ImportacaoCSV
#     list_display = ['tabelaimportacao','dtupload', 'arquivo','stimportacao']
#     list_filter  = ['tabelaimportacao','dtupload','stimportacao']
#     search_fields = ['tabelaimportacao','dtupload','stimportacao']
#     save_on_top = True
#
# admin.site.register(TabelaImportacao);
# admin.site.register(ImportacaoCSV, ImportacaoCSVAdmin);

class ImportacaoXLSAdmin(admin.ModelAdmin):

    model = ImportacaoXLS
    list_display  = ['tabelaimportacao','dtupload','stimportacao']
    list_filter   = ['tabelaimportacao','dtupload','stimportacao']
    search_fields = ['tabelaimportacao','dtupload','stimportacao']
    save_on_top = True

admin.site.register(TabelaImportacao);
admin.site.register(ImportacaoXLS, ImportacaoXLSAdmin);

class BoletimAdmin(admin.ModelAdmin):

    model = Boletim
    list_display  = ['registro_boletim']
    list_filter   = ['registro_boletim']
    search_fields = ['registro_boletim']
    save_on_top = True
    delete_on_top = True

admin.site.register(Boletim,BoletimAdmin);



