import numpy as n
from Tkinter import *
from unidad52p import parte
from inidad52f import fus
class mezcladir:
    def principio(self):
        part=1
        b = open("directa.txt", "r+")
        a = b.readlines()

        v=n.zeros(len(a))
        for t in range(len(a)):
            r=int(a[t])
            v[t] = r
        a= v
        b.close()

        #print "Cerrado o no : ", b.closed

    #    print a

        #a=n.array([10,12,78,56,34,89,45,61,35,99,8,675,2354,9,7,1])
        #a = n.array([9,75,14,68,29,17,31,25,4,5,13,18,72,46,61])

        #while part < (len(a)+1)//2:
        for c in range(len(a)+5):#(len(a)+1//2):
            a1,a2=parte().par(a,part)
            fus().fu(a,a1,a2,part)
            #part =part*2
        print a
        b = open("directa.txt", "w")
        dato =  "\n"
        b.write(dato)
        for q in range(len(a)):
            dato = str(a[q]) + "\n"
            b.write(dato)
        b.close()
        #print "Cerrado o no : ", b.closed


        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text=a, bg='gray').place(x=10, y=50)
        self.v.geometry("700x100")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        self.v.title("Unidad 5")
        Label(self.v, font=("ROCKWELL", 18), fg='black',
              text="los elementos apareceran en el archivo al teminar el proceso", bg='gray').place(x=10,
                                                                                                   y=0)
        self.v = mainloop()
#m=mezcladir()
#m.principio()