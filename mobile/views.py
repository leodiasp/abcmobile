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

from portal.views import form_aluno

from mobile.models import *

from django.db.models import Sum, Avg, FloatField, Count

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import render

def index(request):

    #return render(request, 'dashboard.html')
    return redirect('/dashboard/')


@login_required
def dashboard(request):

   #Instituicao
    instituicao = Instituicao.objects.all()

   # Alunos
    #alunos = Aluno.objects.all()
    alunos = Aluno.objects.filter(responsavel_id=request.user.responsavel_id)

    # Total Alunos
    totAlunos = alunos.count()

    professores = Professor.objects.all()

    # Total Professor
    totProfessores = professores.count()

    # Total Responsavel
    responsavel = Responsavel.objects.filter(pk=request.user.responsavel_id)
    totResponsavel = responsavel.count()

    # Pagtos Confirmados
#    totTitulosPagos = Financeiro.objects.filter(dtbaixa__isnull= False).aggregate(total=Sum('vlr_titulo'))
    #totTitulosPagos = Financeiro.objects.all().exclude(dtbaixa= 'NULL')
    totTitulosPagos = Financeiro.objects.filter(responsavel_id=request.user.responsavel_id).exclude(dtbaixa= 'NULL')

    # Pagtos Pendentes
#    totTitulosAbertos = Financeiro.objects.filter(dtbaixa__isnull= True).aggregate(total=Sum('vlr_titulo'))
    #totTitulosAbertos = Financeiro.objects.filter(dtbaixa = 'NULL')
    totTitulosAbertos = Financeiro.objects.filter(dtbaixa = 'NULL',responsavel_id=request.user.responsavel_id)

    #Mensagem
    totMensagem = Mensagem.objects.all()

    return render(request,'dashboard.html',{'instituicao': instituicao,
                                            'alunos': alunos,
                                            'professores': professores,
                                            'totAlunos': totAlunos,
                                            'totProfessor': totProfessores,
                                            'totResponsavel': totResponsavel,
                                            'totTitulosPagos': totTitulosPagos.count(),
                                            'totTitulosAbertos':totTitulosAbertos.count(),
                                            'totMensagem': totMensagem

                                        })

