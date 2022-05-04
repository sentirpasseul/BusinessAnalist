"""
import PySimpleGUI as sg

sg.theme("SystemDefault1")

input_text = sg.InputText()

layout = [
            [sg.Text('Анализатор ЕЯ-текстов на предмет сарказма', size=(80, 10), font=())],
            [sg.Text("Введите ваш текст"), input_text],
            [sg.Button("Ввести"), sg.Cancel()]
]

window = sg.Window('Анализатор сарказма', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])
    print(input_text)

window.close()

"""