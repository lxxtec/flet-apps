from flet import *
import flet as ft
from controls import add_to_control_reference, return_control_reference
from btn import return_form_button


class AppForm(UserControl):
    def __init__(self):
        super().__init__()

    def add_instance(self):
        key = self.__class__.__name__
        add_to_control_reference(key, self)

    def app_form_input_field(self, name: str, expand=int):
        return Container(
            expand=expand,
            height=45,
            bgcolor='#ebebeb',
            border_radius=6,
            padding=5,
            content=Column(
                spacing=1,
                controls=[
                    Text(
                        value=name,
                        size=11,
                        color='black',
                        weight='bold'
                    ),
                    TextField(
                        border_color='transparent',
                        height=20,
                        text_size=13,
                        content_padding=0,
                        cursor_color='black',
                        cursor_width=1,
                        cursor_height=18,
                        color='black'
                    ),
                ]
            )
        )

    def build(self):
        self.add_instance()
        return Container(
            expand=True,
            height=190,
            bgcolor='white10',
            border=border.all(1, "#ebebeb"),
            padding=15,
            content=Column(
                expand=True,
                controls=[
                    Row(
                        controls=[
                            self.app_form_input_field("Field *", True)
                        ]
                    ),
                    Row(
                        controls=[
                            self.app_form_input_field("Field one*", 3),
                            self.app_form_input_field("Field two*", 2),
                            self.app_form_input_field("Field three*", 1),
                        ]
                    ),
                    Divider(height=1, color='transparent'),
                    Row(
                        alignment=MainAxisAlignment.END,
                        controls=[
                            return_form_button()
                        ]
                    )
                ]
            )
        )
