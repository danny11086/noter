import flet as ft
from  noter.ui.container import  NoterView
def main(page: ft.Page):
    NoterView(page)
   
if __name__ == "__main__":
    ft.app(target=main)