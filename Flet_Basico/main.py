# Para utilizar a biblioteca Flet executar:
# pip install flet

import flet as ft

def main(page: ft.Page):

    def somar(e):
        numero = int(txt_numero.value)  # Converte texto em numero inteiro
        numero = numero + 1             # Incrementar 1 no meu numero
        txt_numero.value = str(numero)  # Converte numero inteiro em texto
        
        if numero >= 10:
            txt_numero.bgcolor = ft.colors.RED   
        
        page.update()

    def subtrair(e):
        numero = int(txt_numero.value)  # Converte texto em numero inteiro
        numero = numero - 1             # Decrementar 1 no meu numero
        txt_numero.value = str(numero)  # Converte numero inteiro em texto

        if numero < 10:
            txt_numero.bgcolor = ft.colors.ORANGE

        page.update()


    page.title = "SENAI - Flet Básico"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    btn_menos = ft.IconButton(ft.icons.REMOVE, on_click=subtrair)
    btn_mais = ft.IconButton(ft.icons.ADD, on_click=somar)

    txt_numero = ft.TextField(
        value="0",
        width=100,
        text_align=ft.TextAlign.CENTER,
        bgcolor=ft.colors.ORANGE_600,
        read_only=True,
        border_radius=20
    )

    page.add(
        ft.Row(
            [
                btn_menos,
                txt_numero,
                btn_mais
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
    )




ft.app(target=main)