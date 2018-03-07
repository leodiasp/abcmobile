# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect,get_object_or_404, render_to_response # funcoes de renderizacao dos templates
from django.contrib.auth import authenticate,login,logout
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime

from portal.models import *
from portal.forms import *

from django.db.models import Sum, Avg, FloatField, Count

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile


from django.utils.formats import localize

import csv
import codecs
import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf8')


from datetime import datetime
# Create your views here.

@login_required
def portal(request):

   #Instituicao
    instituicao = Instituicao.objects.all()

   # Alunos
    alunos = Aluno.objects.all()

    # Total Alunos
    totAlunos = alunos.count()

    professores = Professor.objects.all()

    # Total Professor
    totProfessores = professores.count()

    # Total Responsavel
    responsavel = Responsavel.objects.all()
    totResponsavel = responsavel.count()

    # Pagtos Confirmados
    totTitulosPagos = Financeiro.objects.filter(dtbaixa__isnull= False).aggregate(total=Sum('vlr_titulo'))

    # Pagtos Pendentes
    totTitulosAbertos = Financeiro.objects.filter(dtbaixa__isnull= True).aggregate(total=Sum('vlr_titulo'))

    #Mensagem
    totMensagem = Mensagem.objects.all()

    return render(request,'index.html',{'instituicao': instituicao,
                                        'alunos': alunos,
                                        'professores': professores,
                                        'totAlunos': totAlunos,
                                        'totProfessor': totProfessores,
                                        'totResponsavel': totResponsavel,
                                        'totTitulosPagos': totTitulosPagos,
                                        'totTitulosAbertos':totTitulosAbertos,
                                        'totMensagem': totMensagem

                                        })

def mensagem(request, template="mensagem.html"):

    # usuario = User.objects.filter(pk=request.user.pk)
    # print("Usuario", request.user.pk)
    mensagem = Mensagem.objects.all()

    return render (request,template,{'alerta':mensagem})

def mensagem_new(request,template='form_mensagem.html'):

    mensagem = Mensagem.objects.all()

    if request.method == "POST":
        form = MensagemForm(request.POST, request.FILES or None )

        if form.is_valid():

            form.save()


        # titulo = request.POST['titulo']
        # dtmensagem = request.POST['dtmensagem']
        # descricao = request.POST['descricao']
        # stmensagem = 0
        # #usuario_id = request.user.pk
        #
        # mensagem = Mensagem.objects.create(titulo=titulo,
        #                                    #dtmensagem=dtmensagem,
        #                                    dtmensagem= datetime.strptime(dtmensagem, '%d/%m/%Y').strftime('%Y-%m-%d'),
        #                                    stmensagem = stmensagem,
        #                                    descricao= descricao,usuario_id=request.user.pk)
        #
        # mensagem.save()
        messages.success(request, " Operação Realizada com Sucesso ! ")
        return redirect('mensagem.html')
    else:
        form = MensagemForm(request.POST or None)

    return render(request,template,{'form':form})

def mensagem_edit(request,pk,template_name='form_mensagem.html'):

    mensagem = get_object_or_404(Mensagem, pk=pk)

    if request.method == "POST":
        form = MensagemForm(request.POST, request.FILES, instance=mensagem)
        if form.is_valid():
            mensagem = form.save()
            messages.success(request, " Operação Realizada com Sucesso ! ")
        return render(request, template_name, {'form': form})
    else:
        form = MensagemForm(instance=mensagem)
    return render(request, template_name, {'form': form})



def administracao(request):

    if request.user.is_superuser:
        return redirect('/admin/')
    else:
        return redirect('/portal/')

def perfil(request):

    if request.user.is_superuser:
        #return redirect('/admin/auth/user/')
        return redirect('/admin/auth/user/')
    else:
        return redirect('/portal/')

def upload(request):

    if request.user.is_superuser:
        return redirect ('/admin/portal/importacaocsv/')
    else:
        return redirect('/portal/')


# def set_imagem(usuario):
#
#     #imagem_usuario = ImagemUsuarios.objects.all().filter(usuarios=usuario)
#     imagem_usuario = ImagemUsuarios.objects.all().filter(usuarios=usuario)
#
#     return imagem_usuario

def do_login(request, *args, **kwargs):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/portal/')

    return render(request, 'login.html')

def do_logout(request):
    logout(request)
    return redirect('/login/')

@login_required()
def inbox(request,template='inbox.html'):

    return render(request,template,{'mensagem': 'Mensagem'})

def usuario_new(request, template="form_usuario.html"):

    if request.method =="POST":

        #form = UserForm(request.POST, request.FILES or None)

        username =  request.POST['username']
        email    =  request.POST['email']
        password =   request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        imagem = request.FILES['imagem']

        usuario = User.objects.create_superuser(username=username,email=email,password=password,first_name=first_name,
                                                last_name=last_name, imagem=imagem)
        usuario.save()
        messages.success(request, " Operação Realizada com Sucesso ! ")
        return redirect('/portal/')
    else:
        form = UserForm(request.POST, request.FILES or None)

    return render(request,template,{'form':form})

def usuario_edit(request, pk, template="form_usuario.html"):

    usuario = get_object_or_404(User, pk=pk)

    src_imagem = usuario.imagem

    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            usuario = form.save()
            messages.success(request, " Operação Realizada com Sucesso ! ")
            return redirect('/portal/')
    else:
        form = UserForm(instance=usuario)
    return render(request, template, {'form': form})

    # if request.method =="POST":
    #
    #     #form = UserForm(request.POST, request.FILES or None)
    #
    #     username =  request.POST['username']
    #     email    =  request.POST['email']
    #     password =   request.POST['password']
    #     first_name = request.POST['first_name']
    #     last_name = request.POST['last_name']
    #     imagem = request.FILES['imagem']
    #     print("Imagem: ",imagem)
    #
    #     usuario = User.objects.create_superuser(username=username,email=email,password=password,first_name=first_name,
    #                                             last_name=last_name, imagem=imagem)
    #     usuario.save()
    #     messages.success(request, " Operação Realizada com Sucesso ! ")
    #     return redirect('/portal/')
    # else:
    #     form = UserForm(request.POST, request.FILES or None)
    #
    # return render(request,template,{'form':form})

def instituicao(request,template="instituicao.html"):

    dados = Instituicao.objects.all()

    return render(request,template,{'instituicao': dados})

def instituicao_new(request,template='form_instituicao.html'):

    #estado = Estado.objects.all()
    estado = Estado.objects.all()
    cidade = Cidade.objects.all()

    if request.method == "POST":
        form = InstituicaoForm(request.POST, request.FILES or None )

        if form.is_valid():

            form.save()
            messages.success(request, " Operação Realizada com Sucesso ! ")
            # return redirect('instituicao.html')

    else:
        form = InstituicaoForm(request.POST or None)

    return render(request,template,{'form':form,'estado': estado,'cidade': cidade})

def instituicao_edit(request,pk,template_name='form_instituicao.html'):

    instituicao = get_object_or_404(Instituicao, pk=pk)

    estado = Estado.objects.all()
    cidade = Cidade.objects.all()

    src_imagem = instituicao.imagem

    print(src_imagem)

    if request.method == "POST":
        form = InstituicaoForm(request.POST, request.FILES, instance=instituicao)
        if form.is_valid():
            instituicao = form.save()
            messages.success(request, " Operação Realizada com Sucesso ! ")
            #return redirect('portal:instituicao_new')
    else:
        form = InstituicaoForm(instance=instituicao)
    return render(request, template_name, {'form': form,'estado': estado,'cidade': cidade,
                                           'fotos': str(src_imagem).encode('utf-8')})

# CLASSE PERIODO LETIVO ===============================================================================================
def periodoletivo(request,template="periodoletivo.html"):

    periodoletivo = PeriodoLetivo.objects.all()

    return render(request,template,{'periodoletivo': periodoletivo})

def periodoletivo_new(request,template='form_periodoletivo.html'):

    periodoletivo = PeriodoLetivo.objects.all()

    if request.method == "POST":
        form = PeriodoLetivoForm(request.POST, request.FILES or None )

        if form.is_valid():

            form.save()
            messages.success(request, " Operação Realizada com Sucesso ! ")
            return redirect('periodoletivo.html')
    else:
        form = PeriodoLetivoForm(request.POST or None)

    return render(request,template,{'form':form})

def periodoletivo_edit(request,pk,template_name='form_periodoletivo.html'):

    periodoletivo = get_object_or_404(PeriodoLetivo, pk=pk)

    if request.method == "POST":
        form = PeriodoLetivoForm(request.POST, request.FILES, instance=periodoletivo)
        if form.is_valid():
            periodoletivo = form.save()
            messages.success(request, " Operação Realizada com Sucesso ! ")
        return render(request, template_name, {'form': form, 'img_usuario':set_imagem(request.user)})
    else:
        form = PeriodoLetivoForm(instance=periodoletivo)
    return render(request, template_name, {'form': form,'img_usuario':set_imagem(request.user)})

# CLASSE ALUNO ===============================================================================================
def aluno(request,template="aluno.html"):

    dados = Aluno.objects.all()

    return render(request,template,{'dados': dados})

def form_aluno(request, pk, template_name="form_aluno.html"):

    alunos = get_object_or_404(Aluno, pk=pk)

    estado = Estado.objects.all()
    cidade = Cidade.objects.all()

    src_imagem = alunos.imagem

    print("Foto:",src_imagem)

    if request.method == "POST":
        form = AlunoForm(request.POST, request.FILES, instance=alunos)
        if form.is_valid():
            alunos = form.save()
            messages.success(request, " Operação Realizada com Sucesso ! ")
            #return redirect('portal:alunos')
    else:
        form = AlunoForm(instance=alunos)
        # return render(request, template_name, {'form': form, 'estado': estado, 'cidade': cidade,
        #                                        'img_usuario': set_imagem(request.user), 'fotos': str(src_imagem).encode('utf-8')})

    boletim = Boletim.objects.all().filter(aluno_id=alunos)

    if boletim:
        disciplinas = boletim.values_list('disciplina', flat=True).distinct()
        mensagem = 'Boletim Acadêmico'

        return render(request, template_name, {'form': form, 'estado': estado, 'cidade': cidade,
                                               'fotos': str(src_imagem).encode('utf-8'),
                                               'disciplina': disciplinas,'boletim': boletim, 'mensagem': mensagem
                                              })
    else:
        mensagem = ' '
        # return render(request, template_name, {'aluno': alunos,
        #                                        'img_usuario': set_imagem(request.user),
        #                                        'mensagem': mensagem})

        return render(request, template_name, {'form': form, 'estado': estado, 'cidade': cidade,
                                               'fotos': str(src_imagem).encode('utf-8'),
                                               'mensagem': mensagem
                                              })

# CLASSE PROFESSOR ===============================================================================================
def professor(request,template="professor.html"):

    dados = Professor.objects.all()

    return render(request,template,{'dados': dados})

def form_professor(request, pk, template_name="form_professor.html"):

    professores = get_object_or_404(Professor, pk=pk)
    # return render(request, template_name, {'professor': professores,
    #                                        'img_usuario': set_imagem(request.user)})

    estado = Estado.objects.all()
    cidade = Cidade.objects.all()

    src_imagem = professores.imagem

    print(src_imagem)

    if request.method == "POST":
        form = ProfessorForm(request.POST, request.FILES, instance=professores)
        if form.is_valid():
            professores = form.save()
            messages.success(request, " Operação Realizada com Sucesso ! ")
            #return redirect('portal:responsavel')
    else:
        form = ProfessorForm(instance=professores)
    return render(request, template_name, {'form': form,'estado': estado,'cidade': cidade,
                                           'fotos': str(src_imagem).encode('utf-8')})

# CLASSE RESPONSAVEL ===============================================================================================
def responsavel(request,template="responsavel.html"):

    dados = Responsavel.objects.all()

    return render(request,template,{'dados': dados})

def form_responsavel(request, pk, template_name="form_responsavel.html"):

    responsavel = get_object_or_404(Responsavel, pk=pk)

    estado = Estado.objects.all()
    cidade = Cidade.objects.all()

    src_imagem = responsavel.imagem

    print(src_imagem)

    if request.method == "POST":
        form = ResponsavelForm(request.POST, request.FILES, instance=responsavel)
        if form.is_valid():
            instituicao = form.save()
            messages.success(request, " Operação Realizada com Sucesso ! ")
    else:
        form = ResponsavelForm(instance=responsavel)
    # return render(request, template_name, {'form': form,'estado': estado,'cidade': cidade, 'responsavel': responsavel
    #                                        ,'img_usuario':set_imagem(request.user),'fotos': str(src_imagem).encode('utf-8')})

    financeiro = Financeiro.objects.all().filter(responsavel_id=responsavel)

    if financeiro:
        # nome_responsavel = responsavel.nome
        # mensagem = 'Boletim Acadêmico'

        return render(request, template_name, {'form': form, 'estado': estado, 'cidade': cidade,
                                               'fotos': str(src_imagem).encode('utf-8'),
                                               'financeiro': financeiro, 'responsavel': responsavel
                                              })
    else:
        mensagem = ' '
        # return render(request, template_name, {'aluno': alunos,
        #                                        'img_usuario': set_imagem(request.user),
        #                                        'mensagem': mensagem})

        return render(request, template_name, {'form': form, 'estado': estado, 'cidade': cidade,
                                               'fotos': str(src_imagem).encode('utf-8'),
                                               'responsavel': responsavel
                                              })


# CLASSE FINANCEIRO ===============================================================================================
# def financeiro(request, pk, template="financeiro.html"):
#
#     responsavel = Responsavel.objects.all().filter(pk=pk)
#     dados = Financeiro.objects.all().filter(responsavel_id=pk)
#     # disciplinas = boletim.values_list('disciplina', flat=True).distinct()
#     #dados = Financeiro.objects.all();
#
#     return render(request,template,{'dados': dados,'responsavel': responsavel, 'img_usuario':set_imagem(request.user)})


def form_boletim(request, pk, template_name="boletim.html"):

    alunos = Aluno.objects.all().filter(pk=pk)

    print("Aluno",aluno)

    return render(request, template_name, {'aluno': alunos})

# CLASSE IMPORTACAO CSV ===============================================================================================

def upload_csv (request):

    return redirect('admin/portal/importacaocsv/')
    #return redirect('/admin/auth/user/')

def importacao_csv(request, pk, template_name="importar_csv.html"):

     importacaocsv = ImportacaoCSV.objects.all().filter(pk=pk)

     if not(importacaocsv):

         importacaocsv = ImportacaoCSV.objects.all().filter(stimportacao=False)
         return render(request, template_name, {'importacaocsv': importacaocsv})

     else:

         tabelaimportacao = TabelaImportacao.objects.all().filter(importacaocsv=importacaocsv)

         for regtabelaimportacao in tabelaimportacao:

             for regimportacaocsv in importacaocsv:

                 dtatual = datetime.now().strftime('%Y-%m-%d')

                 arquivo = regimportacaocsv.arquivo
                 csvfile = arquivo
                 dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
                 csvfile.open()
                 reader = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=str(u';').encode('utf-8'), dialect=dialect)
                 csvfile.read(3)
                 dados = reader

                 arquivo = dados

                 for row in reader:

                     print ('CSV: ', row)

                     instituicao = Instituicao.objects.all().filter(codigo=row[0])

                     # ALUNO
                     if regtabelaimportacao.nome == 'ALUNO':

                         t_csv = Aluno(registro_aluno=row[0],
                                       nome=row[1],
                                       nome_abreviado=row[2],
                                       # dtnascimento=row[3],
                                       dtnascimento= datetime.strptime(row[3],'%d/%m/%Y').strftime('%Y-%m-%d'),
                                       sexo=row[4],
                                       cpf=row[5],
                                       identidade=row[6],
                                       email=row[7],
                                       endereco=str(row[8]).decode('latin-1').encode('utf-8'),
                                       complemento=row[9],
                                       bairro=row[10],
                                       cidade=row[11],
                                       uf=row[12],
                                       cep=row[13],
                                       telefone=row[14],
                                       telefone2=row[15],
                                       responsavel_id=row[16]
                                       )

                     # PROFESSOR
                     if regtabelaimportacao.nome == 'PROFESSOR':

                         t_csv = Professor(registro_professor=row[0],
                                           nome=row[1],
                                           nome_abreviado=row[2],
                                           # dtnascimento=row[3],
                                           dtnascimento= datetime.strptime(row[3],'%d/%m/%Y').strftime('%Y-%m-%d'),
                                           sexo=row[4],
                                           cpf=row[5],
                                           identidade=row[6],
                                           email=row[7],
                                           endereco=str(row[8]).decode('latin-1').encode('utf-8'),
                                           complemento=row[9],
                                           bairro=row[10],
                                           cidade=row[11],
                                           uf=row[12],
                                           cep=row[13],
                                           telefone=row[14],
                                           telefone2=row[15]
                                           )

                     # # PROFESSOR
                     # if regtabelaimportacao.nome == 'PROFESSOR':
                     #
                     #     t_csv = Professor(periodoletivo=row[0],
                     #                       aluno=row[1],
                     #                       nome_abreviado=row[2],
                     #                       # dtnascimento=row[3],
                     #                       dtnascimento= datetime.strptime(row[3],'%d/%m/%Y').strftime('%Y-%m-%d'),
                     #                       sexo=row[4],
                     #                       cpf=row[5],
                     #                       identidade=row[6],
                     #                       email=row[7],
                     #                       endereco=str(row[8]).decode('latin-1').encode('utf-8'),
                     #                       complemento=row[9],
                     #                       bairro=row[10],
                     #                       cidade=row[11],
                     #                       uf=row[12],
                     #                       cep=row[13],
                     #                       telefone=row[14],
                     #                       telefone2=row[15]
                     #                   )

                     # BOLETIM
                     if regtabelaimportacao.nome == 'BOLETIM':

                         t_csv = Boletim(periodoletivo_id=row[0],
                                         aluno_id=row[1],
                                         curso=row[2],
                                         serie=row[3],
                                         turno=row[4],
                                         turma=row[5],
                                         disciplina=row[6],
                                         etapa=row[7],
                                         notas=row[8],
                                         faltas=row[9]
                                         )

                     # RESPONSAVEL
                     if regtabelaimportacao.nome == 'RESPONSAVEL':

                         t_csv = Responsavel(registro_responsavel=row[0],
                                             nome=row[1],
                                             nome_abreviado=row[2],
                                             # dtnascimento=row[3],
                                             dtnascimento= datetime.strptime(row[3],'%d/%m/%Y').strftime('%Y-%m-%d'),
                                             sexo=row[4],
                                             cpf=row[5],
                                             identidade=row[6],
                                             email=row[7],
                                             endereco=str(row[8]).decode('latin-1').encode('utf-8'),
                                             complemento=row[9],
                                             bairro=row[10],
                                             cidade=row[11],
                                             uf=row[12],
                                             cep=row[13],
                                             telefone=row[14],
                                             telefone2=row[15]
                                             )


                     # FINANCEIRO
                     if regtabelaimportacao.nome == 'FINANCEIRO':

                         t_csv = Financeiro(periodoletivo_id=row[0],
                                            responsavel_id=row[1],
                                            documento = row[2],
                                            parcela = row[3],
                                            historico=row[4],
                                            dtemissao = datetime.strptime(row[5],'%d/%m/%Y').strftime('%Y-%m-%d'),
                                            vlr_titulo = row[6],
                                            dtbaixa = datetime.strptime(row[7],'%d/%m/%Y').strftime('%Y-%m-%d'),
                                            vlr_baixa = row[8],
                                            vlr_juros = row[9],
                                            vlr_desconto = row[10]
                                            )

                     try:

                         t_csv.save()
                         # # --> Muda o STImportacao e coloca a data atual
                         # regimportacaocsv.dtimportacao = dtatual
                         # regimportacaocsv.stimportacao = True
                         # regimportacaocsv.save()
                         mensagem = "Processado: %s | %s" % (dados.line_num,row)
                         #mensagem = (dados.line_num)
                         messages.success(request, mensagem)

                     except Exception:
                     #except ValueError:
                         mensagem = "Linha: %s | %s" % (dados.line_num,row)
                         messages.error(request, mensagem)

                 return render(request, template_name,{'importacaocsv': importacaocsv})
