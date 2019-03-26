# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
#from portal.models import Pais, Estado,Cidade, Instituicao, TabelaImportacao,ImportacaoCSV, Aluno, Responsavel, Financeiro, Professor
from portal.models import *


from import_export import resources

from import_export.admin import ImportExportModelAdmin

from django.contrib.auth.models import User

import sys
# reload(sys)
import importlib
importlib.reload(sys)
# sys.setdefaultencoding('utf8')
# from portal.models import Estado



# Register your models here.
class EstadoResource(resources.ModelResource):

    class Meta:
        model = Estado

class EstadoAdmin(ImportExportModelAdmin):
    resource_class = EstadoResource



class AlunoResource(resources.ModelResource):

    class Meta:
        model = Aluno
        #fields = ('registro_aluno','nome','nome_abreviado','email','celular','whatsapp')
        import_id_fields = ('registro_aluno','nome','nome_abreviado','email','celular','whatsapp',)
        exclude = (' id ',)
        # skip_unchanged = True
        # report_skipped = True
        # exclude = ('id')


class AlunoAdmin(ImportExportModelAdmin):

    resource_class = AlunoResource

admin.site.register(Aluno, AlunoAdmin);


class UserResource(resources.ModelResource):

    class Meta:
        model = User
        #fields = ('id','username','password','email','first_name','last_name')

# Import/Export
class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource


class PaisAdmin(admin.ModelAdmin):

    model = Pais
    list_display = ['nome','abreviacao','stativo']
    list_filter = ['nome','abreviacao','stativo']
    search_fields = ['nome','abreviacao','stativo']
    save_on_top = True

admin.site.register(Pais);

#admin.site.register(Estado);
admin.site.register(Estado, EstadoAdmin);
admin.site.register(Cidade);
admin.site.register(TipoUser);



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


# class ProfessorAdmin(admin.ModelAdmin):
#
#     model = Professor
#     list_display = ['registro_professor','nome']
#     list_filter  = ['registro_professor','nome']
#     search_fields = ['registro_professor','nome']
#     save_on_top = True
#
# admin.site.register(Professor,ProfessorAdmin);
#
# admin.site.register(Financeiro);
# admin.site.register(Responsavel);


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
    list_display  = ['id']
    list_filter   = ['id']
    search_fields = ['id']
    save_on_top = True
    delete_on_top = True

admin.site.register(Boletim,BoletimAdmin);



