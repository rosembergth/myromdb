import tkinter as ttk
from tkinter import Frame, StringVar, Tk, Label, Button, Entry
from os import system

 # Comando que Limpia pantalla
system("cls")

class MyVentana(Frame):

    def __init__(self, master=None):
        super().__init__(master, width=320, height=170)
        self.master = master
        self.pack()
        self.create_widgets()

    def suma(self):
        n1 = self.txt1.get()
        n2 = self.txt2.get()
        resul = float(n1) + float(n2)
        self.txt3.delete(0, 'end')
        self.txt3.insert(0, resul)

    def create_widgets(self):
        self.lbl1 = Label(self, text='Esta es una etiqueta 1')
        self.lbl2 = Label(self, text='Esta es una etiqueta 2')
        self.lbl3 = Label(self, text='Resultado')
        self.txt1 = Entry(self)
        self.txt2 = Entry(self)
        self.txt3 = Entry(self, bg='red', fg='white')
        self.btn = ttk.Button(self, text='Presionar', command=self.suma, bg='gray', fg='white')


        self.lbl1.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.lbl2.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.lbl3.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.txt1.grid(row=0, column=1, padx=5, pady=5)
        self.txt2.grid(row=1, column=1, padx=5, pady=5)
        self.txt3.grid(row=3, column=3, padx=5, pady=5, ipadx=4, ipady=10, sticky='w')
        self.btn.grid(row=4, column=3, padx=5, pady=5, ipadx=4, ipady=10, sticky='E')



ventana = Tk()
ventana.geometry('900x600')
ventana.resizable(width=0, height=0)
ventana.title("Rom / Sistema Python")

app = MyVentana(ventana)

app.mainloop()