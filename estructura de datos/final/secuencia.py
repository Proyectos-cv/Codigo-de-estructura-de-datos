import numpy as n
from Tkinter import *
class secuencia:
    def sec(self,a,x):
        i=0
        m=len(a)
        #x=int(input("dato a buscar: "))
        band=True
        while i < m and band==True:
            if x==a[i]:
                #print"la informacion se encuentra en la pocision: ",i
                self.v6 = Toplevel()
                Label(self.v6, font=("ROCKWELL", 18), fg='black', text="informacion en posicion: "+str(i) , bg='gray').place(x=10, y=0)
                self.v6.geometry("350x100")
                self.v6.config(bg="gray")
                self.v6 = mainloop()
                band=False
            i = i + 1

        if i > m or band==True:
            #print"la informacion no esta en el arreglo"
            self.v6 = Toplevel()
            Label(self.v6, font=("ROCKWELL", 18), fg='black', text="no esta en el arreglo",
                  bg='gray').place(x=10, y=0)
            self.v6.geometry("350x100")
            self.v6.config(bg="gray")
            self.v6 = mainloop()
#s=secuencia()
#s.sec(a,x)