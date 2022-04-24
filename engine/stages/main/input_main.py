import PySimpleGUI as sg

sg.theme("Dark2")

layout = [ [sg.Text("Введите текст:")],
           [sg.Input(size=(70,1))],
           [sg.Button('Ok')]
           ]



window = sg.Window('Анализ текста на сарказм', layout)
event, values = window.read()
print('Hello', values[0], "! Thanks for trying PySimpleGUI")
window.close()