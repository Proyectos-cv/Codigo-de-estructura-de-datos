import numpy as np
from Tkinter import *
class recursividad():
    #def menu(self):
    def __init__(self):
        #band=True
        #while band==True:
        #self.ventana=Tk()
        self.ventana=Toplevel()
        self.ventana.geometry("440x550")
        self.ventana.config(bg="gray")
        self.ventana.config(cursor="cross")
        self.ventana.config(relief="sunken")
        self.ventana.title("unidad 2")
        #lblEti = Label(self.ventana, text="", bg="orange")
        #lblEti.grid(row=1, column=1)
        lblEti = Label(self.ventana, font=("Arial", 10), fg='black',
    text="selecciona factorial iterativo...........................................(1)\n" \
        "selecciona factorial recursivo...........................................(2)\n" \
        "selecciona fibonacci recursivo...........................................(3)\n"\
        "selecciona fibonacci normal..............................................(4)\n"\
        "selecciona imprimir datos de darreglo de derecha a izquierda recursivo ..(5)\n"\
        "selecciona imprimir datos de darreglo de izquierda a derecha recursivo ..(6)\n"\
        "selecciona imprimir datos de darreglo de derecha a izquierda iterativo ..(7)\n"\
        "selecciona imprimir datos de darreglo de izquierda a derecha iterativo ..(8)\n"\
        "selecciona imprimir la suma de datos de arreglo (recursivo) ............(9)\n"\
        "selecciona imprimir la suma de datos de arreglo (iterativa) ...........(10)\n"\
        "euclides iterativo ....................................................(11)\n"\
        "euclides recursivo.................................................... (12)\n"\
        "torres de hanoi recursivo............................................. (13)")
        lblEti.place(x=0, y=0)
        btnagregarprove = Button(self.ventana, text="1", bg='cyan', command=self.normal)
        btnagregarprove.place(x=30, y=230)
        btnagregarprove = Button(self.ventana, text="2", bg='cyan', command=self.recursivo1)
        btnagregarprove.place(x=30, y=280)
        btnagregarprove = Button(self.ventana, text="3", bg='cyan', command=self.fiborec1)
        btnagregarprove.place(x=30, y=330)
        btnagregarprove = Button(self.ventana, text="4", bg='cyan', command=self.fibonacci)
        btnagregarprove.place(x=30, y=380)
        btnagregarprove = Button(self.ventana, text="5", bg='cyan', command=self.derecha1)
        btnagregarprove.place(x=30, y=430)
        btnagregarprove = Button(self.ventana, text="6", bg='cyan', command=self.izquierda1)
        btnagregarprove.place(x=30, y=480)
        btnagregarprove = Button(self.ventana, text="7", bg='cyan', command=self.derechaiter1)
        btnagregarprove.place(x=130, y=230)
        btnagregarprove = Button(self.ventana, text="8", bg='cyan', command=self.izquierdaiter1)
        btnagregarprove.place(x=130, y=280)
        btnagregarprove = Button(self.ventana, text="9", bg='cyan', command=self.suma1)
        btnagregarprove.place(x=130, y=330)
        btnagregarprove = Button(self.ventana, text="10", bg='cyan', command=self.sumaiter)
        btnagregarprove.place(x=130, y=380)
        btnagregarprove = Button(self.ventana, text="11", bg='cyan', command=self.euclidesiter)
        btnagregarprove.place(x=130, y=430)
        btnagregarprove = Button(self.ventana, text="12", bg='cyan', command=self.euclidesre1)
        btnagregarprove.place(x=130, y=480)
        btnagregarprove = Button(self.ventana, text="13", bg='cyan', command=self.hanoire1)
        btnagregarprove.place(x=230, y=230)
        self.tipo = IntVar()
        caja = Entry(self.ventana, textvariable=self.tipo).place(x=220, y=270)
        self.tipo2 = IntVar()
        caja2 = Entry(self.ventana, textvariable=self.tipo2).place(x=220, y=300)
        self.res = StringVar()
        op=Label(self.ventana,textvariable=str(self.res) , bg="white").place(x=270, y=320)
        #Label(self.ventana, text="factorial: ", textvariable=self.res).place(x=300, y=320)
        self.ventana = mainloop()

    def recursivo1(self):
        b = self.tipo.get()
        o=self.recursivo(b)
        self.res.set("factorial: " + str(o))
    def fiborec1(self):
        b = self.tipo.get()
        o= self.fiborec(b)
        self.res.set("fibonacci: " + str(o))
    def derecha1(self):
        b = int(input("dimension: "))
        a = np.zeros(b)
        for i in range(b):
            a[i] = int(input("numero: "))
        self.derecha(a, b)
    def izquierda1(self):
        b = int(input("inicio de la contabilidad: "))
        f = int(input("dimension del arreglo: "))
        a = np.zeros(f)
        for i in range(f):
            a[i] = int(input("numero: "))
        self.izquierda(a, b, f)
    def derechaiter1(self):
        b = int(input("cantidad de datos: "))
        a=np.zeros(b)
        for i in range(b):
            a[i]=int(input("insertar dato: "))
        self.derechaiter(a,b)
    def izquierdaiter1(self):
        b = int(input("cantidad de datos: "))
        a=np.zeros(b)
        for i in range(b):
            a[i]=int(input("insertar dato: "))
        self.izquierdaiter(a,b)
    def suma1(self):
        b = self.tipo.get()
        a=np.zeros(b)
        for i in range(b):
            a[i]= self.tipo2.get()
        o = self.suma(a, b)
        self.res.set("suma: " + str(o))
        #print self.suma(a,b)
    def euclidesre1(self):
        a=self.tipo.get()
        b = self.tipo2.get()
        #print "maximo comun divisor: ", self.euclidesre(a,b)
        o=self.euclidesre(a, b)
        self.res.set("divisor: " + str(o))
    def hanoire1(self):
        n = self.tipo.get()
        origen = 'a'
        destino = 'b'
        auxiliar = 'c'
        l=[]
        self.hanoire(n,origen,auxiliar,destino,l)
        #print l
        self.res.set(str(l))


    def normal(self):     #
        l=1
        for i in range (1,(self.tipo.get())+1):
           l=l*i
        #print "factorial: ",l
        self.res.set("factorial: "+str(l))

    def recursivo(self,b):
        if b==1:
            return 1
        else:
            return b*self.recursivo(b-1)
    def fibonacci(self):  #
        #b = int(input("cantidad de datos: "))
        lista=[0,1]
        aux=2
        while aux<=self.tipo.get():
            lista.append(lista[aux-1]+lista[aux-2])
            aux=aux+1
        #print lista[b]
        self.res.set("fibonacci: " + str(lista[self.tipo.get()]))


    def fiborec(self,b):
        if b==0:
            return 0
        elif b==1:
            return 1
        else:
            return self.fiborec(b-1)+self.fiborec(b-2)

    def derecha(self, a, b):
        aux = len(a)
        if b > 0:
            print a[b - 1]
            return r.derecha(a, b - 1)

    def izquierda(self, a, b, f):
            aux = len(a)
            if b < aux:
                print a[b]
                return r.izquierda(a, b + 1, f)

    def derechaiter(self,a,b):
        for i in range(b-1,-1,-1):
            print a[i]
    def izquierdaiter(self,a,b):
        for i in range(b):
            print a[i]

    def suma(self,a,b):
        if b==1:
            return a[0]
        else:
            return a[b-1]+self.suma(a,b-1)
    def sumaiter(self):
        #b = int(input("cantidad de datos: "))
        a = np.zeros(self.tipo.get())
        for i in range(self.tipo.get()):
            a[i] = self.tipo2.get()
        s=0
        for i in range(self.tipo.get()):
           s=a[i]+s
        #print s
        self.res.set("suma: " + str(s))
    def euclidesiter(self):          #

        a = self.tipo.get()
        b = self.tipo2.get()
        #Label(self.ventana, text="numero mayor").place(x=250, y=300)
        #Label(self.ventana, text="numero menor").place(x=490, y=320)

        while b!=0:
            y=a%b
            a=b
            b=y
        #print "maximo comun divisor: ", a
        self.res.set("divisor: " + str(a))
    def euclidesre(self,a,b):
        if b==0:
            return a
        else:
            h=b
            return self.euclidesre(h,a%b)

    def hanoire(self,n, origen, auxiliar, destino,l):
        if n == 1:
            #print "se mueve de la torre: ", origen, "a torre: ", destino
            self.res.set(str("se mueve de la torre: " + origen + " a torre: " + destino  +"\n"))
            l.append((str("se mueve de la torre: " + origen + " a torre: " + destino + "\n")))
        else:
            self.hanoire(n - 1, origen, destino, auxiliar,l)
            #print "se mueve de la torre: ", origen, "a torre: ", destino
            self.res.set(str("se mueve de la torre: "+ origen+ " a torre: "+ destino +"\n"))
            l.append((str("se mueve de la torre: " + origen + " a torre: " + destino + "\n")))
            self.hanoire(n - 1, auxiliar, origen, destino,l)
#r=recursividad()
#r.menu()

#caja de texto
#https://www.youtube.com/watch?v=e1hchs5BXhQ
#eliminar label
#https://www.youtube.com/watch?v=2_qUokpB1fw
#info label
#https://www.youtube.com/watch?v=jZn0JgzLP0Y
#listbox
#https://www.youtube.com/watch?v=zNK4aYyRPOY