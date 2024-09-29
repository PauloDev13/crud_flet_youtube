import flet as ft

from typing import Callable


class Button(ft.TextButton):
    def __init__(
        self,
        text: str,
        icon: ft.Icon,
        on_click: Callable[[ft.ControlEvent], None] = None
    ):
        super().__init__()
        self.icon = icon
        self.text = text
        self.on_click = on_click
        self.style = ft.ButtonStyle(
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
        )
