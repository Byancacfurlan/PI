from django.shortcuts import render
from .graficos_util import Grafico
import os
from django.conf import settings

def index(request):
    return render(request, 'graficos/index.html')

def adm(request):
    g = Grafico("respostas.csv")

    # Define o filtro pelo curso "Administração"
    filtro = {'qual_curso_você_faz_na_fmp': 'Administração'}

    g.grafico_barra_dupla('qual_a_sua_faixa_etária', 'qual_curso_você_faz_na_fmp', filtro=filtro)
    g.grafico_empilhado('você_está_trabalhando', 'você_trabalha_na_área_do_curso_em_que_está_matriculado', filtro=filtro)
    g.grafico_barra_simples('como_você_realiza_o_trajeto_até_a_fmp', filtro=filtro)
    g.grafico_barra_simples('como_você_se_identifica_com_relação_a_seu_gênero', filtro=filtro)
    g.grafico_barra_simples('qual_a_sua_escolaridade', filtro=filtro)
    g.grafico_barra_simples('qual_sua_jornada_diária_de_trabalho', filtro=filtro)
    g.grafico_barra_simples('você_pratica_alguma_atividade_física', filtro=filtro)

    pasta_imagens = os.path.join(settings.STATICFILES_DIRS[0], 'graficos', 'img')
    imagens = [f'graficos/img/{arquivo}' 
        for arquivo in os.listdir(pasta_imagens) 
            if arquivo.endswith(('.png', '.jpeg', '.gif', 'html'))]

    return render(request, 'graficos/adm.html', {'imagens': imagens})

def ads(request):
    g = Grafico("respostas.csv")

    # Define o filtro pelo curso "ADS"
    filtro = {'qual_curso_você_faz_na_fmp': 'Tecnólogo em Análise e Desenvolvimento de Sistemas'}

    g.grafico_barra_dupla('qual_a_sua_faixa_etária', 'qual_curso_você_faz_na_fmp', filtro=filtro)
    g.grafico_empilhado('você_está_trabalhando', 'você_trabalha_na_área_do_curso_em_que_está_matriculado', filtro=filtro)
    g.grafico_barra_simples('como_você_realiza_o_trajeto_até_a_fmp', filtro=filtro)
    g.grafico_interativo('qual_a_sua_faixa_etária', 'qual_curso_você_faz_na_fmp', filtro=filtro)
    g.grafico_barra_simples('como_você_realiza_o_trajeto_até_a_fmp', filtro=filtro)
    pasta_imagens = os.path.join(settings.STATICFILES_DIRS[0], 'graficos', 'img')
    imagens = [f'graficos/img/{arquivo}'
        for arquivo in os.listdir(pasta_imagens) 
            if arquivo.endswith(('.png', '.jpeg', '.gif', 'html'))]

    return render(request, 'graficos/ads.html',  {'imagens': imagens})

def ped(request):
    g = Grafico("respostas.csv")


    # Define o filtro pelo curso "Pedagogia"
    filtro = {'qual_curso_você_faz_na_fmp': 'Pedagogia'}

    g.grafico_barra_dupla('qual_a_sua_faixa_etária', 'qual_curso_você_faz_na_fmp', filtro=filtro)
    g.grafico_empilhado('você_está_trabalhando', 'você_trabalha_na_área_do_curso_em_que_está_matriculado', filtro=filtro)
    g.grafico_barra_simples('como_você_realiza_o_trajeto_até_a_fmp', filtro=filtro)
    g.grafico_interativo('qual_a_sua_faixa_etária', 'qual_curso_você_faz_na_fmp', filtro=filtro)


    pasta_imagens = os.path.join(settings.STATICFILES_DIRS[0], 'graficos', 'img')
    imagens = [f'graficos/img/{arquivo}'
        for arquivo in os.listdir(pasta_imagens) 
            if arquivo.endswith(('.png', '.jpeg', '.gif', 'html'))]
    return render(request, 'graficos/ped.html',  {'imagens': imagens})

def prg(request):
    g = Grafico("respostas.csv")

    # Define o filtro pelo curso "Administração"
    filtro = {'qual_curso_você_faz_na_fmp': 'Tecnólogo em Processos Gerenciais'}

    g.grafico_barra_dupla('qual_a_sua_faixa_etária', 'qual_curso_você_faz_na_fmp', filtro=filtro)
    g.grafico_empilhado('você_está_trabalhando', 'você_trabalha_na_área_do_curso_em_que_está_matriculado', filtro=filtro)
    g.grafico_barra_simples('como_você_realiza_o_trajeto_até_a_fmp', filtro=filtro)
    g.grafico_interativo('qual_a_sua_faixa_etária', 'qual_curso_você_faz_na_fmp', filtro=filtro)

    pasta_imagens = os.path.join(settings.STATICFILES_DIRS[0], 'graficos', 'img')
    imagens = [f'graficos/img/{arquivo}'
        for arquivo in os.listdir(pasta_imagens) 
            if arquivo.endswith(('.png', '.jpeg', '.gif', 'html'))]
    return render(request, 'graficos/prg.html',  {'imagens': imagens})

def diversos(request):
    g = Grafico("respostas.csv")
    g.grafico_barra_dupla('qual_a_sua_faixa_etária', 'qual_curso_você_faz_na_fmp')
    g.grafico_empilhado('você_está_trabalhando', 'você_trabalha_na_área_do_curso_em_que_está_matriculado')
    g.grafico_barra_simples('como_você_realiza_o_trajeto_até_a_fmp')
    g.grafico_interativo('qual_a_sua_faixa_etária', 'qual_curso_você_faz_na_fmp')
    g.grafico_pizza('qual_curso_você_faz_na_fmp')


    # Caminho da pasta de imagens de gráficos
    pasta_imagens = os.path.join(settings.STATICFILES_DIRS[0], 'graficos', 'img')

    # Lista os arquivos de imagem
    imagens = []
    for arquivo in os.listdir(pasta_imagens):
        if arquivo.endswith(('.png', '.jpeg', '.gif','html')):
            imagens.append(f'graficos/img/{arquivo}')  # Caminho relativo à pasta static

    return render(request, 'graficos/diversos.html', {'imagens': imagens})

def login_view(request):
    return render(request, 'graficos/login.html')
