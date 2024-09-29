import flet as ft


class Form(ft.UserControl):
    def __init__(self):
        super().__init__(expand=True)

        # Campo nome
        self.name = ft.TextField(
            label='Nome',
            border_color=ft.colors.PURPLE
        )
        # Campo Idade
        self.age = ft.TextField(
            label='Idade',
            border_color=ft.colors.PURPLE,
            input_filter=ft.NumbersOnlyInputFilter(),
            max_length=2
        )

        # Campo Email
        self.email = ft.TextField(
            label='Email',
            border_color=ft.colors.PURPLE
        )

        # Campo Telefone
        self.phone = ft.TextField(
            label='Telefone',
            border_color=ft.colors.PURPLE,
            input_filter=ft.NumbersOnlyInputFilter(),
            max_length=10
        )

        self.form = ft.Container(
            bgcolor='#222222',
            border_radius=10,
            col=4,
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
                                ft.TextButton(
                                    text='Salvar',
                                    icon=ft.icons.SAVE,
                                    style=ft.ButtonStyle(
                                        color=ft.colors.WHITE,
                                        bgcolor=ft.colors.PURPLE,
                                    )
                                ),
                                ft.TextButton(
                                    text='Editar',
                                    icon=ft.icons.EDIT,
                                    style=ft.ButtonStyle(
                                        color=ft.colors.WHITE,
                                        bgcolor=ft.colors.PURPLE,
                                    )
                                ),
                                ft.TextButton(
                                    text='Remover',
                                    icon=ft.icons.DELETE,
                                    style=ft.ButtonStyle(
                                        color=ft.colors.WHITE,
                                        bgcolor=ft.colors.PURPLE,
                                    )
                                )
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
