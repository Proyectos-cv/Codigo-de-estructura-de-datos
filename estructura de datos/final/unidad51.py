from Tkinter import *
class exter:
    def intercalacion(self):
        #str2=3
        band1=True
        band2=True
        n=0
        n1=0
        aux=0
        aux1=0
        e=[]
        file = open("inter1.txt", "r+")
        str1 = file.readlines()

        file1 = open("inter2.txt", "r+")
        str = file1.readlines()

        doc = open("inter.txt", "a")


        while (n1<(len(str1)) or band1==False) and (n<(len(str)) or band2==False):
            if band1==True:
                aux1=int(str1[n1])
                band1=False

            if band2==True:
                aux=int(str[n])
                band2=False

            if str1[n1]<str[n]:
                dato=str1[n1]+"\n"
                e.append(int(str1[n1]))
                doc.write(dato)
                n1=n1+1
                band1=True
            else:

                dato = str[n] + "\n"
                doc.write(dato)
                e.append(int(str[n]))
                n=n+1
                band2=True

        if band1==False:
            dato = str1[n1] + "\n"
            doc.write(dato)
            e.append(int(str1[n1]))
            n1 = n1 + 1
            while n1<len(str1):
                dato = str1[n1] + "\n"
                doc.write(dato)
                e.append(int(str1[n1]))
                n1 = n1 + 1
        if band2==False:
            dato = str[n] + "\n"
            doc.write(dato)
            e.append(int(str[n]))
            n = n + 1
            while n < len(str):
                dato = str[n] + "\n"
                doc.write(dato)
                e.append(int(str[n]))
                n = n + 1
        file.close()
        file1.close()
        doc.close()
        #print e
        #print "Cerrado o no : ", file.closed
        #print "Cerrado o no : ", file1.closed
        #print "Cerrado o no : ", doc.closed

        self.v = Toplevel()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text=e, bg='gray').place(x=10, y=50)
        self.v.geometry("700x100")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        self.v.title("Unidad 5")
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="los elementos apareceran en el archivo al teminar el proceso", bg='gray').place(x=10,
                                                                                                      y=0)
        self.v = mainloop()
#e=exter()
#e.intercalacion()