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

                #band = p.vacio(pila,tope,band)
                #tope=p.pop(pila,tope,band)
                #p.mostrar(pila,tope,maxi,band)
                p.pop(pila, tope, band)

            elif e ==2:
                #band = p.lleno(pila,tope,maxi,band)

                #tope=p.push(pila,tope, maxi, band)
                #p.mostrar(pila, tope, maxi,band)
                p.push(pila, tope, maxi, band)

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

    def push(self,pila,tope, maxi, band):
        if final<maxi:
            final=final+1
            cola[final]=int(input("dato: "))
            if final==0:
                frente=0
            else
                print"cola llena"
    def mostrar(self,pila,tope,maxi,band):
        if band==False:
            b=np.zeros(tope+1)
            for i in range (tope+1):
                b[i] = pila[i]
            print b
p=pilas()
p.inicio()



#CICLO ESQUINA NOROESTE
band=True
resti=[]
resj=[]
x=1
band2=True
mau=np.zeros((2+fil,2+col))
for t in range(1, fil + 1):
    for t1 in range(1, col + 1):
        mau[t][t1] = c[t][t1]

mau[z][z1]=3

while band==True:
    auxz=z
    auxz1=z1
    auz = auxz
    auz1 = auxz1
    if c[z][z1+1]==0 or c[z][z1+1]==1 or c[z][z1+1]==3 and band==True:
        while band2==True:
            for g in range(auz1,col+1):
                if mau[auz][g] == 3:
                    band=False
                    band2=False
                elif mau[auz][g] == 1 :
                    resti.append(auz)
                    resj.append(g)
                    mau[g][auz1] = 4
                    auz = auz
                    auz1 = g
            for g2 in range(auz, 0,-1):
                if mau[auz][g2] == 1 :
                    band = False
                    band2=False
                elif mau[auz][g2] == 1:

                    resti.append(auz)
                    resj.append(g2)
                    mau[g][auz1] = 4
                    auz = auz
                    auz1 = g2
            for g3 in range(auz1, 0 + 1):
                if mau[g3][auz1] == 1 :
                    resti.append(g3)
                    resj.append(auz1)
                    mau[g][auz1] = 4
                    auz = g3
                    auz1 = auz1
            for g1 in range(auz, fil + 1):
                if mau[g1][auz1] == 3:
                    band = False
                    band2=False
                elif mau[g1][auz1]==1:
                    resti.append(g1)
                    resj.append(auz1)
                    mau[g1][auz1]=4
                    auz=g1
                    auz1=auz1
            if band2==True:
                auxz = z
                auxz1 = z1
                auz = auxz
                auz1 = auxz1
                for t in range(1, fil + 1):
                    for t1 in range(1, col + 1):
                        mau[t][t1] = c[t][t1]
                band2=False

    if c[z][z1 - 1] == 0 or c[z][z1 - 1] == 1 or c[z][z1-1]==3 and band == True:
        while band2==True:
            for g3 in range(auz1, 0 + 1):
                if mau[g3][auz1] == 3:
                    band = False
                    band2 = False
                elif mau[g3][auz1] == 1 :
                    resti.append(g3)
                    resj.append(auz1)
                    mau[g][auz1] = 4
                    auz = g3
                    auz1 = auz1
            for g1 in range(auz, fil + 1):
                if mau[g1][auz1] == 3:
                    band = False
                    band2=False
                elif mau[g1][auz1]==1:
                    resti.append(g1)
                    resj.append(auz1)
                    mau[g1][auz1]=4
                    auz=g1
                    auz1=auz1
            for g in range(auz1, col + 1):
                if mau[auz][g] == 1:
                    resti.append(auz)
                    resj.append(g)
                    mau[g][auz1] = 4
                    auz = auz
                    auz1 = g
            for g2 in range(auz, 0,-1):
                if mau[auz][g2] == 1 :
                    band = False
                    band2=False
                elif mau[auz][g2] == 1 :
                    resti.append(auz)
                    resj.append(g2)
                    mau[g][auz1] = 4
                    auz = auz
                    auz1 = g2
                else:
                    band2=False
    if c[z+1][z1] == 0 or c[z+1][z1] == 1 or c[z+1][z1]==3 and band == True:
        while band2==True:
            for g1 in range(auz, fil + 1):
                if mau[g1][auz1] == 3:
                    band = False
                    band2 = False
                elif mau[g1][auz1] == 1:
                    resti.append(g1)
                    resj.append(auz1)
                    mau[g1][auz1] = 4
                    auz = g1
                    auz1 = auz1
            for g3 in range(auz1, 0 + 1):
                if mau[g3][auz1] == 1:
                    band = False
                    band2 = False
                elif mau[g3][auz1] == 1 :
                    resti.append(g3)
                    resj.append(auz1)
                    mau[g][auz1] = 4
                    auz = g3
                    auz1 = auz1
            for g2 in range(auz, 0,-1):
                if mau[auz][g2] == 1 :
                    resti.append(auz)
                    resj.append(g2)
                    mau[g][auz1] = 4
                    auz = auz
                    auz1 = g2
            for g in range(auz1,col+1):
                if mau[auz][g] == 3:
                    band = False
                    band2=False
                elif mau[auz][g] == 1 :
                    resti.append(auz)
                    resj.append(g)
                    mau[g][auz1] = 4
                    auz = auz
                    auz1 = g
                else:
                    band2=False
    if c[z-1][z1] == 0 or c[z-1][z1] == 1 or c[z-1][z1]==3 and band == True:
        while band2==True:
            for g2 in range(auz, 0, -1):
                if mau[auz][g2] == 1:
                    band = False
                    band2 = False
                elif mau[auz][g2] == 1:
                    resti.append(auz)
                    resj.append(g2)
                    mau[g][auz1] = 4
                    auz = auz
                    auz1 = g2
            for g in range(auz1,col+1):
                if mau[auz][g] == 3:
                    band = False
                    band2=False
                elif mau[auz][g] == 1 :
                    resti.append(auz)
                    resj.append(g)
                    mau[g][auz1] = 4
                    auz = auz
                    auz1 = g
            for g1 in range(auz, fil + 1):
                if mau[g1][auz1]==1:
                    resti.append(g1)
                    resj.append(auz1)
                    mau[g1][auz1]=4
                    auz=g1
                    auz1=auz1
            for g3 in range(auz1, 0 + 1):
                if mau[g3][auz1] == 1:
                    band = False
                    band2 = False
                elif mau[g3][auz1] == 1:
                    resti.append(g3)
                    resj.append(auz1)
                    mau[g][auz1] = 4
                    auz = g3
                    auz1 = auz1
                else:
                    band2=False
    else:
        band=False
        print "no hay ciclo"