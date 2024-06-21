import numpy as np
from Tkinter import *
class colacir:
    def empezar(self):
        self.v3 = Toplevel()
        Label(self.v3, font=("ROCKWELL", 18), fg='black', text="Unidad 3", bg='gray').place(x=10, y=0)
        self.v3.geometry("250x270")
        self.v3.config(bg="gray")
        self.v3.config(relief="sunken")
        self.v3.title("Unidad 3")
        Label(self.v3, font=("ROCKWELL", 18), fg='black', text="dimension de arreglo", bg='gray').place(x=10,
                                                                                                        y=0)
        self.dat = IntVar()
        Entry(self.v3, textvariable=self.dat).place(x=70, y=50)
        Button(self.v3, font=("INK FREE", 18), fg='black', text="crear", bg='gray',
               command=self.ini, relief=FLAT).place(x=70, y=100)
        self.v3 = mainloop()
    def ini(self):

        self.band=False
        self.maxi = self.dat.get()
        self.final = -1
        self.frente = -1
        self.cola = np.zeros(self.maxi)
        self.select()
    def select(self):
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
               command=self.agr, relief=FLAT).place(x=70, y=100)
        self.v1 = mainloop()
    def el(self):
        self.vacio(self.cola,self.final,self.band,self.frente,self.maxi)
        self.pop(self.cola,self.final,self.band,self.frente,self.maxi)
        self.mostrar(self.cola,self.final,self.maxi,self.band,self.frente)
    def agr(self):
        self.lleno(self.cola,self.final,self.maxi,self.band,self.frente)
        self.push()
        #self.push(self.cola,self.final, self.maxi, self.band,self.frente)
        #self.mostrar(self.cola, self.final, self.maxi,self.band,self.frente)


    def lleno(self,cola,final,maxi,band,frente):
        self.maxi=maxi
        final = final + 1
        if (final==self.frente):
            self.band=True
            return self.band
        elif (final>=self.maxi and self.frente<=0):
            self.band = True
            return self.band
        else:
            self.band=False
            return self.band
    def vacio(self,cola,final,band,frente,maxi):
        frente = frente + 1
        if frente ==self.final and frente==0 and self.final==0:
            self.band=True
            return self.band
        if frente - 1 == self.final:
            self.band = True
            return self.band
        if self.final == -1:
            self.band = True
            return self.band
        if frente == self.maxi+1 and self.final == 0:
            self.band = True
            # print final
            # print frente
            return self.band
        if frente >= self.final or self.final > 0:
            self.band = False
            # print final
            # print frente
            return self.band
        if self.final == frente:
            self.band = True
            return self.band
        else:
            self.band = False
            # print final
            # print frente
            return self.band
    def pop(self,cola,final,band,frente,maxi):
        if self.band==True:
            self.v3 = Toplevel()
            Label(self.v3, font=("ROCKWELL", 18), fg='black', text="Unidad 1", bg='gray').place(x=10, y=0)
            self.v3.geometry("270x50")
            self.v3.config(bg="gray")
            self.v3.config(relief="sunken")
            Label(self.v3, font=("ROCKWELL", 18), fg='black', text="cola vacia", bg='gray').place(x=10,
                                                                                                  y=0)
            if self.frente!=-1:
                self.frente=frente+1
                self.final=self.final+1
            #print "cola vacia"
        elif self.frente>=self.maxi:
            self.frente=0
            #print"numero a eliminar: ", self.cola[self.frente]
            self.frente=self.frente+1
            #print cola
            return self.frente
        elif self.frente==-1:
            self.frente = self.frente + 1
            #print"numero a eliminar: ",self.cola[self.frente]
            self.frente=self.frente+1
            #print cola
            return self.frente

        else:
            #print"numero a eliminar: ", self.cola[self.frente]
            self.frente = self.frente + 1
            #print cola
            return self.frente
    def push(self):
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
               command=self.push1, relief=FLAT).place(x=70, y=100)
    def push1(self):
        if self.band == True:
            self.v3 = Toplevel()
            Label(self.v3, font=("ROCKWELL", 18), fg='black', text="Unidad 1", bg='gray').place(x=10, y=0)
            self.v3.geometry("270x50")
            self.v3.config(bg="gray")
            self.v3.config(relief="sunken")
            Label(self.v3, font=("ROCKWELL", 18), fg='black', text="cola llena", bg='gray').place(x=10,
                                                                                                  y=0)
            #print"cola llena"
        elif self.final>=self.maxi or self.final+1==self.maxi:
            self.final = -1
            self.final=self.final+1
            self.cola[self.final] = self.dat.get()
            #print cola
            #return self.final
        else:
            self.final= self.final + 1
            self.cola[self.final]=self.dat.get()
            #print cola
            #return self.final
        self.mostrar(self.cola, self.final, self.maxi,self.band,self.frente)
        self.vk.destroy()
    def mostrar(self,cola,final,maxi,band,frente):

        if self.band==False:
            if self.frente<self.final and self.frente==-1:
                #print"a"
                b = []
                frente=frente+1
                for i in range(frente, self.final+1):
                    b.append(self.cola[i])
                self.v3 = Toplevel()
                Label(self.v3, font=("ROCKWELL", 18), fg='black', text="Unidad 3", bg='gray').place(x=10, y=0)
                self.v3.geometry("270x200")
                self.v3.config(bg="gray")
                self.v3.config(relief="sunken")
                Label(self.v3, font=("ROCKWELL", 18), fg='black', text="datos de la cola", bg='gray').place(x=10,
                                                                                                            y=0)
                Label(self.v3, font=("ROCKWELL", 18), fg='black', text=b, bg='gray').place(x=10,
                                                                                           y=50)
                Label(self.v3, font=("ROCKWELL", 18), fg='black', text="arreglo original", bg='gray').place(x=10,
                                                                                                            y=100)
                Label(self.v3, font=("ROCKWELL", 18), fg='black', text=self.cola, bg='gray').place(x=10,
                                                                                                            y=150)
                #print b
            elif self.frente>self.final:
                #print"b"
                b=[]
                for i in range(self.frente,self.maxi):
                    b.append(self.cola[i])
                for j in range(0,self.final+1):
                    b.append(self.cola[j])
                self.v3 = Toplevel()
                Label(self.v3, font=("ROCKWELL", 18), fg='black', text="Unidad 3", bg='gray').place(x=10, y=0)
                self.v3.geometry("270x200")
                self.v3.config(bg="gray")
                self.v3.config(relief="sunken")
                Label(self.v3, font=("ROCKWELL", 18), fg='black', text="datos de la cola", bg='gray').place(x=10,
                                                                                                            y=0)
                Label(self.v3, font=("ROCKWELL", 18), fg='black', text=b, bg='gray').place(x=10,
                                                                                           y=50)
                Label(self.v3, font=("ROCKWELL", 18), fg='black', text="arreglo original", bg='gray').place(x=10,
                                                                                                            y=100)
                Label(self.v3, font=("ROCKWELL", 18), fg='black', text=self.cola, bg='gray').place(x=10,
                                                                                                   y=150)
                #print b
            elif self.frente<self.final and self.frente!=-1:
                #print"c"
                b = []
                for i in range(self.frente, self.final+1):
                    b.append(self.cola[i])
                self.v3 = Toplevel()
                Label(self.v3, font=("ROCKWELL", 18), fg='black', text="Unidad 3", bg='gray').place(x=10, y=0)
                self.v3.geometry("270x200")
                self.v3.config(bg="gray")
                self.v3.config(relief="sunken")
                Label(self.v3, font=("ROCKWELL", 18), fg='black', text="datos de la cola", bg='gray').place(x=10,
                                                                                                            y=0)
                Label(self.v3, font=("ROCKWELL", 18), fg='black', text=b, bg='gray').place(x=10,
                                                                                           y=50)
                Label(self.v3, font=("ROCKWELL", 18), fg='black', text="arreglo original", bg='gray').place(x=10,
                                                                                                            y=100)
                Label(self.v3, font=("ROCKWELL", 18), fg='black', text=self.cola, bg='gray').place(x=10,
                                                                                                   y=150)
                #print b
            elif self.frente==self.final:
                #print"d"
                b=[]
                b.append(self.cola[self.frente])
                self.v3 = Toplevel()
                Label(self.v3, font=("ROCKWELL", 18), fg='black', text="Unidad 3", bg='gray').place(x=10, y=0)
                self.v3.geometry("270x200")
                self.v3.config(bg="gray")
                self.v3.config(relief="sunken")
                Label(self.v3, font=("ROCKWELL", 18), fg='black', text="datos de la cola", bg='gray').place(x=10,
                                                                                                            y=0)
                Label(self.v3, font=("ROCKWELL", 18), fg='black', text=b, bg='gray').place(x=10,
                                                                                           y=50)
                Label(self.v3, font=("ROCKWELL", 18), fg='black', text="arreglo original", bg='gray').place(x=10,
                                                                                                            y=100)
                Label(self.v3, font=("ROCKWELL", 18), fg='black', text=self.cola, bg='gray').place(x=10,
                                                                                                   y=150)
                #print b

            #print b
p=colacir()
#p.inicio()