import flet as ft


class Inputs(ft.TextField):
    def __init__(
            self,
            label: str,
            max_length: float = None,
            is_text: bool = True
    ) -> None:
        super().__init__()
        self.label = label
        self.is_text = is_text
        self.border_color = ft.colors.PURPLE

        if not is_text:
            self.max_length = max_length
            self.input_filter = ft.NumbersOnlyInputFilter()


class DataText(ft.Text):
    def __init__(self, value: str) -> None:
        super().__init__()
        self.value = value
        self.color = ft.colors.PURPLE
        self.weight=ft.FontWeight.BOLD


class TableColumn(ft.DataColumn):
    def __init__(self, data_text: DataText, numeric: bool = None) -> None:
        super().__init__(self)
        self.label = data_text
        self.numeric = numeric
