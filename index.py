import flet as ft

def main(page: ft.Page):
    page.title = "Lahya Nakashimba | Portfolio"
    page.window.width = 800
    page.window.height = 800
    
    info = ft.Text("Welcome to my portfolio!")

    def on_nav_change(e):
        idx = page.navigation_bar.selected_index
        if idx == 0:
            info.value = "Home Page"
        elif idx == 1:
            info.value = "Contributions Page"
        else:
            info.value = "About Me"

        page.update()

    page.navigation_bar = ft.NavigationBar(
        selected_index=0,
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.WORK, label="Contributions"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="About Me")
        ],
        on_change=on_nav_change
    )

    page.add(
        ft.Container(content=info, alignment=ft.alignment.Alignment.CENTER, padding=20),
    )


ft.app(target=main)