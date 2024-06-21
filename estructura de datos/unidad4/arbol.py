class nodo():
    def __init__(self):
        self.dato=None
        #self.liga=None
        self.der=None
        self.izq=None
class arbol():
    def __init__(self):
        self.raiz=None
        self.otro=None
        self.q=None
        self.padre=None
        #self.p=None
        #self.t=None
        #self.x=None
        #self.r=None
    def inicia(self):
        band=True
        while band==True:
            print"insertar nodo........1\n" \
                 "preorden.............2\n" \
                 "inorden..............3\n" \
                 "posorden.............4\n" \
                 "crear raiz...........5\n" \
                 "buscar dato..........6\n" \
                 "eliminar.............7\n"
            e=int(input("seleccion: "))
            if e==1:
                nod=nodo()
                s = int(input("dato: "))
                self.inicio(self.raiz,s)
            elif e==2:
                raiz = self.raiz
                a=self.raiz
                self.preorden(raiz,a)
                self.raiz = a
            elif e==3:
                raiz = self.raiz
                a = self.raiz
                self.inorden(raiz,a)
                self.raiz=a
            elif e==4:
                raiz = self.raiz
                a = self.raiz
                self.posorden(self.raiz,a)
                self.raiz = a
            elif e==5:
                nod = nodo()
                self.inicio2(nod)
            elif e==6:
                i=int(input("dato a buscar: "))
                raiz=self.raiz
                self.buscar(raiz,i)
            elif e==7:
                i1 = int(input("dato a eliminar: "))
                raiz = self.raiz
                l=self.raiz
                self.elimina(raiz,i1,l)

            else:
                band=False
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
                    #print "utilizar funcion 5 para cambiar raiz"
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
                    #if self.raiz.izq==None and self.raiz.izq==None:   error en la derecha
                     #   self.raiz=l
                      #  self.raiz.izq=None
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
                                #aux1.izq=aux.der
                                self.raiz.izq=self.aux.izq

                                self.raiz = l

                    #self.otro = None
                #self.raiz=raiz
                    #quitar
        else:
            print"dato no presente en el arbol"
            self.raiz=l
        #self.raiz=l
        #print self.raiz.dato
    def elimina1(self,raiz,i):
        if self.raiz != None:
            if i < raiz.dato:
                self.buscar(raiz.izq, i)
            elif i > raiz.dato:
                self.buscar(raiz.der, i)
            else:
                a=raiz
                i1=raiz
                self.elimina2(a,i1)
    def elimina2(self,a,i1):
        self.buscar(a.izq, i1)
        self.buscar(a.der, i1)
        if a.izq == None and a.der == None and a.dato < i1.izq and a.dato > i1.der:
            i1.dato=a.dato
            a = None
            a.der=None
            a.izq=None
        #if a.izq == None and a.der == None:
    def buscar(self,raiz,i):
        if raiz != None:
            if i < raiz.dato:
                self.buscar(raiz.izq, i)
            elif i > raiz.dato:
                self.buscar(raiz.der, i)
            else:
                print"dato en la lista"
        else:
            print"el dato no esta en la lista"

    def inicio2(self,nod):
        self.raiz = nod
        a = int(input("dato de la raiz: "))
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
            print "dato en el arbol"

    def inicio1(self, nod):
        self.q=nod
        r=int(input("nodo izquierdo(si=1)(no=2): "))
        if r==1:

            self.otro=nodo()
            t = int(input("dato: "))
            self.otro.dato=t
            self.q.izq = self.otro
            l.inicio(self.q.izq)
        else:
            self.q.izq=None
        r1 = int(input("nodo derecho(si=1)(no=2): "))
        if r1==1:

            self.otro=nodo()
            t = int(input("dato: "))
            self.otro.dato = t
            self.q.der=self.otro
            l.inicio(self.q.der)
        else:
            self.q.der=None
    def preorden(self, raiz,a):
        if  raiz != None:
            print raiz.dato
            l.preorden(raiz.izq,a)
            l.preorden(raiz.der,a)
    def inorden(self, raiz,a):
        if  raiz != None:
            l.inorden(raiz.izq,a)
            print raiz.dato
            l.inorden(raiz.der,a)
    def posorden(self, raiz,a):
        if  raiz != None:
            l.posorden(raiz.izq,a)
            l.posorden(raiz.der,a)
            print raiz.dato
l=arbol()
l.inicia()