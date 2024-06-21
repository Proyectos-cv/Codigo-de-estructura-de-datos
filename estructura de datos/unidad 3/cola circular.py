import numpy as np
class colacir:
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
                frente=p.pop(cola,final,band,frente,maxi)
                p.mostrar(cola,final,maxi,band,frente)
            elif e ==2:
                band = p.lleno(cola,final,maxi,band,frente)
                final=p.push(cola,final, maxi, band,frente)
                p.mostrar(cola, final, maxi,band,frente)
            else:
                band=True

    def lleno(self,cola,final,maxi,band,frente):
        final = final + 1
        if (final==frente):
            band=True
            return band
        elif (final>=maxi and frente<=0):
            band = True
            return band
        else:
            band=False
            return band
    def vacio(self,cola,final,band,frente):
        frente=frente+1
        if frente-1==final:
            band=True
            return band
        if final==-1:
            band=True
            return band
        if frente>=final or final>0:
            band = False
            #print final
            #print frente
            return band
        if final == frente:
            band = True
            return band
        else:
            band=False
            #print final
            #print frente
            return band
    def pop(self,cola,final,band,frente,maxi):
        if band==True:
            print "cola vacia"
        elif frente>=maxi:
            frente=0
            print"numero a eliminar: ", cola[frente]
            frente=frente+1
            #print cola
            return frente
        elif frente==-1:
            frente = frente + 1
            print"numero a eliminar: ",cola[frente]
            frente=frente+1
            #print cola
            return frente
        else:
            print"numero a eliminar: ", cola[frente]
            frente = frente + 1
            #print cola
            return frente
    def push(self,cola,final, maxi, band,frente):
        if band == True:
            print"cola llena"
        elif final>=maxi or final+1==maxi:
            final = -1
            final=final+1
            cola[final] = int(input("insetar un numero: "))
            #print cola
            return final
        else:
            final= final + 1
            cola[final]=int(input("insetar un numero: "))
            #print cola
            return final
    def mostrar(self,cola,final,maxi,band,frente):
        if band==False:
            if frente<final and frente==-1:
                b = []
                frente=frente+1
                for i in range(frente, final+1):
                    b.append(cola[i])
                print b
            if frente>final:
                b=[]
                for i in range(frente,maxi):
                    b.append(cola[i])
                for j in range(0,final+1):
                    b.append(cola[j])
                print b
            if frente<final and frente!=-1:
                b = []
                for i in range(frente, final+1):
                    b.append(cola[i])
                print b
            if frente==final:
                b=[]
                b.append(cola[frente])
                print b
            #print b
p=colacir()
p.inicio()