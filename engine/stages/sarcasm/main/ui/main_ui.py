from tkinter import *
from tkinter import ttk



class MainUI:

    def __init__(self):
        self.window = Tk()
        self.window.title("Анализатор ЕЯ-текстов на предмет сарказма")
        self.window.geometry('800x500')

        self.frm = ttk.Frame(self.window, padding=10)
        frm = self.frm
        self.frm.grid()

    def button_launch(self):
        res = self.txt
        print(res)
        return res

    def frame(self):

        ttk.Label(self.frm, text="Введите текст:", font=("Arial Bold", 12)).grid(column=0,row=0)

        self.txt = Entry()
        self.txt = self.frm.pack

        ttk.Button(self.frm, text="Выйти", command=self.window.destroy).grid(column=1, row=1)
        ttk.Button(self.frm, text="Запуск", command=MainUI.button_launch(self)).grid(column=0, row=1)



        self.window.mainloop()


def main():
    m = MainUI()
    print(m.frame())

main()

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

