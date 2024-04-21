import flet as ft
from flet import Text

def main(page: ft.Page) -> None:
    page.title = 'Hot Reload'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.theme_mode = 'light'
    
    text: Text = Text(value='This is some text',
                      text_align=ft.TextAlign.CENTER,
                      width=200,
                      size=40)
    page.add(text)
    
if __name__ == '__main__':
    ft.app(target=main)