from Tkinter import *
#from unidad2 import recursividad
from unidad22 import recursividad
from unidad4 import arbol
from unidad1 import tarea
from unidad3 import lista
from unidad3c import colas
from unidad3p import pilas
from unidad5 import ordena
from unidad3cc import colacir
from unidad51 import exter
from unidad52 import mezcladir
#import ttk
from secuencia import secuencia
from bin import bina
from bhash import ha

import numpy as n
class proy():
    def __init__(self):
        self.ven= Tk()
        #options=[
         #   "dgc",
          #  "dfgdf"
        #]
        #self.cmb=ttk.Combobox(self.ven,width=21,values=options, state="readonly").place(x=90,y=120)
        Label(self.ven, font=("ROCKWELL", 18), fg='black',text="INTERFAZ GRAFICA",bg='gray').place(x=10,y=0)
        self.ven.geometry("250x400")
        self.ven.config(bg="gray")
        self.ven.config(relief="sunken")
        self.ven.title("proyecto final")
        btnagregarprove = Button(self.ven,font=("INK FREE", 18), fg='black', text="unidad 1", bg='gray', command=self.unidad1, relief=FLAT)
        btnagregarprove.place(x=70, y=50)
        btnagregarprove = Button(self.ven,font=("INK FREE", 18), fg='black', text="unidad 2", bg='gray', command=self.unidad2,relief=FLAT)
        btnagregarprove.place(x=70, y=100)
        btnagregarprove = Button(self.ven,font=("INK FREE", 18), fg='black', text="unidad 3", bg='gray', command=self.unidad3,relief=FLAT)
        btnagregarprove.place(x=70, y=150)
        btnagregarprove = Button(self.ven,font=("INK FREE", 18), fg='black', text="unidad 4", bg='gray', command=self.unidad4,relief=FLAT)
        btnagregarprove.place(x=70, y=200)
        btnagregarprove = Button(self.ven, font=("INK FREE", 18), fg='black', text="unidad 5", bg='gray',
                                 command=self.unidad5, relief=FLAT)
        btnagregarprove.place(x=70, y=250)
        btnagregarprove = Button(self.ven, font=("INK FREE", 18), fg='black', text="unidad 6", bg='gray',
                                 command=self.unidad6, relief=FLAT)
        btnagregarprove.place(x=70, y=300)
        btnagregarprove = Button(self.ven, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
                                 command=self.salir, relief=FLAT)
        btnagregarprove.place(x=70, y=350)
        self.ven = mainloop()
    def salir(self):
        self.ven.destroy()
    def ajuera(self):
        self.v.destroy()
    def unidad1(self):
        self.v1 = Toplevel()
        Label(self.v1, font=("ROCKWELL", 18), fg='black', text="Unidad 1", bg='gray').place(x=10, y=0)
        self.v1.geometry("300x270")
        self.v1.config(bg="gray")
        self.v1.config(relief="sunken")
        self.v1.title("Unidad 1")
        Label(self.v1, font=("ROCKWELL", 18), fg='black', text="contenido unidad 1", bg='gray').place(x=10,
                                                                                                                 y=0)
        Button(self.v1, font=("INK FREE", 18), fg='black', text="arreglo promedio", bg='gray',
               command=self.unidad11, relief=FLAT).place(x=70, y=50)
        Button(self.v1, font=("INK FREE", 18), fg='black', text="doble lectura", bg='gray',
               command=self.unidad12, relief=FLAT).place(x=70, y=100)
        Button(self.v1, font=("INK FREE", 18), fg='black', text="muchas variables", bg='gray',
               command=self.unidad13, relief=FLAT).place(x=70, y=150)
        Button(self.v1, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
              command=self.ajuera1, relief=FLAT).place(x=70, y=200)
        self.v1 = mainloop()
    def ajuera1(self):
        self.v1.destroy()
    def unidad11(self):
        self.nu=0
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="Unidad 1", bg='gray').place(x=10, y=0)
        self.v.geometry("370x250")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        self.v.title("Unidad 1")
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="insertar dimension del arreglo", bg='gray').place(x=10, y=0)
        self.dat = IntVar()
        Entry(self.v, textvariable=self.dat).place(x=70, y=50)
        Button(self.v, font=("INK FREE", 18), fg='black', text="crear", bg='gray',
               command=self.ir, relief=FLAT).place(x=70, y=100)
        Button(self.v, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
               command=self.ajuera, relief=FLAT).place(x=70, y=150)
        self.v=mainloop()
    def ir(self):
        a = self.dat.get()
        self.e = n.zeros(a)
        tarea().arreglos(self.nu, self.e,a)
    def unidad12(self):
        self.nu = 0
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="Unidad 1", bg='gray').place(x=10, y=0)
        self.v.geometry("370x250")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        self.v.title("Unidad 1")
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="insertar dimension del arreglo", bg='gray').place(x=10,
                                                                                                                 y=0)
        self.dat = IntVar()
        Entry(self.v, textvariable=self.dat).place(x=70, y=50)
        Button(self.v, font=("INK FREE", 18), fg='black', text="crear", bg='gray',
               command=self.ir1, relief=FLAT).place(x=70, y=100)
        Button(self.v, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
               command=self.ajuera, relief=FLAT).place(x=70, y=150)
        self.v = mainloop()
    def ir1(self):
        a = self.dat.get()
        self.e = n.zeros(a)
        tarea().cuando(self.nu, self.e,a)
    def unidad13(self):
        tarea().muchas()




    def unidad2(self):
        self.v2 = Toplevel()
        Label(self.v2, font=("ROCKWELL", 18), fg='black', text="Unidad 2", bg='gray').place(x=10, y=0)
        self.v2.geometry("900x700")
        self.v2.config(bg="gray")
        self.v2.config(relief="sunken")
        self.v2.title("Unidad 2")
        Label(self.v2, font=("ROCKWELL", 18), fg='black', text="contenido unidad 2", bg='gray').place(x=10,
                                                                                                      y=0)
        Button(self.v2, font=("INK FREE", 18), fg='black', text="factorial iterativo", bg='gray',
               command=self.bot1, relief=FLAT).place(x=70, y=50)
        Button(self.v2, font=("INK FREE", 18), fg='black', text="factorial recursivo", bg='gray',
               command=self.bot2, relief=FLAT).place(x=70, y=100)
        Button(self.v2, font=("INK FREE", 18), fg='black', text="fibonacci iterativo", bg='gray',
               command=self.bot3, relief=FLAT).place(x=70, y=150)
        Button(self.v2, font=("INK FREE", 18), fg='black', text="fibonacci recursivo", bg='gray',
               command=self.bot4, relief=FLAT).place(x=70, y=200)
        Button(self.v2, font=("INK FREE", 18), fg='black', text="arreglo derecha - izquierda recursivo", bg='gray',
               command=self.bot5, relief=FLAT).place(x=70, y=250)
        Button(self.v2, font=("INK FREE", 18), fg='black', text="arreglo izquierda - derecha recursivo", bg='gray',
               command=self.bot6, relief=FLAT).place(x=70, y=300)
        Button(self.v2, font=("INK FREE", 18), fg='black', text="arreglo derecha - izquierda iterativo", bg='gray',
               command=self.bot7, relief=FLAT).place(x=70, y=350)
        Button(self.v2, font=("INK FREE", 18), fg='black', text="arreglo izquierda - derecha iterativo", bg='gray',
               command=self.bot8, relief=FLAT).place(x=70, y=400)
        Button(self.v2, font=("INK FREE", 18), fg='black', text="suma de datos del arreglo recursivo", bg='gray',
               command=self.bot9, relief=FLAT).place(x=70, y=450)
        Button(self.v2, font=("INK FREE", 18), fg='black', text="suma de datos del arreglo iterativo", bg='gray',
               command=self.bot10, relief=FLAT).place(x=70, y=500)
        Button(self.v2, font=("INK FREE", 18), fg='black', text="euclides iterativo", bg='gray',
               command=self.bot11, relief=FLAT).place(x=70, y=550)
        Button(self.v2, font=("INK FREE", 18), fg='black', text="euclides recursivo", bg='gray',
               command=self.bot12, relief=FLAT).place(x=70, y=600)
        Button(self.v2, font=("INK FREE", 18), fg='black', text="torres de hanoi recursivo", bg='gray',
               command=self.bot13, relief=FLAT).place(x=70, y=650)
        Button(self.v2, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
               command=self.sal, relief=FLAT).place(x=700, y=200)
        self.v2 = mainloop()
        #recursividad()
    def bot1(self):
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="Unidad 1", bg='gray').place(x=10, y=0)
        self.v.geometry("370x250")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="insertar dato", bg='gray').place(x=10,
                                                                                                                 y=0)
        self.dat = IntVar()
        Entry(self.v, textvariable=self.dat).place(x=70, y=50)
        Button(self.v, font=("INK FREE", 18), fg='black', text="factorial", bg='gray',
               command=self.facto, relief=FLAT).place(x=70, y=100)
        self.res = StringVar()
        Label(self.v, textvariable=str(self.res), bg="gray").place(x=200, y=150)
        Button(self.v, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
               command=self.ajuera, relief=FLAT).place(x=70, y=150)
        self.v=mainloop()
    def facto(self):
        b = self.dat.get()
        e=recursividad().normal(b)
        self.res.set("factorial: " + str(e))
    def bot2(self):
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="Unidad 1", bg='gray').place(x=10, y=0)
        self.v.geometry("370x250")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="insertar dato", bg='gray').place(x=10,
                                                                                                y=0)
        self.dat = IntVar()
        Entry(self.v, textvariable=self.dat).place(x=70, y=50)
        Button(self.v, font=("INK FREE", 18), fg='black', text="factorial", bg='gray',
               command=self.facto2, relief=FLAT).place(x=70, y=100)
        self.res = StringVar()
        Label(self.v, textvariable=str(self.res), bg="gray").place(x=200, y=150)
        Button(self.v, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
               command=self.ajuera, relief=FLAT).place(x=70, y=150)
    def facto2(self):
        b = self.dat.get()
        e= recursividad().recursivo(b)
        self.res.set("factorial: "+str(e))
    def bot3(self):
        self.v = Toplevel()
        self.v.geometry("370x250")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="insertar dato", bg='gray').place(x=10,
                                                                                                y=0)
        self.dat = IntVar()
        Entry(self.v, textvariable=self.dat).place(x=70, y=50)
        Button(self.v, font=("INK FREE", 18), fg='black', text="fibonacci", bg='gray',
               command=self.fibo, relief=FLAT).place(x=70, y=100)
        self.res = StringVar()
        Label(self.v, textvariable=str(self.res), bg="gray").place(x=200, y=150)
        Button(self.v, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
               command=self.ajuera, relief=FLAT).place(x=70, y=150)
    def fibo(self):
        b=self.dat.get()
        e=recursividad().fibonacci(b)
        self.res.set("fibonacci: " + str(e))
    def bot4(self):
        self.v = Toplevel()
        self.v.geometry("370x250")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="insertar dato", bg='gray').place(x=10,
                                                                                                y=0)
        self.dat = IntVar()
        Entry(self.v, textvariable=self.dat).place(x=70, y=50)
        Button(self.v, font=("INK FREE", 18), fg='black', text="fibonacci", bg='gray',
               command=self.fibo1, relief=FLAT).place(x=70, y=100)
        self.res = StringVar()
        Label(self.v, textvariable=str(self.res), bg="gray").place(x=200, y=150)
        Button(self.v, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
               command=self.ajuera, relief=FLAT).place(x=70, y=150)
    def fibo1(self):
        b=self.dat.get()
        e=recursividad().fiborec(b)
        self.res.set("fibonacci: " + str(e))


    def bot5(self):
        self.nu = 0
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="Unidad 1", bg='gray').place(x=10, y=0)
        self.v.geometry("370x250")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        self.v.title("Unidad 1")
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="insertar dimension del arreglo", bg='gray').place(x=10,
                                                                                                                 y=0)
        self.dat = IntVar()
        Entry(self.v, textvariable=self.dat).place(x=70, y=50)
        Button(self.v, font=("INK FREE", 18), fg='black', text="crear", bg='gray',
               command=self.der, relief=FLAT).place(x=70, y=100)
        #self.res = StringVar()
        #Label(self.v, textvariable=str(self.res), bg="gray").place(x=200, y=150)
        Button(self.v, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
               command=self.ajuera, relief=FLAT).place(x=70, y=150)
        self.v = mainloop()
    def der(self):
        self.nu=0
        a = self.dat.get()
        self.e = n.zeros(a)
        recursividad().derecha(self.nu, self.e,a)
        #self.res.set("arreglo: " + str(e))
    def bot6(self):
        self.nu = 0
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="Unidad 1", bg='gray').place(x=10, y=0)
        self.v.geometry("370x250")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        self.v.title("Unidad 1")
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="insertar dimension del arreglo", bg='gray').place(x=10,
                                                                                                                 y=0)
        self.dat = IntVar()
        Entry(self.v, textvariable=self.dat).place(x=70, y=50)
        Button(self.v, font=("INK FREE", 18), fg='black', text="crear", bg='gray',
               command=self.izq, relief=FLAT).place(x=70, y=100)
        # self.res = StringVar()
        # Label(self.v, textvariable=str(self.res), bg="gray").place(x=200, y=150)
        Button(self.v, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
               command=self.ajuera, relief=FLAT).place(x=70, y=150)
        self.v = mainloop()
    def izq(self):
        self.nu = 0
        a = self.dat.get()
        self.e = n.zeros(a)
        recursividad().izquierda(self.nu, self.e, a)
    def bot7(self):
        self.nu = 0
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="Unidad 1", bg='gray').place(x=10, y=0)
        self.v.geometry("370x250")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        self.v.title("Unidad 1")
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="insertar dimension del arreglo", bg='gray').place(x=10,
                                                                                                                 y=0)
        self.dat = IntVar()
        Entry(self.v, textvariable=self.dat).place(x=70, y=50)
        Button(self.v, font=("INK FREE", 18), fg='black', text="crear", bg='gray',
               command=self.derit, relief=FLAT).place(x=70, y=100)
        # self.res = StringVar()
        # Label(self.v, textvariable=str(self.res), bg="gray").place(x=200, y=150)
        Button(self.v, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
               command=self.ajuera, relief=FLAT).place(x=70, y=150)
        self.v = mainloop()
    def derit(self):
        self.nu = 0
        a = self.dat.get()
        self.e = n.zeros(a)
        recursividad().deri(self.nu, self.e, a)
    def bot8(self):
        self.nu = 0
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="Unidad 1", bg='gray').place(x=10, y=0)
        self.v.geometry("370x250")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        self.v.title("Unidad 1")
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="insertar dimension del arreglo", bg='gray').place(x=10,
                                                                                                                 y=0)
        self.dat = IntVar()
        Entry(self.v, textvariable=self.dat).place(x=70, y=50)
        Button(self.v, font=("INK FREE", 18), fg='black', text="crear", bg='gray',
               command=self.izqui, relief=FLAT).place(x=70, y=100)
        # self.res = StringVar()
        # Label(self.v, textvariable=str(self.res), bg="gray").place(x=200, y=150)
        Button(self.v, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
               command=self.ajuera, relief=FLAT).place(x=70, y=150)
        self.v = mainloop()
    def izqui(self):
        self.nu = 0
        a = self.dat.get()
        self.e = n.zeros(a)
        recursividad().izqi(self.nu, self.e, a)
    def bot9(self):
        self.nu = 0
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="Unidad 1", bg='gray').place(x=10, y=0)
        self.v.geometry("370x250")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        self.v.title("Unidad 1")
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="insertar dimension del arreglo", bg='gray').place(x=10,
                                                                                                                 y=0)
        self.dat = IntVar()
        Entry(self.v, textvariable=self.dat).place(x=70, y=50)
        Button(self.v, font=("INK FREE", 18), fg='black', text="crear", bg='gray',
               command=self.sumar, relief=FLAT).place(x=70, y=100)
        # self.res = StringVar()
        # Label(self.v, textvariable=str(self.res), bg="gray").place(x=200, y=150)
        Button(self.v, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
               command=self.ajuera, relief=FLAT).place(x=70, y=150)
        self.v = mainloop()
    def sumar(self):
        self.nu = 0
        a = self.dat.get()
        self.e = n.zeros(a)
        recursividad().sum(self.nu, self.e, a)
    def bot10(self):
        self.nu = 0
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="Unidad 1", bg='gray').place(x=10, y=0)
        self.v.geometry("370x250")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        self.v.title("Unidad 1")
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="insertar dimension del arreglo", bg='gray').place(x=10,
                                                                                                                 y=0)
        self.dat = IntVar()
        Entry(self.v, textvariable=self.dat).place(x=70, y=50)
        Button(self.v, font=("INK FREE", 18), fg='black', text="crear", bg='gray',
               command=self.sumaite, relief=FLAT).place(x=70, y=100)
        # self.res = StringVar()
        # Label(self.v, textvariable=str(self.res), bg="gray").place(x=200, y=150)
        Button(self.v, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
               command=self.ajuera, relief=FLAT).place(x=70, y=150)
        self.v=mainloop()
    def sumaite(self):
        self.nu = 0
        a = self.dat.get()
        self.e = n.zeros(a)
        recursividad().sumai(self.nu, self.e, a)
    def bot11(self):
        self.v = Toplevel()
        self.v.geometry("370x250")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="insertar dato", bg='gray').place(x=10,
                                                                                                y=0)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="numero mayor", bg='gray').place(x=70,
                                                                                                y=50)
        self.dat = IntVar()
        Entry(self.v, textvariable=self.dat).place(x=70, y=100)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="numero menor", bg='gray').place(x=70,
                                                                                               y=150)
        self.dat1 = IntVar()
        Entry(self.v, textvariable=self.dat1).place(x=70, y=200)
        Button(self.v, font=("INK FREE", 18), fg='black', text="divisor", bg='gray',
               command=self.euc, relief=FLAT).place(x=270, y=0)
        self.res = StringVar()
        Label(self.v, textvariable=str(self.res), bg="gray").place(x=270, y=150)
        Button(self.v, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
               command=self.ajuera, relief=FLAT).place(x=270, y=50)
    def euc(self):
        a = self.dat.get()
        b = self.dat1.get()
        e = recursividad().euclidesiter(a,b)
        self.res.set("divisor: " + str(e))
    def bot12(self):
        self.v = Toplevel()
        self.v.geometry("370x250")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="insertar dato", bg='gray').place(x=10,
                                                                                                y=0)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="numero mayor", bg='gray').place(x=70,
                                                                                               y=50)
        self.dat = IntVar()
        Entry(self.v, textvariable=self.dat).place(x=70, y=100)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="numero menor", bg='gray').place(x=70,
                                                                                               y=150)
        self.dat1 = IntVar()
        Entry(self.v, textvariable=self.dat1).place(x=70, y=200)
        Button(self.v, font=("INK FREE", 18), fg='black', text="divisor", bg='gray',
               command=self.euc1, relief=FLAT).place(x=270, y=0)
        self.res = StringVar()
        Label(self.v, textvariable=str(self.res), bg="gray").place(x=270, y=150)
        Button(self.v, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
               command=self.ajuera, relief=FLAT).place(x=270, y=50)
    def euc1(self):
        a = self.dat.get()
        b = self.dat1.get()
        e = recursividad().euclidesre(a,b)
        self.res.set("divisor: " + str(e))
    def bot13(self):
        self.v = Toplevel()
        self.v.geometry("370x250")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="insertar numero de discos", bg='gray').place(x=10,
                                                                                                y=0)
        self.dat = IntVar()
        Entry(self.v, textvariable=self.dat).place(x=70, y=50)
        Button(self.v, font=("INK FREE", 18), fg='black', text="comenzar", bg='gray',
               command=self.han, relief=FLAT).place(x=70, y=100)
        self.res = StringVar()
        Label(self.v, textvariable=str(self.res), bg="gray").place(x=200, y=150)
        Button(self.v, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
               command=self.ajuera, relief=FLAT).place(x=70, y=150)
    def han(self):
        n = self.dat.get()
        origen = 'a'
        destino = 'b'
        auxiliar = 'c'
        k=[]
        recursividad().hanoire(n,origen,auxiliar,destino,k)
        self.res.set("movimientos: " + str(len(k)))
    def sal(self):
        self.v2.destroy()





    def unidad3(self):
        self.v1 = Toplevel()
        Label(self.v1, font=("ROCKWELL", 18), fg='black', text="Unidad 1", bg='gray').place(x=10, y=0)
        self.v1.geometry("250x270")
        self.v1.config(bg="gray")
        self.v1.config(relief="sunken")
        self.v1.title("Unidad 1")
        Label(self.v1, font=("ROCKWELL", 18), fg='black', text="contenido unidad 1", bg='gray').place(x=10,
                                                                                                      y=0)
        Button(self.v1, font=("INK FREE", 18), fg='black', text="lista enlazada", bg='gray',
               command=self.list, relief=FLAT).place(x=70, y=50)
        Button(self.v1, font=("INK FREE", 18), fg='black', text="cola", bg='gray',
               command=self.col, relief=FLAT).place(x=70, y=100)
        Button(self.v1, font=("INK FREE", 18), fg='black', text="pila", bg='gray',
               command=self.pi, relief=FLAT).place(x=70, y=150)
        Button(self.v1, font=("INK FREE", 18), fg='black', text="cola circular", bg='gray',
               command=self.colc, relief=FLAT).place(x=70, y=200)
        self.v1 = mainloop()
    def list(self):
        lista().inicia()
    def col(self):
        colas().comienza()
    def pi(self):
        pilas().inicio()
    def colc(self):
        colacir().empezar()


    def unidad4(self):
        arbol().inicia()

    def unidad5(self):
        self.v5 = Toplevel()
        Label(self.v5, font=("ROCKWELL", 18), fg='black', text="Unidad 5", bg='gray').place(x=10, y=0)
        self.v5.geometry("250x350")
        self.v5.config(bg="gray")
        self.v5.config(relief="sunken")
        self.v5.title("Unidad 5")
        Label(self.v5, font=("ROCKWELL", 18), fg='black', text="contenido unidad 5", bg='gray').place(x=10,
                                                                                                      y=0)
        Button(self.v5, font=("INK FREE", 18), fg='black', text="burbuja", bg='gray',
               command=self.bur, relief=FLAT).place(x=70, y=50)
        Button(self.v5, font=("INK FREE", 18), fg='black', text="quicksort", bg='gray',
               command=self.quick, relief=FLAT).place(x=70, y=100)
        Button(self.v5, font=("INK FREE", 18), fg='black', text="shellsort", bg='gray',
               command=self.shell, relief=FLAT).place(x=70, y=150)
        Button(self.v5, font=("INK FREE", 18), fg='black', text="radix", bg='gray',
               command=self.rad, relief=FLAT).place(x=70, y=200)

        Button(self.v5, font=("INK FREE", 18), fg='black', text="intercalacion", bg='gray',
               command=self.intercala, relief=FLAT).place(x=70, y=250)
        Button(self.v5, font=("INK FREE", 18), fg='black', text="mezcla directa", bg='gray',
               command=self.di, relief=FLAT).place(x=70, y=300)
        self.v5 = mainloop()
    def intercala(self):
        self.v51 = Toplevel()
        Label(self.v51, font=("ROCKWELL", 18), fg='black', text="unidad 5", bg='gray').place(x=10, y=0)
        self.v51.geometry("600x100")
        self.v51.config(bg="gray")
        self.v51.config(relief="sunken")
        self.v51.title("Unidad 5")
        Label(self.v51, font=("ROCKWELL", 18), fg='black', text="colocar datos en los archivos de forma ordenada", bg='gray').place(x=10,
                                                                                                      y=0)
        Button(self.v51, font=("INK FREE", 18), fg='black', text="ordenar", bg='gray',
               command=self.intercala1, relief=FLAT).place(x=200, y=50)
    def intercala1(self):
        exter().intercalacion()

    def di(self):
        self.v51 = Toplevel()
        Label(self.v51, font=("ROCKWELL", 18), fg='black', text="unidad 5", bg='gray').place(x=10, y=0)
        self.v51.geometry("600x100")
        self.v51.config(bg="gray")
        self.v51.config(relief="sunken")
        self.v51.title("Unidad 5")
        Label(self.v51, font=("ROCKWELL", 18), fg='black', text="colocar datos a ordenar en el archivo", bg='gray').place(x=10,
                                                                                                      y=0)
        Button(self.v51, font=("INK FREE", 18), fg='black', text="ordenar", bg='gray',
               command=self.di1, relief=FLAT).place(x=200, y=50)
    def di1(self):
        mezcladir().principio()

    def bur(self):
        ordena().bu()
    def quick(self):
        ordena().qui()
    def shell(self):
        ordena().shel()
    def rad(self):
        ordena().radi()
    def unidad6(self):
        self.v6 = Toplevel()
        self.v6.geometry("250x250")
        self.v6.config(bg="gray")
        self.v6.config(relief="sunken")
        self.v6.title("Unidad 6")
        Label(self.v6, font=("ROCKWELL", 18), fg='black', text="tipos de busquedas", bg='gray').place(x=10,
                                                                                                      y=0)
        Button(self.v6, font=("INK FREE", 18), fg='black', text="secuencial", bg='gray',
               command=self.unidad61, relief=FLAT).place(x=70, y=50)
        Button(self.v6, font=("INK FREE", 18), fg='black', text="binaria", bg='gray',
               command=self.bi1, relief=FLAT).place(x=70, y=100)
        Button(self.v6, font=("INK FREE", 18), fg='black', text="hash", bg='gray',
               command=self.has, relief=FLAT).place(x=70, y=150)
        self.v6 = mainloop()
    def has(self):
        self.a = n.array([91,55,1,2,7,3,8,567,79,45,23,86])
        self.v63 = Toplevel()
        self.v63.geometry("500x250")
        self.v63.config(bg="gray")
        self.v63.config(relief="sunken")
        self.v63.title("Unidad 6")
        Label(self.v63, font=("ROCKWELL", 18), fg='black', text="arreglo con datos", bg='gray').place(x=10,
                                                                                                      y=0)
        Label(self.v63, font=("ROCKWELL", 18), fg='black', text=str(self.a), bg='gray').place(x=10,
                                                                                              y=50)
        self.datin = IntVar()
        Entry(self.v63, textvariable=self.datin).place(x=70, y=125)
        Button(self.v63, font=("INK FREE", 18), fg='black', text="buscar", bg='gray',
               command=self.has1, relief=FLAT).place(x=70, y=150)
        self.v63 = mainloop()
    def has1(self):
        ha().bhas(self.a,self.datin.get())


    def bi1(self):
        self.a = n.array([1,2,3,4,5,6,7,8,9])
        self.v62 = Toplevel()
        self.v62.geometry("250x350")
        self.v62.config(bg="gray")
        self.v62.config(relief="sunken")
        self.v62.title("Unidad 6")
        Label(self.v62, font=("ROCKWELL", 18), fg='black', text="arreglo con datos", bg='gray').place(x=10,
                                                                                                      y=0)
        Label(self.v62, font=("ROCKWELL", 18), fg='black', text=str(self.a), bg='gray').place(x=10,
                                                                                         y=50)
        self.dati = IntVar()
        Entry(self.v62, textvariable=self.dati).place(x=70, y=125)
        Button(self.v62, font=("INK FREE", 18), fg='black', text="buscar", bg='gray',
               command=self.bi, relief=FLAT).place(x=70, y=150)
        self.v62 = mainloop()
    def bi(self):
        self.a = n.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
        bina().bin(self.a,self.dati.get())


    def unidad61(self):
        self.a = n.array([5, 6, 4, 7, 3, 2, 8, 9, 1])
        self.v61 = Toplevel()
        self.v61.geometry("250x350")
        self.v61.config(bg="gray")
        self.v61.config(relief="sunken")
        self.v61.title("Unidad 6")
        Label(self.v61, font=("ROCKWELL", 18), fg='black', text="arreglo con datos", bg='gray').place(x=10,
                                                                                                      y=0)
        Label(self.v61, font=("ROCKWELL", 18), fg='black', text=self.a, bg='gray').place(x=10,
                                                                                                     y=50)
        self.dat = IntVar()
        Entry(self.v61, textvariable=self.dat).place(x=70, y=125)
        Button(self.v61, font=("INK FREE", 18), fg='black', text="buscar", bg='gray',
               command=self.secu, relief=FLAT).place(x=70, y=150)
        self.v61 = mainloop()
    def secu(self):
        secuencia().sec(self.a,self.dat.get())

p=proy()