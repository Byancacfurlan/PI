from django.shortcuts import render, redirect
from django.contrib import messages
from .graficos_util import Grafico , UsuarioDAO
import os
from django.conf import settings


def index(request):
    return render(request, 'graficos/index.html')

def adm(request):

    if 'usuario_id' not in request.session:
        return redirect('login')
    g = Grafico("respostas.csv")
    filtro = {'qual_curso_você_faz_na_fmp': 'Administração'}
    g.grafico_barra_dupla('qual_a_sua_faixa_etária', 'qual_curso_você_faz_na_fmp', filtro=filtro, titulo = 'Curso x Idade')
    g.grafico_empilhado('você_está_trabalhando', 'você_trabalha_na_área_do_curso_em_que_está_matriculado', filtro=filtro, titulo =' Trabalha x Trabalha na área em que estuda')
    g.grafico_barra_simples('como_você_realiza_o_trajeto_até_a_fmp', filtro=filtro, titulo = 'Trajeto até a faculdade')
    g.grafico_barra_simples('qual_sua_cor_raça', filtro=filtro, titulo = 'Cor/raça')
    g.grafico_barra_simples('como_você_se_identifica_com_relação_a_seu_gênero', filtro=filtro, titulo = 'Gênero')
    g.grafico_barra_simples('qual_a_sua_escolaridade', filtro=filtro, titulo = 'Escolaridade')
    g.grafico_barra_simples('qual_sua_jornada_diária_de_trabalho', filtro=filtro, titulo ='Jornada diária de trabalho')
    g.grafico_barra_simples('você_pratica_alguma_atividade_física', filtro=filtro, titulo ='Atividade física')
    pasta_imagens = os.path.join(settings.STATICFILES_DIRS[0], 'graficos', 'img')
    imagens = [f'graficos/img/{arquivo}'
        for arquivo in os.listdir(pasta_imagens)
            if arquivo.endswith(('.png', '.jpeg', '.gif'))]
    return render(request, 'graficos/adm.html', {'imagens': imagens})

def ads(request):


    if 'usuario_id' not in request.session:
        return redirect('login')
   
    g = Grafico("respostas.csv")


    # Define o filtro pelo curso "ADS"
    filtro = {'qual_curso_você_faz_na_fmp': 'Tecnólogo em Análise e Desenvolvimento de Sistemas'}


    g.grafico_barra_dupla('qual_a_sua_faixa_etária', 'qual_curso_você_faz_na_fmp', filtro=filtro, titulo = 'Curso x Idade')
    g.grafico_empilhado('você_está_trabalhando', 'você_trabalha_na_área_do_curso_em_que_está_matriculado', filtro=filtro, titulo =' Trabalha x Trabalha na área em que estuda')
    g.grafico_barra_simples('como_você_realiza_o_trajeto_até_a_fmp', filtro=filtro, titulo = 'Trajeto até a faculdade')
    g.grafico_barra_simples('como_você_se_identifica_com_relação_a_seu_gênero', filtro=filtro, titulo = 'Gênero')
    g.grafico_barra_simples('qual_sua_cor_raça', filtro=filtro, titulo = 'Cor/raça')
    g.grafico_barra_simples('qual_a_sua_escolaridade', filtro=filtro, titulo = 'Escolaridade')
    g.grafico_barra_simples('qual_sua_jornada_diária_de_trabalho', filtro=filtro, titulo ='Jornada diária de trabalho')
    g.grafico_barra_simples('você_pratica_alguma_atividade_física', filtro=filtro, titulo ='Atividade física')
   
    pasta_imagens = os.path.join(settings.STATICFILES_DIRS[0], 'graficos', 'img')
    imagens = [f'graficos/img/{arquivo}'
        for arquivo in os.listdir(pasta_imagens)
            if arquivo.endswith(('.png', '.jpeg', '.gif'))]


    return render(request, 'graficos/ads.html',  {'imagens': imagens})

def ped(request):


    if 'usuario_id' not in request.session:
        return redirect('login')
   
    g = Grafico("respostas.csv")




    # Define o filtro pelo curso "Pedagogia"
    filtro = {'qual_curso_você_faz_na_fmp': 'Pedagogia'}


    g.grafico_barra_dupla('qual_a_sua_faixa_etária', 'qual_curso_você_faz_na_fmp', filtro=filtro, titulo = 'Curso x Idade')
    g.grafico_empilhado('você_está_trabalhando', 'você_trabalha_na_área_do_curso_em_que_está_matriculado', filtro=filtro, titulo =' Trabalha x Trabalha na área em que estuda')
    g.grafico_barra_simples('como_você_realiza_o_trajeto_até_a_fmp', filtro=filtro, titulo = 'Trajeto até a faculdade')
    g.grafico_barra_simples('como_você_se_identifica_com_relação_a_seu_gênero', filtro=filtro, titulo = 'Gênero')
    g.grafico_barra_simples('qual_sua_cor_raça', filtro=filtro, titulo = 'Cor/raça')
    g.grafico_barra_simples('qual_a_sua_escolaridade', filtro=filtro, titulo = 'Escolaridade')
    g.grafico_barra_simples('qual_sua_jornada_diária_de_trabalho', filtro=filtro, titulo ='Jornada diária de trabalho')
    g.grafico_barra_simples('você_pratica_alguma_atividade_física', filtro=filtro, titulo ='Atividade física')




    pasta_imagens = os.path.join(settings.STATICFILES_DIRS[0], 'graficos', 'img')
    imagens = [f'graficos/img/{arquivo}'
        for arquivo in os.listdir(pasta_imagens)
            if arquivo.endswith(('.png', '.jpeg', '.gif'))]
    return render(request, 'graficos/ped.html',  {'imagens': imagens})

def prg(request):


    if 'usuario_id' not in request.session:
        return redirect('login')


    g = Grafico("respostas.csv")


    # Define o filtro pelo curso "Tecnólogo em Processos Gerenciais"
    filtro = {'qual_curso_você_faz_na_fmp': 'Tecnólogo em Processos Gerenciais'}
    g.grafico_barra_dupla('qual_a_sua_faixa_etária', 'qual_curso_você_faz_na_fmp', filtro=filtro, titulo = 'Curso x Idade')
    g.grafico_empilhado('você_está_trabalhando', 'você_trabalha_na_área_do_curso_em_que_está_matriculado', filtro=filtro, titulo =' Trabalha x Trabalha na área em que estuda')
    g.grafico_barra_simples('como_você_realiza_o_trajeto_até_a_fmp', filtro=filtro, titulo = 'Trajeto até a faculdade')
    g.grafico_barra_simples('como_você_se_identifica_com_relação_a_seu_gênero', filtro=filtro, titulo = 'Gênero')
    g.grafico_barra_simples('qual_sua_cor_raça', filtro=filtro, titulo = 'Cor/raça')
    g.grafico_barra_simples('qual_a_sua_escolaridade', filtro=filtro, titulo = 'Escolaridade')
    g.grafico_barra_simples('qual_sua_jornada_diária_de_trabalho', filtro=filtro, titulo ='Jornada diária de trabalho')
    g.grafico_barra_simples('você_pratica_alguma_atividade_física', filtro=filtro, titulo ='Atividade física')


    pasta_imagens = os.path.join(settings.STATICFILES_DIRS[0], 'graficos', 'img')
    imagens = [f'graficos/img/{arquivo}'
        for arquivo in os.listdir(pasta_imagens)
            if arquivo.endswith(('.png', '.jpeg', '.gif'))]
    return render(request, 'graficos/prg.html',  {'imagens': imagens})

def diversos(request):


    if 'usuario_id' not in request.session:
        return redirect('login')


    g = Grafico("respostas.csv")
    g.grafico_barra_dupla('qual_a_sua_faixa_etária', 'qual_curso_você_faz_na_fmp', titulo = 'Curso x Idade')
    g.grafico_empilhado('você_está_trabalhando', 'você_trabalha_na_área_do_curso_em_que_está_matriculado', titulo = 'Trabalha x Trabalha na área em que estuda')
    g.grafico_barra_simples('como_você_realiza_o_trajeto_até_a_fmp', titulo = 'Trajeto')
    g.grafico_interativo('qual_a_sua_faixa_etária', 'qual_curso_você_faz_na_fmp', titulo = 'Idade X Curso')
    g.grafico_pizza('qual_curso_você_faz_na_fmp', titulo = 'Quantidade de Alunos por Curso')
    g.grafico_barra_simples('qual_sua_cor_raça',  titulo = 'Cor/raça')
    g.grafico_barra_simples('como_você_se_identifica_com_relação_a_seu_gênero', titulo = 'Gênero')
    g.grafico_barra_simples('qual_a_sua_escolaridade', titulo = 'Escolaridade')
    g.grafico_barra_simples('qual_sua_jornada_diária_de_trabalho', titulo = 'Jornada diária de trabalho')
    g.grafico_barra_simples('você_pratica_alguma_atividade_física', titulo = 'Atividade física')
    g.grafico_sunburst(
        coluna_nivel1='qual_curso_você_faz_na_fmp',
        coluna_nivel2='qual_seu_município_de_residência',
        coluna_nivel3='como_você_se_identifica_com_relação_a_seu_gênero',
        titulo='Distribuição de Curso, Município e Gênero'
)
   


    # Caminho da pasta de imagens de gráficos
    pasta_imagens = os.path.join(settings.STATICFILES_DIRS[0], 'graficos', 'img')


    # Lista os arquivos de imagem
    imagens = []
    for arquivo in os.listdir(pasta_imagens):
        if arquivo.endswith(('.png', '.jpeg', '.gif','html')):
            imagens.append(f'graficos/img/{arquivo}')  # Caminho relativo à pasta static


    return render(request, 'graficos/diversos.html', {'imagens': imagens})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        dao = UsuarioDAO()
        usuario = dao.buscar_por_email(email)

        if usuario and usuario.autenticar(senha):
            request.session['usuario_id'] = usuario.id
            request.session['usuario_email'] = usuario.email
            return redirect('index')
        else:
            messages.error(request, 'Email ou senha incorretos.')

    return render(request, 'graficos/login.html')

def cadastro_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        senha = request.POST.get('senha', '')
        senha2 = request.POST.get('senha2', '')




        # validando
        if not email or not senha or not senha2:
            messages.error(request, 'Preencha todos os campos.')
            return render(request, 'graficos/cadastro.html')

        # validando senhas
        if senha != senha2:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'graficos/cadastro.html')
        
        dao = UsuarioDAO()

        # ve se o email ja ta em uso
        if dao.buscar_por_email(email):
            messages.error(request, 'Este email já está cadastrado.')
            return render(request, 'graficos/cadastro.html')

        # cadastra o usuario
        try:
            dao.adicionar_usuario(email, senha)
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Erro ao cadastrar: {str(e)}')
            return render(request, 'graficos/cadastro.html')




    return render(request, 'graficos/cadastro.html')

def logout_view(request):
    request.session.flush()  # Isso remove todas as variáveis da sessão
    return redirect('login')



