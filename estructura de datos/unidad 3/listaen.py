class nodo():
    def __init__(self):
        self.dato=None
        self.liga=None
class lista():
    def __init__(self):
        self.q=None
        self.p=None
        self.t=None
        self.x=None
        self.r=None
    def inicia(self):
        band=True
        while band==True:
            print"crea inicio..........1\n" \
                 "mostrar..............2\n" \
                 "iniciar final........3\n" \
                 "mostrar recursivo....4\n" \
                 "insertar inicio......5\n" \
                 "insertar final.......6\n" \
                 "eliminar inicio......7\n" \
                 "eliminar fin.........8\n" \
                 "busqueda desorden....9\n" \
                 "busqueda orden.......10\n" \
                 "busqueda recursiva...11\n" \
                 "eliminar nodo x......12\n" \
                 "insertar despues de..13\n" \
                 "insertar antes de....14\n" \
                 "elimina antes de.....15"
            e=int(input("seleccion: "))
            if e==1:
                self.inicio()
            elif e==2:
                self.mostrar()
            elif e==3:
                self.creafin()
            elif e==4:
                r = self.p
                self.muestrarec(self.p,r)
            elif e==5:
                self.insertainicio()
            elif e==6:
                self.insertafin()
            elif e==7:
                self.eliminarinicio()
            elif e==8:
                self.eliminarfin()
            elif e==9:
                self.busquedadesorden()
            elif e==10:
                self.buscarorden()
            elif e==11:
                g = int(input("numero a buscar: "))
                r=self.p
                self.buscarec(self.p,g,r)
            elif e==12:
                self.eliminax()
            elif e==13:
                self.despuesde()
            elif e==14:
                self.antesde()
            elif e==15:
                self.elimainaantesde()
            else:
                band=False

    def inicio(self):
        self.p = nodo()
        f = int(input("dato: "))
        self.p.dato=f
        self.p.liga=None
        d=int(input("continuar(si=1)(no=2): "))
        while d==1:
            self.q = nodo()
            f = int(input("dato"))
            self.q.dato=f
            self.q.liga=self.p
            self.p=self.q
            d=int(input("continuar (si=1)(no=2): "))

    def creafin(self):
        self.p=nodo()
        f = int(input("dato: "))
        self.p.dato=f
        self.p.liga=None
        self.t=self.p
        d = int(input("continuar (si=1)(no=2): "))
        while d == 1:
            self.q = nodo()
            f = int(input("dato: "))
            self.q.dato=f
            self.q.liga=None
            self.t.liga=self.q
            self.t=self.q
            d = int(input("continuar (si=1)(no=2): "))
    def mostrar(self):
        self.q=nodo()
        self.q=self.p
        while self.q!=None:
            print self.q.dato
            self.q=self.q.liga
    def muestrarec(self,a,r):
        self.p=a
        if self.p!=None:
            print self.p.dato
            self.p=self.p.liga
            l.muestrarec(self.p,r)
        self.p=r
    def insertainicio(self):
        self.q=nodo()
        f=int(input("dato: "))
        self.q.dato=f
        self.q.liga=self.p
        self.p=self.q
    def insertafin1(self):
        #self.t=nodo()
        self.t=self.p
        while self.t!=None:
            self.t=self.t.liga
        self.q=nodo()
        f = int(input("dato: "))
        self.q.dato=f
        self.q.liga=None
        self.p.liga=self.q
    def insertafin(self):
        self.t=nodo()
        self.t=self.p
        while self.t.liga != None:
            self.t=self.t.liga

        self.q = nodo()
        f = int(input("dato: "))
        self.q.dato=f
        self.q.liga= None
        self.t.liga = self.q
    def antesde(self):
        self.q = self.p
        band = True
        g = int(input("numero a buscar: "))
        while self.q.dato != g and band==True:
            if self.q.liga!=None:
                self.t=self.q
                self.q=self.q.liga
                #self.q=self.q.liga
            else:
                band=False
        if band==True:
            self.x=nodo()
            h = int(input("valor a ingresar: "))
            self.x.dato=h
            if self.p==self.q:
                self.x.liga=self.p
                self.p=self.x
            else:
                self.t.liga=self.x
                self.x.liga=self.q
        else:
            print"no se encuentra el nodo"
    def despuesde(self):
        self.q=self.p
        band=True
        g=int(input("numero a buscar: "))
        while self.q.dato != g and band==True:
            if self.q.liga!=None:
                self.q=self.q.liga
            else:
                band=False
        if band==True:
            h=int(input("valor a ingresar: "))
            self.t=nodo()
            self.t.dato=h
            self.t.liga=self.q.liga
            self.q.liga=self.t
        else:
            print"el nodo dado no se encuentra"
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
    def busquedadesorden(self):
        self.q=self.p
        z=int(input("numero a buscar: "))
        while self.q!=None and self.q.dato!=z:
            self.q=self.q.liga
        if self.q==None:
            print"elemento no se encuentra en la lista"
        else:
            print"elemento presente en la lista"
    def buscarorden(self):
        self.q=self.p
        g = int(input("numero a buscar: "))
        while self.q !=None and self.q.dato < g:
            self.q=self.q.liga
        if self.q==None or self.q.dato > g:
            print "elemento no encontrado"
        else:
            print"elemento en la lista"
    def buscarec(self,j,g,r):
        self.p = j
        if self.p!=None:
            if self.p.dato==g:
                print"elemento en la lista"
            else:
                l.buscarec(self.p.liga,g,r)
        else:
            print"no esta en la lista"
        self.p=r
    def eliminax(self):
        u=int(input("numero de dato a eliminar"))
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
    def elimainaantesde(self):
        g=int(input("dato del nodo: "))
        if self.p.dato == g:
            print"no hay anterior"
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
                print"elemento no encontrado"
            else:
                if self.p.liga==self.q:
                    self.p=self.q
                else:
                    self.r.liga=self.q
    def eliminadespuesde(self):
        pass
l=lista()
#l.inicia()