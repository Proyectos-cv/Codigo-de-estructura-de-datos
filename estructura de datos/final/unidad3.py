class nodo():
    def __init__(self):
        self.dato=None
        self.liga=None
from Tkinter import *
class lista():
    def __init__(self):
        self.q=None
        self.p=None
        self.t=None
        self.x=None
        self.r=None
    def inicia(self):
        self.vu = Toplevel()
        Label(self.vu, font=("ROCKWELL", 18), fg='black', text="Unidad 3", bg='gray').place(x=10, y=0)
        self.vu.geometry("280x500")
        self.vu.config(bg="gray")
        self.vu.config(relief="sunken")
        self.vu.title("Unidad 1")
        Label(self.vu, font=("ROCKWELL", 18), fg='black', text="contenido unidad 1", bg='gray').place(x=10,
                                                                                                      y=0)
        Button(self.vu, font=("INK FREE", 12), fg='black', text="inicio", bg='gray',
               command=self.inicio, relief=FLAT).place(x=70, y=50)
        Button(self.vu, font=("INK FREE", 12), fg='black', text="crear final", bg='gray',
               command=self.creafin, relief=FLAT).place(x=70, y=75)
        Button(self.vu, font=("INK FREE", 12), fg='black', text="mostrar", bg='gray',
               command=self.mostrar, relief=FLAT).place(x=70, y=100)
        Button(self.vu, font=("INK FREE", 12), fg='black', text="mostrar recursivo", bg='gray',
               command=self.muesrec, relief=FLAT).place(x=70, y=125)
        Button(self.vu, font=("INK FREE", 12), fg='black', text="agregar inicio", bg='gray',
               command=self.insertarinicio, relief=FLAT).place(x=70, y=150)
        Button(self.vu, font=("INK FREE", 12), fg='black', text="agregar fin", bg='gray',
               command=self.insertafin, relief=FLAT).place(x=70, y=175)
        Button(self.vu, font=("INK FREE", 12), fg='black', text="eliminar inicio", bg='gray',
               command=self.eliminarinicio, relief=FLAT).place(x=70, y=200)
        Button(self.vu, font=("INK FREE", 12), fg='black', text="eliminar fin", bg='gray',
               command=self.eliminarfin, relief=FLAT).place(x=70, y=225)
        Button(self.vu, font=("INK FREE", 12), fg='black', text="busqueda desorden", bg='gray',
               command=self.busquedadesorden1, relief=FLAT).place(x=70, y=250)
        Button(self.vu, font=("INK FREE", 12), fg='black', text="busqueda orden", bg='gray',
               command=self.busquedaorden, relief=FLAT).place(x=70, y=275)
        Button(self.vu, font=("INK FREE", 12), fg='black', text="busqueda recursiva", bg='gray',
               command=self.busrec, relief=FLAT).place(x=70, y=300)
        Button(self.vu, font=("INK FREE", 12), fg='black', text="eliminar nodo x", bg='gray',
               command=self.eliminx, relief=FLAT).place(x=70, y=325)
        Button(self.vu, font=("INK FREE", 12), fg='black', text="insertar despues de", bg='gray',
               command=self.desde, relief=FLAT).place(x=70, y=350)
        Button(self.vu, font=("INK FREE", 12), fg='black', text="insertar antes de", bg='gray',
               command=self.antde, relief=FLAT).place(x=70, y=400)
        Button(self.vu, font=("INK FREE", 12), fg='black', text="elimina antes de", bg='gray',
               command=self.antede, relief=FLAT).place(x=70, y=375)
        self.vu = mainloop()
    def sal(self):
        self.vu.destroy()

    def sa(self):
        self.v.destroy()
    def inicio(self):
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="insertar dato", bg='gray').place(x=10, y=0)
        self.v.geometry("250x270")
        self.dat = IntVar()
        Entry(self.v, textvariable=self.dat).place(x=70, y=50)
        self.v.config(bg="gray")
        Button(self.v, font=("INK FREE", 18), fg='black', text="continuar", bg='gray',
               command=self.sigue1, relief=FLAT).place(x=70, y=200)
        Button(self.v, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
               command=self.sa, relief=FLAT).place(x=120, y=200)
        self.v=mainloop()

    def continua(self):
        self.v.destroy()
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="insertar dato", bg='gray').place(x=10, y=0)
        self.v.geometry("250x270")
        self.dato = IntVar()
        Entry(self.v, textvariable=self.dato).place(x=70, y=50)
        self.v.config(bg="gray")
        Button(self.v, font=("INK FREE", 18), fg='black', text="continuar", bg='gray',
               command=self.sigue, relief=FLAT).place(x=70, y=200)
        Button(self.v, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
               command=self.sa, relief=FLAT).place(x=120, y=200)
        self.v=mainloop()
    def sigue1(self):
        self.p = nodo()
        self.p.dato = self.dat.get()
        self.p.liga = None
        self.continua()
    def sigue(self):
        self.q = nodo()
        self.q.dato = self.dato.get()
        self.q.liga = self.p
        self.p = self.q
        self.continua()
    def creafin(self):
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="insertar dato", bg='gray').place(x=10, y=0)
        self.v.geometry("250x270")
        self.dat = IntVar()
        Entry(self.v, textvariable=self.dat).place(x=70, y=50)
        self.v.config(bg="gray")
        Button(self.v, font=("INK FREE", 18), fg='black', text="continuar", bg='gray',
               command=self.siguen, relief=FLAT).place(x=70, y=200)
        Button(self.v, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
               command=self.sa, relief=FLAT).place(x=120, y=200)
        self.v = mainloop()

    def continuaa(self):
        self.v.destroy()
        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="insertar dato", bg='gray').place(x=10, y=0)
        self.v.geometry("250x270")
        self.dato = IntVar()
        Entry(self.v, textvariable=self.dato).place(x=70, y=50)
        self.v.config(bg="gray")
        Button(self.v, font=("INK FREE", 18), fg='black', text="continuar", bg='gray',
               command=self.siguen1, relief=FLAT).place(x=70, y=200)
        Button(self.v, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
               command=self.sa, relief=FLAT).place(x=120, y=200)
        self.v = mainloop()
    def siguen(self):
        self.p = nodo()
        self.p.dato = self.dat.get()
        self.p.liga = None
        self.t = self.p
        self.continuaa()
    def siguen1(self):
        self.q = nodo()
        self.q.dato = self.dato.get()
        self.q.liga = None
        self.t.liga = self.q
        self.t = self.q
        self.continuaa()


    def mostrar(self):
        l=[]
        self.q=nodo()
        self.q=self.p
        while self.q!=None:
            l.append(self.q.dato)
            self.q=self.q.liga
        self.v = Toplevel()
        self.v.geometry("370x250")
        self.v.config(bg="gray")
        Label(self.v, font=("ROCKWELL", 18), fg='black', text=l, bg='gray').place(x=10,
                                                                                                            y=0)
        self.v=mainloop()
    def muesrec(self):
        k=[]
        r=self.p
        self.muestrarec(self.p,r,k)
        self.v = Toplevel()
        self.v.geometry("370x250")
        self.v.config(bg="gray")
        Label(self.v, font=("ROCKWELL", 18), fg='black', text=k, bg='gray').place(x=10,
                                                                                  y=0)
        self.v = mainloop()
    def muestrarec(self,a,r,k):
        self.p=a
        if self.p!=None:
            k.append(self.p.dato)
            self.p=self.p.liga
            self.muestrarec(self.p,r,k)
        self.p=r

    def insertarinicio(self):
        self.vo = Toplevel()
        Label(self.vo, font=("ROCKWELL", 18), fg='black', text="insertar inicio", bg='gray').place(x=10, y=0)
        self.vo.geometry("250x270")
        self.dato = IntVar()
        Entry(self.vo, textvariable=self.dato).place(x=70, y=50)
        self.vo.config(bg="gray")
        Button(self.vo, font=("INK FREE", 18), fg='black', text="continuar", bg='gray',
               command=self.insertainicio1, relief=FLAT).place(x=70, y=200)
        Button(self.vo, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
               command=self.sa, relief=FLAT).place(x=120, y=200)
        self.vo = mainloop()
    def insertainicio1(self):
        self.q=nodo()
        self.q.dato=self.dato.get()
        self.q.liga=self.p
        self.p=self.q
        self.vo.destroy()
    def insertafin(self):
        self.vo = Toplevel()
        Label(self.vo, font=("ROCKWELL", 18), fg='black', text="insertar inicio", bg='gray').place(x=10, y=0)
        self.vo.geometry("250x270")
        self.dato = IntVar()
        Entry(self.vo, textvariable=self.dato).place(x=70, y=50)
        self.vo.config(bg="gray")
        Button(self.vo, font=("INK FREE", 18), fg='black', text="continuar", bg='gray',
               command=self.insertafin2, relief=FLAT).place(x=70, y=200)
        Button(self.vo, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
               command=self.sa, relief=FLAT).place(x=120, y=200)
    def insertafin2(self):
        self.t=nodo()
        self.t=self.p
        while self.t.liga != None:
            self.t=self.t.liga

        self.q = nodo()
        f = self.dato.get()
        self.q.dato=f
        self.q.liga= None
        self.t.liga = self.q
        self.vo.destroy()


    def antde(self):
        self.vo = Toplevel()
        Label(self.vo, font=("ROCKWELL", 18), fg='black', text="insertar inicio", bg='gray').place(x=10, y=0)
        self.vo.geometry("250x270")
        Label(self.vo, font=("ROCKWELL", 16), fg='black', text="buscar", bg='gray').place(x=10, y=25)
        self.dato = IntVar()
        Entry(self.vo, textvariable=self.dato).place(x=70, y=50)
        Label(self.vo, font=("ROCKWELL", 16), fg='black', text="nuevo valor", bg='gray').place(x=10, y=75)
        self.dato1 = IntVar()
        Entry(self.vo, textvariable=self.dato1).place(x=70, y=100)
        self.vo.config(bg="gray")
        Button(self.vo, font=("INK FREE", 18), fg='black', text="continuar", bg='gray',
               command=self.antesde, relief=FLAT).place(x=70, y=200)
        Button(self.vo, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
               command=self.sa, relief=FLAT).place(x=120, y=200)
    def antesde(self):
        self.q = self.p
        band = True
        g =self.dato.get()
        while self.q.dato != g and band==True:
            if self.q.liga!=None:
                self.t=self.q
                self.q=self.q.liga
                #self.q=self.q.liga
            else:
                band=False
        if band==True:
            self.x=nodo()
            h = self.dato1.get()
            self.x.dato=h
            if self.p==self.q:
                self.x.liga=self.p
                self.p=self.x
            else:
                self.t.liga=self.x
                self.x.liga=self.q
        else:
            self.vol = Toplevel()
            self.vol.config(bg="gray")
            Label(self.vol, font=("ROCKWELL", 18), fg='black', text="elemento no se encuentra", bg='gray').place(x=10,
                                                                                                                 y=0)
            self.vol.geometry("350x50")
            self.vol = mainloop()
        self.vo.destroy()
    def desde(self):
        self.vo = Toplevel()
        Label(self.vo, font=("ROCKWELL", 18), fg='black', text="insertar inicio", bg='gray').place(x=10, y=0)
        self.vo.geometry("250x270")
        Label(self.vo, font=("ROCKWELL", 16), fg='black', text="buscar", bg='gray').place(x=10, y=25)
        self.dato = IntVar()
        Entry(self.vo, textvariable=self.dato).place(x=70, y=50)
        Label(self.vo, font=("ROCKWELL", 16), fg='black', text="nuevo valor", bg='gray').place(x=10, y=75)
        self.dato1 = IntVar()
        Entry(self.vo, textvariable=self.dato1).place(x=70, y=100)
        self.vo.config(bg="gray")
        Button(self.vo, font=("INK FREE", 18), fg='black', text="continuar", bg='gray',
               command=self.despuesde, relief=FLAT).place(x=70, y=200)
        Button(self.vo, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
               command=self.sa, relief=FLAT).place(x=120, y=200)
    def despuesde(self):
        self.q=self.p
        band=True
        g=self.dato.get()
        while self.q.dato != g and band==True:
            if self.q.liga!=None:
                self.q=self.q.liga
            else:
                band=False
        if band==True:
            h=self.dato1.get()
            self.t=nodo()
            self.t.dato=h
            self.t.liga=self.q.liga
            self.q.liga=self.t
        else:
            self.vol = Toplevel()
            self.vol.config(bg="gray")
            Label(self.vol, font=("ROCKWELL", 18), fg='black', text="elemento no se encuentra", bg='gray').place(x=10,
                                                                                                                 y=0)
            self.vol.geometry("350x50")
            self.vol = mainloop()



    def eliminarinicio(self):
        self.q=self.p
        self.p=self.q.liga

    def eliminarfin(self):
        self.q=self.p
        if self.p.liga==None:
            self.p=None
        else:
            while self.q.liga != None:
                self.t=self.q
                self.q=self.q.liga
            self.q = self.t
            self.q.liga=None
    def busquedadesorden1(self):
        self.vo = Toplevel()
        Label(self.vo, font=("ROCKWELL", 18), fg='black', text="elemento a buscar", bg='gray').place(x=10, y=0)
        self.vo.geometry("250x270")
        self.dato = IntVar()
        Entry(self.vo, textvariable=self.dato).place(x=70, y=50)
        self.vo.config(bg="gray")
        Button(self.vo, font=("INK FREE", 18), fg='black', text="continuar", bg='gray',
               command=self.busquedadesorden, relief=FLAT).place(x=70, y=200)
        Button(self.vo, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
               command=self.sa, relief=FLAT).place(x=120, y=200)
    def busquedadesorden(self):
        self.q=self.p
        z=self.dato.get()
        while self.q!=None and self.q.dato!=z:
            self.q=self.q.liga
        if self.q==None:
            self.vol = Toplevel()
            self.vol.config(bg="gray")
            Label(self.vol, font=("ROCKWELL", 18), fg='black', text="elemento no se encuentra", bg='gray').place(x=10, y=0)
            self.vol.geometry("350x50")
            self.vol=mainloop()
        else:
            self.vol = Toplevel()
            Label(self.vol, font=("ROCKWELL", 18), fg='black', text="elemento presente", bg='gray').place(x=10,
                                                                                                                 y=0)
            self.vol.geometry("300x50")
            self.vol.config(bg="gray")
            self.vol = mainloop()
    def busquedaorden(self):
        self.vo = Toplevel()
        Label(self.vo, font=("ROCKWELL", 18), fg='black', text="elemento a buscar", bg='gray').place(x=10, y=0)
        self.vo.geometry("250x270")
        self.dato = IntVar()
        Entry(self.vo, textvariable=self.dato).place(x=70, y=50)
        self.vo.config(bg="gray")
        Button(self.vo, font=("INK FREE", 18), fg='black', text="continuar", bg='gray',
               command=self.buscarorden, relief=FLAT).place(x=70, y=200)
        Button(self.vo, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
               command=self.sa, relief=FLAT).place(x=120, y=200)
    def buscarorden(self):
        self.q=self.p
        g = self.dato.get()
        while self.q !=None and self.q.dato < g:
            self.q=self.q.liga
        if self.q==None or self.q.dato > g:
            self.vol = Toplevel()
            self.vol.config(bg="gray")
            Label(self.vol, font=("ROCKWELL", 18), fg='black', text="elemento no se encuentra", bg='gray').place(x=10,
                                                                                                                 y=0)
            self.vol.geometry("350x50")
            self.vol = mainloop()
        else:
            self.vol = Toplevel()
            Label(self.vol, font=("ROCKWELL", 18), fg='black', text="elemento presente", bg='gray').place(x=10,
                                                                                                          y=0)
            self.vol.geometry("300x50")
            self.vol.config(bg="gray")
            self.vol = mainloop()
    def busrec(self):
        self.vo = Toplevel()
        Label(self.vo, font=("ROCKWELL", 18), fg='black', text="elemento a buscar", bg='gray').place(x=10, y=0)
        self.vo.geometry("250x270")
        self.dato = IntVar()
        Entry(self.vo, textvariable=self.dato).place(x=70, y=50)
        self.vo.config(bg="gray")
        Button(self.vo, font=("INK FREE", 18), fg='black', text="continuar", bg='gray',
               command=self.buscrec, relief=FLAT).place(x=70, y=200)
        Button(self.vo, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
               command=self.sa, relief=FLAT).place(x=120, y=200)
    def buscrec(self):
        r=self.p
        g=self.dato.get()
        self.buscarec(self.p,g,r)
    def buscarec(self,j,g,r):
        self.p = j
        if self.p!=None:
            if self.p.dato==g:
                self.p = r
                self.vol = Toplevel()
                Label(self.vol, font=("ROCKWELL", 18), fg='black', text="elemento presente", bg='gray').place(x=10,
                                                                                                              y=0)
                self.vol.geometry("300x50")
                self.vol.config(bg="gray")
                self.vol = mainloop()
            else:
                self.buscarec(self.p.liga,g,r)
        else:
            self.p = r
            self.vol = Toplevel()
            self.vol.config(bg="gray")
            Label(self.vol, font=("ROCKWELL", 18), fg='black', text="elemento no se encuentra", bg='gray').place(x=10,
                                                                                                                 y=0)
            self.vol.geometry("350x50")
            self.vol = mainloop()
    def eliminx(self):
        self.vo = Toplevel()
        Label(self.vo, font=("ROCKWELL", 18), fg='black', text="elemento a eliminar", bg='gray').place(x=10, y=0)
        self.vo.geometry("250x270")
        self.dato = IntVar()
        Entry(self.vo, textvariable=self.dato).place(x=70, y=50)
        self.vo.config(bg="gray")
        Button(self.vo, font=("INK FREE", 18), fg='black', text="continuar", bg='gray',
               command=self.eliminax, relief=FLAT).place(x=70, y=200)
        Button(self.vo, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
               command=self.sa, relief=FLAT).place(x=120, y=200)
    def eliminax(self):
        u=self.dato.get()
        self.q=self.p
        band=True
        while self.q.liga != None and band==True:
            self.t=self.q
            if self.q.dato==u and self.p==self.q:
                self.p=self.q.liga
                band=False
            self.q=self.q.liga
            if self.q.dato==u:
                self.t.liga=self.q.liga
                band=False
    def antede(self):
        self.vo = Toplevel()
        Label(self.vo, font=("ROCKWELL", 18), fg='black', text="eliminar antes de:", bg='gray').place(x=10, y=0)
        self.vo.geometry("300x300")
        self.dato = IntVar()
        Entry(self.vo, textvariable=self.dato).place(x=70, y=50)
        self.vo.config(bg="gray")
        Button(self.vo, font=("INK FREE", 18), fg='black', text="continuar", bg='gray',
               command=self.eliminaantesde, relief=FLAT).place(x=70, y=200)
        Button(self.vo, font=("INK FREE", 18), fg='black', text="salir", bg='gray',
               command=self.sa, relief=FLAT).place(x=120, y=200)
    def eliminaantesde(self):
        g=self.dato.get()
        if self.p.dato == g:
            self.vol = Toplevel()
            self.vol.config(bg="gray")
            Label(self.vol, font=("ROCKWELL", 18), fg='black', text="no hay anterior", bg='gray').place(x=10,
                                                                                                                 y=0)
            self.vol.geometry("350x50")
            self.vol = mainloop()
        else:
            self.q=self.p
            self.t=self.p
            band=True
            while self.q.dato !=g and band==True:
                if self.q.liga!=None:
                    self.r=self.t
                    self.t=self.q
                    self.q=self.q.liga
                else:
                    band=False
            if band==False:
                self.vol = Toplevel()
                self.vol.config(bg="gray")
                Label(self.vol, font=("ROCKWELL", 18), fg='black', text="elemento no se encuentra", bg='gray').place(
                    x=10,
                    y=0)
                self.vol.geometry("350x50")
                self.vol = mainloop()
            else:
                if self.p.liga==self.q:
                    self.p=self.q
                else:
                    self.r.liga=self.q
    def eliminadespuesde(self):
        pass
