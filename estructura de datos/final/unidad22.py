import numpy as np
from Tkinter import *
class recursividad():

    def normal(self,b):
        #b=int(input("dame un numero de entrada: "))
        l=1
        for i in range (1,b+1):
           l=l*i
        return l
    def recursivo(self,b):
        if b==1:
            return 1
        else:
            return b*self.recursivo(b-1)

    def fibonacci(self,b):

        lista=[0,1]
        aux=2
        while aux<=b:
            lista.append(lista[aux-1]+lista[aux-2])
            aux=aux+1
        return lista[b]
    def fiborec(self,b):
        if b==0:
            return 0
        elif b==1:
            return 1
        else:
            return self.fiborec(b-1)+self.fiborec(b-2)
######################
    def derecha(self, nu, e,a):
        self.nu=nu
        self.a=a
        self.e=e
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="agregar dato", bg='gray').place(x=10, y=0)
        self.v.geometry("300x250")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        self.v.title("Unidad 1")

        self.da = IntVar()
        Entry(self.v, textvariable=self.da).place(x=70, y=70)
        Button(self.v, font=("INK FREE", 18), fg='black', text="agregar", bg='gray',
               command=self.derecha1, relief=FLAT).place(x=70, y=100)
        self.v=mainloop()
    def derecha1(self):
        self.e[self.nu] = self.da.get()
        self.nu = self.nu + 1
        #print self.e
        #print self.nu
        self.v.destroy()
        if self.nu<self.a:
            recursividad().derecha(self.nu,self.e,self.a)
        elif self.nu==self.a:
            h=[]
            i=recursividad().derecha2(self.e,self.nu,h)
            #print self.e
            #print h
            self.vo = Toplevel()
            Label(self.vo, font=("ROCKWELL", 18), fg='black', text="resultado", bg='gray').place(x=10, y=0)
            self.vo.geometry("300x250")
            self.vo.config(bg="gray")
            Label(self.vo, font=("ROCKWELL", 16), fg='black', text=self.e, bg='gray').place(x=10, y=50)
            Label(self.vo, font=("ROCKWELL", 16), fg='black', text=h, bg='gray').place(x=10, y=100)
    def derecha2(self,e,nu,h):
         aux = len(e)
         if nu > 0:
             h.append(e[nu - 1])
             return self.derecha2(e, nu - 1,h)
################
    def izquierda(self, nu, e,a):
        self.nu = nu
        self.a = a
        self.e = e
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="agregar dato", bg='gray').place(x=10, y=0)
        self.v.geometry("300x250")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        self.v.title("Unidad 1")

        self.da = IntVar()
        Entry(self.v, textvariable=self.da).place(x=70, y=70)
        Button(self.v, font=("INK FREE", 18), fg='black', text="agregar", bg='gray',
               command=self.izquierda1, relief=FLAT).place(x=70, y=100)
        self.v = mainloop()
    def izquierda1(self):
        self.e[self.nu] = self.da.get()
        self.nu = self.nu + 1
        #print self.e
        #print self.nu
        self.v.destroy()
        if self.nu < self.a:
            recursividad().izquierda(self.nu, self.e, self.a)
        elif self.nu == self.a:
            h = []
            recursividad().izquierda2(self.e, 0, self.nu,h)
            #print self.e
            #print h
            self.vo = Toplevel()
            Label(self.vo, font=("ROCKWELL", 18), fg='black', text="resultado", bg='gray').place(x=10, y=0)
            self.vo.geometry("300x250")
            self.vo.config(bg="gray")
            Label(self.vo, font=("ROCKWELL", 16), fg='black', text=self.e, bg='gray').place(x=10, y=50)
            Label(self.vo, font=("ROCKWELL", 16), fg='black', text=h, bg='gray').place(x=10, y=100)
    def izquierda2(self, a, b, f,h):
            aux = len(a)
            if b < aux:
                h.append(a[b])
                return self.izquierda2(a, b + 1, f,h)
################
    def deri(self,nu, e, a):
        self.nu = nu
        self.a = a
        self.e = e
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="agregar dato", bg='gray').place(x=10, y=0)
        self.v.geometry("300x250")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        self.v.title("Unidad 1")

        self.da = IntVar()
        Entry(self.v, textvariable=self.da).place(x=70, y=70)
        Button(self.v, font=("INK FREE", 18), fg='black', text="agregar", bg='gray',
               command=self.deri1, relief=FLAT).place(x=70, y=100)
        self.v = mainloop()
    def deri1(self):
        self.e[self.nu] = self.da.get()
        self.nu = self.nu + 1
        #print self.e
        #print self.nu
        self.v.destroy()
        if self.nu < self.a:
            recursividad().deri(self.nu, self.e, self.a)
        elif self.nu == self.a:
            h = []
            recursividad().derechaiter(self.e, self.nu, h)
            #print self.e
            #print h
            self.vo = Toplevel()
            Label(self.vo, font=("ROCKWELL", 18), fg='black', text="resultado", bg='gray').place(x=10, y=0)
            self.vo.geometry("300x250")
            self.vo.config(bg="gray")
            Label(self.vo, font=("ROCKWELL", 16), fg='black', text=self.e, bg='gray').place(x=10, y=50)
            Label(self.vo, font=("ROCKWELL", 16), fg='black', text=h, bg='gray').place(x=10, y=100)
    def derechaiter(self,a,b,h):
        for i in range(b-1,-1,-1):
            h.append(a[i])

    def izqi(self,nu, e, a):
        self.nu = nu
        self.a = a
        self.e = e
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="agregar dato", bg='gray').place(x=10, y=0)
        self.v.geometry("300x250")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        self.v.title("Unidad 1")

        self.da = IntVar()
        Entry(self.v, textvariable=self.da).place(x=70, y=70)
        Button(self.v, font=("INK FREE", 18), fg='black', text="agregar", bg='gray',
               command=self.izqi1, relief=FLAT).place(x=70, y=100)
        self.v = mainloop()
    def izqi1(self):
        self.e[self.nu] = self.da.get()
        self.nu = self.nu + 1
        #print self.e
        #print self.nu
        self.v.destroy()
        if self.nu < self.a:
            recursividad().izqi(self.nu, self.e, self.a)
        elif self.nu == self.a:
            h = []
            recursividad().izquierdaiter(self.e, self.nu, h)
            #print self.e
            #print h
            self.vo = Toplevel()
            Label(self.vo, font=("ROCKWELL", 18), fg='black', text="resultado", bg='gray').place(x=10, y=0)
            self.vo.geometry("300x250")
            self.vo.config(bg="gray")
            Label(self.vo, font=("ROCKWELL", 16), fg='black', text=self.e, bg='gray').place(x=10, y=50)
            Label(self.vo, font=("ROCKWELL", 16), fg='black', text=h, bg='gray').place(x=10, y=100)
    def izquierdaiter(self,a,b,h):
        for i in range(b):
            h.append(a[i])
##########
    def sum(self,nu, e, a):
        self.nu = nu
        self.a = a
        self.e = e
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="agregar dato", bg='gray').place(x=10, y=0)
        self.v.geometry("300x250")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        self.v.title("Unidad 1")

        self.da = IntVar()
        Entry(self.v, textvariable=self.da).place(x=70, y=70)
        Button(self.v, font=("INK FREE", 18), fg='black', text="agregar", bg='gray',
               command=self.sum1, relief=FLAT).place(x=70, y=100)
    def sum1(self):
        self.e[self.nu] = self.da.get()
        self.nu = self.nu + 1
        #print self.e
        #print self.nu
        self.v.destroy()
        if self.nu < self.a:
            recursividad().sum(self.nu, self.e, self.a)
        elif self.nu == self.a:
            h = 0
            h=recursividad().suma(self.e, self.nu, h)
            #print self.e
            #print h
            self.vo = Toplevel()
            Label(self.vo, font=("ROCKWELL", 18), fg='black', text="resultado", bg='gray').place(x=10, y=0)
            self.vo.geometry("300x250")
            self.vo.config(bg="gray")
            Label(self.vo, font=("ROCKWELL", 16), fg='black', text=self.e, bg='gray').place(x=10, y=50)
            Label(self.vo, font=("ROCKWELL", 16), fg='black', text=h, bg='gray').place(x=10, y=100)
    def suma(self,a,b,h):
        if b==1:
            return a[0]
        else:
            return a[b-1]+self.suma(a,b-1,h)
    def sumai(self,nu, e, a):
        self.nu = nu
        self.a = a
        self.e = e
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="agregar dato", bg='gray').place(x=10, y=0)
        self.v.geometry("300x250")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        self.v.title("Unidad 1")

        self.da = IntVar()
        Entry(self.v, textvariable=self.da).place(x=70, y=70)
        Button(self.v, font=("INK FREE", 18), fg='black', text="agregar", bg='gray',
               command=self.sumai1, relief=FLAT).place(x=70, y=100)
    def sumai1(self):
        self.e[self.nu] = self.da.get()
        self.nu = self.nu + 1
        #print self.e
        #print self.nu
        self.v.destroy()
        if self.nu < self.a:
            recursividad().sumai(self.nu, self.e, self.a)
        elif self.nu == self.a:
            h = 0
            h=recursividad().sumaiter(self.e, self.nu, h)
            # print self.e
            # print h
            self.vo = Toplevel()
            Label(self.vo, font=("ROCKWELL", 18), fg='black', text="resultado", bg='gray').place(x=10, y=0)
            self.vo.geometry("300x250")
            self.vo.config(bg="gray")
            Label(self.vo, font=("ROCKWELL", 16), fg='black', text=self.e, bg='gray').place(x=10, y=50)
            Label(self.vo, font=("ROCKWELL", 16), fg='black', text=h, bg='gray').place(x=10, y=100)
    def sumaiter(self,a,b,h):
        for i in range(b):
           h=a[i]+h
        return h
#########################
    def euclidesiter(self,a,b):
        while b!=0:
            y=a%b
            a=b
            b=y
        return a
        #print "maximo comun divisor: ", a
    def euclidesre(self,a,b):
        if b==0:
            return a
        else:
            h=b
            return self.euclidesre(h,a%b)

    def hanoire(self,n, origen, auxiliar, destino,k):
        k.append(1)
        if n == 1:
            #print "se mueve de la torre: ", origen, "a torre: ", destino
            pass
        else:
            self.hanoire(n - 1, origen, destino, auxiliar,k)
            #print "se mueve de la torre: ", origen, "a torre: ", destino
            self.hanoire(n - 1, auxiliar, origen, destino,k)
#r=recursividad()
#r.menu()