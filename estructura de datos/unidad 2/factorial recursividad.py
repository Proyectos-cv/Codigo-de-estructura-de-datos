import numpy as np
class recursividad():
    def menu(self):
        band=True
        while band==True:
            print"selecciona factorial iterativo...........................................(1)"
            print"selecciona factorial recursivo...........................................(2)"
            print"selecciona fibonacci recursivo...........................................(3)"
            print"selecciona fibonacci normal..............................................(4)"
            print"selecciona imprimir datos de darreglo de derecha a izquierda recursivo ..(5)"
            print"selecciona imprimir datos de darreglo de izquierda a derecha recursivo ..(6)"
            print"selecciona imprimir datos de darreglo de derecha a izquierda iterativo ..(7)"
            print"selecciona imprimir datos de darreglo de izquierda a derecha iterativo ..(8)"
            print "selecciona imprimir la suma de datos de arreglo (recursivo) ............(9)"
            print "selecciona imprimir la suma de datos de arreglo (iterativa) ...........(10)"
            print "euclides iterativo ....................................................(11)"
            print "euclides recursivo.................................................... (12)"
            print "torres de hanoi recursivo............................................. (13)"
            e=int(input("seleccion: "))
            if e==1:
                r.normal()
            elif e==2:
                b = int(input("dame un numero de entrada: "))
                print "factorial: ",r.recursivo(b)
                #print "factorial: ", y
            elif e==3:
                b = int(input("dame un numero de entrada: "))
                print r.fiborec(b)
            elif e==4:
                b = int(input("dame un numero de entrada: "))
                r.fibonacci(b)
            #elif e==5:
             #   b = int(input("dame un numero de entrada(8,dimension dl arreglo): "))
              #  r.derecha(b)
            #elif e==6:
             #   b = int(input("dame un numero de entrada(0,comienzo del arreglo): "))
              #  r.izquierda(b)
            elif e==5:
                b = int(input("dimension: "))
                a = np.zeros(b)
                for i in range(b):
                    a[i] = int(input("numero: "))
                r.derecha(a, b)
            elif e==6:
                b = int(input("inicio de la contabilidad: "))
                f = int(input("dimension del arreglo: "))
                a = np.zeros(f)
                for i in range(f):
                    a[i] = int(input("numero: "))
                r.izquierda(a, b, f)
            elif e==7:
                b = int(input("cantidad de datos: "))
                a=np.zeros(b)
                for i in range(b):
                    a[i]=int(input("insertar dato: "))
                r.derechaiter(a,b)
            elif e==8:
                b = int(input("cantidad de datos: "))
                a=np.zeros(b)
                for i in range(b):
                    a[i]=int(input("insertar dato: "))
                r.izquierdaiter(a,b)
            elif e==9:
                b = int(input("cantidad de datos: "))
                a=np.zeros(b)
                for i in range(b):
                    a[i]=int(input("insertar dato: "))
                print r.suma(a,b)
            elif e==10:
                b = int(input("cantidad de datos: "))
                a=np.zeros(b)
                for i in range(b):
                    a[i]=int(input("insertar dato: "))
                r.sumaiter(a,b)
            elif e==11:
                a=int(input("cantidad mayor: "))
                b = int(input("numero menor: "))
                r.euclidesiter(a,b)
            elif e==12:
                a=int(input("cantidad mayor: "))
                b = int(input("numero menor: "))
                print "maximo comun divisor: ", r.euclidesre(a,b)
            elif e==13:
                n = int(input("numero de discos: "))
                origen = 'a'
                destino = 'b'
                auxiliar = 'c'
                r.hanoire(n,origen,auxiliar,destino)
            else:
                band=False





    def normal(self):
        b=int(input("dame un numero de entrada: "))
        l=1
        for i in range (1,b+1):
           l=l*i
        print "factorial: ",l
    def recursivo(self,b):
        if b==1:
            return 1
        else:
            return b*r.recursivo(b-1)
    def fibonacci(self,b):

        lista=[0,1]
        aux=2
        while aux<=b:
            lista.append(lista[aux-1]+lista[aux-2])
            aux=aux+1
        print lista[b]
    def fiborec(self,b):
        if b==0:
            return 0
        elif b==1:
            return 1
        else:
            return r.fiborec(b-1)+r.fiborec(b-2)

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
    #def derecha(self,b):
     #   a=np.array([1,2,3,4,5,6,7,8,9])
      #  if b >= 0:
       #     print a[b]
        #    return r.derecha (b-1)
    #def izquierda(self,b):
     #   a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
      #  aux = len(a)
       # if b < aux:
        #    print a[b]
         #   return r.izquierda (b+1)

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
            return a[b-1]+r.suma(a,b-1)
    def sumaiter(self,a,b):
        s=0
        for i in range(b):
           s=a[i]+s
        print s
    def euclidesiter(self,a,b):
        while b!=0:
            y=a%b
            a=b
            b=y
        print "maximo comun divisor: ", a
    def euclidesre(self,a,b):
        if b==0:
            return a
        else:
            h=b
            return r.euclidesre(h,a%b)

    def hanoire(self,n, origen, auxiliar, destino):
        if n == 1:
            print "se mueve de la torre: ", origen, "a torre: ", destino
        else:
            r.hanoire(n - 1, origen, destino, auxiliar)
            print "se mueve de la torre: ", origen, "a torre: ", destino
            r.hanoire(n - 1, auxiliar, origen, destino)
r=recursividad()
r.menu()