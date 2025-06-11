import pandas as pd
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


# Funções para integração com o banco de dados
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
    def grafico_barra_simples(self, coluna, titulo=''):
        plt.figure(figsize=(10, 5))
        sns.countplot(data=self.df, x=coluna, order=self.df[coluna].value_counts().index)
        plt.title(titulo or f'Contagem por {coluna}')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('static/graficos/img/grafico_barra_simples.png')
        plt.close() 



    def grafico_barra_dupla(self, coluna_x, coluna_hue, titulo=''):
        plt.figure(figsize=(10, 6))
        sns.countplot(data=self.df, x=coluna_x, hue=coluna_hue, order=self.df[coluna_x].value_counts().index)
        plt.title(titulo or f'{coluna_x} vs {coluna_hue}')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('static/graficos/img/grafico_barra_dupla.png')
        plt.close() 




    def grafico_empilhado(self, coluna_x, coluna_stack, titulo=''):
        crosstab = pd.crosstab(self.df[coluna_x], self.df[coluna_stack])
        crosstab.plot(kind='bar', stacked=True, figsize=(10, 6))
        plt.title(titulo or f'{coluna_x} x {coluna_stack} (empilhado)')
        plt.xlabel(coluna_x)
        plt.ylabel('Contagem')
        plt.legend(title=coluna_stack)
        plt.tight_layout()
        plt.savefig('static/graficos/img/grafico_empilhado.png')
        plt.close() 


        


    def grafico_interativo(self, coluna_x, coluna_color, titulo=''):
        fig = px.histogram(
            self.df,
            x=coluna_x,
            color=coluna_color,
            barmode='group',
            title=titulo or f'{coluna_x} vs {coluna_color}',
            labels={coluna_x: coluna_x.replace('_', ' ').title()}
        )
        fig.update_layout(xaxis_title=coluna_x.replace('_', ' ').title(), yaxis_title='Contagem')
        fig.write_html('static/graficos/img/grafico_interativo.html')
        plt.close() 


        




