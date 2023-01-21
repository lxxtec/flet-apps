# -*- encoding: utf-8 -*-
'''
@File    : datatable.py
@Time    : 2023/01/21 13:08:09
@Author  : lxxtec
@Contact : 631859877@qq.com
@Version : 0.1
@Desc    : None
'''


import flet as ft
from flet import *
from header import AppHeader
from form import AppForm
from data_table import AppDataTable


def main(page: Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    page.bgcolor = '#fdfdfd'
    page.padding = 20
    page.add(
        Column(
            expand=True,
            controls=[
                # class instance here
                AppHeader(),
                Divider(height=3, color='transparent'),
                AppForm(),
                Column(
                    scroll='auto',
                    expand=True,
                    controls=[
                        AppDataTable()
                    ]
                )
            ]
        )
    )

    page.update()


if __name__ == "__main__":
    ft.app(target=main)
