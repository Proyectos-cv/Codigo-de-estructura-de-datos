import numpy as n
from Tkinter import *
class ordena:
    def bu(self):
        q = n.array([5, 6, 7, 4, 8, 3, 9, 2, 1])
        ordena().bubble(q)
    def qui(self):
        a = n.array([5, 6, 7, 4, 8, 3, 9, 2, 1])
        #print a
        ini=0
        fin=8
        ordena().quicksort(ini,fin,a)
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="Unidad 1", bg='gray').place(x=10, y=0)
        self.v.geometry("270x250")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="arreglo en desorden", bg='gray').place(x=10,
                                                                                                      y=0)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="[5, 6, 7, 4, 8, 3, 9, 2, 1]", bg='gray').place(x=10,
                                                                                                              y=50)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="arreglo en orden", bg='gray').place(x=10,
                                                                                                   y=100)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text=a, bg='gray').place(x=10,
                                                                                  y=150)
        self.v = mainloop()
        #print a
    def shel(self):
        a = n.array([5, 6, 7, 4, 8, 3, 9, 2, 1])
        nu=9
        #print a
        ordena().shellsort(nu,a)
        #print a
    def radi(self):
        a = n.array([5, 6, 7, 4, 8, 3, 9, 2, 1])
        #print a
        ordena().radix(a)
        #print a
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="Unidad 1", bg='gray').place(x=10, y=0)
        self.v.geometry("270x250")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="arreglo en desorden", bg='gray').place(x=10,
                                                                                                      y=0)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="[5, 6, 7, 4, 8, 3, 9, 2, 1]", bg='gray').place(x=10,
                                                                                                              y=50)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="arreglo en orden", bg='gray').place(x=10,
                                                                                                   y=100)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text=a, bg='gray').place(x=10,
                                                                                  y=150)
        self.v = mainloop()



    def bubble(self,q):
        #print q
        for i in range(8):
            for j in range(8):
                if q[j] > q[j + 1]:
                    s = q[j]
                    q[j] = q[j + 1]
                    q[j + 1] = s
        #print q
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="Unidad 1", bg='gray').place(x=10, y=0)
        self.v.geometry("270x250")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="arreglo en desorden", bg='gray').place(x=10,
                                                                                              y=0)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="[5, 6, 7, 4, 8, 3, 9, 2, 1]", bg='gray').place(x=10,
                                                                                             y=50)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="arreglo en orden", bg='gray').place(x=10,
                                                                                             y=100)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text=q, bg='gray').place(x=10,
                                                                                             y=150)
        self.v=mainloop()
    def quicksort(self,ini,fin,a):
        izq=ini
        der=fin
        pos =ini
        band=True
        while band==True:
            band=False
            while a[pos]<=a[der] and pos!=der:
                der=der-1
            if pos!=der:
                aux=a[pos]
                a[pos]=a[der]
                a[der]=aux
                pos=der
                while a[pos]>=a[izq] and pos!=izq:
                    izq=izq+1
                    if pos !=izq:
                        band=True
                        aux=a[pos]
                        a[pos]=a[izq]
                        a[izq]=aux
                        pos=izq
        if pos-1>ini:
            ordena().quicksort(ini,pos-1,a)
        if fin>pos+1:
            ordena().quicksort(pos+1,fin,a)
    def shellsort(self,nu,a):
        int=nu+1
        while int>1:
            int=int//2
            band=True
            while band==True:
                band=False
                i=0
                while i+int<nu:
                    if a[i]>a[i+int]:
                        aux=a[i]
                        a[i]=a[i+int]
                        a[i+int]=aux
                        band=True
                    i=i+1
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="Unidad 1", bg='gray').place(x=10, y=0)
        self.v.geometry("270x250")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="arreglo en desorden", bg='gray').place(x=10,
                                                                                                      y=0)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="[5, 6, 7, 4, 8, 3, 9, 2, 1]", bg='gray').place(x=10,
                                                                                                              y=50)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="arreglo en orden", bg='gray').place(x=10,
                                                                                                   y=100)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text=a, bg='gray').place(x=10,
                                                                                  y=150)
        self.v = mainloop()
    def radix(self,a):
        radix=10
        band=True
        tem=-1
        lugar=1
        while band==True:
            li=[list() for _ in range(radix) ]
            for i in a:
                tem=i/lugar
                li[tem%radix].append(i)
                if band==True and tem>0:
                    band=False
            c=0
            for b in range(radix):
                lis=li[b]
                for k in lis:
                    a[c]=k
                    c=c+1
            lugar=radix
o=ordena()
#o.menu()