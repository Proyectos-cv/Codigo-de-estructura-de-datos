#cola simple
import numpy as np
class colas:
    def inicio(self):
        band=False
        maxi = int(input("dimension del arreglo: "))
        final = -1
        frente = -1
        cola = np.zeros(maxi)
        while band == False:
            print"eliminar....1"
            print"insertar....2"
            e=int(input("seleccion: "))
            if e==1:
                band = p.vacio(cola,final,band,frente)
                frente=p.pop(cola,final,band,frente)
                p.mostrar(cola,final,maxi,band,frente)
            elif e ==2:
                band = p.lleno(cola,final,maxi,band,frente)
                final=p.push(cola,final, maxi, band,frente)
                p.mostrar(cola, final, maxi,band,frente)
            else:
                band=True

    def lleno(self,cola,final,maxi,band,frente):
        final = final + 1
        if final==maxi:
            band=True
            return band
        else:
            band=False
            return band
    def vacio(self,cola,final,band,frente):
        frente=frente+1
        if frente>=final:
            band = True
            return band
        else:
            band=False
            return band
    def pop(self,cola,final,band,frente):
        if band==True:
            print "cola vacia"
        else:
            frente = frente + 1
            print"numero a eliminar: ",cola[frente]
            return frente
    def push(self,cola,final, maxi, band,frente):
        if band == True:
            print"cola llena"
        else:
            final= final + 1
            cola[final]=int(input("insetar un numero: "))
            return final
    def mostrar(self,cola,final,maxi,band,frente):
        if band==False:
            b=[]
            frente=frente+1
            final=final+1
            for i in range (frente,final):
                b.append(cola[i])
            print b
p=colas()
#p.inicio()