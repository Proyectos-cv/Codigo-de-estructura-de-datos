import numpy as n
from Tkinter import *
class bina:
    def bin(self,a,x):
        #a=n.array([1,2,3,4,5,6,7,8,9])
        der=len(a)
        izq=0
        cen=(der+izq)//2
        #x=int(input("dato a buscar: "))
        band=True
        while izq < der and x!=a[cen]:
            if x>a[cen]:
                izq=izq+1
            else:
                der=der-1
            cen = (der + izq) // 2

        if izq >= der:
            #print"la informacion no esta en el arreglo"
            self.v622 = Toplevel()
            Label(self.v622, font=("ROCKWELL", 18), fg='black', text="no esta en el arreglo",
                  bg='gray').place(x=10, y=0)
            self.v622.geometry("350x100")
            self.v622.config(bg="gray")
            self.v622 = mainloop()

        else:
            #print"informacion en el arreglo: ",cen
            self.v622 = Toplevel()
            Label(self.v622, font=("ROCKWELL", 18), fg='black', text="informacion en posicion: " + str(cen),
                  bg='gray').place(x=10, y=0)
            self.v622.geometry("350x100")
            self.v622.config(bg="gray")
            self.v622 = mainloop()
