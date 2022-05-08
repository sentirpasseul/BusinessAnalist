from tkinter import *
from tkinter import  ttk

window = Tk()
window.title("Анализатор ЕЯ-текстов на предмет сарказма")
window.geometry('800x500')

frm = ttk.Frame(window, padding=10)
frm.grid()

def button_launch():
    res = txt.get()
    return res

ttk.Label(frm, text="Введите текст:", font=("Arial Bold", 12)).grid(column=0,row=0)

txt = Entry(Text(frm, width=60, height=10).grid(column=1, row=0))
ttk.Button(frm, text="Выйти", command=window.destroy).grid(column=1, row=1)
ttk.Button(frm, text="Запуск", command=button_launch).grid(column=0, row=1)
print(txt.get())


window.mainloop()





""""
import PySimpleGUI as sg

sg.theme("SystemDefault1")



layout = [
            [sg.Text('Анализатор ЕЯ-текстов на предмет сарказма', size=(80, 10), font=())],
            [sg.InputText()],
            [sg.Button("Ввести"), sg.Cancel()]
]





window = sg.Window('Анализатор сарказма', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    #print('You entered ', f)
    print(event, f)


window.close()
"""

