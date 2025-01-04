import  flet as ft
from noter.modle.note import Note
from noter.config import APP_DESCRIPTION,DB_PATH,DB_NAME
from noter.db.crud import DbCrud
from noter.db.datasource import Database
import os
class NoterView:
    def init_DB(self):
        try:
            self.crud = DbCrud()
            # 从数据库加载笔记
            self.notes: list[Note] = self.crud.get_all_notes()
        except Exception as e:
            print(f"数据库初始化错误: {e}")
            # 显示错误提示
            self.page.show_snack_bar(
                ft.SnackBar(content=ft.Text("数据库初始化失败，请检查数据库文件"))
            )
            self.notes = []
    def __init__(self,page: ft.Page):
        self.page = page
        self.setup_page()
        self.notes: list[Note] = []
        self.init_DB()
        self.current_note: Note = None
        self.setup_controls()
        self.render()
    def setup_page(self):
        # 配置页面基本属性
        self.page.title = APP_DESCRIPTION
        self.page.window_width = 1100
        self.page.window_height = 800
        self.page.padding = 0
        self.page.theme_mode = "light"
        # 设置窗口最小尺寸
        self.page.window_min_width = 800
        self.page.window_min_height = 600
    def create_note(self, e=None):
        # 创建新笔记
        note = Note.create("新建笔记", "")
        self.notes.append(note)
        self.crud.save_note(note)  # 保存到数据库
        self.select_note(note)
        self.update_notes_list()
        # 聚焦标题输入框
        self.title_field.focus()
        self.page.update()
    def update_notes_list(self):
       self.notes_list.controls = [
           self.create_note_item(note) for note in reversed(self.notes)
       ]
       self.page.update()

    def create_note_item(self, note: Note) -> ft.Container:
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(
                                note.title,
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                expand=True
                            ),
                            ft.IconButton(
                                icon=ft.icons.DELETE,
                                icon_size=16,
                                on_click=lambda e, note=note: self.delete_note(note)
                            )
                        ]
                    ),
                    ft.Text(
                        note.preview,
                        size=14,
                        color=ft.colors.GREY_700,
                        overflow=ft.TextOverflow.ELLIPSIS,
                    ),
                ],
            ),
            data=note,  # 存储笔记引用
            padding=10,
            bgcolor=ft.colors.WHITE,
            border_radius=8,
            ink=True,
            on_click=lambda e, note=note: self.select_note(note)
        )


    def select_note(self, note: Note):
        self.current_note = note
        self.title_field.value = note.title
        self.content_field.value = note.content
        self.page.update()

    def delete_note(self, note: Note):
        if note in self.notes:
            # 从列表和数据库中删除笔记
            try:
                self.notes.remove(note)
                self.crud.delete_note(note.id)  # 从数据库删除
                if self.current_note == note:
                    self.current_note = None
                    self.title_field.value = ""
                    self.content_field.value = ""
                self.update_notes_list()
                self.page.update()
            except Exception as e:
                print(f"删除笔记错误: {e}")
                self.page.show_snack_bar(
                    ft.SnackBar(content=ft.Text("删除笔记失败"))
                )
    def on_title_change(self, e):
        if self.current_note:
            try:
                self.current_note.update(title=e.control.value)
                self.crud.save_note(self.current_note)  # 保存到数据库
                self.update_notes_list()
                self.page.update()
            except Exception as e:
               print(f"保存笔记错误: {e}")
               self.page.show_snack_bar(
                   ft.SnackBar(content=ft.Text("保存笔记失败"))
               )   
    def on_content_change(self, e):
        if self.current_note:
            try:
                self.current_note.update(content=e.control.value)
                self.crud.save_note(self.current_note)  # 保存到数据库
                self.update_notes_list()
                self.page.update()
            except Exception as e:
               print(f"保存笔记错误: {e}")
               self.page.show_snack_bar(
                   ft.SnackBar(content=ft.Text("保存笔记失败"))
               )
    def search_notes(self, e):
        query = e.control.value.lower()
        if query:
            # 执行搜索
            self.notes=self.crud.search_notes(query)
        else:
            # 如果查询为空，显示所有笔记
            self.notes = self.crud.get_all_notes()
        """  for note_container in self.notes_list.controls:
            note = note_container.data
            visible = (
                query in note.title.lower() or
                query in note.content.lower()
            )
            note_container.visible = visible """
        self.update_notes_list()
        self.page.update()

    def setup_controls(self):
       # 创建搜索框
       self.search_field = ft.TextField(
           hint_text="搜索笔记...",
           prefix_icon=ft.icons.SEARCH,
           width=200,
           on_change=self.search_notes
       )

       # 创建笔记列表
       self.notes_list = ft.ListView(
           spacing=2,
           padding=10,
       )

       # 创建标题输入框
       self.title_field = ft.TextField(
           label="标题",
           border=ft.InputBorder.NONE,
           text_style=ft.TextStyle(size=24, weight=ft.FontWeight.BOLD),
           on_change=self.on_title_change
       )

       # 创建内容输入框
       self.content_field = ft.TextField(
           label="开始输入笔记内容...",
           border=ft.InputBorder.NONE,
           multiline=True,
           min_lines=20,
           on_change=self.on_content_change
       )

       # 创建侧边栏
       self.sidebar = ft.Container(
           content=ft.Column(
               controls=[
                   ft.Container(
                       content=ft.Text("Noter", size=32, weight=ft.FontWeight.BOLD),
                       padding=ft.padding.only(left=20, top=20, bottom=20)
                   ),
                   ft.Container(
                       content=ft.ElevatedButton(
                           "新建笔记",
                           icon=ft.icons.ADD,
                           width=200,
                           on_click=self.create_note
                       ),
                       padding=ft.padding.only(left=20)
                   ),
                   ft.Container(
                       content=self.search_field,
                       padding=ft.padding.only(left=20, top=20)
                   ),
               ],
           ),
           width=250,
           bgcolor=ft.colors.BLUE_GREY_50,
           border=ft.border.only(right=ft.BorderSide(1, ft.colors.BLACK12)),
       )

       # 创建编辑区
       self.editor = ft.Container(
           content=ft.Column(
               controls=[
                   self.title_field,
                   self.content_field,
               ],
               spacing=20,
           ),
           padding=30,
           expand=True,
       )
    def render(self):
        # 主布局
        self.page.add(
            ft.Row(
                controls=[
                    self.sidebar,
                    ft.Container(
                        content=self.notes_list,
                        width=300,
                        bgcolor=ft.colors.with_opacity(0.5, ft.colors.BLUE_GREY_50),
                    ),
                    self.editor,
                ],
                expand=True,
            )
        )
        self.update_notes_list()