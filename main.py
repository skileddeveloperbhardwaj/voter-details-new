import flet as flt 
  
def myapp(page: flt.Page): 
    pass
  
  
flt.app(target=myapp)

# import flet as ft
# # import pandas as pd

# def main(page: ft.Page):
#     page.title = "Flet counter example"
#     page.theme_mode = ft.ThemeMode.LIGHT
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER

#     txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

#     def minus_click(e):
#         txt_number.value = str(int(txt_number.value) - 1)
#         page.update()

#     def plus_click(e):
#         txt_number.value = str(int(txt_number.value) + 1)
#         page.update()

#     # def panda_check(e):
#     #     mydataset = {
#     #     'cars': ["BMW", "Volvo", "Ford"],
#     #     'passings': [3, 7, 2]
#     #     }
#     #     myvar = pd.DataFrame(mydataset)
#     #     txt_number.value = str(myvar)
#     #     page.update()

#     page.add(
#         ft.Row(
#             [
#                 ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
#                 txt_number,
#                 ft.IconButton(ft.icons.ADD, on_click=plus_click),
#                 # ft.FilledButton(text="Filled button", on_click=panda_check),
#             ],
#             alignment=ft.MainAxisAlignment.CENTER,
#         )
#     )


# ft.app(main, view=ft.AppView.WEB_BROWSER)
