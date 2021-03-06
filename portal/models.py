from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


from decimal import Decimal

# Create your models here.

# CLASSE PAÍS -----------------------------------------------------------------------------

class Pais(models.Model):

    nome = models.CharField(max_length=40, verbose_name="Nome do País")
    abreviacao = models.CharField(max_length=3, verbose_name="Abreviação do País")
    stativo = models.BooleanField(default=False)


    def __str__(self):
        # return self.nome.encode('utf-8')
        return str(self.nome)

# CLASSE ESTADO -----------------------------------------------------------------------------

class Estado(models.Model):

    pais = models.ForeignKey(Pais)

    ibge = models.CharField(max_length=2, primary_key=True)
    nome = models.CharField(max_length=40)
    uf = models.CharField(max_length=2)
    arquivo_importado = models.CharField(max_length=200)


    def __str__(self):
        return str(self.uf)
        # return (self.uf.str('utf-8'))
        # return (self.uf.encode('utf-8'))
        # return u'%s %s' % (self.estado_uf.encode('utf-8'), self.id)

# CLASSE CIDADE ===============================================================================

class Cidade(models.Model):

    pais = models.ForeignKey(Pais,null=True)
    estado = models.ForeignKey(Estado, null=True)

    ibge = models.CharField(max_length=10, primary_key=True, default=0)
    nome = models.CharField(max_length=60, null=True)
    arquivo_importado = models.CharField(max_length=200)

    class Meta:
        ordering = ['nome']

    def __str__(self):

        return "{0} / {1}".format(self.nome,self.estado.uf)

        # return ('%s %s' % str(self.nome), str(self.estado.uf))

        # return str(self.nome, self.estado.uf)
        # return ('%s %s' % str(self.nome.encode('utf-8')), str(self.arquivo_importado.encode('utf-8')))

class Mensagem(models.Model):

    #usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    usuario = models.ManyToManyField(User, related_name="usuarios")

    titulo     = models.CharField(max_length=100)
    dtmensagem = models.DateField()
    descricao  = models.TextField()
    stmensagem = models.BooleanField()

    def __str__(self):
        # return self.titulo.encode('utf-8')
        return str(self.titulo)

# class ImagemUsuarios(models.Model):
#
#     usuarios = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     imagem  = models.ImageField(upload_to="usuarios", default = 'usuarios/sem_foto.jpg', blank=True, null=True)

class Instituicao(models.Model):

    #estado = models.ForeignKey(Estado)
    cidade = models.ForeignKey(Cidade)

    razaosocial   = models.CharField(max_length=100, null=True)
    nomefantasia  = models.CharField(max_length=100)
    cgc           = models.CharField(max_length=20)
    inscestadual  = models.CharField(max_length=20, null=True, blank=True)
    telefone      = models.CharField(max_length=15, null=True, blank=True)
    telefax       = models.CharField(max_length=15, null=True, blank=True)
    email         = models.CharField(max_length=60)
    endereco      = models.CharField(max_length=100)
    complemento   = models.CharField(max_length=60, null=True, blank=True)
    bairro        = models.CharField(max_length=80)
    cep           = models.CharField(max_length=10)
    contato       = models.CharField(max_length=40)
    imagem        = models.ImageField(upload_to="instituicao", default = 'instituicao/sem_foto.png', blank=True, null=True)
    #imagem        = models.FileField(upload_to="imagens", blank=True, null=True)
    dtcadastro    = models.DateField(auto_now=True)

    numero_alunos = models.IntegerField()

    def __str__(self):
        # return self.nomefantasia.encode('utf-8')
        return str(self.nomefantasia)

class TabelaImportacao(models.Model):

    nome = models.CharField(max_length=100, null=False)
    descricao = models.TextField()

    def __str__(self):
        # return self.nome.encode('utf-8')
        return str(self.nome)

class TipoUser(models.Model):


    # usuario = models.ManyToManyField(User, related_name="tp_usuario")
    nome = models.CharField(max_length=50, null=False)

    def __str__(self):
        return str(self.nome)



# class ImportacaoCSV(models.Model):
#
#     tabelaimportacao = models.ForeignKey(TabelaImportacao)
#
#     nome_importacao = models.CharField(max_length=100)
#     observacao = models.TextField()
#     dtupload = models.DateField()
#     stimportacao = models.BooleanField(default=False)
#     dtimportacao = models.DateField(null=True, blank=True)
#     arquivo = models.FileField(upload_to='csv')

class ImportacaoXLS(models.Model):

    tabelaimportacao = models.ForeignKey(TabelaImportacao)

    nome_importacao = models.CharField(max_length=100)
    observacao = models.TextField()
    dtupload = models.DateField()
    #posicao_xls  = models.IntegerField()
    arquivo = models.FileField(upload_to='csv')
    stimportacao = models.BooleanField(default=False)
    dtimportacao = models.DateField(null=True, blank=True)

    def __str__(self):
        # return self.nome_importacao.encode('utf-8')
        return self.nome_importacao


class PeriodoLetivo(models.Model):

    #instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)

    codigo = models.CharField(max_length=10, primary_key=True)
    descricao = models.CharField(max_length=60)
    diasletivos = models.IntegerField()
    dtinicial = models.DateField()
    dtfinal   = models.DateField(null=True, blank=True)
    calendario = models.CharField(max_length=16)

# class Responsavel(models.Model):
#
#     #aluno = models.ManyToManyField(Aluno, related_name="aluno")
#
#     #usuario = models.ForeignKey(User, related_name="usuario")
#
#     # registro_responsavel = models.CharField(max_length=20, primary_key=True)
#     # #codigo = models.IntegerField()
#     # nome   = models.CharField(max_length=120)
#     # nome_abreviado = models.CharField(max_length=40)
#     # dtnascimento = models.DateField()
#     # sexo         = models.CharField(max_length=10)
#     # cpf = models.CharField(max_length=20)
#     # identidade = models.CharField(max_length=20)
#     # email = models.EmailField(max_length=60)
#     # endereco = models.CharField(max_length=140)
#     # complemento = models.CharField(max_length=60)
#     # bairro = models.CharField(max_length=80)
#     # cidade = models.CharField(max_length=60)
#     # uf = models.CharField(max_length=3)
#     # cep = models.CharField(max_length=15)
#     # telefone = models.CharField(max_length=20, null=True, blank=True)
#     # telefone2 = models.CharField(max_length=20, null=True, blank=True)
#     # imagem        = models.ImageField(upload_to="responsavel",  default = 'responsavel/sem_foto.png', blank=True, null=True)
#     # arquivo_importado = models.CharField(max_length=200)
#
#     registro_responsavel = models.CharField(max_length=20, primary_key=True)
#     nome   = models.CharField(max_length=120)
#     cpf = models.CharField(max_length=20)
#     email = models.EmailField(max_length=60)
#     celular  = models.CharField(max_length=20, null=True, blank=True)
#     whatsapp  = models.CharField(max_length=20, null=True, blank=True)
#     imagem        = models.ImageField(upload_to="responsavel",  default = 'responsavel/sem_foto.png', blank=True, null=True)
#     arquivo_importado = models.CharField(max_length=200)


class Aluno(models.Model):

    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'user_{0}/{1}'.format(instance.user.id, filename)

    # responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    registro_aluno = models.CharField(max_length=20, primary_key=True)
    nome   = models.CharField(max_length=120)
    nome_abreviado = models.CharField(max_length=40)
    email = models.EmailField(max_length=60, null=True, blank=True)
    celular  = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20)
    imagem    = models.FileField(upload_to="alunos", default = 'alunos/sem_foto.png', blank=True, null=True)
    arquivo_importado = models.CharField(max_length=200)

class Professor(models.Model):

    #instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)

    # usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    registro_professor = models.CharField(max_length=20, primary_key=True)
    nome   = models.CharField(max_length=120)
    cpf = models.CharField(max_length=20)
    email = models.EmailField(max_length=60)
    celular  = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20)
    imagem    = models.FileField(upload_to="alunos", default = 'professores/sem_foto.png', blank=True, null=True)

    arquivo_importado = models.CharField(max_length=200)

    def __str__(self):
        return str(self.nome)

class Boletim(models.Model):

    periodoletivo = models.ForeignKey(PeriodoLetivo, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)

    curso = models.CharField(max_length=30)
    serie = models.CharField(max_length=30)
    turno = models.CharField(max_length=30)
    turma = models.CharField(max_length=30)
    disciplina = models.CharField(max_length=10)
    nome_disciplina = models.CharField(max_length=50)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    etapa = models.CharField(max_length=10)
    nome_etapa = models.CharField(max_length=40)
    notas  = models.DecimalField(max_digits=5, decimal_places=1)
    faltas = models.IntegerField()
    arquivo_importado = models.CharField(max_length=200)

class Financeiro(models.Model):

    periodoletivo = models.ForeignKey(PeriodoLetivo, on_delete=models.CASCADE)

    # responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)

    documento = models.CharField(max_length=10)
    parcela = models.CharField(max_length=5)
    cota = models.CharField(max_length=5)
    historico = models.TextField()
    dtemissao = models.CharField(max_length=10)
    vlr_titulo = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('00000000.00'))
    dtbaixa = models.CharField(max_length=10)
    vlr_baixa = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('00000000.00'))
    vlr_juros = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('00000000.00'))
    vlr_desconto = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('00000000.00'))
    arquivo_importado = models.CharField(max_length=200)
