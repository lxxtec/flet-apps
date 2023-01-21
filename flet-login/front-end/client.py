import flet as ft
from flet import *
import requests


def main(page: Page):
    page.title = 'Routes Example'
    snack = SnackBar(
        Text("Registration successfull!"),
    )

    def GradientGenerator(start, end):
        colorgradient = LinearGradient(
            begin=alignment.bottom_left,
            end=alignment.top_right,
            colors=[
                start,
                end,
            ]
        )
        return colorgradient

    """ main ui section"""
    def route_change(route):
        email = TextField(
            label='Email',
            border='underline',
            width=320,
            text_size=14,
        )
        password = TextField(
            label='Password',
            border='underline',
            width=320,
            text_size=14,
            password=True,
            can_reveal_password=True,
        )
        page.views.clear()

        # each page will have a seperate view, login page, register page ,etc..

        """ start with the registration page """
        page.views.append(
            View(
                "/register",
                horizontal_alignment="center",
                vertical_alignment="center",
                controls=[
                    Column(
                        alignment="center",
                        controls=[
                            Card(
                                elevation=15,
                                content=Container(
                                    width=550,
                                    height=550,
                                    padding=padding.all(30),
                                    gradient=GradientGenerator(
                                        "#1f2937", "#111827"),
                                    border_radius=border_radius.all(12),
                                    content=Column(
                                        horizontal_alignment="center",
                                        alignment="start",
                                        controls=[
                                            Text(
                                                "Mock Registration Form With Python API",
                                                size=32,
                                                weight='w700',
                                                text_align='center',
                                            ),
                                            Text(
                                                "This FLet web-app/registration page is routed to a Flask server",
                                                size=14,
                                                weight="w700",
                                                text_align="center",
                                                color="#64748b",
                                            ),
                                            Container(
                                                padding=padding.only(bottom=20)), email,
                                            Container(
                                                padding=padding.only(bottom=20)), password,
                                            Container(
                                                padding=padding.only(
                                                    bottom=20),
                                            ),
                                            Row(
                                                alignment="center",
                                                spacing=20,
                                                controls=[
                                                    FilledButton(
                                                        content=Text(
                                                            "Register",
                                                            weight="w700",
                                                        ),
                                                        width=160,
                                                        height=40,
                                                        on_click=lambda e: req_register(
                                                            e, email.value, password.value
                                                        ),
                                                    ),
                                                    FilledButton(
                                                        content=Text(
                                                            "Login",
                                                            weight="w700",
                                                        ),
                                                        width=160,
                                                    )
                                                ]
                                            )

                                        ]
                                    )
                                )
                            )
                        ]
                    )
                ]
            )
        )

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = None
    page.on_view_pop = None
    page.go(page.route)


if __name__ == '__main__':
    ft.app(target=main, host="localhost", port=9999, view=ft.WEB_BROWSER)
