import numpy as n
class bina:
    def bin(self):
        a=n.array([1,2,3,4,5,6,7,8,9])
        der=len(a)
        izq=0
        cen=(der+izq)//2
        x=int(input("dato a buscar: "))
        band=True
        while izq < der and x!=a[cen]:
            if x>a[cen]:
                izq=izq+1
            else:
                der=der-1
            cen = (der + izq) // 2

        if izq >= der:
            print"la informacion no esta en el arreglo"
        else:
            print"informacion en el arreglo: ",cen
b=bina()
b.bin()