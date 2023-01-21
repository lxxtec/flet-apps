# -*- encoding: utf-8 -*-
'''
@File    : main.py
@Time    : 2023/01/21 20:53:53
@Author  : lxxtec
@Contact : 631859877@qq.com
@Version : 0.1
@Desc    : None
'''
import flet
from flet import *


class MainContainer(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return Container(
            width=275,
            height=60,
            content=Column(
                spacing=5,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Text(
                        "Modern Dropdown",
                        size=10,
                        weight='w400',
                        color='white54',
                    ),
                    Text(
                        "Have a Try",
                        size=30,
                        weight='bold'
                    )
                ]
            )
        )


class DropDownContainer(UserControl):
    def __init__(
        self,
        initials: str,
        name: str,
        gend: str,
        title: str,
        description: str,
        salary: str
    ):
        super().__init__()
        self.initials = initials
        self.name = name
        self.gend = gend
        self.title = title
        self.description = description
        self.salary = salary

    def expandContainer(self, e):
        if self.controls[0].height != 180:
            self.controls[0].height = 180
            self.controls[0].update()
        else:
            self.controls[0].height = 90
            self.controls[0].update()

    def TopContainer(self):
        return Container(
            width=265, height=70,
            content=Column(
                spacing=0,
                controls=[
                    Row(
                        controls=[
                            Container(
                                width=40,
                                height=40,
                                bgcolor='white24',
                                border_radius=40,
                                alignment=alignment.center,
                                content=Text(
                                    self.initials,
                                    size=11,
                                    weight="bold"
                                ),
                            ),
                            VerticalDivider(width=2),
                            Container(
                                content=Column(
                                    spacing=1,
                                    alignment=MainAxisAlignment.CENTER,
                                    controls=[
                                        Text(self.name, size=11),
                                        Text(self.gend, size=9,
                                             color="white54"),
                                    ]
                                )
                            ),
                        ]
                    ),
                    Row(
                        alignment=MainAxisAlignment.END,
                        controls=[
                            Container(
                                content=IconButton(
                                    icon=icons.ARROW_DROP_DOWN_CIRCLE_ROUNDED,
                                    icon_size=20,
                                    on_click=lambda e: self.expandContainer(e),
                                )
                            )
                        ]

                    ),
                ],
            ),
        )

    def getEmployeeData(self):
        items = [
            ["Job Title", self.title],
            ["Description", self.description],
            ["Salary", self.salary],
        ]
        l = []
        for item in items:
            l.append(Row(
                controls=[
                    Column(
                        expand=1,
                        horizontal_alignment=CrossAxisAlignment.START,
                        controls=[
                            Text(
                                item[0],
                                size=9,
                                weight='bold',
                            )
                        ]
                    ),
                    Column(
                        expand=2,
                        horizontal_alignment=CrossAxisAlignment.END,
                        controls=[
                            Text(
                                item[1],
                                size=9,
                                weight='bold',
                                color='white54'
                            )
                        ]
                    ),
                ]
            ))
        return l

    def BottomContainer(self):
        # unpack list
        title, desc, salary = self.getEmployeeData()
        return Container(
            width=265,
            height=100,
            bgcolor='transparent',
            content=Column(
                controls=[
                    # add the unpacked list here
                    title,
                    desc,
                    salary,
                ]
            )
        )

    def build(self):
        return Container(
            width=275,
            height=90,
            bgcolor='white54',
            border_radius=11,
            animate=animation.Animation(400, "decelerate"),
            padding=padding.only(left=10, right=10, top=10),
            # clip behavior allows us to clip hte contents to the container
            # this cancels out the overflow but it costly production wise
            clip_behavior=ClipBehavior.ANTI_ALIAS,
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    self.TopContainer(),
                    self.BottomContainer(),
                ]
            )
        )


def main(page: Page):
    page.title = "Flet Modern Dropdown"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    main_container = Container(
        width=280,
        height=600,
        bgcolor='black',
        border_radius=40,
        padding=20,
        content=Column(
            # add classes here
            controls=[
                Divider(height=20, color='transparent'),
                MainContainer(),
                Divider(height=20, color='white24'),
                Text("Employees", size=12),
                DropDownContainer(
                    "WX",
                    "王小明",
                    "Engineer",
                    "Senior SoftWare Engineer",
                    "Full Stack",
                    "$120,000"
                ),
                DropDownContainer(
                    "LX",
                    "李小明",
                    "Engineer",
                    "Senior SoftWare Engineer",
                    "Full Stack",
                    "$120,000"
                ),
                DropDownContainer(
                    "ZH",
                    "张小明",
                    "Engineer",
                    "Senior SoftWare Engineer",
                    "Full Stack",
                    "$120,000"
                ),

            ]
        )
    )
    page.add(main_container)
    page.update()


if __name__ == "__main__":
    flet.app(target=main)
