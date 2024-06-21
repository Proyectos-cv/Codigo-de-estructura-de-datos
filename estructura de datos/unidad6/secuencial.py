import numpy as n
class secuencia:
    def sec(self):
        a=n.array([5,6,4,7,3,2,8,9,1])
        i=0
        m=len(a)
        x=int(input("dato a buscar: "))
        band=True
        while i < m and band==True:
            if x==a[i]:
                print"la informacion se encuentra en la pocision: ",i
                band=False
            i = i + 1

        if i > m or band==True:
            print"la informacion no esta en el arreglo"
s=secuencia()
s.sec()