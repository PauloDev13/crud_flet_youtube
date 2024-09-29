import flet as ft

from form.controls.buttons import Button
from form.controls.inputs import Inputs


class Form(ft.UserControl):
    def __init__(self):
        super().__init__(expand=True)

        # Definindo os controles de texto do formulário
        self.name = Inputs(label='Nome')
        self.age = Inputs(label='Idade', text=False, max_length=2)
        self.email = Inputs(label='E-mail')
        self.phone = Inputs(label='Telefone', text=False, max_length=10)

        # Definindo os controles de botões do formulário
        btn_save = Button(text='Salvar', icon=ft.icons.SAVE)
        btn_edit = Button(text='Editar', icon=ft.icons.EDIT)
        btn_remove = Button(text='Remover', icon=ft.icons.DELETE)

        self.form = ft.Container(
            bgcolor='#222222',
            border_radius=10,
            col=4,
            padding=20,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        value='Entre com os dados',
                        size=40,
                        text_align=ft.TextAlign.CENTER,
                        font_family='arial'
                    ),
                    self.name,
                    self.age,
                    self.email,
                    self.phone,
                    ft.Container(
                        content=ft.Row(
                            spacing=10,
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                btn_save,
                                btn_edit,
                                btn_remove
                            ]
                        )
                    )
                ]
            )
        )

        self.data_table = ft.Container(
            bgcolor='#222222',
            border_radius=10,
            col=8
        )

        self.content = ft.ResponsiveRow(
            controls=[
                self.form,
                self.data_table,
            ]
        )

    def build(self):
        return self.content
