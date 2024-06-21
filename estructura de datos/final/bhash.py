from numpy import *
from Tkinter import *
class ha:
    def bhas(self,arre,x):
        d1=11
        #arre = array([91,55,1,2,7,3,8,567,79,45,23,86])
        #x=int(input("dato a buscar: "))
        dif=(x%d1)+1
        dx=0
        if arre[dx]!=-1 and arre[dif]==x:
            #print"dato en el archivo en: ",dif
            self.v623 = Toplevel()
            Label(self.v623, font=("ROCKWELL", 18), fg='black', text="dato en la posicion: "+str(dif),
                  bg='gray').place(x=10, y=0)
            self.v623.geometry("350x100")
            self.v623.config(bg="gray")
            self.v623 = mainloop()
        elif arre[0]==x:
            #print"dato en: ",dx
            self.v623 = Toplevel()
            Label(self.v623, font=("ROCKWELL", 18), fg='black', text="dato en la posicion: " + str(dx),
                  bg='gray').place(x=10, y=0)
            self.v623.geometry("350x100")
            self.v623.config(bg="gray")
            self.v623 = mainloop()

        else:
            dx=(dif%d1)+1
            while dx<=d1 and arre[dx]!=-1 and arre[dx]!=x and dx!=dif:
                dx=(dx%d1)+1
            if arre[dx]==-1 or arre[dx]!=x:
                #print "el dato no esta"
                self.v623 = Toplevel()
                Label(self.v623, font=("ROCKWELL", 18), fg='black', text="el dato no se encuentra",
                      bg='gray').place(x=10, y=0)
                self.v623.geometry("350x100")
                self.v623.config(bg="gray")
                self.v623 = mainloop()
            else:
                #print"dato en: ",dx
                self.v623 = Toplevel()
                Label(self.v623, font=("ROCKWELL", 18), fg='black', text="dato en la posicion: " + str(dx),
                      bg='gray').place(x=10, y=0)
                self.v623.geometry("350x100")
                self.v623.config(bg="gray")
                self.v623 = mainloop()
#print dif