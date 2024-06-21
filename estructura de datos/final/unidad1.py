#ejemplo 1
import numpy as n
from Tkinter import *
#ejemplo 1
class tarea:

    def arreglos(self,nu,e,a):
        #self.e = n.zeros(10)
        self.a=a
        self.e=e
        self.nu=nu
        #print self.nu
        o = 0
        u = 0
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="agregar dato", bg='gray').place(x=10, y=0)
        self.v.geometry("300x250")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        self.v.title("Unidad 1")
        self.dat = IntVar()
        #Entry(self.v, textvariable=self.dat).place(x=140, y=190)
        self.da = IntVar()
        Entry(self.v, textvariable=self.da).place(x=70, y=70)
        Button(self.v, font=("INK FREE", 18), fg='black', text="agregar", bg='gray',
               command=self.pro, relief=FLAT).place(x=70, y=100)

        self.v = mainloop()
    def pro(self):
        self.e[self.nu]=self.da.get()
        self.nu=self.nu+1
        self.v.destroy()
        #print self.e
        if self.nu<self.a:
             tarea().arreglos(self.nu,self.e,self.a)
        elif self.nu==self.a:
            o=0
            u=0
            for j in range (self.nu):
                 o = o + self.e[j]
            promedio = o / self.nu
            for k in range(self.nu):
                if self.e[k] > promedio:
                    u = u + 1
            self.v = Toplevel()
            Label(self.v, font=("ROCKWELL", 18), fg='black', text="resultados", bg='gray').place(x=10, y=0)
            self.v.geometry("350x200")
            self.v.config(bg="gray")
            self.v.config(relief="sunken")
            self.v.title("resulatdos")
            Label(self.v, font=("ROCKWELL", 12), fg='black', text="promedio: "+ str(promedio), bg='gray').place(x=10, y=50)
            Label(self.v, font=("ROCKWELL", 12), fg='black', text=("datos mas grandes que el promedio: "+str(u)), bg='gray').place(x=10, y=100)
            self.v=mainloop()

# ejemplo 2
    def cuando(self,nu,e,a):
        self.a = a
        self.e = e
        self.nu = nu
        # print self.nu
        o = 0
        u = 0
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="agregar dato", bg='gray').place(x=10, y=0)
        self.v.geometry("300x250")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        self.v.title("Unidad 1")
        self.dat = IntVar()
        # Entry(self.v, textvariable=self.dat).place(x=140, y=190)
        self.da = IntVar()
        Entry(self.v, textvariable=self.da).place(x=70, y=70)
        Button(self.v, font=("INK FREE", 18), fg='black', text="agregar", bg='gray',
               command=self.cuando1, relief=FLAT).place(x=70, y=100)
    def cuando1(self):
        self.e[self.nu] = self.da.get()
        self.nu = self.nu + 1
        self.v.destroy()
        # print self.e
        if self.nu < self.a:
            tarea().cuando(self.nu, self.e, self.a)
        elif self.nu == self.a:
            import numpy as n
            self.o = 0
            self.u = 0
            m = 0
            n = 0
            while m < self.nu:
                self.o = self.o + self.e[m]
                m = m + 1
            promedio = self.o / self.nu
            while n < self.nu:
                if self.e[n] > promedio:
                    self.u = self.u + 1
                n = n + 1
            self.v = Toplevel()
            Label(self.v, font=("ROCKWELL", 18), fg='black', text="resultados", bg='gray').place(x=10, y=0)
            self.v.geometry("350x200")
            self.v.config(bg="gray")
            self.v.config(relief="sunken")
            self.v.title("resulatdos")
            Label(self.v, font=("ROCKWELL", 12), fg='black', text="promedio: " + str(promedio), bg='gray').place(
                x=10, y=50)
            Label(self.v, font=("ROCKWELL", 12), fg='black', text=("datos mas grandes que el promedio: " + str(self.u)),
                  bg='gray').place(x=10, y=100)
            self.v = mainloop()

#ejemplo 3
    def muchas(self):
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="insertar datos", bg='gray').place(x=10, y=0)
        self.v.geometry("250x400")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        self.v.title("Unidad 1  //  3")
        self.da = IntVar()
        Entry(self.v, textvariable=self.da).place(x=70, y=50)
        self.da1 = IntVar()
        Entry(self.v, textvariable=self.da1).place(x=70, y=100)
        self.da2 = IntVar()
        Entry(self.v, textvariable=self.da2).place(x=70, y=150)
        self.da3 = IntVar()
        Entry(self.v, textvariable=self.da3).place(x=70, y=200)
        self.da4 = IntVar()
        Entry(self.v, textvariable=self.da4).place(x=70, y=250)
        Button(self.v, font=("INK FREE", 18), fg='black', text="promedio", bg='gray',
               command=self.muchos1, relief=FLAT).place(x=70, y=300)
        self.ve = mainloop()

    def muchos1(self):
        b = 0
        a1=self.da.get()
        a2 = self.da1.get()
        a3 = self.da2.get()
        a4 = self.da3.get()
        a5 = self.da4.get()
        prom = (a1 + a2 + a3 + a4 + a5)
        promedio= prom/5
        if a1 > promedio:
            b = b + 1
        if a2 > promedio:
            b = b + 1
        if a3 > promedio:
            b = b + 1
        if a4 > promedio:
            b = b + 1
        if a5 > promedio:
            b = b + 1
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="resultados", bg='gray').place(x=10, y=0)
        self.v.geometry("350x200")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        self.v.title("resulatdos")
        Label(self.v, font=("ROCKWELL", 12), fg='black', text="promedio: " + str(promedio), bg='gray').place(x=10, y=50)
        Label(self.v, font=("ROCKWELL", 12), fg='black', text=("datos mas grandes que el promedio: " + str(b)),
              bg='gray').place(x=10, y=100)
        self.v = mainloop()
