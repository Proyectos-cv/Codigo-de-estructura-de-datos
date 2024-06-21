import numpy as np
class pilas:
    def inicio(self):
        band=False
        maxi = int(input("dimension del arreglo: "))
        tope = (-1)
        pila = np.zeros(maxi)
        while band == False:
            print"eliminar....1"
            print"insertar....2"
            e=int(input("seleccion: "))
            if e==1:

                band = p.vacio(pila,tope,band)
                tope=p.pop(pila,tope,band)
                p.mostrar(pila,tope,maxi,band)


            elif e ==2:
                band = p.lleno(pila,tope,maxi,band)

                tope=p.push(pila,tope, maxi, band)
                p.mostrar(pila, tope, maxi,band)


            else:
                band=True
    def lleno(self,pila,tope,maxi,band):
        tope = tope + 1
        if tope==maxi:
            band=True
            return band
        else:
            band=False
            return band
    def vacio(self,pila,tope,band):
        tope=tope-1
        if tope==-1 or tope<-1:
            band = True
            return band
        else:
            band=False
            return band
    def pop(self,pila,tope,band):
        if band==True:
            print "pila vacia"
        else:
            print"numero a eliminar: ",pila[tope]
            pila[tope]=0#int(input("elimina un numero: "))
            tope=tope-1
            return tope
    def push(self,pila,tope, maxi, band):
        if band == True:
            print"pila llena"
        else:
            tope= tope + 1
            pila[tope]=int(input("insetar un numero: "))
            return tope
    def mostrar(self,pila,tope,maxi,band):
        if band==False:
            b=np.zeros(tope+1)
            for i in range (tope+1):
                b[i] = pila[i]
            print b
p=pilas()
#p.inicio()