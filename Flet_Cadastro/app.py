# Aplicativo Simples de Cadastro de Produto + Preço
# No aplicativo de cadastro vamos utilizar o Banco de Dados Local - SQLite

# Utilizar o Modelo de Desenvolvimento - MVC (Model/View/Control)
#  - Model      - SQLite (ORM - SQLAlquemy / Python) - Dados/BD
#  - View       - Flet (Python) - Visualização/Integração com Usário
#  - Control    - Python - Lógica do Sistema/Regra de Negócio

import flet as ft
from models import Produto

# 1. Sessão e Conexão com o Banco de Dados - DB ---------

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CONN = "sqlite:///projeto.db"

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# -----------------------------------------------

def main(page: ft.Page):

    lista_produtos = ft.ListView()

    def cadastrar(e):
        try:
            novo_produto = Produto(titulo=produto.value, preco=preco.value)

            session.add(novo_produto)
            session.commit()

            lista_produtos.controls.append(
                ft.Container(
                    ft.Text(produto.value),
                    bgcolor = ft.colors.BLACK87,
                    padding=15,
                    alignment=ft.alignment.center,
                    margin=3,
                    border_radius=10
                )
            )           

            print("Cadastro realizado com sucesso")
            txt_cadastroOK.visible = True
            txt_erro.visible = False
        except:
            print("Erro ao cadastrar")
            txt_erro.visible = True
            txt_cadastroOK.visible = False
        finally:
            session.close()

        page.update()

        session.

    txt_erro = ft.Container(
        ft.Text("Erro ao cadastrar!!!"),
        bgcolor=ft.colors.RED,
        padding=10,
        alignment=ft.alignment.center,
        visible=False
    )

    txt_cadastroOK = ft.Container(
        ft.Text("Cadastro realizado com sucesso!!!"),
        bgcolor=ft.colors.GREEN,
        padding=10,
        alignment=ft.alignment.center,
        visible=False
    )

    page.title = "App Cadastro"

    txt_titulo = ft.Text("Título do Produto")

    produto = ft.TextField(
        label="Digite o título do produto",
        text_align=ft.TextAlign.LEFT   
    )

    txt_preco = ft.Text("Preço do Produto")

    preco = ft.TextField(
        label="Digite o preço do produto",
        text_align=ft.TextAlign.LEFT,
        input_filter=ft.InputFilter(allow=True, regex_string=r"\d|\.", replacement_string="")
    )

    btn_produto = ft.ElevatedButton("Cadastrar", on_click=cadastrar)

    page.add(
        txt_erro,
        txt_cadastroOK,
        txt_titulo,
        produto,
        txt_preco,
        preco,
        btn_produto
    )

    for p in session.query(Produto).all():
        lista_produtos.controls.append(
            ft.Container(
                ft.Text(p.titulo),
                bgcolor = ft.colors.BLACK87,
                padding=15,
                alignment=ft.alignment.center,
                margin=3,
                border_radius=10
            )
        )

    page.add(
        lista_produtos
    )

ft.app(target=main)