import numpy as n
class ordena:
    def menu(self):
        band=True
        while band==True:
            print"burbuja........1"
            print"quicksort......2"
            print"shellsort......3"
            print"radix..........4"
            e=int(input("seleccion: "))
            if e==1:
                ordena().bubble()
            elif e==2:
                a = n.array([5, 6, 7, 4, 8, 3, 9, 2, 1])
                print a
                ini=0
                fin=8
                ordena().quicksort(ini,fin,a)
                print a
            elif e==3:
                a = n.array([5, 6, 7, 4, 8, 3, 9, 2, 1])
                nu=9
                print a
                ordena().shellsort(nu,a)
                print a
            elif e==4:
                a = n.array([5, 6, 7, 4, 8, 3, 9, 2, 1])
                print a
                ordena().radix(a)
                print a
            else:
                band=False
    def bubble(self):
        a=int(input("dimension del arreglo: "))
        q=n.zeros(a)
        for k in range(a):
            q[k]=int(input("dato: "))
        print q
        for i in range(a-1):
            for j in range(a-1):
                if q[j] > q[j + 1]:
                    s = q[j]
                    q[j] = q[j + 1]
                    q[j + 1] = s
        print q
    def quicksort(self,ini,fin,a):
        izq=ini
        der=fin
        pos =ini
        band=True
        while band==True:
            band=False
            while a[pos]<=a[der] and pos!=der:
                der=der-1
            if pos!=der:
                aux=a[pos]
                a[pos]=a[der]
                a[der]=aux
                pos=der
                while a[pos]>=a[izq] and pos!=izq:
                    izq=izq+1
                    if pos !=izq:
                        band=True
                        aux=a[pos]
                        a[pos]=a[izq]
                        a[izq]=aux
                        pos=izq
        if pos-1>ini:
            ordena().quicksort(ini,pos-1,a)
        if fin>pos+1:
            ordena().quicksort(pos+1,fin,a)
    def shellsort(self,nu,a):
        int=nu+1
        while int>1:
            int=int//2
            band=True
            while band==True:
                band=False
                i=0
                while i+int<nu:
                    if a[i]>a[i+int]:
                        aux=a[i]
                        a[i]=a[i+int]
                        a[i+int]=aux
                        band=True
                    i=i+1
    def radix(self,a):
        radix=10
        band=True
        tem=-1
        lugar=1
        while band==True:
            li=[list() for _ in range(radix) ]
            for i in a:
                tem=i/lugar
                li[tem%radix].append(i)
                if band==True and tem>0:
                    band=False
            c=0
            for b in range(radix):
                lis=li[b]
                for k in lis:
                    a[c]=k
                    c=c+1
            lugar=radix
o=ordena()
o.menu()