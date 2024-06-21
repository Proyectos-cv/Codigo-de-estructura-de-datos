import numpy as n
from partir import parte
from fusion import fus
class mezcladir:
    def principio(self):
        part=1
        b = open("ar1.txt", "r+")
        a = b.readlines()

        #a1 = open("myFile1.txt", "a")
        ##a1 = b1.readlines()

        #a2 = open("res.txt", "a")
        #a2=b2.readlines()
        v=n.zeros(len(a))
        for t in range(len(a)):
            r=int(a[t])
            v[t] = r
        a= v
        b.close()
        #a1.close()
        #a2.close()
        print "Cerrado o no : ", b.closed
        #print "Cerrado o no : ", a1.closed
        #print "Cerrado o no : ", a2.closed
        print a

        #a=n.array([10,12,78,56,34,89,45,61,35,99,8,675,2354,9,7,1])
        #a = n.array([9,75,14,68,29,17,31,25,4,5,13,18,72,46,61])
        #a1=[]
        #a2=[]
        print a
        #print a1
        #print a2
        #print ""
        #while part < (len(a)+1)//2:
        for c in range(len(a)+5):#(len(a)+1//2):
            a1,a2=parte().par(a,part)
            fus().fu(a,a1,a2,part)
            #part =part*2
        print a

        b = open("ar1.txt", "w")
        dato =  "\n"
        b.write(dato)
        for q in range(len(a)):
            dato = str(a[q]) + "\n"
            b.write(dato)
        b.close()
        print "Cerrado o no : ", b.closed

m=mezcladir()
m.principio()
#p=part()









    #def archi(self):
        #doc = open("ar1.txt", "w")

        #producto = str("clave") + "     " + "prod" + "     " + str("preciounitario") + "\n"
        #doc.write(producto)
        #print "El archivo esta creado"
        #doc.close()
        #print doc.closed

        #doc1 = open("ar2.txt", "w")

        #producto1 = str("clave") + "     " + "prod" + "     " + str("preciounitario") + "\n"
        #doc1.write(producto1)
        #print "El archivo esta creado"
        #doc1.close()
        #print doc1.closed

        #doc2 = open("res1.txt", "w")

        #producto2 = str("clave") + "     " + "prod" + "     " + str("preciounitario") + "\n"
        #doc2.write(producto2)
        #print "El archivo esta creado"
        #doc2.close()
        #print doc2.closed

#m=mezcladir()
#m.archi()
#m.principio()
