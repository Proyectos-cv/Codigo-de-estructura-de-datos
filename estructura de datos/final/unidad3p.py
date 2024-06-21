import numpy as np
from Tkinter import *
class pilas:
    def inicio(self):
        self.v3 = Toplevel()
        Label(self.v3, font=("ROCKWELL", 18), fg='black', text="Unidad 1", bg='gray').place(x=10, y=0)
        self.v3.geometry("250x270")
        self.v3.config(bg="gray")
        self.v3.config(relief="sunken")
        self.v3.title("Unidad 1")
        Label(self.v3, font=("ROCKWELL", 18), fg='black', text="dimension de arreglo", bg='gray').place(x=10,
                                                                                                        y=0)
        self.dat = IntVar()
        Entry(self.v3, textvariable=self.dat).place(x=70, y=50)
        Button(self.v3, font=("INK FREE", 18), fg='black', text="crear", bg='gray',
               command=self.comienzo, relief=FLAT).place(x=70, y=100)
        self.v3 = mainloop()
    def comienzo(self):
        self.band=True
        self.maxi = self.dat.get()
        self.tope = -1
        self.pila = np.zeros(self.maxi)
        self.reg()
    def reg(self):
        self.v1 = Toplevel()
        Label(self.v1, font=("ROCKWELL", 18), fg='black', text="Unidad 3", bg='gray').place(x=10, y=0)
        self.v1.geometry("250x270")
        self.v1.config(bg="gray")
        self.v1.config(relief="sunken")
        self.v1.title("Unidad 1")
        Label(self.v1, font=("ROCKWELL", 18), fg='black', text="contenido unidad 3", bg='gray').place(x=10,
                                                                                                      y=0)
        Button(self.v1, font=("INK FREE", 18), fg='black', text="eliminar", bg='gray',
               command=self.eli, relief=FLAT).place(x=70, y=50)
        Button(self.v1, font=("INK FREE", 18), fg='black', text="insertar", bg='gray',
               command=self.agre, relief=FLAT).place(x=70, y=100)
        self.v1 = mainloop()
    def eli(self):
        self.vacio(self.pila,self.tope,self.band)
        self.pop(self.pila,self.tope,self.band)
        self.mostrar(self.pila,self.tope,self.maxi,self.band)
    def agre(self):
        band = self.lleno(self.pila,self.tope,self.maxi,self.band)
        self.pon()
        #tope=p.push(self.pila,self.tope, self.maxi, self.band)
        #p.mostrar(self.pila, self.tope, self.maxi,self.band)

    def lleno(self,pila,tope,maxi,band):
        self.maxi=maxi
        tope = tope + 1
        if tope==self.maxi:
            self.band=True
            return self.band
        else:
            self.band=False
            return self.band
    def vacio(self,pila,tope,band):
        tope=tope-1
        if tope==-1 or tope < -1:
            tope=tope+1
            self.band = True
            return self.band
        else:
            self.band=False
            return self.band
    def pop(self,pila,tope,band):
        if band==True:
            self.tope = self.tope - 1
            self.v3 = Toplevel()
            Label(self.v3, font=("ROCKWELL", 18), fg='black', text="Unidad 1", bg='gray').place(x=10, y=0)
            self.v3.geometry("270x50")
            self.v3.config(bg="gray")
            self.v3.config(relief="sunken")
            Label(self.v3, font=("ROCKWELL", 18), fg='black', text="pila vacia", bg='gray').place(x=10,
                                                                                                  y=0)
            #print "pila vacia"
        else:
            #print"numero a eliminar: ",pila[tope]
            self.pila[self.tope]=0#int(input("elimina un numero: "))
            self.tope=self.tope-1
            return self.tope
    def pon(self):
        self.vk = Toplevel()
        Label(self.vk, font=("ROCKWELL", 18), fg='black', text="Unidad 3", bg='gray').place(x=10, y=0)
        self.vk.geometry("370x250")
        self.vk.config(bg="gray")
        self.vk.config(relief="sunken")
        self.vk.title("Unidad 3")
        Label(self.vk, font=("ROCKWELL", 18), fg='black', text="agregar elemento", bg='gray').place(x=10,
                                                                                                    y=0)
        self.dat = IntVar()
        Entry(self.vk, textvariable=self.dat).place(x=70, y=50)
        Button(self.vk, font=("INK FREE", 18), fg='black', text="agregar", bg='gray',
               command=self.push, relief=FLAT).place(x=70, y=100)
    def push(self):
        #print self.tope
        tope=self.tope+1
        if self.band == True:
            self.v3 = Toplevel()
            Label(self.v3, font=("ROCKWELL", 18), fg='black', text="Unidad 1", bg='gray').place(x=10, y=0)
            self.v3.geometry("270x50")
            self.v3.config(bg="gray")
            self.v3.config(relief="sunken")
            Label(self.v3, font=("ROCKWELL", 18), fg='black', text="pila llena", bg='gray').place(x=10,
                                                                                                  y=0)
            #print"pila llena"
        elif tope<self.maxi:
            #print self.tope
            self.tope = self.tope + 1
            self.pila[self.tope]=self.dat.get()
            #return self.tope
        self.mostrar(self.pila,self.tope,self.maxi,self.band)
        self.vk.destroy()
    def mostrar(self,pila,tope,maxi,band):
        if band==False:
            b=np.zeros(tope+1)
            for i in range (tope+1):
                b[i] = pila[i]
            self.v3 = Toplevel()
            Label(self.v3, font=("ROCKWELL", 18), fg='black', text="Unidad 1", bg='gray').place(x=10, y=0)
            self.v3.geometry("270x100")
            self.v3.config(bg="gray")
            self.v3.config(relief="sunken")
            Label(self.v3, font=("ROCKWELL", 18), fg='black', text="datos de la pila", bg='gray').place(x=10,
                                                                                                        y=0)
            Label(self.v3, font=("ROCKWELL", 18), fg='black', text=b, bg='gray').place(x=10,
                                                                                       y=50)
            #print b
p=pilas()
#p.inicio()