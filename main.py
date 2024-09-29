import flet as ft

# importação dos módulos locais
from form.form import Form


def main(page: ft.Page):
    page.bgcolor = 'black'
    page.title = 'CRUD Flet YouTube'
    page.window.min_height = 500
    page.window.min_width = 100

    page.add(Form())


ft.app(target=main)
