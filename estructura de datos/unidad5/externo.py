
class exter:
    def intercalacion(self):
        #str2=3
        band1=True
        band2=True
        n=0
        n1=0
        aux=0
        aux1=0
        file = open("myFile.txt", "r+")
        str1 = file.readlines()

        file1 = open("myFile1.txt", "r+")
        str = file1.readlines()

        doc = open("res.txt", "a")


        while (n1<(len(str1)) or band1==False) and (n<(len(str)) or band2==False):
            if band1==True:
                aux1=int(str1[n1])
                band1=False

            if band2==True:
                aux=int(str[n])
                band2=False

            if str1[n1]<str[n]:
                dato=str1[n1]+"\n"

                doc.write(dato)
                n1=n1+1
                band1=True
            else:

                dato = str[n] + "\n"
                doc.write(dato)

                n=n+1
                band2=True

        if band1==False:
            dato = str1[n1] + "\n"
            doc.write(dato)

            n1 = n1 + 1
            while n1<len(str1):
                dato = str1[n1] + "\n"
                doc.write(dato)

                n1 = n1 + 1
        if band2==False:
            dato = str[n] + "\n"
            doc.write(dato)

            n = n + 1
            while n < len(str):
                dato = str[n] + "\n"
                doc.write(dato)
                n = n + 1
        file.close()
        file1.close()
        doc.close()
        print "Cerrado o no : ", file.closed
        print "Cerrado o no : ", file1.closed
        print "Cerrado o no : ", doc.closed
e=exter()
e.intercalacion()
