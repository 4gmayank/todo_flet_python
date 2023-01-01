import flet

from flet import Page, TextField, Row, IconButton, icons

def main(page: Page):
  page.title = "Counter App"
  page.vertical_alignment = 'center'
  textField = TextField(value="0", width=100, text_align="right")
  def minus_clicked(e):
    textField.value = int(textField.value)-1
    page.update()
    
  def plus_clicked(e):
    textField.value = int(textField.value)+1  
    page.update()
  page.add(Row(
    [IconButton(icons.REMOVE, on_click=minus_clicked), 
    textField,
    IconButton(icons.ADD, on_click=plus_clicked),  
    ], alignment='center'
  ))


# flet.app(target=main)
flet.app(target=main, view=flet.WEB_BROWSER)


# python3 counter.py // runt the file as it is
# elements have same main.dart.js
# it is also using web kit
# console flutter web