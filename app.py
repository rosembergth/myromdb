from tkinter import *
import tkinter as ttk
from os import system

# Comando que Limpia pantalla
system("cls")

class MyVentana(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.fr_titulo()
        self.fr_mensaje1()
        self.fr_opc1()
        self.fr_izq()
        self.fr_der()
        self.fr_cen()
        
    # Title bar function   
    def fr_titulo(self):
        self.titulo_ppal = Frame(self, bg='gray')
        self.titulo_ppal.pack(fill='both', ipady=17)
        self.titulo_ppal.config(relief="ridge")
        self.titulo_ppal.config(bd=2)
        self.descripcion = Label(self, text="♣ Database management systems", bg='gray', fg='white')
        self.boton_salir = Button(self, text='Quit', fg='black', bg='white', command=ventana.destroy)
        self.boton_salir.place(x=790, y=5, width=100, height=25)
        self.descripcion.place(x=5, y=7)

    # Menu bar function
    def fr_mensaje1(self):
        self.mensaje1 = Frame(self, bg='orange')
        self.mensaje1.pack(fill='both', ipady=17)
        self.mensaje1.config(relief="ridge")
        self.mensaje1.config(bd=2)
        self.boton_opcion1 = Button(self, text='Connection', fg='black', bg='white')
        self.boton_opcion2 = Button(self, text='Databases', fg='black', bg='white')
        self.boton_opcion3 = Button(self, text='SQL', fg='black', bg='white')
        self.boton_opcion4 = Button(self, text='Licence', fg='black', bg='white')
        self.boton_opcion1.place(x=5, y=40, width=100, height=25)
        self.boton_opcion2.place(x=110, y=40, width=100, height=25)
        self.boton_opcion3.place(x=217, y=40, width=100, height=25)
        self.boton_opcion4.place(x=324, y=40, width=100, height=25)

    # Left frame function
    def fr_izq(self):
        self.fr_izq = Frame(self, bg='black',)
        self.fr_izq.pack(ipadx=130, ipady=155, side='left')
        self.fr_izq.config(relief="ridge")
        self.fr_izq.config(bd=5)

    # Center frame function
    def fr_cen(self):
        self.fr_cen = Frame(self, bg='gray')
        self.fr_cen.pack(ipadx=189, ipady=155)
        self.fr_cen.config(relief="ridge")
        self.fr_cen.config(bd=5)

    # Right frame function
    def fr_der(self):
        self.fr_der = Frame(self, bg='black',)
        self.fr_der.pack(ipadx=130, ipady=155, side='right')
        self.fr_der.config(relief="ridge")
        self.fr_der.config(bd=5)

    # information bar function
    def fr_opc1(self):
        self.fr_opc1 = Frame(self, bg='blue')
        self.fr_opc1.pack(fill='x', ipady=15, side='bottom')
        self.fr_opc1.config(relief="ridge")
        self.fr_opc1.config(bd=2)

ventana = Tk()

# Center window
ancho_ventana = 900
alto_ventana = 380
x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventana.geometry(posicion)

# Window icon and title
ventana.title("Data Base Manager - Rosembergth Ordoñez Mujica")
ventana.resizable(width=0, height=0)
ventana.iconbitmap('D://PROYECTOS_PYTHON/PYTHON21/bdrom.ico')


app = MyVentana(ventana)

app.mainloop()