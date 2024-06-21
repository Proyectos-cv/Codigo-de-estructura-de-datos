import numpy as np
from Tkinter import *
class colas:
    def comienza(self):
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
               command=self.comenzar, relief=FLAT).place(x=70, y=100)
        self.v3=mainloop()
    def comenzar(self):
        self.band=True
        self.maxi = self.dat.get()
        self.final = -1
        self.frente = -1
        self.cola = np.zeros(self.maxi)
        self.inicio()
    def inicio(self):
        self.v1 = Toplevel()
        Label(self.v1, font=("ROCKWELL", 18), fg='black', text="Unidad 3", bg='gray').place(x=10, y=0)
        self.v1.geometry("250x270")
        self.v1.config(bg="gray")
        self.v1.config(relief="sunken")
        self.v1.title("Unidad 3")
        Label(self.v1, font=("ROCKWELL", 18), fg='black', text="contenido unidad 3", bg='gray').place(x=10,
                                                                                                      y=0)
        Button(self.v1, font=("INK FREE", 18), fg='black', text="eliminar", bg='gray',
               command=self.el, relief=FLAT).place(x=70, y=50)
        Button(self.v1, font=("INK FREE", 18), fg='black', text="insertar", bg='gray',
               command=self.ins, relief=FLAT).place(x=70, y=100)
        self.v1 = mainloop()
    def el(self):
        self.vacio(self.cola, self.final, self.band, self.frente)
        self.pop(self.cola, self.final, self.band, self.frente)
        self.mostrar(self.cola, self.final, self.maxi, self.band, self.frente)
    def ins(self):
        self.band = p.lleno(self.cola, self.final, self.maxi, self.band, self.frente)
        self.da()
        #self.final = p.push(self.cola, self.final, self.maxi, self.band, self.frente)
        #self.mostrar(self.cola, self.final, self.maxi, self.band, self.frente)

    def lleno(self,cola,final,maxi,band,frente):
        self.maxi=maxi
        final = final + 1
        if final==self.maxi:
            self.band=True
            return self.band
        else:
            self.band=False
            return self.band
    def vacio(self,cola,final,band,frente):
        frente=self.frente+1
        if frente>=self.final:
            self.band = True
            return self.band
        else:
            self.band=False
            return self.band
    def pop(self,cola,final,band,frente):

        if self.band==True:
            self.v3 = Toplevel()
            Label(self.v3, font=("ROCKWELL", 18), fg='black', text="Unidad 1", bg='gray').place(x=10, y=0)
            self.v3.geometry("270x50")
            self.v3.config(bg="gray")
            self.v3.config(relief="sunken")
            Label(self.v3, font=("ROCKWELL", 18), fg='black', text="cola vacia", bg='gray').place(x=10,
                                                                                                            y=0)
            #print "cola vacia"
        else:
            self.frente = self.frente + 1
            #print"numero a eliminar: ",self.cola[self.frente]
            return self.frente
    def da(self):
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
        if self.band == True:
            self.v3 = Toplevel()
            Label(self.v3, font=("ROCKWELL", 18), fg='black', text="Unidad 3", bg='gray').place(x=10, y=0)
            self.v3.geometry("270x50")
            self.v3.config(bg="gray")
            self.v3.config(relief="sunken")
            Label(self.v3, font=("ROCKWELL", 18), fg='black', text="cola llena", bg='gray').place(x=10,
                                                                                                  y=0)
            #print"cola llena"
        else:
            self.final= self.final + 1
            self.cola[self.final]=self.dat.get()
            #return self.final
        self.mostrar(self.cola, self.final, self.maxi, self.band, self.frente)
        self.vk.destroy()
    def mostrar(self,cola,final,maxi,band,frente):
        if self.band==False:
            b=[]
            frente=self.frente
            frente=frente+1
            final=final+1
            for i in range (frente,final):
                b.append(cola[i])
            self.v3 = Toplevel()
            Label(self.v3, font=("ROCKWELL", 18), fg='black', text="Unidad 3", bg='gray').place(x=10, y=0)
            self.v3.geometry("270x100")
            self.v3.config(bg="gray")
            self.v3.config(relief="sunken")
            Label(self.v3, font=("ROCKWELL", 18), fg='black', text="datos de la cola", bg='gray').place(x=10,
                                                                                         y=0)
            Label(self.v3, font=("ROCKWELL", 18), fg='black', text=b, bg='gray').place(x=10,
                                                                                                  y=50)
            #print b
            #print self.cola
p=colas()
#p.inicio()