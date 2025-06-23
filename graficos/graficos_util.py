import pandas as pd
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os
import sqlite3
from django.conf import settings

os.makedirs('static/graficos/img', exist_ok=True)

class Usuario:
    def __init__(self, id, email, senha):
        self.id = id
        self.email = email
        self.senha = senha

    def autenticar(self, senha_digitada):
        return self.senha == senha_digitada

    def alterar_senha(self, nova_senha):
        self.senha = nova_senha

class UsuarioDAO:
    def __init__(self, db_name="usuarios.db"):
        self.conn = sqlite3.connect(db_name)
    
        self.cursor = self.conn.cursor()
        self._criar_tabela()

    def _criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def adicionar_usuario(self, email, senha):
        self.cursor.execute("INSERT INTO usuario (email, senha) VALUES (?, ?)", (email, senha))
        self.conn.commit()

    def buscar_por_email(self, email):
        self.cursor.execute("SELECT * FROM usuario WHERE email = ?", (email,))
        resultado = self.cursor.fetchone()
        if resultado:
            return Usuario(*resultado)
        return None


class GraficoBase:
    def __init__(self, caminho_csv):
        self.df = pd.read_csv(caminho_csv, encoding='utf-8-sig')
        self._padronizar_colunas()

    def _padronizar_colunas(self):
        self.df.columns = [
            col.strip().lower()
            .replace(' ', '_')
            .replace('/', '_')
            .replace('?', '')
            .replace('"', '')
            .replace(',', '')
            .replace('__', '_')
            for col in self.df.columns
        ]
    
class Grafico(GraficoBase):    
        
    def grafico_barra_simples(self, coluna, filtro=None, titulo=''):
        
        df = self.df.copy()
        if filtro:
            for col, val in filtro.items():
                df = df[df[col] == val]
        plt.figure(figsize=(10, 5))
        ax = sns.countplot(data=df, x=coluna, order=df[coluna].value_counts().index)
        plt.title(titulo or f'Contagem por {coluna}')
        plt.xlabel(" ")
        plt.ylabel(" ")
        plt.xticks(rotation=45, ha='center', fontsize=8)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        for p in ax.patches:
            altura = p.get_height()
            ax.text(p.get_x() + p.get_width() / 2.,altura + 0.5, int(altura), ha='center', fontsize=8, color='black')
        plt.tight_layout()
        nome_arquivo = f'grafico_barra_simples_{coluna}.png'.replace(' ', '_')
        caminho_completo = os.path.join('static/graficos/img', nome_arquivo)
        plt.savefig(caminho_completo)
        plt.close()
    def grafico_barra_dupla(self, coluna_x, coluna_hue, filtro=None, titulo=''):
        df = self.df.copy()
        if filtro:
            for col, val in filtro.items():
                df = df[df[col] == val]
        plt.figure(figsize=(10, 6))
        ax = sns.countplot(data=df, x=coluna_x, hue=coluna_hue, order=df[coluna_x].value_counts().index)
        plt.title(titulo)
        plt.xlabel(" ")
        plt.ylabel(" ")
        plt.xticks( ha='center', fontsize=8)
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        for p in ax.patches:
            altura = p.get_height()
            if altura > 0:
                ax.text(p.get_x() + p.get_width() / 2., altura + 0.5,
                        int(altura), ha='center', fontsize=8, color='black')
        plt.tight_layout()
        
        # Nome único baseado nas colunas
        nome_arquivo = f'grafico_barra_dupla_{coluna_x}_{coluna_hue}.png'.replace(' ', '_')
        caminho_completo = os.path.join('static/graficos/img', nome_arquivo)
        plt.savefig(caminho_completo)
        plt.close()

    def grafico_empilhado(self, coluna_x, coluna_stack, filtro=None, titulo=''):
        df = self.df
        if filtro:
            for col, val in filtro.items():
                df = df[df[col] == val]
        crosstab = pd.crosstab(df[coluna_x], df[coluna_stack])
        ax = crosstab.plot(kind='bar', stacked=True, figsize=(10, 6))
        plt.title(titulo or f"{coluna_x.replace('_', ' ')} x {coluna_stack.replace('_', ' ')} (empilhado)")
        plt.xlabel(" ")
        plt.ylabel(" ")
        plt.legend(title=coluna_stack)
        plt.xticks(rotation=45, ha='center', fontsize=8)
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        for p in ax.patches:
            altura = p.get_height()
            if altura > 0:
                ax.text(p.get_x() + p.get_width() / 2., altura + 0.5,
                        int(altura), ha='center', fontsize=8, color='black')

        plt.tight_layout()
        
        # Nome único baseado nas colunas
        nome_arquivo = f'grafico_empilhado_{coluna_x}_{coluna_stack}.png'.replace(' ', '_')
        
        caminho_completo = os.path.join('static/graficos/img', nome_arquivo)
        plt.savefig(caminho_completo)
        plt.close()

    def grafico_interativo(self, coluna_x, coluna_color, filtro=None, titulo=''):
        fig = px.histogram(
            self.df,
            x=coluna_x,
            color=coluna_color,
            barmode='group',
            title=titulo or f'{coluna_x} vs {coluna_color}',
            labels={coluna_x: coluna_x.replace('_', ' ').title()}
        )
        fig.update_layout(xaxis_title=coluna_x.replace('_', ' ').title(), yaxis_title='Contagem')
        caminho = 'static/graficos/img/grafico_interativo.html'
        fig.write_html(caminho)
        plt.close() 
     
    def grafico_pizza(self, coluna, filtro=None, titulo=''):
        df = self.df.copy()

        if filtro:
            for col, val in filtro.items():
                df = df[df[col] == val]


        fig = px.pie(
            df,
            names=coluna,
            title=titulo or f'Distribuição por {coluna}',
            hole=0.4  # rosquinha
        )
        fig.update_traces(textinfo='percent+label+value')

        caminho = 'static/graficos/img/grafico_pizza.html'
        fig.write_html(caminho)
        plt.close()

    def grafico_sunburst(self, coluna_nivel1, coluna_nivel2, coluna_nivel3, filtro=None, titulo=''):
        df = self.df.copy()
        if filtro:
            for col, val in filtro.items():
                df = df[df[col] == val]

        fig = px.sunburst(
            df,
            path=[coluna_nivel1, coluna_nivel2, coluna_nivel3],
            title=titulo
        )

        nome_arquivo = f'grafic_sunburst_{coluna_nivel1}_{coluna_nivel2}_{coluna_nivel3}.html'.replace(' ', '_')
        caminho = os.path.join('static/graficos/img', nome_arquivo)
        fig.write_html(caminho)
