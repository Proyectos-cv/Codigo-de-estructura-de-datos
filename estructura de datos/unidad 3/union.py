
import pila
import listaen
import cola
import colacircular
class ini():
    def __init__(self):
        band=True
        while band==True:
            print "pilas....................1\n" \
                  "cola.....................2\n" \
                  "cola circular............3\n" \
                  "lista enlazada...........4\n"
            e = int(input("seleccion: "))
            if e == 1:
                pila.pilas().inicio()
            elif e == 2:
                cola.colas().inicio()
            elif e == 3:
                colacircular.colacir().inicio()
            elif e == 4:
                listaen.lista().inicia()
            else:
                band=False
s = ini()