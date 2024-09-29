import flet as ft


class Inputs(ft.TextField):
    def __init__(
            self,
            label: str,
            max_length: float = None,
            text: bool = True
    ) -> None:
        super().__init__()
        self.label = label
        self.text = text
        self.border_color = ft.colors.PURPLE

        if not text:
            self.max_length = max_length
            self.input_filter = ft.NumbersOnlyInputFilter()
