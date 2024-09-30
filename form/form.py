import flet as ft

from form.controls.buttons import TextButton, IconButtons
from form.controls.inputs import Inputs, DataText, TableColumn
from connection.con_manager import ConnectionManager


class Form(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True)

        self.page = page
        self.selected_row = None

        # Abrindo conexão com o banco de dados
        self.data: ConnectionManager = ConnectionManager()

        # Definindo os controles de texto do formulário
        self.name = Inputs(label='Nome')
        self.age = Inputs(label='Idade', is_text=False, max_length=2)
        self.email = Inputs(label='E-mail')
        self.phone = Inputs(label='Telefone', is_text=False, max_length=11)

        # Definindo os botões do tipo texto do formulário
        btn_save = TextButton(
            text='Salvar',
            icon=ft.icons.SAVE,
            on_click=self.add_data
        )
        btn_edit = TextButton(
            text='Atualizar',
            icon=ft.icons.EDIT,
            on_click=self.update_data
        )
        btn_remove = TextButton(
            text='Remover',
            icon=ft.icons.DELETE,
            on_click=self.remove_data
        )

        # Definindo os botões do tipo ícone da barra de tarefas
        btn_icon_edit = IconButtons(
            tooltip='Editar dados',
            icon=ft.icons.EDIT,
            on_click=self.edit_filed_text
        )
        btn_icon_pdf = IconButtons(
            tooltip='Baixar em PDF',
            icon=ft.icons.PICTURE_AS_PDF
        )
        btn_icon_excel = IconButtons(
            tooltip='Baixar em Excel',
            icon=ft.icons.SAVE_ALT
        )

        # Definindo o campo de busca que fica na barra de tarefas
        self.search_filed = ft.TextField(
            label='Buscar por nome',
            suffix_icon=ft.icons.SEARCH,
            border=ft.InputBorder.UNDERLINE,
            border_color=ft.colors.WHITE,
            label_style=ft.TextStyle(color=ft.colors.WHITE),
            on_change=self.search_data
        )

        # Definindo os rótulos das colunas da tabela
        col_name = TableColumn(data_text=DataText('NOME'))

        # Criando a tabela
        self.data_table = ft.DataTable(
            divider_thickness=1,
            expand=True,
            sort_column_index=0,
            sort_ascending=True,
            show_checkbox_column=True,
            data_row_color={
                ft.ControlState.SELECTED: 'purple',
                ft.ControlState.PRESSED: 'black'
            },
            heading_row_color=ft.colors.BLACK12,
            border=ft.border.all(2, 'purple'),
            border_radius=10,
            columns=[
                col_name,
                ft.DataColumn(
                    DataText(value='IDADE'),
                    numeric=True
                ),
                ft.DataColumn(DataText(value='EMAIL')),
                ft.DataColumn(DataText(value='TELEFONE')),

            ]
        )

        # Chama a função que exibe os dados na tabela
        self.show_data()

        # Container com o formulário
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

        # Container com a barra de tarefa e a tabela
        self.table = ft.Container(
            padding=10,
            bgcolor='#222222',
            border_radius=10,
            col=8,
            content=ft.Column(
                expand=True,
                controls=[
                    # Container da barra de tarefa acima da tabela
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
                    # Coluna da tabela
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
        # Linha que cria a linha com o formulário e a tabela
        self.content = ft.ResponsiveRow(
            controls=[
                self.form,
                self.table,
            ]
        )

    # Função que busca todos os registros no banco de dados e popula a tabela
    def show_data(self):
        self.data_table.rows = []

        for row in self.data.get_all_contacts():
            self.data_table.rows.append(
                ft.DataRow(
                    on_select_changed=self.get_index,
                    cells=[
                        ft.DataCell(content=ft.Text(value=row[1])),
                        ft.DataCell(content=ft.Text(value=str(row[2]))),
                        ft.DataCell(content=ft.Text(value=row[3])),
                        ft.DataCell(content=ft.Text(value=row[4])),
                    ]
                )
            )

        self.update()

    # Função que adiciona um contato ao banco de dados
    def add_data(self, e):
        name = self.name.value
        age = self.age.value
        email = self.email.value
        phone = self.phone.value

        if len(name) and len(str(age)) and len(email) and len(phone) > 0:
            contact_exists = False

            for row in self.data.get_all_contacts():
                if row[1] == name:
                    contact_exists = True
                    print('Contato já cadastrado')
                    break
            if not contact_exists:
                # Chama a função que insere os dados no banco
                self.data.add_contact(name, age, email, phone)
                # Chama a função que limpa os controles do formulário
                self.clean_fields()
                # Chama a função que atualiza a exibição dos dados na tabela
                self.show_data()
                # Chama a função que fecha a conexão
                self.data.close_connection()

    def get_index(self, e):
        if e.control.selected:
            e.control.selected = False
        else:
            e.control.selected = True

        name = e.control.cells[0].content.value

        for row in self.data.get_all_contacts():
            if row[1] == name:
                self.selected_row = row
                break

        self.update()

    def edit_filed_text(self, e):
        try:
            self.name.value = self.selected_row[1]
            self.age.value = self.selected_row[2]
            self.email.value = self.selected_row[3]
            self.phone.value = self.selected_row[4]

        except Exception as e:
            print('Ocorreu um erro ao editar', e)
        self.update()

    def update_data(self, e):
        name = self.name.value
        age = self.age.value
        email = self.email.value
        phone = self.phone.value

        if len(name) and len(str(age)) and len(email) and len(phone) > 0:
            self.clean_fields()
            self.data.update_contact(self.selected_row[0], name, age, email, phone)
            self.show_data()

        self.update()

    def remove_data(self, e):
        self.data.delete_contact(self.selected_row[1])
        self.clean_fields()
        self.show_data()

    def search_data(self, e):
        search = self.search_filed.value.lower()
        name = list(filter(lambda x: search in x[1].lower(), self.data.get_all_contacts()))
        self.data_table.rows = []

        if not self.search_filed.value == '':
            if len(name) > 0:
                for x in name:
                    self.data_table.rows.append(
                        ft.DataRow(
                            on_select_changed=self.get_index,
                            cells=[
                                ft.DataCell(content=ft.Text(value=x[1])),
                                ft.DataCell(content=ft.Text(value=str(x[2]))),
                                ft.DataCell(content=ft.Text(value=x[3])),
                                ft.DataCell(content=ft.Text(value=x[4])),
                            ]
                        )
                    )
                    self.update()

        else:
            self.show_data()

    def clean_fields(self):
        self.name.value = ''
        self.age.value = ''
        self.email.value = ''
        self.phone.value = ''

    # Retorna o conteúdo da classe Form
    def build(self):
        return self.content
