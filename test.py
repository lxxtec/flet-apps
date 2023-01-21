import flet as ft


def main(page):

    first_name = ft.TextField(label="First name", autofocus=False)
    last_name = ft.TextField(label="Last name")
    greetings = ft.Column(scroll='auto', expand=True, auto_scroll=True)

    def btn_click(e):
        greetings.controls.append(
            ft.Text(f"Hello, {first_name.value} {last_name.value}!"))
        # first_name.value = ""
        # last_name.value = ""
        page.update()
        first_name.focus()

    page.add(
        first_name,
        last_name,
        ft.ElevatedButton("Say hello!", on_click=btn_click),
        greetings,
    )


ft.app(target=main)
