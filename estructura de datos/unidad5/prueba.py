#doc = open("res.txt", "a")

#producto = str("clave") + "     " + "prod" + "     " + str("preciounitario") + "\n"
#doc.write(producto)
#print "El archivo esta creado"
##doc.close()
#print doc.closed
#file = open("myFile.txt", "r+")
#str1 = file.readlines()
#print len(str1[1])
#for i in range(len(str1)):
 #   print str1[i]
#a=int(str)+7
#print a
#print "Lo que tenemos en el archivo es : ", str
#file.close()
#print "Cerrado o no : ", file.closed

#file1 = open("myFile1.txt", "r+")
#str = file1.readlines()
#print str
#print len(str[1])
#for i in range(len(str1)):
 #   print str1[i]
#a=int(str)+7
#print a
#print "Lo que tenemos en el archivo es : ", str
#file1.close()
#print "Cerrado o no : ", file1.closed
import numpy
class exter:
    def intercalacion(self):
        #str2=3
        band1=True
        band2=True
        n=0
        n1=0
        aux=0
        aux1=0
        #file = open("myFile.txt", "r+")
        #str1 = file.readlines()

        #file1 = open("myFile1.txt", "r+")
        #str = file1.readlines()

        #doc = open("res.txt", "a")
        str = numpy.array([15, 20, 35])
        str1 = numpy.array([10, 12, 25])
        print str
        print str1
        l=[]

        while (n1<(len(str1)) or band1==False) and (n<(len(str)) or band2==False):
            if band1==True:
                aux1=int(str1[n1])
                band1=False

            if band2==True:
                aux=int(str[n])
                band2=False

            if str1[n1]<str[n]:
                dato=str1[n1]#+"\n"
                l.append(dato)
                #doc.write(dato)
                n1=n1+1
                band1=True
            else:
            #if str[n]<str1[n1]:
                dato = str[n] #+ "\n"
                #doc.write(dato)
                l.append(dato)
                n=n+1
                band2=True
        #band1=False
        if band1==False:
            dato = str1[n1] #+ "\n"
            #doc.write(dato)
            l.append(dato)
            n1 = n1 + 1
            while n1<len(str1):
                dato = str1[n1] #+ "\n"
                #doc.write(dato)
                l.append(dato)
                n1 = n1 + 1
        if band2==False:
            dato = str[n]# + "\n"
            #doc.write(dato)
            l.append(dato)
            n = n + 1
            while n < len(str):
                dato = str[n]# + "\n"
                #doc.write(dato)
                l.append(dato)
                n = n + 1
        print l
        #file.close()
        #file1.close()
        #doc.close()
e=exter()
e.intercalacion()
