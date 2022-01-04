from guizero import App, Text, TextBox, PushButton

#Functions
def say_my_name():
        welcome_message.value = my_name.value

app = App("Locuras varias")

#Text Widget
welcome_message = Text(app, text="Siempre papi, nunca impapi", size= 30, font="Times New Roman", color="blue")

#Text Box
my_name = TextBox(app)

#Push Button
update_text = PushButton(app, command=say_my_name, text="Solo lo sabe el sabio")

app.display()

