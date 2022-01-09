from guizero import App, Text, TextBox, PushButton, Picture, system_config
import requests

url = 'https://corlysis.com:8086/query'
params = {"db": "Technology_Health_Computing", "u": "token", "p": "ecbef8c057c4ebac95399b37189bcf5e"}


#Functions
def say_my_name():
        welcome_message.value = my_name.value
def read_distance_bd():
    r = request.get(url)
    print(r)
    
app = App("Locuras varias")

#print(system_config.supported_image_types)

#Text Widget
welcome_message = Text(app, text="Siempre papi, nunca impapi", size= 30, font="Times New Roman", color="blue")

#Text Box
my_name = TextBox(app)

#Text Box BD
my_info = TextBox(app, read_distance_bd)


#Push Button
update_text = PushButton(app, command=say_my_name, text="Solo lo sabe el sabio")

#Picture
#my_pic = Picture(app, image="IOT-Proyect/dwarf_PNG32.png")

app.display()

