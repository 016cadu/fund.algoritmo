from tkinter import *

janela = Tk()

janela.title("Nova Tela")

janela.geometry('350x200')

btn1 = Button(janela, text = "Botão 1")
btn1.place(relx = 0.5, rely = 0.5, anchor=CENTER)

btn2 = Button(janela, text = "Botão 2")
btn2.place(x = 100, y = 50, anchor=CENTER)

janela.mainloop()