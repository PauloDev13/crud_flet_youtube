import flet as ft

from form.controls.buttons import TextButton, IconButtons
from form.controls.inputs import Inputs
from connection.con_manager import ConnectionManager


class Form(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True)

        self.page = page

        # Abrindo conexão com o banco de dados
        self.data: ConnectionManager = ConnectionManager()

        # Definindo os controles de texto do formulário
        self.name = Inputs(label='Nome')
        self.age = Inputs(label='Idade', text=False, max_length=2)
        self.email = Inputs(label='E-mail')
        self.phone = Inputs(label='Telefone', text=False, max_length=10)

        # Definindo os botões do tipo texto do formulário
        btn_save = TextButton(text='Salvar', icon=ft.icons.SAVE)
        btn_edit = TextButton(text='Editar', icon=ft.icons.EDIT)
        btn_remove = TextButton(text='Remover', icon=ft.icons.DELETE)

        # Definindo os botões do tipo ícone do formulário
        btn_icon_edit = IconButtons(tooltip='Editar dados', icon=ft.icons.EDIT)
        btn_icon_pdf = IconButtons(tooltip='Baixar em PDF', icon=ft.icons.PICTURE_AS_PDF)
        btn_icon_excel = IconButtons(tooltip='Baixar em Excel', icon=ft.icons.SAVE_ALT)

        self.search_filed = ft.TextField(
            label='Buscar por nome',
            suffix_icon=ft.icons.SEARCH,
            border=ft.InputBorder.UNDERLINE,
            border_color=ft.colors.WHITE,
            label_style=ft.TextStyle(color=ft.colors.WHITE),
        )

        self.data_table = ft.DataTable(
            expand=True,
            border=ft.border.all(2, 'purple'),
            data_row_color={
                ft.ControlState.SELECTED: 'purple',
                ft.ControlState.PRESSED: 'black'
            },
            border_radius=10,
            show_checkbox_column=True,
            columns=[
                ft.DataColumn(ft.Text(
                    value='Nome',
                    color=ft.colors.PURPLE,
                    weight=ft.FontWeight.BOLD
                )),

                ft.DataColumn(ft.Text(
                    value='Idade',
                    color=ft.colors.PURPLE,
                    weight=ft.FontWeight.BOLD,
                ),
                    numeric=True
                ),

                ft.DataColumn(ft.Text(
                    value='Email',
                    color=ft.colors.PURPLE,
                    weight=ft.FontWeight.BOLD
                )),

                ft.DataColumn(ft.Text(
                    value='Telefone',
                    color=ft.colors.PURPLE,
                    weight=ft.FontWeight.BOLD
                )),
            ]
        )

        self.show_data()

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

        self.table = ft.Container(
            padding=10,
            bgcolor='#222222',
            border_radius=10,
            col=8,
            content=ft.Column(
                expand=True,
                controls=[
                    ft.Container(
                        padding=10,
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                            controls=[
                                self.search_filed,
                                btn_icon_edit,
                                btn_icon_pdf,
                                btn_icon_excel
                            ]
                        )
                    ),
                    ft.Column(
                        expand=True,
                        scroll=ft.ScrollMode(value='auto'),
                        controls=[
                            ft.ResponsiveRow(
                                controls=[
                                    self.data_table,
                                ]
                            )
                        ]
                    )
                ]
            )
        )

        self.content = ft.ResponsiveRow(
            controls=[
                self.form,
                self.table,
            ]
        )

    def show_data(self):
        self.data_table.rows = []

        for row in self.data.get_all_contacts():
            self.data_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(value=row[1])),
                        ft.DataCell(ft.Text(value=str(row[2]))),
                        ft.DataCell(ft.Text(value=row[3])),
                        ft.DataCell(ft.Text(value=row[4])),
                    ]
                )
            )

        self.update()

    def build(self):
        return self.content
