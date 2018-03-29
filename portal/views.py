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

from django.db.models import Sum, Avg, FloatField, Count, F

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile


from django.utils.formats import localize

import json
import decimal

import csv
import codecs
import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf8')


from datetime import datetime
# Create your views here.

def mobile(request):

    return redirect('mobile:index')

@login_required
def portal(request):

   #Instituicao
    instituicao = Instituicao.objects.all()

   # Alunos

    if request.user.is_superuser:
        alunos = Aluno.objects.all()
    else:
        alunos = Aluno.objects.filter(responsavel_id=request.user.responsavel_id)


    # Total Alunos
    totAlunos = alunos.count()

    professores = Professor.objects.all()

    # Total Professor
    totProfessores = professores.count()

    # Total Responsavel
    responsavel = Responsavel.objects.all()
    totResponsavel = responsavel.count()

    # Pagtos Confirmados
#    totTitulosPagos = Financeiro.objects.filter(dtbaixa__isnull= False).aggregate(total=Sum('vlr_titulo'))
    totTitulosPagos = Financeiro.objects.all().exclude(dtbaixa= 'NULL')

    # Pagtos Pendentes
#    totTitulosAbertos = Financeiro.objects.filter(dtbaixa__isnull= True).aggregate(total=Sum('vlr_titulo'))
    totTitulosAbertos = Financeiro.objects.filter(dtbaixa = 'NULL')

    #Mensagem
    totMensagem = Mensagem.objects.all()

    return render(request,'index.html',{'instituicao': instituicao,
                                        'alunos': alunos,
                                        'professores': professores,
                                        'totAlunos': totAlunos,
                                        'totProfessor': totProfessores,
                                        'totResponsavel': totResponsavel,
                                        'totTitulosPagos': totTitulosPagos.count(),
                                        'totTitulosAbertos':totTitulosAbertos.count(),
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
                #if user.is_superuser:
                return redirect('/portal/')
                # else:
                #     return redirect('mobile:index')

    return render(request, 'login.html')

def do_logout(request):
    logout(request)
    return redirect('/login/')

@login_required()
def inbox(request,template='inbox.html'):

    return render(request,template,{'mensagem': 'Mensagem'})


def responsavel_usuario (request,template_name="usuario.html"):

    #responsavel = Responsavel.objects.all()
    usuario = User.objects.all()

    return render(request,template_name,{'usuario':usuario})

    # for reg in responsavel:
    #
    #     username = reg.cpf
    #     email =    reg.email
    #     password = reg.cpf
    #     first_name = reg.nome
    # #    last_name = request.POST['last_name']
    #     imagem = reg.imagem
    #
    #     responsavel = reg.pk
    #
    #     usuario = User.objects.create_user(username=username, email=email, password=password, first_name=first_name,
    #                                        imagem=imagem,responsavel_id=responsavel )
    #     usuario.save()
    #
    #     # reg.usuario = request.user.pk
    #     # reg.save()
    #
    # messages.success(request, " Usuários x Responsável Criado com Sucesso ! ")
    # return redirect('/portal/')

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

    #usuario = get_object_or_404(User, pk=pk)
    #usuario = User.objects.filter(pk=pk)

    #if (usuario):
    if pk!=0:

        #print("Usuario",usuario)

        usuario = get_object_or_404(User, pk=pk)

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
    else:

        responsavel = Responsavel.objects.all()

        for reg in responsavel:

            username = reg.cpf
            #username = reg.email
            email =    reg.email
            password = reg.cpf
            first_name = reg.nome
        #    last_name = request.POST['last_name']
            imagem = reg.imagem

            reg_id = reg.pk

            usuario = User.objects.create_user(username=username, email=email, password=password, first_name=first_name,
                                               imagem=imagem,responsavel_id=reg_id )
            usuario.save()

            # reg.usuario = request.user.pk
            # reg.save()

        messages.success(request, " Usuários x Responsável Criado com Sucesso ! ")
        return redirect('/responsavel_usuario/')


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
        return render(request, template_name, {'form': form})
    else:
        form = PeriodoLetivoForm(instance=periodoletivo)
    return render(request, template_name, {'form': form})

# CLASSE ALUNO ===============================================================================================
def aluno(request,template="aluno.html"):

    dados = Aluno.objects.all()

    return render(request,template,{'dados': dados})

def form_aluno(request, pk, template_name="form_aluno.html"):

    alunos = get_object_or_404(Aluno, pk=pk)

    estado = Estado.objects.all()
    cidade = Cidade.objects.all()

    src_imagem = alunos.imagem

    if request.method == "POST":
        form = AlunoForm(request.POST, request.FILES, instance=alunos)
        if form.is_valid():
            alunos = form.save()
            messages.success(request, " Operação Realizada com Sucesso ! ")
            #return redirect('portal:alunos')
    else:
        form = AlunoForm(instance=alunos)
        # return render(request, template_name, {'form': form, 'estado': estado, 'cidade': cidade,
        #                                        'fotos': str(src_imagem).encode('utf-8')})

    periodoletivo = PeriodoLetivo.objects.filter(dtfinal__isnull=True)
    boletim = Boletim.objects.filter(aluno_id=alunos,periodoletivo_id=periodoletivo)

    if boletim:

        turma = boletim.values_list('turma', flat=True).distinct()
        disciplinas = boletim.values_list('disciplina', flat=True).distinct()
        nome_disciplinas = boletim.values_list('nome_disciplina', flat=True).distinct()

        for qryPeriodoLetivo in periodoletivo:
            mensagem = "Boletim Acadêmico - %s" % (qryPeriodoLetivo.codigo)

        mAluno = boletim.values('disciplina','nome_disciplina').annotate(media_disc=Avg(F('notas')))

        #valor1 = mAluno

        print("Valor1:",mAluno)
        #mTurma = boletim.values('turma','disciplina').annotate(media_turma=Avg(F('notas')))
        #mTurma = Boletim.objects.values('turma','disciplina').annotate(media_turma=Avg(F('notas'))).filter(turma=202)
        mTurma = Boletim.objects.values('turma','disciplina','nome_disciplina').annotate(media_turma=Avg(F('notas'))).filter(turma=turma, periodoletivo_id=periodoletivo)

        print("Valor2:",mTurma)
        #return render(request, template_name, {'valor1': json.dumps(valor1), 'valor2': json.dumps(valor2)})

        return render(request, template_name, {'form': form, 'estado': estado, 'cidade': cidade,
                                               'fotos': str(src_imagem).encode('utf-8'),
                                               'disciplina': disciplinas,
                                               'nome_disciplina': nome_disciplinas,
                                               'boletim': boletim, 'mensagem': mensagem,
                                               #'valor1': json.dumps(valor1),'valor2': json.dumps(valor2)
                                               'valor1': mAluno,'valor2': mTurma
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

def graficos (request, pk, template_name="graficos.html"):

     valor1 = int(100)
     valor2 = int(200)
     return render (request,template_name, { 'valor1': json.dumps(valor1), 'valor2': json.dumps(valor2)})

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

                     print ('CSV: ', row[0])

                     instituicao = Instituicao.objects.all()

                     print("Tabela",regtabelaimportacao.nome)

                     # ESTADO
                     if regtabelaimportacao.nome == 'ESTADO':

                         t_csv = Estado(nome=row[1],
                                        uf=row[2],
                                        ibge=row[3],
                                        pais_id=row[4]
                                        )

                     # CIDADE
                     if regtabelaimportacao.nome == 'CIDADE':

                         t_csv = Cidade(nome=row[1],
                                        ibge=row[2],
                                        estado_id=row[3],
                                        pais_id=row[4]
                                        )

                     # ALUNO
                     if regtabelaimportacao.nome == 'ALUNO':


                         t_csv = Aluno(registro_aluno=row[0],
                                       nome=row[1],
                                       nome_abreviado=row[2],
                                       # dtna   cimento=row[3],
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
        #                               responsavel_id=99
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

                     # BOLETIM
                     if regtabelaimportacao.nome == 'BOLETIM':

                         t_csv = Boletim(periodoletivo_id=row[0],
                                         aluno_id=row[1],
                                         curso=row[2],
                                         serie=row[3],
                                         turma=row[4],
                                         turno=row[5],
                                         disciplina=row[6],
                                         nome_disciplina=row[7],
                                         etapa = row[8],
                                         notas = row[9],
                                         faltas = row[10]

                         )

                         # t_csv = Boletim(periodoletivo_id=row[0],
                         #                 aluno_id=row[1],
                         #                 curso=row[2],
                         #                 serie=row[3],
                         #                 turma=row[4],
                         #                 turno=row[5],
                         #                 disciplina=row[6],
                         #                 notas1=row[7],
                         #                 notas2=row[8],
                         #                 notas3=row[9],
                         #                 notas4=row[10],
                         #                 faltas1=row[11],
                         #                 faltas2=row[12],
                         #                 faltas3=row[13],
                         #                 faltas4=row[14],
                         #                 media=row[15],
                         #                 recuperacao=row[16],
                         #                 faltas=row[17]
                         #
                         # # etapa=row[7],
                         #                 # notas=row[8],
                         #                 # faltas=row[9],
                         #                 #
                         #
                         #
                         #                 )

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

                         t_csv = Financeiro(
                                            aluno_id=row[0],
                                            responsavel_id=row[1],
                                            documento = row[2],
                                            parcela = row[3],
                                            cota=row[4],
                                            historico=row[5],
                                           # dtemissao = datetime.strptime(row[6],'%d/%m/%Y').strftime('%Y-%m-%d'),
                                            dtemissao = row[6],
                                            vlr_titulo = row[7],
                                           # dtbaixa = datetime.strptime(row[8],'%d/%m/%Y').strftime('%Y-%m-%d'),
                                            dtbaixa = row[8],
                                            vlr_juros = row[9],
                                            vlr_desconto = row[10],
                                            periodoletivo_id = row[11],
                                            vlr_baixa=row[12]

                         )

                     try:

                         t_csv.save()
                         # # --> Muda o STImportacao e coloca a data atual
                         regimportacaocsv.dtimportacao = dtatual
                         regimportacaocsv.stimportacao = True
                         regimportacaocsv.save()
                         mensagem = "Processado: %s | %s" % (dados.line_num,row)
                         #mensagem = (dados.line_num)
                         messages.success(request, mensagem)

                     #except Exception:
                     except ValueError:
                         mensagem = "Linha: %s | %s" % (dados.line_num,row)
                         messages.error(request, mensagem)

                 return render(request, template_name,{'importacaocsv': importacaocsv})
