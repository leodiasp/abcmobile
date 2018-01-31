# -*- coding: utf-8 -*-
from django.contrib import admin
from portal.models import Pais,Estado,Cidade, Instituicao, TabelaImportacao,ImportacaoCSV, ImagemUsuarios

# Register your models here.

admin.site.register(Pais);
admin.site.register(Estado);
admin.site.register(Cidade);

class InstituicaoAdmin(admin.ModelAdmin):

    model = Instituicao
    list_display = ['razaosocial','nomefantasia','cgc','inscestadual','telefone','email','endereco','complemento',
                    'bairro','cep','estado','cidade','contato','imagem','telefax','codigo']
    list_filter = ['razaosocial','nomefantasia','cgc','codigo','cidade','estado']
    search_fields = ['razaosocial','nomefantasia','cgc','codigo','cidade','estado']
    save_on_top = True

admin.site.register(Instituicao,InstituicaoAdmin)

# class TabelaImportacaoAdmin(admin.ModelAdmin):
#
#     model = TabelaImportacao
#     list_display = ['nome','descricao']
#     list_filter  = ['nome']
#     search_fields = ['nome']
#     save_on_top = True
#
# admin.site.register(TabelaImportacao, TabelaImportacaoAdmin)



class ImportacaoCSVAdmin(admin.ModelAdmin):

    model = ImportacaoCSV
    list_display = ['tabelaimportacao','dtupload', 'arquivo','stimportacao']
    list_filter  = ['tabelaimportacao','dtupload','stimportacao']
    search_fields = ['tabelaimportacao','dtupload','stimportacao']
    save_on_top = True

admin.site.register(TabelaImportacao);
admin.site.register(ImportacaoCSV, ImportacaoCSVAdmin);

class ImagemUsuariosAdmin(admin.ModelAdmin):

    model = ImagemUsuarios
    list_display = ['usuarios','imagem']
    list_filter  = ['usuarios','imagem']
    search_fields = ['usuarios','imagem']
    save_on_top = True

admin.site.register(ImagemUsuarios,ImagemUsuariosAdmin);




