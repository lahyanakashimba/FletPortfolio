import flet as ft

from index import main


ft.run(main, assets_dir="assets", web_renderer=ft.WebRenderer.CANVAS_KIT, no_cdn=True)
