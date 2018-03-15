# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django import forms

from portal.models import *
from django.forms.widgets import ClearableFileInput
from django.contrib.admin.widgets import AdminDateWidget


class UserForm(forms.ModelForm):

    imagem = forms.ImageField(widget=ClearableFileInput)

    class Meta:

        model = User

        fields = ['username','email','password','first_name','last_name','is_superuser']

        widgets = {

            'username': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'username', 'placeholder': 'Login de Acesso',
                'title': 'Login de Acesso'
            }),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'E-mail',
                       'title': 'E-mail'
                       }),
            'password': forms.PasswordInput(
                attrs={'class': 'form-control', 'id': 'password', 'placeholder': 'Senha',
                       'title': 'Senha'}),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'first_name', 'placeholder': 'Nome do Usuário', 'title': 'Nome do Usuário'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'last_name', 'placeholder': 'Ultimo Nome do Usuário',
                       'title': 'Ultimo Nome do Usuário'}),
            # 'is_usersuper' :forms.CheckboxInput(
            #     attrs={'class': 'form-control', 'id': 'is_superuser', 'placeholder': 'Administrador ?',
            #            'title': 'Administrador ?'}
            # )


        }

class InstituicaoForm(forms.ModelForm):
    imagem = forms.ImageField(widget=ClearableFileInput)
    class Meta:

        model = Instituicao
        estado = models.ForeignKey(Estado, null=True)
        cidade = models.ForeignKey(Cidade, null=True)
        fields = ['estado','cidade','razaosocial','nomefantasia','cgc','inscestadual','telefone','email','endereco','complemento',
                   'bairro','cep','contato','imagem','telefax','codigo','numero_alunos']


        widgets = {

            'estado': forms.Select(attrs={
                'class': 'form-control', 'id': 'uf', 'onfocus': "CarregaUF();", 'onclick': "CarregaCidade();"
            }),
            'cidade': forms.Select(attrs={'class': 'form-control', 'id': 'cidade'}),
            'razaosocial': forms.TextInput(attrs={
                'class': 'form-control','id': 'razaosocial', 'placeholder' : 'Razao Social'
            }),
            'nomefantasia': forms.TextInput(attrs={
                'class': 'form-control','id': 'nomefantasia', 'placeholder' : 'Nome Fantasia'
            }),
            'cgc': forms.TextInput(attrs={'class': 'form-control','id': 'cgc', 'placeholder' : 'CNPJ',
                                          'onKeyPress': "MascaraCNPJ(cgc);",
                                          'onBlur': "ValidaCNPJ(cgc)",
        }),
            'inscestadual':  forms.TextInput(attrs={'class': 'form-control','id': 'inscestadual', 'placeholder' : 'Insc. Estadual' }),
            'telefone':  forms.TextInput(attrs={'class': 'form-control','id': 'telefone', 'placeholder' : 'Telefone',
                                          'onKeyPress': "MascaraTelefone(telefone);",
                                          }),
            'email':  forms.TextInput(attrs={'class': 'form-control','id': 'email', 'placeholder' : 'E-mail' }),
            'endereco':  forms.TextInput(attrs={'class': 'form-control','id': 'endereco', 'placeholder' : 'Endereço' }),
            'complemento':  forms.TextInput(attrs={'class': 'form-control','id': 'complemento', 'placeholder' : 'Complemento' }),
            'bairro':  forms.TextInput(attrs={'class': 'form-control','id': 'bairro', 'placeholder' : 'Bairro' }),
            'cep':  forms.TextInput(attrs={'class': 'form-control','id': 'cep', 'placeholder' : 'Cep',
                                          'onKeyPress': "MascaraCep(cep);",
                                           }),
            'contato':  forms.TextInput(attrs={'class': 'form-control','id': 'contato', 'placeholder' : 'Contato' }),
            #'imagem':  forms.ImageField(attrs={'class': 'form-control','onclick':"UploadFoto();"}),
            #'imagem':  forms.TextInput(attrs={'class': 'form-control','id': 'imagem', 'placeholder' : 'Imagem' }),
            # 'dtcadastro':  forms.TextInput(attrs={'class': 'form-control','id': 'dtcadastro', 'placeholder' : 'Data Cadasttro',
            #                                       'readonly':'readonly' }),
            'telefax':  forms.TextInput(attrs={'class': 'form-control','id': 'telefax', 'placeholder' : 'Fax',
                                          'onKeyPress': "MascaraTelefone(telefax);",

                                               }),
            'codigo': forms.TextInput(attrs={'class': 'form-control','id': 'codigo', 'placeholder' : 'Código'}),
            'numero_alunos': forms.TextInput(attrs={'class': 'form-control','id': 'numero', 'placeholder' : 'Número / Aluno(s)'})


        }

class MensagemForm(forms.ModelForm):

    class Meta:

        model = Mensagem

        usuario = forms.ModelMultipleChoiceField(queryset=User.objects.none(), widget=forms.CheckboxSelectMultiple())

        fields = ['titulo','dtmensagem','descricao','stmensagem','usuario']

        widgets = {

            'titulo': forms.TextInput(attrs={
            'class': 'form-control','id': 'titulo', 'placeholder' : 'Título da Mensagem','title': 'Título', 'onblur': "SetUsuario();"
                }),
            'dtmensagem': forms.DateInput(format='%d/%m/%Y',attrs={
                'class': 'form-control','id': 'dtmensagem', 'placeholder' : 'Data da Mensagem','title': 'Data da Mensagem',
                'onKeyPress': "MascaraData(dtmensagem);"
                }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control','id': 'descricao', 'placeholder' : 'Texto da Mensagem', 'title':'Texto da Mensagem'
            }),
            # 'usuario': forms.MultipleChoiceField(attrs={
            #     'class': 'form-control','id': 'usuario'
            # }),



        }

class PeriodoLetivoForm(forms.ModelForm):
    class Meta:

        model = PeriodoLetivo
        instituicao = models.ForeignKey(Instituicao, null=True)

        fields = ['codigo','descricao','diasletivos','dtinicial','dtfinal','calendario']

        widgets = {

            # 'instituicao': forms.Select(attrs={
            #     'class': 'form-control', 'id': 'instituicao','select':'Instituição','title': 'Instituição'
            # }),
            'codigo': forms.TextInput(attrs={
                'class': 'form-control','id': 'codigo', 'placeholder' : 'Código','title': 'Código'
            }),
            'descricao': forms.TextInput(attrs={
                'class': 'form-control','id': 'descricao', 'placeholder' : 'Descrição do Período Letivo', 'title':'Descrição do Período Letivo'
            }),
            'diasletivos': forms.TextInput(attrs={'class': 'form-control','id': 'diasletivos', 'placeholder' : 'Dias Letivo',
                                                  'title': 'Dias Letivo'
                                                  }),
            'dtinicial':  forms.DateInput(format='%d/%m/%Y',attrs={'class': 'form-control','id': 'dtinicial', 'placeholder' : 'Data Inícial', 'title': 'Data Inicial',
                                          'onKeyPress': "MascaraData(dtinicial);"}),
            'dtfinal':  forms.DateInput(format='%d/%m/%Y',attrs={'class': 'form-control','id': 'dtfinal', 'placeholder' : 'Data Final','title': 'Data Final',
                                          'onKeyPress': "MascaraData(dtfinal);"}),
            'calendario':  forms.TextInput(attrs={'class': 'form-control','id': 'calendario', 'placeholder' : 'Calendário Período Letivo',
                                                  'title': 'Calendário' }),

        }

# class TurmaForm(forms.ModelForm):
#     class Meta:
#
#         model = Turma
#         #instituicao = models.ForeignKey(Instituicao, null=True)
#
#         fields = ['codigo','nome','abreviacao']
#
#         widgets = {
#
#             # 'instituicao': forms.Select(attrs={
#             #     'class': 'form-control', 'id': 'instituicao','select':'Instituição','title': 'Instituição'
#             # }),
#             #
#             # 'turma': forms.Select(attrs={
#             #     'class': 'form-control', 'id': 'turma','select':'Instituição','title': 'Instituição'
#             # }),
#             'codigo': forms.TextInput(attrs={
#                 'class': 'form-control','id': 'codigo', 'placeholder' : 'Código', 'title':'Código'
#             }),
#             'nome': forms.TextInput(attrs={
#                 'class': 'form-control','id': 'nome', 'placeholder' : 'Nome da Turma','title': 'Nome da Turma'
#             }),
#             'abreviacao': forms.TextInput(attrs={
#                 'class': 'form-control','id': 'nome', 'placeholder' : 'Abreviação da Turma','title': 'Abreviação da Turma'
#             }),
#
#         }
#
# class DisciplinaForm(forms.ModelForm):
#     class Meta:
#
#         model = Disciplina
#         instituicao = models.ForeignKey(Instituicao, null=True)
#
#
#         fields = ['codigo','nome','abreviacao']
#
#         widgets = {
#
#             # 'instituicao': forms.Select(attrs={
#             #     'class': 'form-control', 'id': 'instituicao', 'select': 'Instituição', 'title': 'Instituição'
#             # }),
#             # 'turma': forms.Select(attrs={
#             #     'class': 'form-control', 'id': 'turma', 'select': 'Turma', 'title': 'Turma'
#             # }),
#
#             'codigo': forms.TextInput(attrs={
#                 'class': 'form-control','id': 'codigo', 'placeholder' : 'Código'
#             }),
#             'nome': forms.TextInput(attrs={
#                 'class': 'form-control','id': 'nome', 'placeholder' : 'Nome da Disciplina'
#             }),
#             'abreviacao': forms.TextInput(attrs={
#                 'class': 'form-control','id': 'abreviacao', 'placeholder' : 'Abrev. Disciplina'
#             }),
#
#         }

# class TurmaDisciplinaForm(forms.ModelForm):
#     class Meta:
#
#         model = TurmaDisciplina
#         instituicao = models.ForeignKey(Instituicao, null=True)
#
#
#         fields = ['instituicao','codigo','codturma','nometurma','coddisciplina','nomedisciplina','disciplinaabreviado']
#
#         widgets = {
#
#             'instituicao': forms.Select(attrs={
#                 'class': 'form-control', 'id': 'instituicao', 'select': 'Instituição', 'title': 'Instituição','readonly':'readonly'
#             }),
#             # 'periodoletivo': forms.Select(attrs={
#             #     'class': 'form-control', 'id': 'periodoletivo', 'select': 'PeriodoLetivo', 'title': 'Instituição','readonly':'readonly'
#             # }),
#             'codigo': forms.TextInput(attrs={
#                 'class': 'form-control','id': 'codigo', 'placeholder' : 'Código', 'title': 'Código','readonly':'readonly'
#             }),
#             'codturma': forms.TextInput(attrs={
#                 'class': 'form-control','id': 'codturma', 'placeholder' : 'Código da Turma', 'title': 'Código da Turma','readonly':'readonly'
#             }),
#             'nometurma': forms.TextInput(attrs={
#                 'class': 'form-control','id': 'nometurma', 'placeholder' : 'Nome da Turma', 'title': 'Nome da Turma','readonly':'readonly'
#             }),
#              'coddisciplina': forms.TextInput(attrs={
#                 'class': 'form-control','id': 'coddisciplina', 'placeholder' : 'Código da Disciplina', 'title': 'Código da Disciplina','readonly':'readonly'
#             }),
#              'nomedisciplina': forms.TextInput(attrs={
#                 'class': 'form-control','id': 'nomedisciplina', 'placeholder' : 'Nome da Disciplina', 'title': 'Nome da Disciplina','readonly':'readonly'
#             }),
#             'disciplinaabreviado': forms.TextInput(attrs={
#                 'class': 'form-control','id': 'disciplinaabreviado', 'placeholder' : 'Abrev. Disciplina','title': 'Abrev. Disciplina','readonly':'readonly'
#             }),
#
#         }

class AlunoForm(forms.ModelForm):
    imagem = forms.ImageField(widget=ClearableFileInput)
    class Meta:

        model = Aluno
        instituicao = models.ForeignKey(Instituicao, null=True)

        fields = ['registro_aluno','nome','nome_abreviado','dtnascimento','sexo','cpf','identidade','email',
                  'endereco','complemento','bairro','cidade','uf','cep','telefone','telefone2', 'imagem']

        widgets = {

            # 'instituicao': forms.Select(attrs={
            #     'class': 'form-control', 'id': 'instituicao', 'select': 'Instituição', 'title': 'Instituição'
            # }),
            'registro_aluno': forms.TextInput(attrs={
                'class': 'form-control','id': 'registro_aluno', 'placeholder' : 'Registro do Aluno', 'title': 'Registro do Aluno',
                'readonly': 'readonly'

            }),
            # 'codigo': forms.TextInput(attrs={
            #     'class': 'form-control','id': 'codigo', 'placeholder' : 'Código', 'title': 'Código'
            # }),
            'nome': forms.TextInput(attrs={
                'class': 'form-control','id': 'nome', 'placeholder' : 'Nome do Professor', 'title': 'Nome do Professor'
            }),
            'nome_abreviado': forms.TextInput(attrs={
                'class': 'form-control','id': 'nome_abreviado', 'placeholder' : 'Nome Apelido', 'title': 'Nome Apelido'
            }),
             'dtnascimento': forms.DateInput(format='%d/%m/%Y', attrs={
                'class': 'form-control','id': 'data', 'placeholder' : 'Data de Nascimento', 'title': 'Data de Nascimento',
                 'onKeyPress':"MascaraData(dtnascimento);"
            }),
             'nomedisciplina': forms.TextInput(attrs={
                'class': 'form-control','id': 'nomedisciplina', 'placeholder' : 'Nome da Disciplina', 'title': 'Nome da Disciplina'
            }),
            'sexo': forms.TextInput(attrs={
                'class': 'form-control','id': 'sexo', 'placeholder' : 'Sexo','title': 'Sexo'
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control','id': 'cpf', 'placeholder' : 'CPF','title': 'CPF',
                'onKeyPress': "MascaraCPF(cpf);"
            }),
            'identidade': forms.TextInput(attrs={
                'class': 'form-control','id': 'identidade', 'placeholder' : 'Identidade','title': 'Identidade',
                'onKeyPress': "MascaraRG(identidade);"

            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control','id': 'email', 'placeholder' : 'E-mail','title': 'E-mail'

            }),
            'endereco': forms.TextInput(attrs={
                'class': 'form-control','id': 'endereco', 'placeholder' : 'Endereço','title': 'Endereço'

            }),
            'complemento': forms.TextInput(attrs={
                'class': 'form-control','id': 'complemento', 'placeholder' : 'Complemento','title': 'Complemento'

            }),
            'bairro': forms.TextInput(attrs={
                'class': 'form-control','id': 'bairro', 'placeholder' : 'Bairro','title': 'Bairro'

            }),
            'cidade': forms.TextInput(attrs={
                'class': 'form-control','id': 'cidade', 'placeholder' : 'Cidade','title': 'Cidade'

            }),
            'uf': forms.TextInput(attrs={
                'class': 'form-control','id': 'uf', 'placeholder' : 'UF','title': 'UF'

            }),
            'cep': forms.TextInput(attrs={
                'class': 'form-control','id': 'cep', 'placeholder' : 'Cep','title': 'Cep'

            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control','id': 'telefone', 'placeholder' : 'Telefone','title': 'Telefone',
                'onKeyPress': "MascaraTelefone(telefone);"

            }),
            'telefone2': forms.TextInput(attrs={
                'class': 'form-control','id': 'celular', 'placeholder' : 'Celular','title': 'Celular',
                'onKeyPress': "MascaraTelefone(celular);"

            }),

        }

class ProfessorForm(forms.ModelForm):
    imagem = forms.ImageField(widget=ClearableFileInput)
    class Meta:

        model = Professor
        instituicao = models.ForeignKey(Instituicao, null=True)

        fields = ['registro_professor','nome','nome_abreviado','dtnascimento','sexo','cpf','identidade','email',
                  'endereco','complemento','bairro','cidade','uf','cep','telefone','telefone2', 'imagem']

        widgets = {

            # 'instituicao': forms.Select(attrs={
            #     'class': 'form-control', 'id': 'instituicao', 'select': 'Instituição', 'title': 'Instituição'
            # }),
            'registro_professor': forms.TextInput(attrs={
                'class': 'form-control','id': 'registro_professor', 'placeholder' : 'Registro do Professor', 'title': 'Registro do Professor',
                'readonly': 'readonly'

            }),
            # 'codigo': forms.TextInput(attrs={
            #     'class': 'form-control','id': 'codigo', 'placeholder' : 'Código', 'title': 'Código'
            # }),
            'nome': forms.TextInput(attrs={
                'class': 'form-control','id': 'nome', 'placeholder' : 'Nome do Professor', 'title': 'Nome do Professor'
            }),
            'nome_abreviado': forms.TextInput(attrs={
                'class': 'form-control','id': 'nome_abreviado', 'placeholder' : 'Nome Apelido', 'title': 'Nome Apelido'
            }),
             'dtnascimento': forms.DateInput(format='%d/%m/%Y',attrs={
                'class': 'form-control','id': 'dtnascimento', 'placeholder' : 'Data de Nascimento', 'title': 'Data de Nascimento',
                 'onKeyPress':"MascaraData(dtnascimento);"
            }),
             'nomedisciplina': forms.TextInput(attrs={
                'class': 'form-control','id': 'nomedisciplina', 'placeholder' : 'Nome da Disciplina', 'title': 'Nome da Disciplina'
            }),
            'sexo': forms.TextInput(attrs={
                'class': 'form-control','id': 'sexo', 'placeholder' : 'Sexo','title': 'Sexo'
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control','id': 'cpf', 'placeholder' : 'CPF','title': 'CPF',
                'onKeyPress': "MascaraCPF(cpf);"
            }),
            'identidade': forms.TextInput(attrs={
                'class': 'form-control','id': 'identidade', 'placeholder' : 'Identidade','title': 'Identidade',
                'onKeyPress': "MascaraRG(identidade);"

            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control','id': 'email', 'placeholder' : 'E-mail','title': 'E-mail'

            }),
            'endereco': forms.TextInput(attrs={
                'class': 'form-control','id': 'endereco', 'placeholder' : 'Endereço','title': 'Endereço'

            }),
            'complemento': forms.TextInput(attrs={
                'class': 'form-control','id': 'complemento', 'placeholder' : 'Complemento','title': 'Complemento'

            }),
            'bairro': forms.TextInput(attrs={
                'class': 'form-control','id': 'bairro', 'placeholder' : 'Bairro','title': 'Bairro'

            }),
            'cidade': forms.TextInput(attrs={
                'class': 'form-control','id': 'cidade', 'placeholder' : 'Cidade','title': 'Cidade'

            }),
            'uf': forms.TextInput(attrs={
                'class': 'form-control','id': 'uf', 'placeholder' : 'UF','title': 'UF'

            }),
            'cep': forms.TextInput(attrs={
                'class': 'form-control','id': 'cep', 'placeholder' : 'Cep','title': 'Cep'

            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control','id': 'telefone', 'placeholder' : 'Telefone','title': 'Telefone',
                'onKeyPress': "MascaraTelefone(telefone);"

            }),
            'telefone2': forms.TextInput(attrs={
                'class': 'form-control','id': 'telefone2', 'placeholder' : 'Telefone2','title': 'Telefone2',
                'onKeyPress': "MascaraTelefone(telefone2);"

            }),

        }


class ResponsavelForm(forms.ModelForm):
    imagem = forms.ImageField(widget=ClearableFileInput)
    class Meta:

        model = Responsavel
        instituicao = models.ForeignKey(Instituicao, null=True)

        fields = ['registro_responsavel','nome','nome_abreviado','dtnascimento','sexo','cpf','identidade','email',
                  'endereco','complemento','bairro','cidade','uf','cep','telefone','telefone2', 'imagem']

        widgets = {

            # 'instituicao': forms.Select(attrs={
            #     'class': 'form-control', 'id': 'instituicao', 'select': 'Instituição', 'title': 'Instituição'
            # }),
            'registro_responsavel': forms.TextInput(attrs={
                'class': 'form-control','id': 'registro_professor', 'placeholder' : 'Registro do Responsavel', 'title': 'Registro do Responsavel',
                'readonly': 'readonly'

            }),
            # 'codigo': forms.TextInput(attrs={
            #     'class': 'form-control','id': 'codigo', 'placeholder' : 'Código', 'title': 'Código'
            # }),
            'nome': forms.TextInput(attrs={
                'class': 'form-control','id': 'nome', 'placeholder' : 'Nome do Professor', 'title': 'Nome do Professor'
            }),
            'nome_abreviado': forms.TextInput(attrs={
                'class': 'form-control','id': 'nome_abreviado', 'placeholder' : 'Nome Apelido', 'title': 'Nome Apelido'
            }),
             'dtnascimento': forms.DateInput(format='%d/%m/%Y',attrs={
                'class': 'form-control','id': 'dtnascimento', 'placeholder' : 'Data de Nascimento', 'title': 'Data de Nascimento',
                 'onKeyPress':"MascaraData(dtnascimento);"
            }),
             'nomedisciplina': forms.TextInput(attrs={
                'class': 'form-control','id': 'nomedisciplina', 'placeholder' : 'Nome da Disciplina', 'title': 'Nome da Disciplina'
            }),
            'sexo': forms.TextInput(attrs={
                'class': 'form-control','id': 'sexo', 'placeholder' : 'Sexo','title': 'Sexo'
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control','id': 'cpf', 'placeholder' : 'CPF','title': 'CPF',
                'onKeyPress': "MascaraCPF(cpf);"
            }),
            'identidade': forms.TextInput(attrs={
                'class': 'form-control','id': 'identidade', 'placeholder' : 'Identidade','title': 'Identidade',
                'onKeyPress': "MascaraRG(identidade);"

            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control','id': 'email', 'placeholder' : 'E-mail','title': 'E-mail'

            }),
            'endereco': forms.TextInput(attrs={
                'class': 'form-control','id': 'endereco', 'placeholder' : 'Endereço','title': 'Endereço'

            }),
            'complemento': forms.TextInput(attrs={
                'class': 'form-control','id': 'complemento', 'placeholder' : 'Complemento','title': 'Complemento'

            }),
            'bairro': forms.TextInput(attrs={
                'class': 'form-control','id': 'bairro', 'placeholder' : 'Bairro','title': 'Bairro'

            }),
            'cidade': forms.TextInput(attrs={
                'class': 'form-control','id': 'cidade', 'placeholder' : 'Cidade','title': 'Cidade'

            }),
            'uf': forms.TextInput(attrs={
                'class': 'form-control','id': 'uf', 'placeholder' : 'UF','title': 'UF'

            }),
            'cep': forms.TextInput(attrs={
                'class': 'form-control','id': 'cep', 'placeholder' : 'Cep','title': 'Cep'

            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control','id': 'telefone', 'placeholder' : 'Telefone','title': 'Telefone',
                'onKeyPress': "MascaraTelefone(telefone);"

            }),
            'telefone2': forms.TextInput(attrs={
                'class': 'form-control','id': 'telefone2', 'placeholder' : 'Telefone2','title': 'Telefone2',
                'onKeyPress': "MascaraTelefone(telefone2);"

            }),

        }

