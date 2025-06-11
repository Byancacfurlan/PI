from django.shortcuts import render
from .graficos_util import Grafico
import os
from django.conf import settings

def index(request):
    return render(request, 'graficos/index.html')

def adm(request):
    return render(request, 'graficos/adm.html')

def ads(request):
    # Geração dos gráficos (mantido como estava)
   
    return render(request, 'graficos/ads.html')

def ped(request):
    return render(request, 'graficos/ped.html')

def prg(request):
    return render(request, 'graficos/prg.html')

def diversos(request):
    g = Grafico("respostas.csv")
    g.grafico_barra_dupla('qual_a_sua_faixa_etária', 'qual_curso_você_faz_na_fmp')
    g.grafico_empilhado('você_está_trabalhando', 'você_trabalha_na_área_do_curso_em_que_está_matriculado')
    g.grafico_barra_simples('como_você_realiza_o_trajeto_até_a_fmp')
    g.grafico_interativo('qual_a_sua_faixa_etária', 'qual_curso_você_faz_na_fmp')

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
