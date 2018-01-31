# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-10 18:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alertas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('dtalerta', models.DateField()),
                ('descricao', models.TextField()),
                ('stmensagem', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('registro_aluno', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('codigo', models.IntegerField()),
                ('nome', models.CharField(max_length=120)),
                ('nome_abreviado', models.CharField(max_length=40)),
                ('dtnascimento', models.DateField()),
                ('sexo', models.CharField(max_length=2)),
                ('cpf', models.CharField(max_length=20)),
                ('identidade', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=60)),
                ('endereco', models.CharField(max_length=140)),
                ('complemento', models.CharField(max_length=60)),
                ('bairro', models.CharField(max_length=80)),
                ('cidade', models.CharField(max_length=60)),
                ('uf', models.CharField(max_length=2)),
                ('cep', models.CharField(max_length=15)),
                ('telefone', models.CharField(max_length=20)),
                ('telefone2', models.CharField(max_length=20)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='alunos')),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('codigo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('abreviacao', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ImportacaoCSV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_importacao', models.CharField(max_length=100)),
                ('observacao', models.TextField()),
                ('dtupload', models.DateField()),
                ('stimportacao', models.BooleanField(default=False)),
                ('dtimportacao', models.DateField(blank=True, null=True)),
                ('arquivo', models.FileField(upload_to='csv')),
            ],
        ),
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('razaosocial', models.CharField(max_length=100, null=True)),
                ('nomefantasia', models.CharField(max_length=100)),
                ('cgc', models.CharField(max_length=20)),
                ('inscestadual', models.CharField(blank=True, max_length=20, null=True)),
                ('telefone', models.CharField(blank=True, max_length=15, null=True)),
                ('telefax', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.CharField(max_length=60)),
                ('endereco', models.CharField(max_length=100)),
                ('complemento', models.CharField(blank=True, max_length=60, null=True)),
                ('bairro', models.CharField(max_length=80)),
                ('cep', models.CharField(max_length=10)),
                ('contato', models.CharField(max_length=40)),
                ('imagem', models.ImageField(blank=True, default='media/imagens/sem_foto.jpg', null=True, upload_to='imagens')),
                ('dtcadastro', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PeriodoLetivo',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=60)),
                ('diasletivos', models.IntegerField()),
                ('dtinicial', models.DateField()),
                ('dtfinal', models.DateField()),
                ('calendario', models.CharField(max_length=16)),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Instituicao')),
            ],
        ),
        migrations.CreateModel(
            name='TabelaImportacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('codigo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=60)),
                ('abreviacao', models.CharField(max_length=30)),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Instituicao')),
            ],
        ),
        migrations.RenameField(
            model_name='cidade',
            old_name='cidade_ibge',
            new_name='ibge',
        ),
        migrations.RenameField(
            model_name='cidade',
            old_name='cidade_nome',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='estado',
            old_name='estado_ibge',
            new_name='ibge',
        ),
        migrations.RenameField(
            model_name='estado',
            old_name='estado_nome',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='estado',
            old_name='estado_uf',
            new_name='uf',
        ),
        migrations.RenameField(
            model_name='pais',
            old_name='pais_abreviacao',
            new_name='abreviacao',
        ),
        migrations.RenameField(
            model_name='pais',
            old_name='pais_nome',
            new_name='nome',
        ),
        migrations.AddField(
            model_name='instituicao',
            name='cidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Cidade'),
        ),
        migrations.AddField(
            model_name='instituicao',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Estado'),
        ),
        migrations.AddField(
            model_name='importacaocsv',
            name='instituicao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Instituicao'),
        ),
        migrations.AddField(
            model_name='importacaocsv',
            name='tabelaimportacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.TabelaImportacao'),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='turmas',
            field=models.ManyToManyField(related_name='disciplinas', to='portal.Turma'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='instituicao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Instituicao'),
        ),
    ]