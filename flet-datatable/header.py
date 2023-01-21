from flet import *
from controls import add_to_control_reference, return_control_reference


control_map = return_control_reference()


class AppHeader(UserControl):
    def __init__(self):
        super().__init__()

    def add_instance(self):
        key = self.__class__.__name__
        print(key)
        add_to_control_reference(key, self)

    def show_search_bar(self, e):
        if e.data == 'true':
            self.controls[0].content.controls[1].opacity = 1
            self.controls[0].content.controls[1].update()
        else:
            self.controls[0].content.controls[1].content.controls[1].value = ''
            self.controls[0].content.controls[1].opacity = 0.6
            self.controls[0].content.controls[1].update()

    def app_header_brand(self):
        return Container(
            content=Text("lxxtec data serve", size=15)
        )

    def app_header_search(self):
        return Container(
            width=320,
            bgcolor='white10',
            border_radius=6,
            padding=8,
            opacity=0.6,
            animate_opacity=320,
            content=Row(
                spacing=10,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Icon(name=icons.SEARCH_ROUNDED, size=17, opacity=0.85),
                    TextField(
                        border_color='transparent',
                        height=20,
                        text_size=14,
                        content_padding=0,
                        cursor_color='white',
                        cursor_width=1,
                        hint_text="Search",
                        on_change=lambda e: self.filter_data_table(e),

                    )
                ]
            )
        )

    def app_header_avatar(self):
        return Container(
            content=IconButton(icons.PERSON)
        )

    def filter_data_table(self, e):
        for key, value in control_map.items():
            if key == 'AppDataTable':
                if len(value.controls[0].controls[0].rows) != 0:
                    for data in value.controls[0].controls[0].rows:
                        s1 = str(e.data)
                        s2 = str(data.cells[0].content.controls[0].value)
                        print(s1, s2)
                        if s1 == s2:
                            data.visable = True
                            print('=')
                            data.update()
                        else:
                            data.visable = False
                            print('!=')
                            data.update()

    def build(self):
        self.add_instance()

        return Container(
            expand=True,
            on_hover=lambda e: self.show_search_bar(e),
            height=60,
            bgcolor='#081d33',
            border_radius=border_radius.only(topLeft=15, topRight=15),
            padding=padding.only(left=15, right=15),
            content=Row(
                expand=True,
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    self.app_header_brand(),
                    self.app_header_search(),
                    self.app_header_avatar(),
                ]
            )
        )


if __name__ == "__main__":
    app = AppHeader()
    print(app.__class__.__name__)
