from Tkinter import *
import sys
class nodo():
    def __init__(self):
        self.dato=None
        self.der=None
        self.izq=None
class arbol():
    def __init__(self):
        self.raiz=None
        self.otro=None
        self.q=None
        self.padre=None
    def inicia(self):
        self.ve=Toplevel()
        Label(self.ve, font=("ROCKWELL", 18), fg='black', text="ARBOL BINARIO", bg='gray').place(x=10, y=0)
        self.ve.geometry("450x450")
        self.ve.config(bg="gray")
        self.ve.config(relief="sunken")
        self.ve.title("arbol binario")

        btnagregarprove = Button(self.ve, font=("INK FREE", 18), fg='black', text="insertar nodo", bg='gray',
                                 command=self.inicio1, relief=FLAT).place(x=70, y=50)
        btnagregarprove = Button(self.ve, font=("INK FREE", 18), fg='black', text="preorden", bg='gray',
                                 command=self.preorden1, relief=FLAT).place(x=70, y=100)
        btnagregarprove = Button(self.ve, font=("INK FREE", 18), fg='black', text="inorden", bg='gray',
                                 command=self.inorden1, relief=FLAT).place(x=70, y=150)
        btnagregarprove = Button(self.ve, font=("INK FREE", 18), fg='black', text="posorden", bg='gray',
                                 command=self.posorden1, relief=FLAT).place(x=70, y=200)
        btnagregarprove = Button(self.ve, font=("INK FREE", 18), fg='black', text="crear raiz", bg='gray',
                                 command=self.inicio21, relief=FLAT).place(x=70, y=250)
        btnagregarprove = Button(self.ve, font=("INK FREE", 18), fg='black', text="buscar dato", bg='gray',
                                 command=self.buscar1, relief=FLAT).place(x=70, y=300)
        btnagregarprove = Button(self.ve, font=("INK FREE", 18), fg='black', text="eliminar", bg='gray',
                                 command=self.elimina1, relief=FLAT).place(x=70, y=350)
        btnagregarprove = Button(self.ve, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
                                 command=self.salir, relief=FLAT).place(x=70, y=400)
        self.re = StringVar()
        Label(self.ve,font=("INK FREE", 18), text="datos del arbol: ", bg="gray").place(x=270, y=150)
        op = Label(self.ve, textvariable=str(self.re), bg="gray").place(x=270, y=200)
        self.ve=mainloop()
    def salir(self):
        self.ve.destroy()
    def inicio1(self):
        #nod=nodo()
        #s = int(input("dato: "))
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 14), fg='black', text="insertar nodo", bg='gray').place(x=10, y=0)
        self.v.geometry("250x450")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        self.v.title("agregar nodo")
        self.da=IntVar()
        Entry(self.v, textvariable=self.da).place(x=70, y=70)
        Button(self.v, font=("INK FREE", 18), fg='black', text="agregar", bg='gray',
               command=self.ini, relief=FLAT).place(x=70, y=100)

    def ini(self):
        s=self.da.get()
        self.inicio(self.raiz,s)
    def preorden1(self):
        raiz = self.raiz.izq
        a=self.raiz
        l=[]
        self.preorden(raiz,a,l)
        self.re.set(str(l))
        self.raiz = a
    def inorden1(self):
        raiz = self.raiz.izq
        a = self.raiz
        l=[]
        self.inorden(raiz,a,l)
        self.re.set(str(l))
        self.raiz=a
    def posorden1(self):
        raiz = self.raiz
        a = self.raiz
        l=[]
        self.posorden(self.raiz,a,l)
        l[len(l) - 1] = str("fin")
        self.re.set(str(l))
        self.raiz = a
    def inicio21(self):
        nod = nodo()
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 14), fg='black', text="insertar raiz", bg='gray').place(x=10, y=0)
        self.v.geometry("250x450")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        self.v.title("agregar raiz")
        self.da = IntVar()
        Entry(self.v, textvariable=self.da).place(x=70, y=70)
        Button(self.v, font=("INK FREE", 18), fg='black', text="agregar", bg='gray',
               command=self.ini, relief=FLAT).place(x=70, y=100)
        self.inicio2(nod)
    def emp(self):
        a=self.da.get()
        self.inicio2(a)
    def buscar1(self):
        #i=int(input("dato a buscar: "))
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 14), fg='black', text="buscar", bg='gray').place(x=10, y=0)
        self.v.geometry("250x450")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        self.v.title("busqueda")
        self.da = IntVar()
        Entry(self.v, textvariable=self.da).place(x=70, y=70)
        Button(self.v, font=("INK FREE", 18), fg='black', text="buscar", bg='gray',
               command=self.bu, relief=FLAT).place(x=70, y=100)
    def bu(self):
        i=self.da.get()
        raiz = self.raiz
        self.buscar(raiz,i)
    def elimina1(self):
        #i1 = int(input("dato a eliminar: "))
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 14), fg='black', text="eliminar", bg='gray').place(x=10, y=0)
        self.v.geometry("250x450")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        self.v.title("eliminar")
        self.da = IntVar()
        Entry(self.v, textvariable=self.da).place(x=70, y=70)
        Button(self.v, font=("INK FREE", 18), fg='black', text="eliminar", bg='gray',
               command=self.eli, relief=FLAT).place(x=70, y=100)
    def eli(self):
        raiz = self.raiz
        l=self.raiz
        i1=self.da.get()
        self.elimina(raiz,i1,l)

    def elimina(self,raiz,i1,l):
        band=True
        self.aux=nodo()
        self.aux1=nodo()
        self.raiz=raiz
        if self.raiz!=None:
            if i1<self.raiz.dato:
                self.padre=self.raiz
                self.elimina(self.raiz.izq, i1,l)
            else:
                if i1>self.raiz.dato:
                    self.padre=self.raiz
                    self.elimina(self.raiz.der, i1,l)
                elif i1==l.dato and l.izq==None and l.der==None:
                    self.raiz=None
                elif self.raiz.izq == None and self.raiz.der == None:
                    if self.padre.der==self.raiz:
                        self.padre.der=None

                        self.raiz = l

                    elif self.padre.izq==self.raiz:
                        self.padre.izq=None

                        self.raiz = l

                else:
                    self.otro=nodo()
                    self.otro=self.raiz
                    if self.raiz.der == None:
                        n=self.otro.izq
                        self.raiz.dato = n.dato
                        self.raiz.izq = n.izq
                        self.raiz.der = n.der

                        self.raiz = l

                    else:
                        if self.otro.izq == None:
                            n = self.otro.der
                            self.raiz.dato = n.dato
                            self.raiz.izq = n.izq
                            self.raiz.der = n.der

                            self.raiz = l

                        else:
                            self.aux=self.raiz.izq
                            bo=False
                            while self.aux.der!=None:
                                self.aux1=self.aux
                                self.aux=self.aux.der
                                bo=True
                            self.raiz.dato=self.aux.dato
                            self.otro=self.aux
                            if bo==True:
                                self.aux1.der=self.aux.izq

                                self.raiz = l

                            else:
                                self.raiz.izq=self.aux.izq

                                self.raiz = l
        else:
            #print"dato no presente en el arbol"
            self.v = Toplevel()
            Label(self.v, font=("ROCKWELL", 14), fg='black', text="el dato no esta en el arbol", bg='gray').place(x=10,
                                                                                                                y=0)
            self.v.geometry("250x200")
            self.v.config(bg="gray")
            self.v.config(relief="sunken")
            self.v.title("eliminar")
            self.raiz=l
    def buscar(self,raiz,i):
        if raiz != None:
            if i < raiz.dato:
                self.buscar(raiz.izq, i)
            elif i > raiz.dato:
                self.buscar(raiz.der, i)
            else:
                self.v = Toplevel()
                Label(self.v, font=("ROCKWELL", 14), fg='black', text="dato en el arbol", bg='gray').place(x=10, y=0)
                self.v.geometry("250x200")
                self.v.config(bg="gray")
                self.v.config(relief="sunken")
                self.v.title("busqueda")
                #print"dato en la lista"
        else:
            self.v = Toplevel()
            Label(self.v, font=("ROCKWELL", 14), fg='black', text="el dato no esta en el arbol", bg='gray').place(x=10, y=0)
            self.v.geometry("250x200")
            self.v.config(bg="gray")
            self.v.config(relief="sunken")
            self.v.title("busqueda")
            #print"el dato no esta en la lista"

    def inicio2(self,a):
        self.raiz = nodo()
        #a = int(input("dato de la raiz: "))
        self.raiz.dato = a
        self.raiz.der=None
        self.raiz.izq = None
    def inicio(self, nod,s):

        self.q=nod
        if s<self.q.dato:
            if self.q.izq==None:
                self.otro = nodo()
                self.otro.dato = s
                self.otro.izq=None
                self.otro.der = None
                self.q.izq=self.otro
            else:
                self.inicio(self.q.izq,s)
        elif s > self.q.dato:
            if self.q.der == None:
                self.otro = nodo()
                self.otro.dato = s
                self.otro.der = None
                self.otro.izq = None
                self.q.der = self.otro
            else:
                self.inicio(self.q.der,s)
        else:
            self.v = Toplevel()
            Label(self.v, font=("ROCKWELL", 14), fg='black', text="dato en el arbol", bg='gray').place(x=10, y=0)
            self.v.geometry("250x200")
            self.v.config(bg="gray")
            self.v.config(relief="sunken")
            self.v.title("nodo")
            #print "dato en el arbol"
    def preorden(self, raiz,a,l):
        if  raiz != None:
            #print raiz.dato
            l.append(raiz.dato)
            self.preorden(raiz.izq,a,l)
            self.preorden(raiz.der,a,l)
    def inorden(self, raiz,a,l):
        if  raiz != None:
            self.inorden(raiz.izq,a,l)
            #print raiz.dato
            l.append(raiz.dato)
            self.inorden(raiz.der,a,l)
    def posorden(self, raiz,a,l):
        if  raiz != None:
            self.posorden(raiz.izq,a,l)
            self.posorden(raiz.der,a,l)
            #print raiz.dato
            l.append(raiz.dato)
#l=arbol()
#l.inicia()