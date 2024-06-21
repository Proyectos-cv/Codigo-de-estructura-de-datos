import random as r
from numpy import *
#d=int(input("dame un dato: "))
#d1=int(input("dame longitud del arreglo: "))
d1=11
arre = array([91,55,1,2,7,3,8,567,79,45,23,86])


x=int(input("dato a buscar: "))
dif=(x%d1)+1
dx=0
if arre[dx]!=-1 and arre[dif]==x:
    print"dato en el archivo en: ",dif
elif arre[0]==x:
    print"dato en: ",dx

else:
    dx=(dif%d1)+1
    while dx<=d1 and arre[dx]!=-1 and arre[dx]!=x and dx!=dif:
        dx=(dx%d1)+1
    if arre[dx]==-1 or arre[dx]!=x:
        print "el dato no esta"
    else:
        print"dato en: ",dx
#print dif