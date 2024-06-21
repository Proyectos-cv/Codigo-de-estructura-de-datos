#ejemplo 1
import numpy as n
#ejemplo 1
class tarea:
    def arreglos(self):
        e = n.zeros(10)
        o = 0
        u = 0
        for i in range(10):
            e[i] = int(input("dato: "))
            o = o + e[i]

        promedio = o / 10
        for i in range(10):
            if e[i] > promedio:
                u = u + 1

        print "promedio: ", promedio
        print "datos mas altos al promedio: ", u

# ejemplo 2
    def cuando(self):
        import numpy as n
        y = n.zeros(10)
        o = 0
        u = 0
        m = 0
        n = 0
        while m < 10:
            y[m] = int(input("dato: "))
            o = o + y[m]
            m = m + 1
        promedio = o / 10
        print promedio
        while n < 10:
            y[n] = int(input("dato: "))
            if y[n] > promedio:
                u = u + 1
            n = n + 1
        print "promedio: ", promedio
        print "datos mas altos al promedio: ", u

#ejemplo 3
    def muchas(self):
        b = 0
        a1 = int(input("dato: "))
        a2 = int(input("dato: "))
        a3 = int(input("dato: "))
        a4 = int(input("dato: "))
        a5 = int(input("dato: "))
        a6 = int(input("dato: "))
        a7 = int(input("dato: "))
        a8 = int(input("dato: "))
        a9 = int(input("dato: "))
        a10 = int(input("dato: "))
        prom = (a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10)
        promedio= prom/10
        if a1 > promedio:
            b = b + 1
        if a2 > promedio:
            b = b + 1
        if a3 > promedio:
            b = b + 1
        if a4 > promedio:
            b = b + 1
        if a5 > promedio:
            b = b + 1
        if a6 > promedio:
            b = b + 1
        if a7 > promedio:
            b = b + 1
        if a8 > promedio:
            b = b + 1
        if a9 > promedio:
            b = b + 1
        if a10 > promedio:
            b = b + 1
        print promedio
        print b
t=tarea()
t.arreglos()
t.cuando()
t.muchas()