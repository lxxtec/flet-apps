from flet import *
from controls import add_to_control_reference


class AppDataTable(UserControl):
    def __init__(self):
        super().__init__()

    def add_instance(self):
        key = self.__class__.__name__
        print(key)
        add_to_control_reference(key, self)

    def build(self):
        self.add_instance()
        return Row(
            expand=True,
            controls=[
                DataTable(
                    expand=True,
                    border_radius=8,
                    border=border.all(2, '#ebebeb'),
                    horizontal_lines=border.BorderSide(1, '#ebebeb'),
                    columns=[
                        DataColumn(
                            Text("Column one", size=12,
                                 color='black', weight='bold')
                        ),
                        DataColumn(
                            Text("Column two", size=12,
                                 color='black', weight='bold')
                        ),
                        DataColumn(
                            Text("Column three", size=12,
                                 color='black', weight='bold')
                        ),
                        DataColumn(
                            Text("Column four", size=12,
                                 color='black', weight='bold')
                        ),
                    ],
                    rows=[],
                )
            ],
        )
