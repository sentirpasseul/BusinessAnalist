import tkinter as tk

def GUI():
    text_list = list()
    window = tk.Tk()
    label = tk.Label(
        text="Введите текст для анализа на сарказм:",
        foreground="white",  # Устанавливает белый текст
        background="black",  # Устанавливает черный фон,
        width=50,
        height=5
    )
    label_s = tk.Label(height=2)
    label_s2 = tk.Label(height=2)
    text_input = tk.Text(
        width = 40,
        height=5
    )
    button_input = tk.Button(
        width=2,
        height=2,
        value=text_list.append(text_input.get(input()))
    )
    label.pack()
    label_s.pack()
    text_input.pack()
    button_input.pack()
    label_s2.pack()
    window.mainloop()


GUI()